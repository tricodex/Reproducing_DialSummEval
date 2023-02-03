# Reproduction of DialSummEval  
### Evaluation of automatic summarization evaluation metrics

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/) [![Anaconda](https://anaconda.org/conda-forge/terraform-provider-github/badges/version.svg)](https://docs.anaconda.com/anaconda/install/)

This repository is created for the reproduction of [DialSummEval: Revisiting summarization evaluation for dialogues](https://aclanthology.org/2022.naacl-main.418). The code and data of the original authors and ourselves are included in the repository. 

The link to the reproduction paper will be included here.

- Annotations and Correlations
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
- figures (output from analysis.py)
- original_annotations
    - human_judgment.jsonl   
- reproduce
    - analysis
        - models_eval_new
            - ... (scores and summaries for and from each model)
        - analysis.py
    - metrics
        - ... (metrics)
- environment.yml
- requirements.txt


## Environment Setup

Anaconda environments have been used for this repository. You can set up the environment using the following steps:

1. Install [Anaconda](https://docs.anaconda.com/anaconda/install/)
2. Clone this repository
3. Navigate to the repository directory and run the following command in the terminal/command prompt: `conda env create -f environment.yml`
4. Activate the environment using the following command: `conda activate combotenv`

NOTE: It is advised to use seperate environments for the metrics.

## Requirements

The required packages are listed in the `requirements.txt` file. You can install these packages using the following command in the terminal/command prompt: `pip install -r requirements.txt`. Some metrics require packages that are not in the PyPI, this will be specified.

NOTE: [CUDA installation guide Windows](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/), [CUDA installation guide Linux](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)

## Annotation

The annotation tool is located in the following directory: `.\Annotations and Correlations` and contains a separate `README.md`. This Jupyter Notebook can be used to annotate the dialogue summaries. The reproduced annotations are also stored in in this directory.

We conducted an ablation study to examine the impact of the annotation tool on the annotation procedure. 140 summaries (14 summaries per 10 randomly selected dialogues) were annotated using the same method as in the original paper with an Excel sheet, where each model’s summaries were displayed on separate sheets. The results reveal a strong correlation between the results obtained through the tool and the original annotation process, supporting the use of the tool.

| Dimension | Reproduction-Original | Full Reproduction-Ablation |
|-----------|------------------|------------------|
| Coherence | 0.42             | 0.70             |
| Consistency | 0.77             | 0.66             |
| Fluency | 0.55             | 0.77             |
| Relevance | 0.69             | 0.51             |

## Code

Most paths are setup for Unix-like systems (Mac OS X and Linux) `path\to\file`, but since the experiments were ran on Windows some path are `path//to//file`, these should be changed if not ran on Windows and also because they are local paths. 

## Analysis

The analysis of the human annotations compared to the metric scores is located in the following path: `.\reproduce\analysis\analysis.py` and contains a seperate `README.md` for the `analysis.py` file. The script can be run using the following command in the terminal/command prompt: `python .\reproduce\analysis\analysis.py`

## Metrics

The metrics are stored in the following path: `.\reproduce\metrics` and contains a seperate `README.md`. The metrics were calculated using the evaluation metrics such as ROUGE, BLEU, METEOR, BERTScore, MoverScore, BARTScore, SMS, Embedding average, Vector extrema, FEQA, SummaQA, QuestEval, FactCC, and DAE.

## Summarization Models

Each of the 100 dialogues was summarized using 13 models, in addition to one human reference summary. The present paper uses the generated outputs that were used in the original paper. The original summary outputs are stored inside `.\reproduce\analysis\models_eval_new`, inside a a file called `summs.txt` stored inside its respective directory. Each directory represents a model with an ID, as can be seen in the table underneath. Model-ID `A` contains human made summaries. The scores aquired through the metric calculations are also stored in these directories.

| Model-ID | Model        |
|----------|--------------|
|   A      | Reference|
|   B      | LONGEST-3|
|   C      | LEAD-3|
|   D      | [PGN](https://doi.org/10.18653/v1/P17-1099)|
|   E      | [Transformer](https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf)|
|   F      | [BART](https://doi.org/10.18653/v1/2020.acl-main.703)|
|   G      | [PEGASUS](https://arxiv.org/pdf/1912.08777.pdf)|
|   H      | [UniLM](https://proceedings.neurips.cc/paper/2019/file/c20bb2d9a50d5ac1f713f8b34d9aac5a-Paper.pdf)|
|   I      | [CODS](https://doi.org/10.18653/v1/2021.findings-acl.454)|
|   J      | [ConvoSumm](https://doi.org/10.18653/v1/2021.acl-long.535)|
|   K      | [MV-BART](https://doi.org/10.18653/v1/2020.emnlp-main.336)|
|   L      | [PLM-BART](https://doi.org/10.18653/v1/2021.acl-long.117)|
|   M      | [Ctrl-DiaSumm](https://aclanthology.org/2021.emnlp-main.8/)|
|   N      | [S-BART](https://aclanthology.org/2021.naacl-main.109/)|


## Results

The original paper’s main claims were reproduced. While not all original authors arguments were replicated (e.g. ROUGE scoring higher for relevance), the correlation between metrics and human judgments showed similar tendencies as in the original paper. The annotations correlated with the original at a Pearson score of 0.6, sufficient for reproducing main claims.





