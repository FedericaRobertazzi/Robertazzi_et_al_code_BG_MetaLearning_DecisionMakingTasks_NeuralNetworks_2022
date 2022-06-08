#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: federicarobertazzi
"""
import numpy as np
from mechanisms_meta_learning import D2_Striatum

class PPC:
    def __init__(self,tau,x0,s0,slope):
        self.tau = tau 
        self.x = x0 
        self.s0 = s0 
        self.slope = slope
        self.memory = []
        self.sigmoid()
    def update(self,deltaT,inp):
        self.x = self.x + deltaT*((-self.x + inp)/self.tau)
    def sigmoid(self):
        self.out=1./(1+np.exp(-self.slope*(self.x-self.s0)))
        self.memory.append(self.out)
 
class ACC_Q:
    def __init__(self,alpha,Q0):
        self.alpha=alpha
        self.Q = Q0
        self.memory = []
        self.memory.append(self.Q)
    def update(self,TD,firing_PMC):
        self.Q=self.Q+self.alpha*TD*firing_PMC
        self.memory.append(self.Q)
          
class ACC:
    def __init__(self,tau,x0,s0,slope):
        self.tau = tau 
        self.x = x0 
        self.s0 = s0
        self.slope = slope
        self.memory = []
        self.store()
    def update(self,deltaT,inp):
        self.x = self.x + deltaT*((-self.x + inp)/self.tau)
    def store(self):
        self.out = self.x
        self.memory.append(self.out)

class LPFC:
    def __init__(self,tau,x0,s0,slope,prob0):
        self.tau = tau 
        self.x = x0 
        self.s0 = s0
        self.slope = slope
        self.memory = []
        self.sigmoid()
        self.action_filtered(prob0)
    def update(self,deltaT,inp):
        self.x = self.x + deltaT*((-self.x + inp)/self.tau) 
    def sigmoid(self):
        self.out=1./(1+np.exp(-self.slope*(self.x-self.s0)))
    def action_filtered(self,prob):  
        self.out = self.out*prob
        self.memory.append(self.out) 
        
class Striatum:
    def __init__(self,tau,x0,s0,slope):
        self.tau = tau 
        self.x = x0 
        self.s0 = s0
        self.slope = slope
        self.memory = []
        self.sigmoid()
        self.s0_memory = []
        self.s0_memory.append(s0)
    def update(self,deltaT,inp):
        self.x = self.x + deltaT*((-self.x + inp)/self.tau) 
    def sigmoid(self):
        self.out=1./(1+np.exp(-self.slope*(self.x-self.s0)))
        self.memory.append(self.out)
    #update s0 according D2 level
    def update_s0(self, D2, a0_D2_to_beta):
        self.s0 = D2_Striatum(a0_D2_to_beta,D2)
        self.s0_memory.append(self.s0)

class SNr:
    def __init__(self,tau,x0,s0,slope):
        self.tau = tau 
        self.x = x0 
        self.s0 = s0
        self.slope = slope
        self.memory = []
        self.sigmoid()
    def update(self,deltaT,inp):
        self.x = self.x + deltaT*((-self.x + inp)/self.tau) 
    def sigmoid(self):
        self.out=1./(1+np.exp(-self.slope*(self.x-self.s0)))
        self.memory.append(self.out)
        
class Thalamus:
    def __init__(self,tau,x0,s0,slope):
        self.tau = tau 
        self.x = x0 
        self.s0 = s0
        self.slope = slope
        self.memory = []
        self.sigmoid()
    def update(self,deltaT,inp):
        self.x = self.x + deltaT*((-self.x + inp)/self.tau) 
    def sigmoid(self):
        self.out=1./(1+np.exp(-self.slope*(self.x-self.s0)))
        self.memory.append(self.out)
        
class PMC:
    def __init__(self,tau,x0,s0,slope):
        self.tau = tau 
        self.x = x0 
        self.s0 = s0
        self.slope = slope
        self.memory = []
        self.sigmoid()
    def update(self,deltaT,inp):
        self.x = self.x + deltaT*((-self.x + inp)/self.tau)
    def sigmoid(self):
        self.out=1./(1+np.exp(-self.slope*(self.x-self.s0)))
        self.memory.append(self.out) 
    def set_tau(self,new_tau):
        self.tau= new_tau 
       
       
       
       
