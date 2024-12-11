
# README: Gene Interaction Pipeline

## 1. Overview
The Gene Interaction Pipeline is a Python-based program designed to identify transcription factors that interact with genes from a specified KEGG pathway. The program performs the following key steps:

1. **Retrieve Genes from KEGG**: Extract a list of genes relevant to the given KEGG pathway.
2. **Translate Gene IDs**: Convert KEGG gene entry IDs to human-readable gene names.
3. **Fetch Gene IDs**: Obtain unique identifiers for each gene from the Enrichr database.
4. **Fetch Transcription Factors**: Identify and record transcription factors interacting with each gene using Enrichr's API.

The program saves the results in a CSV file for further analysis.

Below is the url for our writeup:
https://docs.google.com/document/d/11d9HB1cBRPzJLsrz6KXePb6exK29FUqgfcVfzdZnarU/edit?usp=sharing


---

## 2. Prerequisites
- **Python Version**: Python 3.9 or later
- **Required Libraries**:
  - `requests`
  - `json`
  - `re`
  - `pandas`
  - `csv`
  - `concurrent.futures`
  - `Bio.KEGG.REST`
  
Install the required libraries via pip:
```bash
pip install requests pandas biopython
```

---

## 3. File Structure
- **main.py**: Contains the main pipeline logic and function definitions.
- **enrichr_interacting_gene_results.csv**: The output file containing transcription factor interaction results.

---

## 4. Usage Instructions
1. Open a terminal or command prompt.
2. Run the script by executing the following command:
   ```bash
   python pipeline.py
   ```
3. The script will prompt for a KEGG pathway ID. Provide the ID in the format `hsaXXXXX`, where `XXXXX` is the numeric identifier (e.g., `hsa00010`).
4. The script will display the progress of each step and save the results in `enrichr_interacting_gene_results.csv`.

---

## 5. Input Format
- **KEGG Pathway ID**: The pathway identifier must be in the format `hsaXXXXX`, where `XXXXX` is a five-digit number.
- Example: `hsa00010`

---

## 6. Output
- The program generates a CSV file named **enrichr_interacting_gene_results.csv** containing the following columns:
  - **Gene Target**: The target gene for the interaction.
  - **Interacting Gene**: The gene interacting with the target gene.
  - **Tissue**: The tissue where the interaction occurs (if specified).
  - **Enrichr Library**: The Enrichr library from which the interaction was identified.

---

## 7. Error Handling
- **API Call Failures**: If API requests fail, the script retries up to 10 times. If all attempts fail, the script logs the error and continues with the next task.
- **Invalid KEGG Pathway ID**: If the pathway ID format is invalid, the program will display an error and terminate.

---

## 8. Performance Tips
- To improve speed, the program utilizes parallel API requests using Python's `ThreadPoolExecutor`.
- Batch processing and chunked CSV writing are used to reduce memory usage and prevent large in-memory DataFrames.

---

## 9. Example
Run the following command in your terminal to analyze KEGG pathway `hsa00010`:
```bash
python main.py
```
When prompted, enter `hsa00010` as the pathway ID. The output file **enrichr_interacting_gene_results.csv** will be created in the current working directory.

---

## 10. Known Issues
- Some API calls may fail due to temporary outages of the KEGG or Enrichr API services.
- For large datasets, consider increasing the chunk size in the CSV writer to optimize performance.
