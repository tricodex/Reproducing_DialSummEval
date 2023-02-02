# Annotations and Calculations

[![Language](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/) [![Framework](https://img.shields.io/badge/Jupyter-Notebook-red.svg)](https://jupyter.org/)

A project to perform annotations and calculations on the DialSummEval dataset.


## Table of Contents
- [Directory Structure](#directory-structure)
- [Scripts](#scripts)
  - [ablation_corr.py](#ablation_corr.py)
  - [originalVpresent_iaa_corr.py](#originalVpresent_iaa_corr.py)
  - [IAA_CORR_calc.ipynb](#IAA_CORR_calc.ipynb)
  - [Annotation_tool.ipynb](#Annotation_tool.ipynb)

## Directory Structure

- Annotations And Calculations/
    - data
        - ablation_results_annX.xlsx (where x is 1-3, for three annotators)
        - original_paper_results.json
        - saved_df_annX.csv (where x is 1-3, for three annotators)
    - utils
        - iaa_util.py
    - ablation_corr.py
    - originalVpresent_iaa_corr.py
    - IAA_CORR_calc.ipynb
    - Annotation_tool.ipynb


## Scripts

### ablation_corr.py
`ablation_corr.py` 
This code calculates the correlation between two sets of annotations, one from a full annotation study and another from a smaller study. The full study uses a special annotation tool while the smaller study uses Excel.

The code reads the full study data (ann1, ann2, ann3) and ablation study data (df_1, df_2, df_3) into Pandas dataframes. Next, the code performs some preprocessing and extracts only the dialogues used in the ablation study from the full study data. Finally, the code performs the correlation calculation by transforming the list of evaluation values into a 2D array with dimensions [n * 14] * 10, where n is the number of annotators. This transformation is performed for each of the four evaluation criteria: coherence, consistency, fluency, and relevance. The code then proceeds to perform the correlation calculation.

### originalVpresent_iaa_corr.py
This code calculates the inter-annotator agreement (IAA) scores between the annotations of three annotators (ann1, ann2, and ann3) and the annotations of the original paper. It does this by comparing the scores for four dimensions of each annotation: consistency, coherence, fluency, and relevance. The annotations are loaded from two sources, the annotations from the present paper are stored in .csv files, while the annotations from the original paper are stored in a .jsonl file. The .csv files are loaded using the Pandas library, and the .jsonl file is loaded using the built-in Python library for reading files. The original paper annotations are then transformed to match the format of the annotations from the present paper. Both sets of annotations are then prepared for calculations by transforming their values into lists of 100 items with each item being a list of 14 values. Finally, the IAA scores are calculated using the Krippendorff library.

### IAA_CORR_calc.ipynb
`IAA_CORR_calc.ipynb` is a Jupyter Notebook that combines `ablation_corr.py` and `originalVpresent_iaa_corr.py`. This is done to have quick and easy access to all information needed to compare agains the present paper's claims

### Annotation_tool.ipynb
`Annotation_tool.ipynb` is a Jupyter Notebook containing the newly built Annotation tool that works completely within Jupyter notebooks.

## Dependencies
krippendorff==0.5.2\
numpy==1.22.4\
pandas==1.4.4\
ipywidgets==7.6.5

## Conclusion
Please refer to the paper (found in the root of this directory) for more information on the Annotation Tool and the calculations done in the scripts
