#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: federicarobertazzi
"""
import numpy as np

def Boltzman_softmax_equation(beta,acc,ai):
    totQ = 0
    for i in range(2):
       for j in range(2):
            totQ = totQ + np.exp(beta*acc[i][j].Q)
    P = (np.exp(beta*acc[ai[0]][ai[1]].Q))/(totQ)
    return P

def motor_output(PMC):
    PMC = [j for sub in PMC for j in sub] 
    action_selected= PMC[0]  
    imax = 0
    for i in range(len(PMC)):
        if(PMC[i]>action_selected):
            action_selected=PMC[i]
            imax = i
    return action_selected,imax
            
def compute_reward(imax,r_values):
    reward = r_values[imax]
    return reward

def check_pcc(reward,count):
    if count<4:
        if (reward == 1):
            count=count+1
        else:
            count=0
    else:
        count=count+1
    return count

def check_salience(visual_inp,salience0):
    salience = []
    for n in range(visual_inp.shape[1]):
        if n == 0:
            salience.append(salience0)
        elif ((visual_inp[:,n-1]!=visual_inp[:,n]).any()): 
             salience.append(True)
        else:
            salience.append(False)
    return salience

def visual_input(niter,inp_start,inp_stop):    
    s = len(inp_start)
    l = len(inp_start[0])
    matrix_inp = np.zeros((s,niter))
    for n in range(niter):#tempo
        for i in range(s):#categories 
            for j in range(l):#stimuli
                if n <= inp_stop[i][j] and n >= inp_start[i][j]:                   
                    matrix_inp[i][n]=1
    return matrix_inp

def get_activity(Neu):
    curr_Neu = [[0 for i in range(2)] for j in range(2)]
    for i in range(2):
        for j in range(2):
            curr_Neu[i][j] = Neu[i][j].out
    return curr_Neu

def get_QAct(Q):
    QAct = [[0 for i in range(2)] for j in range(2)]
    for i in range(2):
        for j in range(2):
            QAct[i][j] = Q[i][j].memory[-1]
    return QAct

def get_QPrev(Q):
    QPrev = [[0 for i in range(2)] for j in range(2)]
    for i in range(2):
        for j in range(2):
            QPrev[i][j] = Q[i][j].memory[-2]
    return QPrev

def prevent_Qstack(ACC_Q):
    for i in range(2):
        for j in range(2):
            if i == 0 and j == 0 and ACC_Q[i][j].Q < 0.3:
               ACC_Q[i][j].Q = 0.52 + np.random.uniform(0,0.1)
            elif i == 0 and j == 1 and ACC_Q[i][j].Q < 0.3:
               ACC_Q[i][j].Q = 0.52 +np.random.uniform(0,0.1)
            elif i == 1 and j == 0 and ACC_Q[i][j].Q < 0.3:
               ACC_Q[i][j].Q = 0.52 + np.random.uniform(0,0.1)
    return ACC_Q

def reset_Q(ACC_Q):
    for i in range(2):
        for j in range(2):
            if i == 0 and j == 0:
               ACC_Q[i][j].Q = 0.2+ np.random.uniform(0,0.3)
            elif i == 0 and j == 1:
               ACC_Q[i][j].Q = 0.2+np.random.uniform(0,0.3)
    return ACC_Q

def reset_beta(beta):
    beta[-1]=0.2 + np.random.uniform(0,0.1)
    return beta

def stationary_stochastic_reward(rew,rew_matrix):
    temp = [0  for j in range(len(rew))]
    for i in range(len(rew)):
        if rew[i] == 1:
           temp[i] =1#custom 
        else:
           temp[i] = 0#custom
    rew_values = rew_matrix[random_distr([0,1,2,3],temp)]
    return rew_values

def random_distr(values,probab):
    r = np.random.uniform(0, 1)
    s = 0
    for i in range(len(values)):
        s += probab[i]
        if s >= r:
            return values[i]
    return values[i]  
    
def update_metavalue(MetaValue_Direction,MetaValue_Hold,reward_vec,eta,flag_Hold):
    if len(reward_vec) >=3 and flag_Hold:
        deltaReward = -(reward_vec[-2] + reward_vec[-3])/2 + (reward_vec[-1] + reward_vec[-2])/2
        MetaValue_Direction.append(MetaValue_Direction[-1]+ eta*deltaReward)      
        MetaValue_Hold.append(MetaValue_Hold[-1]+ eta*deltaReward)
    elif len(reward_vec) >=3 and not(flag_Hold):
        deltaReward = -(reward_vec[-2] + reward_vec[-3])/2 + (reward_vec[-1] + reward_vec[-2])/2
        MetaValue_Direction.append(MetaValue_Direction[-1]+ eta*deltaReward)
        MetaValue_Hold.append(MetaValue_Hold[-1])  
    else:
        deltaReward = 0  
    return MetaValue_Direction,MetaValue_Hold,deltaReward

def action_vec_to_mat(action_vec):
    if action_vec == 0:
       action_conv_i = 0
       action_conv_j = 0
    elif action_vec == 1:
       action_conv_i = 0
       action_conv_j = 1
    elif action_vec == 2:
       action_conv_i = 1
       action_conv_j = 0 
    else:
       action_conv_i = 1
       action_conv_j = 1 
    return action_conv_i, action_conv_j
 
def action_mat_to_vec(action_conv_i, action_conv_j):
    action_vec = 2*action_conv_i + action_conv_j
    return action_vec

def hold_react(MetaValue_Direction,MetaValue_Hold,beta,ACC_Q,MetaValue_Thr):
    print('react done')
    if MetaValue_Hold[-1] <= MetaValue_Thr:
        beta.append(9+ np.random.uniform(0,0.1))
        ACC_Q = reset_Q(ACC_Q)
    return ACC_Q, beta