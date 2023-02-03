# requirements
import numpy as np
import pandas as pd
import json
import itertools

from utils.iaa_util import chonker, filter_noise_scores

### Filepaths ###
# Full results
ann1_results_path = f'data/saved_df_ann1.csv'
ann2_results_path = f'data/saved_df_ann2.csv'
ann3_results_path = f'data/saved_df_ann3.csv'

# Original paper results
original_results_path = 'data/original_human_judgment.jsonl'

### Load data ###
# Present paper data
ann1 = pd.read_csv(ann1_results_path, delimiter=';')
ann2 = pd.read_csv(ann2_results_path, delimiter=';')
ann3 = pd.read_csv(ann3_results_path, delimiter=';')

# original data
fname = original_results_path
data = [] #NEWstart
with open(fname, 'r', encoding='utf-8') as f:
    for line in f:
        data.append(json.loads(line.rstrip('\n|\r')))

### transform original data to match our data ###
original_annotator_scores= []

# a row in the data: id, dialogue, summary, annotations, model_id
# loop through annotator and each dimension 
for annotator in [0,1,2]:  
    scores = []  
    for type in ['consistency', 'coherence', 'fluency', 'relevance']:
        list_annotations=[]
        # store all annotations for an annotator 
        for row in data:
            annotations = row.get('annotations')
            list_annotations.append(annotations[annotator])
        dimension_list=[]
        # 
        for dimensions in list_annotations:
            dimension=dimensions.get(type.lower())
            dimension_list.append(dimension)
        scores.append(dimension_list)
    original_annotator_scores.append(scores)

orig_ann1 = pd.DataFrame(zip(original_annotator_scores[0][0], original_annotator_scores[0][1], original_annotator_scores[0][2], original_annotator_scores[0][3]), 
        columns=['consistency_results', 'coherence_results', 'fluency_results', 'relevance_results'])

orig_ann2 = pd.DataFrame(zip(original_annotator_scores[1][0], original_annotator_scores[1][1], original_annotator_scores[1][2], original_annotator_scores[1][3]), 
        columns=['consistency_results', 'coherence_results', 'fluency_results', 'relevance_results'])

orig_ann3 = pd.DataFrame(zip(original_annotator_scores[2][0], original_annotator_scores[2][1], original_annotator_scores[2][2], original_annotator_scores[2][3]), 
        columns=['consistency_results', 'coherence_results', 'fluency_results', 'relevance_results'])

### Prepare Data for Calculations ###

# transform the list of evaluation values into: [[n*14]*100]
# Present paper annotations
coherence_ann1 = chonker(list(ann1['coherence_results']), 14)
coherence_ann2 = chonker(list(ann2['coherence_results']), 14)
coherence_ann3 = chonker(list(ann3['coherence_results']), 14)

consistency_ann1 = chonker(list(ann1['consistency_results']), 14)
consistency_ann2 = chonker(list(ann2['consistency_results']), 14)
consistency_ann3 = chonker(list(ann3['consistency_results']), 14)

fluency_ann1 = chonker(list(ann1['fluency_results']), 14)
fluency_ann2 = chonker(list(ann2['fluency_results']), 14)
fluency_ann3 = chonker(list(ann3['fluency_results']), 14)

relevance_ann1 = chonker(list(ann1['relevance_results']), 14)
relevance_ann2 = chonker(list(ann2['relevance_results']), 14)
relevance_ann3 = chonker(list(ann3['relevance_results']), 14)

# Original Paper's annotations
coherence_orig_ann1 = chonker(list(orig_ann1['coherence_results']), 14)
coherence_orig_ann2 = chonker(list(orig_ann2['coherence_results']), 14)
coherence_orig_ann3 = chonker(list(orig_ann3['coherence_results']), 14)

consistency_orig_ann1 = chonker(list(orig_ann1['consistency_results']), 14)
consistency_orig_ann2 = chonker(list(orig_ann2['consistency_results']), 14)
consistency_orig_ann3 = chonker(list(orig_ann3['consistency_results']), 14)

fluency_orig_ann1 = chonker(list(orig_ann1['fluency_results']), 14)
fluency_orig_ann2 = chonker(list(orig_ann2['fluency_results']), 14)
fluency_orig_ann3 = chonker(list(orig_ann3['fluency_results']), 14)

relevance_orig_ann1 = chonker(list(orig_ann1['relevance_results']), 14)
relevance_orig_ann2 = chonker(list(orig_ann2['relevance_results']), 14)
relevance_orig_ann3 = chonker(list(orig_ann3['relevance_results']), 14)


### Average Annotator scores ###
# Present paper results
coherence_filtered = filter_noise_scores(coherence_ann1, coherence_ann2, coherence_ann3, 100)
consistency_filtered = filter_noise_scores(consistency_ann1, consistency_ann2, consistency_ann3, 100)
fluency_filtered = filter_noise_scores(fluency_ann1, fluency_ann2, fluency_ann3, 100)
relevance_filtered = filter_noise_scores(relevance_ann1, relevance_ann2, relevance_ann3, 100) 

# original paper results
orig_coherence_filtered = filter_noise_scores(coherence_orig_ann1, coherence_orig_ann2, coherence_orig_ann3, 100)
orig_consistency_filtered = filter_noise_scores(consistency_orig_ann1, consistency_orig_ann2, consistency_orig_ann3, 100)
orig_fluency_filtered = filter_noise_scores(fluency_orig_ann1, fluency_orig_ann2, fluency_orig_ann3, 100)
orig_relevance_filtered = filter_noise_scores(relevance_orig_ann1, relevance_orig_ann2, relevance_orig_ann3, 100)


### Calculate Correlation ###
# first transform filtered arrays into a single long list
# for each dimension, for both present paper and original results
list_coh_fil = list(itertools.chain(*coherence_filtered))
list_coh_fil_orig = list(itertools.chain(*orig_coherence_filtered))

list_con_fil = list(itertools.chain(*consistency_filtered))
list_con_fil_orig = list(itertools.chain(*orig_consistency_filtered))

list_flu_fil = list(itertools.chain(*fluency_filtered))
list_flu_fil_orig = list(itertools.chain(*orig_fluency_filtered))

list_rel_fil = list(itertools.chain(*relevance_filtered))
list_rel_fil_orig = list(itertools.chain(*orig_relevance_filtered))

print('Coherence correlation', round(np.corrcoef(list_coh_fil, list_coh_fil_orig)[0][1],3))
print('Consistency correlation', round(np.corrcoef(list_con_fil, list_con_fil_orig)[0][1],3))
print('Fluency correlation', round(np.corrcoef(list_flu_fil, list_flu_fil_orig)[0][1],3))
print('Relevance correlation', round(np.corrcoef(list_rel_fil, list_rel_fil_orig)[0][1],3))