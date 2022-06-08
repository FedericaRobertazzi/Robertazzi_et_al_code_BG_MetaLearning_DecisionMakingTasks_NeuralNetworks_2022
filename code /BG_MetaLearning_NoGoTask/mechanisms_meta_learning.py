#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: federica robertazzi
"""
import math as m

def rel_D1_beta(a0_D1_to_beta,D1_TD): 
    return a0_D1_to_beta[0]/(1+m.exp(-(a0_D1_to_beta[1]*(D1_TD - a0_D1_to_beta[2]))))

def D2_Striatum(a0_D2_to_s0,D2):
    return a0_D2_to_s0[0]/(1+m.exp(-(a0_D2_to_s0[1]*(D2 - a0_D2_to_s0[2]))))

def serotonin_to_dopamine(serotonin,k_VTA_D1,k_SNc_D2):
    D1 = k_VTA_D1[0]*m.log(serotonin + k_VTA_D1[1],m.e)
    D2 = k_SNc_D2[0]*m.log(serotonin + k_SNc_D2[1],m.e)
    return D1,D2  

def compute_TD_meta_learning(reward,Q_now,Q_prev, serotonin,D1):
    salientEvent = 1.0;
    tderror = (reward + serotonin* Q_now - Q_prev)*D1
    print('reward, sero, Q_prev:',[reward, serotonin*Q_now, Q_prev])
    return tderror, salientEvent   

def compute_forgetting(Q_now, action_sel_conv,forget_factor):
    for i in range(len(Q_now)):
        for j in range(len(Q_now[0])):
            if(i != action_sel_conv[0]) or (j != action_sel_conv[1]):
                 if i == 1 and j == 0:
                    Q_now[i][j].Q = Q_now[i][j].Q*(1-0.01) 
                    Q_now[i][j].memory.append(Q_now[i][j].Q)
                 else:                     
                    Q_now[i][j].Q = Q_now[i][j].Q*(1-forget_factor)
                    Q_now[i][j].memory.append(Q_now[i][j].Q)
    return Q_now
        
    
    
    
    
    