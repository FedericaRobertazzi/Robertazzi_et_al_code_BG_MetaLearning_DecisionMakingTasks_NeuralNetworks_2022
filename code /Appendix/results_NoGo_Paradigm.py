#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: federicarobertazzi
"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
                            
data_training = pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_training.head()

data_test = pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_test.head()

#thr 0.25
vec_mean_mean_reaction_time_Go_1=[np.mean(data_training['mean_reaction_time_Go_1']),np.mean(data_test['mean_reaction_time_Go_1'])]
vec_mean_mean_reaction_time_NoGo_total_1=[np.mean(data_training['mean_reaction_time_NoGo_total_1']),np.mean(data_test['mean_reaction_time_NoGo_total_1'])]
vec_mean_mean_reaction_time_NoGo_1=[np.mean(data_training['mean_reaction_time_NoGo_1']),np.mean(data_test['mean_reaction_time_NoGo_1'])]
vec_mean_mean_reaction_time_NoGo_correct_1=[np.mean(data_training['mean_reaction_time_NoGo_correct_1']),np.mean(data_test['mean_reaction_time_NoGo_correct_1'])]

vec_mean_mean_max_PMC_Go=[np.mean(data_training['mean_max_PMC_Go']),np.mean(data_test['mean_max_PMC_Go'])]
vec_mean_mean_max_PMC_NoGo_total=[np.mean(data_training['mean_max_PMC_NoGo_total']),np.mean(data_test['mean_max_PMC_NoGo_total'])]
vec_mean_mean_max_PMC_NoGo=[np.mean(data_training['mean_max_PMC_NoGo']),np.mean(data_test['mean_max_PMC_NoGo'])]
vec_mean_mean_max_PMC_NoGo_correct=[np.mean(data_training['mean_max_PMC_NoGo_correct']),np.mean(data_test['mean_max_PMC_NoGo_correct'])]

vec_mean_mean_Pmax_Go=[np.mean(data_training['mean_Pmax_Go']),np.mean(data_test['mean_Pmax_Go'])]
vec_mean_mean_Pmax_NoGo_total=[np.mean(data_training['mean_Pmax_NoGo_total']),np.mean(data_test['mean_Pmax_NoGo_total'])]
vec_mean_mean_Pmax_NoGo=[np.mean(data_training['mean_Pmax_NoGo']),np.mean(data_test['mean_Pmax_NoGo'])]
vec_mean_mean_Pmax_NoGo_correct=[np.mean(data_training['mean_Pmax_NoGo_correct']),np.mean(data_test['mean_Pmax_NoGo_correct'])]

vec_mean_right_inhibition=[np.mean(data_training['right_inhibition']),np.mean(data_test['right_inhibition'])]
vec_mean_accuracy=[np.mean(data_training['accuracy']),np.mean(data_test['accuracy'])]

#thr 0.25
vec_std_mean_reaction_time_Go_1=[np.std(data_training['mean_reaction_time_Go_1']),np.std(data_test['mean_reaction_time_Go_1'])]
vec_std_mean_reaction_time_NoGo_total_1=[np.std(data_training['mean_reaction_time_NoGo_total_1']),np.std(data_test['mean_reaction_time_NoGo_total_1'])]
vec_std_mean_reaction_time_NoGo_1=[np.std(data_training['mean_reaction_time_NoGo_1']),np.std(data_test['mean_reaction_time_NoGo_1'])]
vec_std_mean_reaction_time_NoGo_correct_1=[np.std(data_training['mean_reaction_time_NoGo_correct_1']),np.std(data_test['mean_reaction_time_NoGo_correct_1'])]

vec_std_mean_max_PMC_Go=[np.std(data_training['mean_max_PMC_Go']),np.std(data_test['mean_max_PMC_Go'])]
vec_std_mean_max_PMC_NoGo_total=[np.std(data_training['mean_max_PMC_NoGo_total']),np.std(data_test['mean_max_PMC_NoGo_total'])]
vec_std_mean_max_PMC_NoGo=[np.std(data_training['mean_max_PMC_NoGo']),np.std(data_test['mean_max_PMC_NoGo'])]
vec_std_mean_max_PMC_NoGo_correct=[np.std(data_training['mean_max_PMC_NoGo_correct']),np.std(data_test['mean_max_PMC_NoGo_correct'])]

vec_std_mean_Pmax_Go=[np.std(data_training['mean_Pmax_Go']),np.std(data_test['mean_Pmax_Go'])]
vec_std_mean_Pmax_NoGo_total=[np.std(data_training['mean_Pmax_NoGo_total']),np.std(data_test['mean_Pmax_NoGo_total'])]
vec_std_mean_Pmax_NoGo=[np.std(data_training['mean_Pmax_NoGo']),np.std(data_test['mean_Pmax_NoGo'])]
vec_std_mean_Pmax_NoGo_correct=[np.std(data_training['mean_Pmax_NoGo_correct']),np.std(data_test['mean_Pmax_NoGo_correct'])]

vec_std_right_inhibition=[np.std(data_training['right_inhibition']),np.std(data_test['right_inhibition'])]
vec_std_accuracy=[np.std(data_training['accuracy']),np.std(data_test['accuracy'])]

