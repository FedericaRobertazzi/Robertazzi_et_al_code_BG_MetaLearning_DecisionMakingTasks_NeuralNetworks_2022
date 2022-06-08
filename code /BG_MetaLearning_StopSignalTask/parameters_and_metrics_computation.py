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
    n_Stop_Signal=sum(np.logical_and((trial_type==0), (reward_vec_crucial==0)))
    n_Stop_Signal_correct=sum(np.logical_and((trial_type==0), (reward_vec_crucial==1)))
    
    # f_Go=np.zeros((n_Go,200))
    # f_Stop_Signal=np.zeros((n_Stop_Signal,200))
    # f_Stop_Signal_correct=np.zeros((n_Stop_Signal_correct,200))
    
    # count_Go =0
    # count_Stop_Signal=0
    # count_Stop_Signal_correct=0
    # for j in range(len(action_vec_crucial)):
    #     [x,y]=action_vec_to_mat(action_vec_crucial[j])
    #     f=firing_PMC[x,y,start_stimuli_crucial[j]:(start_stimuli_crucial[j]+200)]
    #     if trial_type[j]==1:
    #         f_Go[count_Go,:]=f
    #         count_Go=count_Go+1
    #     if ((trial_type[j]==0)and (reward_vec_crucial[j]==0)):
    #         f_Stop_Signal[count_Stop_Signal,:]=f
    #         count_Stop_Signal=count_Stop_Signal+1
    #     if ((trial_type[j]==0)and (reward_vec_crucial[j]==1)):
    #           f_Stop_Signal_correct[count_Stop_Signal_correct,:]=f
    #           count_Stop_Signal_correct=count_Stop_Signal_correct+1

    for i in range(len(action_vec_crucial)):
        [x,y]=action_vec_to_mat(action_vec_crucial[i])
        f=firing_PMC[x,y,start_stimuli_crucial[i]:(start_stimuli_crucial[i]+200)]
        max_PMC.append(max(f))
        var_f_1=0.25*(max(f)-min(f))+min(f) 
        react_time_1.append(np.where(f>=var_f_1)[0][0]) #0.25 threshold
    
    a_1=np.array(react_time_1) #0.25
    react_time_Go_1= a_1[trial_type==1]  
    react_time_Stop_Signal_total_1= a_1[trial_type==0]   
    react_time_Stop_Signal_1= a_1[np.logical_and((trial_type==0), (reward_vec_crucial==0)) ]  
    react_time_Stop_Signal_correct_1= a_1[np.logical_and((trial_type==0), (reward_vec_crucial==1))]

    b=np.array(max_PMC)
    max_PMC_Go=b[trial_type==1] 
    max_PMC_Stop_Signal_total=b[trial_type==0] 
    max_PMC_Stop_Signal=b[np.logical_and((trial_type==0), (reward_vec_crucial==0))]  
    max_PMC_Stop_Signal_correct=b[np.logical_and((trial_type==0), (reward_vec_crucial==1))] 
  
    c=np.array(Pmax)
    Pmax_Go=c[np.where(trial_type==1)] 
    Pmax_Stop_Signal_total=c[np.where(trial_type==0)] 
    Pmax_Stop_Signal=c[np.where(np.logical_and((trial_type==0), (reward_vec_crucial==0)))] 
    Pmax_Stop_Signal_correct=c[np.where(np.logical_and((trial_type==0), (reward_vec_crucial==1)))] 
    
    return n_Go, n_Stop_Signal,n_Stop_Signal_correct, react_time_Go_1, react_time_Stop_Signal_total_1, react_time_Stop_Signal_1,react_time_Stop_Signal_correct_1, max_PMC_Go,max_PMC_Stop_Signal_total, max_PMC_Stop_Signal,max_PMC_Stop_Signal_correct, Pmax_Go,Pmax_Stop_Signal_total,Pmax_Stop_Signal, Pmax_Stop_Signal_correct

def compute_SSRT(react_time_Go, delay_type, trial_type, time_crucial_trial,right_inhibition):
    #quantile method ((Band et al., 2003)
    delay_type_crucial=delay_type[np.where(time_crucial_trial)]
    delay_type_Stop_Signal=delay_type_crucial[trial_type==0]
    ssd=np.mean(delay_type_Stop_Signal)
    pfailure=(100-right_inhibition)
    print(pfailure)
    react_time_Go_sorted=np.sort(react_time_Go)
    SSRT=(np.percentile(react_time_Go_sorted,pfailure))-ssd
    print('delay type StopSignal',delay_type_Stop_Signal) 
    return SSRT, delay_type_Stop_Signal

def compute_right_inhibition(reward_vec,trial_type, time_crucial_trial):
    reward_vec_crucial=reward_vec[np.where(time_crucial_trial)]
    reward_vec_Stop_Signal=reward_vec_crucial[trial_type==0]
    print('reward vec crucial',reward_vec_crucial)
    return np.mean( reward_vec_Stop_Signal)*100
     
def compute_global_accuracy(reward_vec,time_crucial_trial):
    reward_vec_crucial=reward_vec[np.where(time_crucial_trial)]
    accuracy=np.mean(reward_vec_crucial)*100
    return accuracy
