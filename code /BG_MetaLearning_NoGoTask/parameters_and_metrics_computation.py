#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: federica robertazzi
"""
import numpy as np
from utility import  action_vec_to_mat

def compute_net_parameters(firing_PMC,start_stimuli,trial_type,action_vec,time_crucial_trial,delay_type,Pmax,reward_vec): 
    react_time_1=[]
    max_PMC=[]
    
    reward_vec_crucial=reward_vec[np.where(time_crucial_trial)]
    action_vec_crucial=action_vec[np.where(time_crucial_trial)]
    start_stimuli_crucial=start_stimuli[np.where(time_crucial_trial)]
    
    n_Go=sum(trial_type==1)
    n_No_Go=sum(np.logical_and((trial_type==0), (reward_vec_crucial==0)))
    n_No_Go_correct=sum(np.logical_and((trial_type==0), (reward_vec_crucial==1)))

    # f_Go=np.zeros((n_Go,200))
    # f_No_Go=np.zeros((n_No_Go,200))
    # f_No_Go_correct=np.zeros((n_No_Go_correct,200))
    
    # count_Go =0
    # count_No_Go=0
    # count_No_Go_correct=0
    # for j in range(len(action_vec_crucial)):
    #     [x,y]=action_vec_to_mat(action_vec_crucial[j])
    #     f=firing_PMC[x,y,start_stimuli_crucial[j]:(start_stimuli_crucial[j]+200)]
    #     if trial_type[j]==1:
    #         f_Go[count_Go,:]=f
    #         count_Go=count_Go+1
    #     if ((trial_type[j]==0)and (reward_vec_crucial[j]==0)):
    #         f_No_Go[count_No_Go,:]=f
    #         count_No_Go=count_No_Go+1
    #     if ((trial_type[j]==0)and (reward_vec_crucial[j]==1)):
    #           f_No_Go_correct[count_No_Go_correct,:]=f
    #           count_No_Go_correct=count_No_Go_correct+1

    for i in range(len(action_vec_crucial)):
        [x,y]=action_vec_to_mat(action_vec_crucial[i])
        f=firing_PMC[x,y,start_stimuli_crucial[i]:(start_stimuli_crucial[i]+200)]
        max_PMC.append(max(f))
        var_f_1=0.25*(max(f)-min(f))+min(f) 
        react_time_1.append(np.where(f>=var_f_1)[0][0]) #0.25 threshold
    
    a_1=np.array(react_time_1) #0.25
    react_time_Go_1= a_1[trial_type==1]  
    react_time_No_Go_total_1= a_1[trial_type==0]   
    react_time_No_Go_1= a_1[np.logical_and((trial_type==0), (reward_vec_crucial==0)) ]  
    react_time_No_Go_correct_1= a_1[np.logical_and((trial_type==0), (reward_vec_crucial==1))]

    b=np.array(max_PMC)
    max_PMC_Go=b[trial_type==1] 
    max_PMC_No_Go_total=b[trial_type==0] 
    max_PMC_No_Go=b[np.logical_and((trial_type==0), (reward_vec_crucial==0))]  
    max_PMC_No_Go_correct=b[np.logical_and((trial_type==0), (reward_vec_crucial==1))] 
  
    c=np.array(Pmax)
    Pmax_Go=c[np.where(trial_type==1)] 
    Pmax_No_Go_total=c[np.where(trial_type==0)] 
    Pmax_No_Go=c[np.where(np.logical_and((trial_type==0), (reward_vec_crucial==0)))] 
    Pmax_No_Go_correct=c[np.where(np.logical_and((trial_type==0), (reward_vec_crucial==1)))] 
    
    return n_Go, n_No_Go,n_No_Go_correct, react_time_Go_1, react_time_No_Go_total_1, react_time_No_Go_1,react_time_No_Go_correct_1, max_PMC_Go,max_PMC_No_Go_total, max_PMC_No_Go,max_PMC_No_Go_correct, Pmax_Go,Pmax_No_Go_total,Pmax_No_Go, Pmax_No_Go_correct

def compute_right_inhibition(reward_vec,trial_type, time_crucial_trial):
    reward_vec_crucial=reward_vec[np.where(time_crucial_trial)]
    reward_vec_No_Go=reward_vec_crucial[trial_type==0]
    print('reward vec crucial',reward_vec_crucial)
    return np.mean( reward_vec_No_Go)*100
     
def compute_global_accuracy(reward_vec,time_crucial_trial):
    reward_vec_crucial=reward_vec[np.where(time_crucial_trial)]
    accuracy=np.mean(reward_vec_crucial)*100
    return accuracy
