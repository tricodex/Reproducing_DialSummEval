## Analysis

The following noteworthy functions are included in analysis.py:
- `get_human_scores`: reads human ratings from a CSV file and returns the ratings for a specified dimension as a list of lists. There are 3 versions of this function inside the file.
- `print_human_ratings`: prints the average human ratings for each model for a specified rating dimension. It works by:
  - Reading in the human ratings from the appropriate CSV file using the `get_human_scores` function.
  - Chunking the human ratings into lists of length 14 (one list for each model).
  - Returning the list of human ratings for the specified dimension.
- `get_metric_scores`: reads automatic evaluation scores from a CSV file and returns the scores as a NumPy array
- `print_rouge_sample`: prints out the Rouge- 1, 2 and L scores for each model in a LateX table format.
- `filter_noise_scores`: filters noise ratings from human ratings and returns the average value as a NumPy array. It works by:
  - Initializing an empty NumPy array to hold the filtered ratings.
  - Iterating through the three input arrays using the `enumerate` function, with the index representing the rating number and the values representing the ratings given by each annotator.
  - For each set of ratings, comparing the values and assigning the value that appears twice to the filtered ratings array. If no value appears twice, taking the average of the three 
  - Return the filtered ratings array.
- `cal_pearsonr`: calculates Pearson correlations between human ratings and automatic evaluation scores for a specified rating dimension and a list of metrics, and returns the correlations as a dictionary. To do this, the function:
  - Reads human ratings for the specified dimension and filters out noise ratings.
  - Reads automatic evaluation scores for the specified list of metrics
  - Calculates Pearson correlations between the filtered human ratings and the automatic evaluation scores for each metric.
  - oReturns the correlations as a dictionary with the metric names as keys and the correlations as values.
