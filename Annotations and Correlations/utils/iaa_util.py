import numpy as np
import re

# adjusted functions for our input data
def chonker(seq, size):
    return [seq[pos:pos+size] for pos in range(0, len(seq), size)]

def filter_noise_scores(t_1, t_2, t_3, n):
    """Average out over the scores of multiple annotators. Take the majority 
       vote when possible, or the average if all scores are different
       return numpy.array (100, 14)

    Args:
        t_1 (list): List of lists of equal length
        t_2 (list): List of lists of equal length
        t_3 (list): List of lists of equal length

    Returns:
        res: numpy.array (100, 14)
    """
    
    s_1 = t_1[:]
    s_2 = t_2[:]
    s_3 = t_3[:]
    res = np.zeros((n, 14))
    for i, (r_1, r_2, r_3) in enumerate(zip(s_1, s_2, s_3)):
        for j, (a, b, c) in enumerate(zip(r_1, r_2, r_3)):
            if a == b and a != c:
                res[i,j] = a
            elif a == c and a != b:
                res[i,j] = c
            elif b == c and a != b:
                res[i,j] = b
            else:
                res[i,j] = (a + b + c) / 3
    return res

def no_noise_lists(t_1, t_2, t_3):
    """Filter odd one out scores by replacing odd score with NaN.

    Args:
        t_1 (list): List of lists of equal length
        t_2 (list): List of lists of equal length
        t_3 (list): List of lists of equal length

    Returns:
        _type_: _description_
    """
        
    s_1 = t_1[:]
    s_2 = t_2[:]
    s_3 = t_3[:]

    new_ann1 = []
    new_ann2 = []
    new_ann3 = []
    nans=0
    for (r_1, r_2, r_3) in zip(s_1, s_2, s_3):
        for (a, b, c) in zip(r_1, r_2, r_3):
            if a == b and a != c:
                new_ann1.append(a)
                new_ann2.append(b)
                new_ann3.append(np.nan)
                nans+=1
            elif a == c and a != b:
                new_ann1.append(a)
                new_ann2.append(np.nan)
                new_ann3.append(c)
                nans+=1
            elif b == c and a != b:
                new_ann1.append(np.nan)
                new_ann2.append(b)
                new_ann3.append(c)
                nans+=1
            else:
                new_ann1.append(a)
                new_ann2.append(b)
                new_ann3.append(c)

    print('Number of scores that were not filtered:', 4200-nans)
    return new_ann1, new_ann2, new_ann3


def dia_ex(val):
    """Extract only the dialogue from the html type text

    Args:
        val (str): string representing the dialogue and summary to fit 
        html display methods

    Returns:
        new_val: string containing only the dialogue
    """
    new_val = re.sub(r'<br>|<font color=\'blue\'>|</font>|(?<!-)---(?!-)', '', val)
    new_val = re.sub(r'\s{3,}', ' ', new_val)
    new_val = new_val.split('Summary:')[0].strip()
    return new_val

def sum_ex(val):
    """Extract only the summary from the html type text

    Args:
        val (str): string representing the dialogue and summary to fit 
        html display methods

    Returns:
        new_val: string containing only the summary
    """
    new_val = re.sub(r'<br>|<font color=\'blue\'>|</font>|(?<!-)---(?!-)', '', val)
    new_val = re.sub(r'\s{3,}', ' ', new_val)
    new_val = new_val.split('Summary:')[1].strip()
    return new_val