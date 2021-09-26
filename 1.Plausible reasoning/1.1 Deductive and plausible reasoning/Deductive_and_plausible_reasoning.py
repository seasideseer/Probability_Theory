
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 09:29:25 2021
@author: user
"""

import numpy as np
import pandas as pd
    
def syllogisms_sample(A_True_prob=0.5,B_True_prob=0.5,print_sample_result=True):
    A = np.random.choice([0,1],p=[A_True_prob,(1-A_True_prob)])
    if A == 0:
        B = 0
    else:
        B = np.random.choice([0,1],p=[B_True_prob,(1-B_True_prob)])
    if print_sample_result:
        print(np.r_[A,B])
    return(np.r_[A,B])

def syllogisms_trial(A_True_prob=0.5,B_True_prob=0.5,B=1000,
                     print_sample_result=False,
                     print_trial_result=True):
    trial_sample = np.zeros([B,2])
    for i in range(B):
        ab=syllogisms_sample(A_True_prob=A_True_prob,
                             B_True_prob=B_True_prob,
                             print_sample_result=print_sample_result)
        trial_sample[i,:]=ab
    trial_sample=pd.DataFrame(trial_sample)
    trial_sample.columns=['A','B']
    trial_result=pd.DataFrame(trial_sample.groupby(['A','B']).size())
    trial_result=trial_result.reset_index()
    trial_result=trial_result.rename(columns={0:'count'})
    if print_trial_result:
        print(trial_result)
    return(trial_sample,trial_result)

trial_sample,trial_result=syllogisms_trial()
