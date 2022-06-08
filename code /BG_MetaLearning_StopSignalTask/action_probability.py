#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: federicarobertazzi
"""
from utility import Boltzman_softmax_equation

class action_probability():
    def __init__(self,beta0,prob0,ai):
        self.beta = beta0
        self.probability = prob0
        self.ai = ai
        self.memory = []
        self.memory.append(self.probability)
    def set_values(self,beta,Q):
       self.beta=beta
       self.Q=Q
    def probab(self):
        self.probability = Boltzman_softmax_equation(self.beta, self.Q,self.ai) 
        self.memory.append(self.probability)
   
   
  
   
 