# requirements
import numpy as np
import pandas as pd
import itertools

from utils.iaa_util import chonker, filter_noise_scores, dia_ex, sum_ex

# Filepaths
# Ablation results
ann1_ablation_path = 'data/ablation_ann1.xlsx'
ann2_ablation_path = 'data/ablation_ann2.xlsx'
ann3_ablation_path = 'data/ablation_ann3.xlsx'

# Full results
ann1_results_path = f'data/saved_df_ann1.csv'
ann2_results_path = f'data/saved_df_ann2.csv'
ann3_results_path = f'data/saved_df_ann3.csv'


# Present paper data
ann1 = pd.read_csv(ann1_results_path, delimiter=';')
ann2 = pd.read_csv(ann2_results_path, delimiter=';')
ann3 = pd.read_csv(ann3_results_path, delimiter=';')

# Ablation data
tab_names = ['A', 'B', 'C', 'D', 'E' ,'F', 'G' ,'H' ,'I','J' ,'K', 'L', 'M' , 'N']
df_1 = pd.concat(pd.read_excel(ann1_ablation_path, sheet_name=tab_names))
df_2 = pd.concat(pd.read_excel(ann2_ablation_path, sheet_name=tab_names))
df_3 = pd.concat(pd.read_excel(ann3_ablation_path, sheet_name=tab_names))

# The full data has its text displayed differently from the ablation data
# The following code aligns this:
for df in [ann1, ann2, ann3]:
    df['dialogue'] = df.texts.transform(dia_ex)
    df['summary'] = df.texts.transform(sum_ex)

# extract dialogues from full data to adhere to only the dialogues used in the ablation
ann1_selection = ann1[ann1['summary'].isin(list(df_1['summary']))]
ann2_selection = ann2[ann2['summary'].isin(list(df_2['summary']))]
ann3_selection = ann3[ann3['summary'].isin(list(df_3['summary']))]


# transform the list of evaluation values into: [[n*14]*10]
# selection from full results
coherence_ann1_sel = chonker(list(ann1_selection['coherence_results']), 14)
coherence_ann2_sel = chonker(list(ann2_selection['coherence_results']), 14)
coherence_ann3_sel = chonker(list(ann3_selection['coherence_results']), 14)

consistency_ann1_sel = chonker(list(ann1_selection['consistency_results']), 14)
consistency_ann2_sel = chonker(list(ann2_selection['consistency_results']), 14)
consistency_ann3_sel = chonker(list(ann3_selection['consistency_results']), 14)

fluency_ann1_sel = chonker(list(ann1_selection['fluency_results']), 14)
fluency_ann2_sel = chonker(list(ann2_selection['fluency_results']), 14)
fluency_ann3_sel = chonker(list(ann3_selection['fluency_results']), 14)

relevance_ann1_sel = chonker(list(ann1_selection['relevance_results']), 14)
relevance_ann2_sel = chonker(list(ann2_selection['relevance_results']), 14)
relevance_ann3_sel = chonker(list(ann3_selection['relevance_results']), 14)


# new ablation results
coherence_ann1_abl = [[item[i] for item in chonker(list(df_1['Coherence']), 10)] for i in range(10)]
coherence_ann2_abl = [[item[i] for item in chonker(list(df_2['Coherence']), 10)] for i in range(10)]
coherence_ann3_abl = [[item[i] for item in chonker(list(df_3['Coherence']), 10)] for i in range(10)]

consistency_ann1_abl = [[item[i] for item in chonker(list(df_1['Consistency']), 10)] for i in range(10)]
consistency_ann2_abl = [[item[i] for item in chonker(list(df_2['Consistency']), 10)] for i in range(10)]
consistency_ann3_abl = [[item[i] for item in chonker(list(df_3['Consistency']), 10)] for i in range(10)]

fluency_ann1_abl = [[item[i] for item in chonker(list(df_1['Fluency']), 10)] for i in range(10)]
fluency_ann2_abl = [[item[i] for item in chonker(list(df_2['Fluency']), 10)] for i in range(10)]
fluency_ann3_abl = [[item[i] for item in chonker(list(df_3['Fluency']), 10)] for i in range(10)]

relevance_ann1_abl = [[item[i] for item in chonker(list(df_1['Relevance']), 10)] for i in range(10)]
relevance_ann2_abl = [[item[i] for item in chonker(list(df_2['Relevance']), 10)] for i in range(10)]
relevance_ann3_abl = [[item[i] for item in chonker(list(df_3['Relevance']), 10)] for i in range(10)]

# Average out scores from the three annotators
coherence_filtered_sel = filter_noise_scores(coherence_ann1_sel, coherence_ann2_sel, coherence_ann3_sel, 10)
consistency_filtered_sel = filter_noise_scores(consistency_ann1_sel, consistency_ann2_sel, consistency_ann3_sel, 10)
fluency_filtered_sel = filter_noise_scores(fluency_ann1_sel, fluency_ann2_sel, fluency_ann3_sel, 10)
relevance_filtered_sel = filter_noise_scores(relevance_ann1_sel, relevance_ann2_sel, relevance_ann3_sel, 10) 

coherence_filtered_abl = filter_noise_scores(coherence_ann1_abl, coherence_ann2_abl, coherence_ann3_abl, 10)
consistency_filtered_abl = filter_noise_scores(consistency_ann1_abl, consistency_ann2_abl, consistency_ann3_abl, 10)
fluency_filtered_abl = filter_noise_scores(fluency_ann1_abl, fluency_ann2_abl, fluency_ann3_abl, 10)
relevance_filtered_abl = filter_noise_scores(relevance_ann1_abl, relevance_ann2_abl, relevance_ann3_abl, 10) 

# Flatten dimensions
list_coh_fil = list(itertools.chain(*coherence_filtered_sel))
list_coh_fil_orig = list(itertools.chain(*coherence_filtered_abl))
list_con_fil = list(itertools.chain(*consistency_filtered_sel))
list_con_fil_orig = list(itertools.chain(*consistency_filtered_abl))
list_flu_fil = list(itertools.chain(*fluency_filtered_sel))
list_flu_fil_orig = list(itertools.chain(*fluency_filtered_abl))
list_rel_fil = list(itertools.chain(*relevance_filtered_sel))
list_rel_fil_orig = list(itertools.chain(*relevance_filtered_abl))

# print correlation between ablation and full results for each dimension
print('Coherence correlation', round(np.corrcoef(list_coh_fil, list_coh_fil_orig)[0][1],3))
print('Consistency correlation', round(np.corrcoef(list_con_fil, list_con_fil_orig)[0][1],3))
print('Fluency correlation', round(np.corrcoef(list_flu_fil, list_flu_fil_orig)[0][1],3))
print('Relevance correlation', round(np.corrcoef(list_rel_fil, list_rel_fil_orig)[0][1],3))