N = 2
fig, ax = plt.subplots()
ind = np.arange(N)
width = 0.18
ax.bar(ind - 2*width, vec_mean_mean_reaction_time_Go_1, width, yerr=vec_std_mean_reaction_time_Go_1, label='Go Trials', align='center', edgecolor='black',facecolor='black', ecolor='black',alpha=0.8, capsize=10)
ax.bar(ind-width, vec_mean_mean_reaction_time_NoGo_1, width,yerr=vec_std_mean_reaction_time_NoGo_1,
       label='NoGo failure Trials ',align='center',facecolor='#4F4F4F',edgecolor='black',ecolor='black',alpha=0.8, capsize=10)
ax.bar(ind , vec_mean_mean_reaction_time_NoGo_correct_1, width,yerr=vec_std_mean_reaction_time_NoGo_correct_1,
       label='NoGo correct Trials',align='center',facecolor='#8E8E8E',edgecolor='black',ecolor='black',alpha=0.8, capsize=10)
ax.bar(ind + width, vec_mean_mean_reaction_time_NoGo_total_1, width,yerr=vec_std_mean_reaction_time_NoGo_total_1,
       label='NoGo total Trials',align='center',facecolor='gainsboro',edgecolor='black',ecolor='black',alpha=0.8, capsize=10)
ax.set_ylabel('RT [samples]',size=17)
plt.xticks(ind, ['Training', 'Test'],size=17)
ax.legend()
ax.autoscale_view()
plt.ylim(0,50)
plt.show()

N = 2
fig, ax = plt.subplots()
ind = np.arange(N) 
width = 0.18
ax.bar(ind - 2*width, vec_mean_mean_max_PMC_Go, width, yerr=vec_std_mean_max_PMC_Go, label='Go Trials', align='center', edgecolor='black',facecolor='black', ecolor='black',alpha=0.8, capsize=10)
ax.bar(ind-width, vec_mean_mean_max_PMC_NoGo, width,yerr=vec_std_mean_max_PMC_NoGo,
       label='NoGo failure Trials',align='center',facecolor='#4F4F4F',edgecolor='black',ecolor='black',alpha=0.8, capsize=10)
ax.bar(ind , vec_mean_mean_max_PMC_NoGo_correct, width,yerr= vec_std_mean_max_PMC_NoGo_correct,
       label='NoGo correct Trials  ',align='center',facecolor='#8E8E8E',edgecolor='black',ecolor='black',alpha=0.8, capsize=10)
ax.bar(ind + width, vec_mean_mean_max_PMC_NoGo_total, width,yerr=vec_std_mean_max_PMC_NoGo_total,
       label='NoGo total Trials',align='center',facecolor='gainsboro',edgecolor='black',ecolor='black',alpha=0.8, capsize=10)
ax.set_ylabel('Max PMC [a.u.]',size=17)
ax.set_xticks(ind + width / 2)
plt.xticks(ind, ['Training', 'Test'],size=17)
ax.legend()
ax.autoscale_view()
plt.ylim(0,1)
plt.show()

N = 2
fig, ax = plt.subplots()
ind = np.arange(N) 
width = 0.18
ax.bar(ind - 2*width, vec_mean_mean_Pmax_Go, width, yerr=vec_std_mean_Pmax_Go, label='Go Trials', align='center', edgecolor='black',facecolor='black', ecolor='black',alpha=0.8, capsize=10)
ax.bar(ind-width , vec_mean_mean_Pmax_NoGo, width,yerr=vec_std_mean_Pmax_NoGo,
       label='NoGo failure Trials',align='center',facecolor='#4F4F4F',edgecolor='black',ecolor='black',alpha=0.8, capsize=10)
ax.bar(ind , vec_mean_mean_Pmax_NoGo_correct, width,yerr= vec_std_mean_Pmax_NoGo_correct,
       label='NoGo correct Trials',align='center',facecolor='#8E8E8E',edgecolor='black',ecolor='black',alpha=0.8, capsize=10)
ax.bar(ind + width, vec_mean_mean_Pmax_NoGo_total, width,yerr=vec_std_mean_Pmax_NoGo_total,
       label='NoGo total Trials',align='center',facecolor='gainsboro',edgecolor='black',ecolor='black',alpha=0.8, capsize=10)
ax.set_ylabel('P${max}$ ',size=17)
ax.set_xticks(ind + width / 2)
plt.xticks(ind, ['Training', 'Test'],size=17)
ax.legend()
ax.autoscale_view()
plt.ylim(0,1)
plt.show()

fig, ax = plt.subplots()
width = 0.2 
ax.bar((0,0.3), vec_mean_right_inhibition, width, yerr=vec_std_right_inhibition,align='center', edgecolor='black',facecolor='white', ecolor='black', alpha=0.8, capsize=10)
ax.set_ylabel('Right Inhibition [%]',size=17)
ax.set_xticks(((0,0.3)))
ax.set_xticklabels(('Training', 'Test'),size=17)
ax.autoscale_view()
plt.ylim(0,100)
plt.show()

fig, ax = plt.subplots()
width = 0.20
ax.bar((0,0.3), vec_mean_accuracy, width, yerr=vec_std_accuracy,align='center', edgecolor='black',facecolor='white', ecolor='black', alpha=0.9, capsize=10)
ax.set_ylabel('Accuracy [%]',size=17)
ax.set_xticks(((0,0.3)))
ax.set_xticklabels(('Training', 'Test'),size=17)
ax.autoscale_view()
plt.ylim(0,100)
plt.show()

