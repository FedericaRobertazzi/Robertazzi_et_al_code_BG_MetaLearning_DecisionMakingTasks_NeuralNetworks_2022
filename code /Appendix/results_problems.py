#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: federicarobertazzi
"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data_training_01 = pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_training_01.head()

data_test_01 = pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_test_01.head()

##################################

data_training_03 = pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_training_03.head()

data_test_03 = pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_test_03.head()

##################################

data_training_05 = pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_training_05.head()

data_test_05 = pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_test_05.head()

##################################

data_training_07 = pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_training_07.head()

data_test_07 = pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_test_07.head()

##################################

data_training_09= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_training_09.head()

data_test_09 = pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_test_09.head()

##################################

#training
vec_mean_num_problems_tot_training=[np.mean(data_training_01['Total']),np.mean(data_training_03['Total']),np.mean(data_training_05['Total']),np.mean(data_training_07['Total']),np.mean(data_training_09['Total'])]
vec_mean_num_problems_Go_training=[np.mean(data_training_01['Go']),np.mean(data_training_03['Go']),np.mean(data_training_05['Go']),np.mean(data_training_07['Go']),np.mean(data_training_09['Go'])]
vec_mean_num_problems_Hold_training=[np.mean(data_training_01['Hold']),np.mean(data_training_03['Hold']),np.mean(data_training_05['Hold']),np.mean(data_training_07['Hold']),np.mean(data_training_09['Hold'])]
vec_mean_num_trials_between_two_problems_training=[np.mean(data_training_01['Between']),np.mean(data_training_03['Between']),np.mean(data_training_05['Between']),np.mean(data_training_07['Between']),np.mean(data_training_09['Between'])]

vec_std_num_problems_tot_training=[np.std(data_training_01['Total']),np.std(data_training_03['Total']),np.std(data_training_05['Total']),np.std(data_training_07['Total']),np.std(data_training_09['Total'])]
vec_std_num_problems_Go_training=[np.std(data_training_01['Go']),np.std(data_training_03['Go']),np.std(data_training_05['Go']),np.std(data_training_07['Go']),np.std(data_training_09['Go'])]
vec_std_num_problems_Hold_training=[np.std(data_training_01['Hold']),np.std(data_training_03['Hold']),np.std(data_training_05['Hold']),np.std(data_training_07['Hold']),np.std(data_training_09['Hold'])]
vec_std_num_trials_between_two_problems_training=[np.std(data_training_01['Between']),np.std(data_training_03['Between']),np.std(data_training_05['Between']),np.std(data_training_07['Between']),np.std(data_training_09['Between'])]

#test
vec_mean_num_problems_tot_test=[np.mean(data_test_01['Total']),np.mean(data_test_03['Total']),np.mean(data_test_05['Total']),np.mean(data_test_07['Total']),np.mean(data_test_09['Total'])]
vec_mean_num_problems_Go_test=[np.mean(data_test_01['Go']),np.mean(data_test_03['Go']),np.mean(data_test_05['Go']),np.mean(data_test_07['Go']),np.mean(data_test_09['Go'])]
vec_mean_num_problems_Hold_test=[np.mean(data_test_01['Hold']),np.mean(data_test_03['Hold']),np.mean(data_test_05['Hold']),np.mean(data_test_07['Hold']),np.mean(data_test_09['Hold'])]
vec_mean_num_trials_between_two_problems_test=[np.mean(data_test_01['Between']),np.mean(data_test_03['Between']),np.mean(data_test_05['Between']),np.mean(data_test_07['Between']),np.mean(data_test_09['Between'])]

vec_std_num_problems_tot_test=[np.std(data_test_01['Total']),np.std(data_test_03['Total']),np.std(data_test_05['Total']),np.std(data_test_07['Total']),np.std(data_test_09['Total'])]
vec_std_num_problems_Go_test=[np.std(data_test_01['Go']),np.std(data_test_03['Go']),np.std(data_test_05['Go']),np.std(data_test_07['Go']),np.std(data_test_09['Go'])]
vec_std_num_problems_Hold_test=[np.std(data_test_01['Hold']),np.std(data_test_03['Hold']),np.std(data_test_05['Hold']),np.std(data_test_07['Hold']),np.std(data_test_09['Hold'])]
vec_std_num_trials_between_two_problems_test=[np.std(data_test_01['Between']),np.std(data_test_03['Between']),np.std(data_test_05['Between']),np.std(data_test_07['Between']),np.std(data_test_09['Between'])]

x=['0.1','0.3','0.5','0.7','0.9']   

plt.figure() 
plt.errorbar(x,vec_mean_num_problems_tot_test, yerr= vec_std_num_problems_tot_test/np.sqrt(40), color='black', alpha=0.8)
plt.scatter(x,vec_mean_num_problems_tot_test,s=40, color='black', alpha=0.8, marker='o')   
plt.xlabel('serotonin',size=17)
plt.ylabel("# trials test",size=17)
plt.show()

plt.figure()   
plt.errorbar(x,vec_mean_num_problems_Go_test, yerr= vec_std_num_problems_Go_test/np.sqrt(40), color='black', alpha=0.8)
plt.scatter(x,vec_mean_num_problems_Go_test,s=40, color='black', alpha=0.8, marker='o')   
plt.xlabel('serotonin',size=17)
plt.ylabel("# trials Go test",size=17)
plt.ylim(65,90)
plt.show()

plt.figure() 
plt.errorbar(x,vec_mean_num_problems_Hold_test, yerr= vec_std_num_problems_Hold_test/np.sqrt(40), color='black', alpha=0.8)
plt.scatter(x,vec_mean_num_problems_Hold_test,s=40, color='black', alpha=0.8, marker='o')    
plt.xlabel('serotonin',size=17)
plt.ylabel("# trials Hold test",size=17)
plt.ylim(65,90)
plt.show()

plt.figure()
plt.errorbar(x, vec_mean_num_trials_between_two_problems_training, yerr= vec_std_num_trials_between_two_problems_training/np.sqrt(40), color='black', alpha=0.8,linestyle='dashed')
plt.scatter(x, vec_mean_num_trials_between_two_problems_training,s=40, color='black', alpha=0.8, marker='o') 
plt.errorbar(x, vec_mean_num_trials_between_two_problems_test, yerr= vec_std_num_trials_between_two_problems_test/np.sqrt(40), color='black', alpha=0.8)
plt.scatter(x, vec_mean_num_trials_between_two_problems_test,s=40, color='black', alpha=0.8, marker='o') 
plt.xlabel('serotonin',size=17)
plt.ylabel("# trials between",size=17)
plt.ylim(1.5,3.2)
plt.show()
