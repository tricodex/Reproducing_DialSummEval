# requirements
import numpy as np
import pandas as pd
import krippendorff
import json
import itertools

from utils.iaa_util import chonker, no_noise_lists

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

### Replace noisy annotations ###
print('Original Paper:')
coherence_nonoise1, coherence_nonoise2, coherence_nonoise3 = no_noise_lists(coherence_ann1, coherence_ann2, coherence_ann3)
consistency_nonoise1,consistency_nonoise2,consistency_nonoise3 = no_noise_lists(consistency_ann1, consistency_ann2, consistency_ann3)
fluency_nonoise1, fluency_nonoise2,fluency_nonoise3 = no_noise_lists(fluency_ann1, fluency_ann2, fluency_ann3)
relevance_nonoise1,relevance_nonoise2,relevance_nonoise3 = no_noise_lists(relevance_ann1, relevance_ann2, relevance_ann3)

# Original paper's annotations
print('Present paper')
orig_coherence_nonoise1, orig_coherence_nonoise2, orig_coherence_nonoise3 = no_noise_lists(coherence_orig_ann1, coherence_orig_ann2, coherence_orig_ann3)
orig_consistency_nonoise1, orig_consistency_nonoise2, orig_consistency_nonoise3 = no_noise_lists(consistency_orig_ann1, consistency_orig_ann2, consistency_orig_ann3)
orig_fluency_nonoise1, orig_fluency_nonoise2, orig_fluency_nonoise3 = no_noise_lists(fluency_orig_ann1, fluency_orig_ann2, fluency_orig_ann3)
orig_relevance_nonoise1, orig_relevance_nonoise2, orig_relevance_nonoise3 = no_noise_lists(relevance_orig_ann1, relevance_orig_ann2, relevance_orig_ann3)


### Calculate IAA ###
# Original IAA
coherence_IAA = krippendorff.alpha(reliability_data=[list(orig_ann1['coherence_results']),list(orig_ann2['coherence_results']),list(orig_ann3['coherence_results'])], level_of_measurement="interval")
fluency_IAA = krippendorff.alpha(reliability_data=[list(orig_ann1['fluency_results']),list(orig_ann2['fluency_results']),list(orig_ann3['fluency_results'])],level_of_measurement="interval")
consistency_IAA = krippendorff.alpha(reliability_data=[list(orig_ann1['consistency_results']),list(orig_ann2['consistency_results']),list(orig_ann3['consistency_results'])],level_of_measurement="interval")
relevance_IAA = krippendorff.alpha(reliability_data=[list(orig_ann1['relevance_results']),list(orig_ann2['relevance_results']),list(orig_ann3['relevance_results'])],level_of_measurement="interval")
print(f'Original IAA scores:\nCoherence: {coherence_IAA} \nConsistency: {consistency_IAA} \nFluency: {fluency_IAA} \nRelevance: {relevance_IAA}')
# cleaned original
coherence_IAA = krippendorff.alpha(reliability_data=[orig_coherence_nonoise1, orig_coherence_nonoise2, orig_coherence_nonoise3], level_of_measurement="interval")
fluency_IAA = krippendorff.alpha(reliability_data=[orig_fluency_nonoise1, orig_fluency_nonoise2, orig_fluency_nonoise3],level_of_measurement="interval")
consistency_IAA = krippendorff.alpha(reliability_data=[orig_consistency_nonoise1, orig_consistency_nonoise2, orig_consistency_nonoise3],level_of_measurement="interval")
relevance_IAA = krippendorff.alpha(reliability_data=[orig_relevance_nonoise1, orig_relevance_nonoise2, orig_relevance_nonoise3],level_of_measurement="interval")
print(f'Original IAA scores (cleaned):\nCoherence: {coherence_IAA} \nConsistency: {consistency_IAA} \nFluency: {fluency_IAA} \nRelevance: {relevance_IAA}')

# Our IAA
coherence_IAA = krippendorff.alpha(reliability_data=[list(ann1['coherence_results']),list(ann2['coherence_results']),list(ann3['coherence_results'])], level_of_measurement="interval")
fluency_IAA = krippendorff.alpha(reliability_data=[list(ann1['fluency_results']),list(ann2['fluency_results']),list(ann3['fluency_results'])],level_of_measurement="interval")
consistency_IAA = krippendorff.alpha(reliability_data=[list(ann1['consistency_results']),list(ann2['consistency_results']),list(ann3['consistency_results'])],level_of_measurement="interval")
relevance_IAA = krippendorff.alpha(reliability_data=[list(ann1['relevance_results']),list(ann2['relevance_results']),list(ann3['relevance_results'])],level_of_measurement="interval")
print(f'Our IAA scores:\nCoherence: {coherence_IAA} \nConsistency: {consistency_IAA} \nFluency: {fluency_IAA} \nRelevance: {relevance_IAA}')

# Our IAA cleaned
coherence_IAA = krippendorff.alpha(reliability_data=[coherence_nonoise1, coherence_nonoise2, coherence_nonoise3], level_of_measurement="interval")
fluency_IAA = krippendorff.alpha(reliability_data=[fluency_nonoise1, fluency_nonoise2, fluency_nonoise3],level_of_measurement="interval")
consistency_IAA = krippendorff.alpha(reliability_data=[consistency_nonoise1, consistency_nonoise2, consistency_nonoise3],level_of_measurement="interval")
relevance_IAA = krippendorff.alpha(reliability_data=[relevance_nonoise1, relevance_nonoise2, relevance_nonoise3],level_of_measurement="interval")
print(f'Our IAA scores (cleaned):\nCoherence: {coherence_IAA} \nConsistency: {consistency_IAA} \nFluency: {fluency_IAA} \nRelevance: {relevance_IAA}')

