# coding: utf-8

"""
Gene Interaction Pipeline

This script identifies interacting transcription factors for a given KEGG pathway. The following steps are executed:

1. **Get Genes from KEGG**: Retrieve genes relevant to a given KEGG pathway.
2. **Translate Gene IDs**: Convert gene entry IDs to readable gene names.
3. **Get Gene IDs**: Fetch unique identifiers for each gene name from the Enrichr database.
4. **Fetch Transcription Factors**: Identify transcription factors that interact with the given genes.

Each module includes detailed documentation, follows a consistent coding style, and provides robust error handling.
"""

import json
import re
import requests
import pandas as pd
from Bio.KEGG import REST
import urllib.parse


def get_gene_ids(genes):
    """Fetch unique Enrichr IDs for a list of genes.

    Args:
        genes (list): List of gene names to retrieve IDs for.

    Returns:
        list: List of Enrichr user list IDs for the input genes.
    """
    ENRICHR_URL = 'https://maayanlab.cloud/Enrichr/addList'
    gene_ids = []

    for gene in genes[:20]:  # Limit to 20 genes
        genes_str = '\n'.join(list(gene))
        payload = {'list': (None, genes_str), 'description': (None, 'Query gene list')}

        for attempt in range(10):  # Retry up to 10 times
            response = requests.post(ENRICHR_URL, files=payload)
            if response.ok:
                break
            if attempt >= 5:
                raise Exception(f"Error analyzing gene list for gene: {gene}")

        data = json.loads(response.text)
        gene_ids.append(data['userListId'])

    return gene_ids


def is_substring(sub_string, larger_string, chk_lower_upper_cap=True):
    """Check if a substring exists in a larger string, optionally considering case variants.

    Args:
        sub_string (str): The substring to search for.
        larger_string (str): The larger string to search within.
        chk_lower_upper_cap (bool, optional): Check for lowercase, uppercase, and capitalized versions. Defaults to True.

    Returns:
        str or bool: Matched substring or False if no match is found.
    """
    variations = [
        sub_string,
        sub_string.lower(),
        sub_string.upper(),
        sub_string.capitalize()
    ]
    for variant in variations if chk_lower_upper_cap else [sub_string]:
        match = re.search(f"({variant})", larger_string)
        if match:
            return match[1]
    return False


def get_genes_from_kegg(pathway_id):
    """Retrieve a list of genes associated with a KEGG pathway.

    Args:
        pathway_id (str): KEGG pathway identifier (e.g., 'hsa00010').

    Returns:
        list: List of gene identifiers related to the pathway.
    """
    kegg_base_url = "http://rest.kegg.jp/link/hsa/"
    url = f"{kegg_base_url}{urllib.parse.quote(pathway_id)}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from KEGG API. Status Code: {response.status_code}")

    genes = [line.split('\t')[1] for line in response.text.splitlines()]
    return genes


def translate_genes_to_names(genes):
    """Translate gene identifiers to gene names using the KEGG API.

    Args:
        genes (list): List of gene identifiers.

    Returns:
        list: List of human-readable gene names.
    """
    gene_names = []
    for gene_id in genes[:5]:
        result = REST.kegg_list(gene_id).read()
        parsed_result = result.split(';')[0].split(',')[0].split('\t')
        gene_names.extend([name.strip() for name in parsed_result[1:]])
    return gene_names


def fetch_tfs(gene_name_list, gene_ids):
    """Fetch transcription factors that interact with specified genes.

    Args:
        gene_name_list (list): List of gene names.
        gene_ids (list): List of corresponding gene IDs.
    """
    ENRICHR_URL = 'https://maayanlab.cloud/Enrichr/enrich'
    query_string = '?userListId=%s&backgroundType=%s'
    results = []

    for gene_name, gene_id in zip(gene_name_list, gene_ids):
        response = requests.get(ENRICHR_URL + query_string % (gene_id, "ENCODE_TF_ChIP-seq_2015"))
        if not response.ok:
            raise Exception(f"Error fetching enrichment results for gene: {gene_name}")

        data = json.loads(response.text)
        if "ENCODE_TF_ChIP-seq_2015" in data:
            for entry in data["ENCODE_TF_ChIP-seq_2015"]:
                tissue_match = is_substring(" ", entry[1])
                interacting_gene = entry[1].split()[0]
                results.append([gene_name, interacting_gene, tissue_match or "Unspecified", "ENCODE_TF_ChIP-seq_2015"])

    enrichr_results = pd.DataFrame(results, columns=["Gene Target", "Interacting Gene", "Tissue", "Enrichr Library"])
    enrichr_results.to_csv("enrichr_interacting_gene_results.csv", index=False, encoding='utf-8')


def pipeline(pathway_id):
    """Run the full pipeline to identify transcription factors for a KEGG pathway.

    Args:
        pathway_id (str): KEGG pathway identifier.
    """
    gene_ids = get_genes_from_kegg(pathway_id)
    gene_name_list = translate_genes_to_names(gene_ids)
    enrichr_ids = get_gene_ids(gene_name_list)
    fetch_tfs(gene_name_list, enrichr_ids)


def main():
    pathway_id = "hsa00010"  # Example KEGG pathway ID
    pipeline(pathway_id)


if __name__ == "__main__":
    main()
else:
    print("wip_pipeline.py: Is intended to be executed and not imported.")
