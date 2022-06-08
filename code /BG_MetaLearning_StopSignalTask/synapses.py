#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: federicarobertazzi
"""
# static synapses
class synapse:
     def __init__(self, weight):
         self.w = weight 
         if weight > 0:
             self.type = "exc"
         else:
             self.type = "inh"
     def connect(self,pre):
         self.inp = self.w*pre.out
         
# plastic synapses        
class synaptic_plasticity:
     def __init__(self,weight,P0):
        self.w = weight
        self.memory=[]
        self.weight_plastic=P0*self.w
        self.memory.append(self.weight_plastic) 
     def update(self,P):
        self.weight_plastic=P.probability*self.w
        self.memory.append(self.weight_plastic)
     def connect(self,pre):
        self.inp = self.weight_plastic*pre.out
        