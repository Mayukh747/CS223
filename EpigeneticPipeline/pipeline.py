import json
import re

import requests
import pandas as pd
from Bio.KEGG import REST

#####
# HELPER FUNS
#####
def get_gene_ids(genes):
    # ENRICHR URL
    ENRICHR_URL = 'https://maayanlab.cloud/Enrichr/addList'

    # INIT GENE IDE LIST
    gene_ids = []

    # NOW GET ID FOR EACH GENE
    for gene in genes[:20]:
        genes_str = '\n'.join(list(gene))
        description = 'Query gene list'
        payload = {
            'list': (None, genes_str),
            'description': (None, description)
        }

        # GET ID
        response = requests.post(ENRICHR_URL, files=payload)
        if not response.ok:
            # Try a couple more times since NCBI might not return
            # info on the first call
            for i in range(10):
                response = requests.post(ENRICHR_URL, files=payload)
                if response.ok:
                    break
                elif i >= 5:
                    raise Exception('Error analyzing gene list for gene: ', gene)

        data = json.loads(response.text)
        gene_ids.append(data['userListId'])

    return gene_ids


###
# FIND A TISSUE TYPE (I.E., SUBSTRING) WITHIN THE
# LARGER DESCRIPTION OF A RETURNED RESULT
def is_substring(sub_string, larger_string, chk_lower_upper_cap = True):
    # If chk_lower_upper_cap is False, then only the provided sub_string, without modification
    # is checked for being part of the larger_string
    # First make all sub_string characters lower case, uppercase, and capitalized
    # then check for being paer of the larger string.
    lc_substring = sub_string.lower()
    uc_substring = sub_string.upper()
    cap_substring = lc_substring.capitalize()

    # Now check if any of the lower, upper, or capitalized sub strings
    # are within the larger string.
    lc_res = re.search("("+lc_substring+")", larger_string)
    uc_res = re.search("("+uc_substring+")", larger_string)
    cap_res = re.search("("+cap_substring+")", larger_string)
    unchanged_res = re.search("("+sub_string+")", larger_string)

    if chk_lower_upper_cap:
        if unchanged_res:
            return unchanged_res[1]
        elif lc_res:
            return lc_res[1]
        elif uc_res:
            return uc_res[1]
        elif cap_res:
            return cap_res[1]
        else:
            return False
    else: # We checked only the original sub string
        if unchanged_res:
            return unchanged_res[1]
        else:
            return False


# Step 1: Retrieve Gene List from KEGG API
def get_genes_from_kegg(pathway_id):
    import urllib.parse

    kegg_base_url = "http://rest.kegg.jp/link/hsa/"
    pathway_id = urllib.parse.quote(pathway_id)  # Ensure pathway ID is URL-safe
    url = kegg_base_url + pathway_id

    print(f"Requesting KEGG API URL: {url}")
    response = requests.get(url)

    if response.status_code == 200:
        data = response.text.splitlines()
        genes = [line.split('\t')[1] for line in data]
        return genes
    else:
        raise Exception(
            f"Failed to fetch data from KEGG API. Status Code: {response.status_code}, Response: {response.text}")


# Step 2: Translate gene ids to gene names
def translate_genes_to_names(genes):
    gene_names = []
    for id in genes[:5]:
        result = REST.kegg_list(id).read()
        result = result.split(';')[0].split(',')
        result[0] = result[0].split('\t')[1]
        gene_names.extend([name.strip() for name in result])
    return gene_names


#Step 4: Fetch Transcription Factors
def fetch_tfs(gene_name_list, gene_ids):
    # SPECIFY URL OF ENRICHR DB TO USE AND CREATE QUERY STRING
    ENRICHR_URL = 'https://maayanlab.cloud/Enrichr/enrich'
    query_string = '?userListId=%s&backgroundType=%s'

    # CREATE A RESULT PANDAS OBJECT
    results_col_names = ["Gene Target", "Interacting Gene", "Tissue", "Enrichr Library"]
    # results = pd.DataFrame(columns=results_col_names)
    results = []



    # SPECIFY URL OF ENRICHR DB TO USE AND CREATE QUERY STRING
    ENRICHR_URL = 'https://maayanlab.cloud/Enrichr/enrich'
    query_string = '?userListId=%s&backgroundType=%s'

    # CREATE A RESULT PANDAS OBJECT
    results_col_names = ["Gene Target", "Interacting Gene", "Tissue", "Enrichr Library"]
    # results = pd.DataFrame(columns=results_col_names)
    results = []

    # Loop through each gene of interest to find interacting genes
    for gene_name, gene_id in zip(gene_name_list, gene_ids):
        tissue_name = " "
        lib_name = "ENCODE_TF_ChIP-seq_2015"

        print("Retrieving interacting genes for " + gene_name + " with id: " + str(gene_id) + " for tissue: " + str(
            tissue_name) + " and enrichment library: " + lib_name)
        response = requests.get(ENRICHR_URL + query_string % (gene_id, lib_name))
        # MAKE SURE WE HAVE VALID RESPONSE
        if not response.ok:
            raise Exception('Error fetching enrichment results for gene: ' + gene_name)

        # EXTRACT RESULTS
        data = json.loads(response.text)

        # RETRIEVE INFO FOR THE DESIRED TISSUE AND FROM THE DESIRED LIBRARY
        if lib_name in data.keys():
            tissue_info = data[lib_name]  # Extract the entry for the specified library
            entry_found = False
            for entry in tissue_info:
                tissue_match_res = is_substring(tissue_name, entry[1])
                if tissue_match_res:
                    interacting_gene = entry[1].split()[0]
                    if tissue_match_res == ' ':
                        tissue_match_res = "Unspecified"
                    print("      The Gene Name that interacts with " + str(gene_name) + " is " + str(
                        interacting_gene) + " in " + str(tissue_match_res) + " tissue.")
                    new_result_row = [gene_name, interacting_gene, tissue_match_res, lib_name]
                    results.append(new_result_row)
                    entry_found = True

            if not entry_found:
                print(
                    "      Interacting Gene(s) for " + gene_name + " in tissue " + tissue_name + " in library " + lib_name + " not found")
                entry_found = False

            print("==========\n")

    # WRITE RESULTS TO .csv  FILE
    enrichr_results = pd.DataFrame(results, columns=results_col_names)
    enrichr_results.to_csv("enrichr_interacting_gene_results.csv", index=False, encoding='utf-8')

    print("#####################################")
    print("Result Data Frame")
    print(results)
    print("#####################################")
    print("Completed writing enrichr results to the file named 'enrichr_interacting_gene_results.csv'")
    print()
    print(">>>>>>>>>> DONE <<<<<<<<<<")


def pipeline(pathway_id):
    '''
    Given a pathway ID
    1. get genes relevant to the pathway
    2. Translate gene entry IDS to gene names
    3. Fetch gene ids for every gene name
    4. Fetch Transcription Factors for all genes.
    '''

    gene_ids = get_genes_from_kegg(pathway_id)
    gene_name_list = translate_genes_to_names(gene_ids)
    # gene_name_list = hard_coded_gene_name_list

    gene_ids = get_gene_ids(gene_name_list)

    fetch_tfs(gene_name_list, gene_ids)


# Example Usage
pathway_id = "hsa00010"  # Replace with the KEGG pathway ID
pipeline(pathway_id)
