# Annotations and Calculations

[![Language](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/) [![Framework](https://img.shields.io/badge/Jupyter-Notebook-red.svg)](https://jupyter.org/)

A collection of scripts and Jupyter notebooks to perform annotations and calculations on the DialSummEval dataset.


## Table of Contents
- [Directory Structure](#directory-structure)
- [Scripts](#scripts)
  - [ablation_corr.py](#ablation_corr.py)
  - [originalVpresent_corr.py](#originalVpresent_corr.py)
  - [IAA_CORR_calc.ipynb](#IAA_CORR_calc.ipynb)
  - [Annotation_tool.ipynb](#Annotation_tool.ipynb)
- [Dependencies](#dependencies)
- [Conclusion](#conclusion)

## Directory Structure

- Annotations And Calculations
    - data
        - ablation_results_annX.xlsx (where x is 1-3, for three annotators)
        - original_paper_results.json
        - saved_df_annX.csv (where x is 1-3, for three annotators)
    - utils
        - iaa_util.py
    - ablation_corr.py
    - originalVpresent_corr.py
    - iaa_calculation.py
    - IAA_CORR_calc.ipynb
    - Annotation_tool.ipynb


## Scripts

#### ablation_corr.py
`ablation_corr.py` 
This script calculates the correlation between two sets of annotations, one from a full annotation study and another from the ablation study. The full study's results were created using a special annotation tool while the ablation results used Excel.

The code reads the full study data (ann1, ann2, ann3) and ablation study data (df_1, df_2, df_3) into Pandas dataframes. Next, the code extracts only the dialogues used in the ablation study from the full study data. Finally, the code performs the correlation calculation using Pearson's R. This calculation is performed for each of the four evaluation criteria: coherence, consistency, fluency, and relevance.

#### iaa_calculation.py
This code calculates the inter-annotator agreement (IAA) scores between the annotations of three annotators (ann1, ann2, and ann3). It does this by comparing the scores for four dimensions of each annotation. It uses Krippendirff's alpha to calculate the IAA. This calculation is done for the present paper, and redone for the original paper by Gao & Wan (2022)

#### originalVpresent_corr.py
Like `ablation_corr.py`, this code calculates the correlation between two sets of annotations. This code calculated it between the results from Goa & Wan (2022) and the full results from the present paper.

#### IAA_CORR_calc.ipynb
A Jupyter Notebook that combines `ablation_corr.py`, `iaa_calculation.py`, and `originalVpresent_iaa_corr.py`. This is done to have quick and easy access to all information needed to compare agains the present paper's claims

#### Annotation_tool.ipynb
`Annotation_tool.ipynb` is a Jupyter Notebook containing the newly built Annotation tool that works completely within Jupyter notebooks.

## Dependencies
krippendorff==0.5.2\
numpy==1.22.4\
pandas==1.4.4\
ipywidgets==7.6.5

## Conclusion
Please refer to the paper (link will be included here) for more information on the Annotation Tool and the calculations done in the scripts

## Reference
M. Gao and X. Wan. “DialSummEval: Revisiting Summarization Evaluation for Dialogues.” In: Proceedings of
the 2022 Conference of the North American Chapter of the Association for Computational Linguistics:
Human Language Technologies. 2022, pp. 5693–5709.
