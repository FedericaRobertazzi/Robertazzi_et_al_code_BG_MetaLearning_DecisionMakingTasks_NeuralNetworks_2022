#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: federicarobertazzi
"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.interpolate as interp
from scipy.stats import t

data_RI_Hold_01 = pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_RI_Hold_01.head()

data_ReactTime_Hold_01 = pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_ReactTime_Hold_01.head()

##################################

data_RI_Hold_03 = pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_RI_Hold_03.head()

data_ReactTime_Hold_03 = pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_ReactTime_Hold_03.head()

##################################

data_RI_Hold_05 = pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_RI_Hold_05.head()

data_ReactTime_Hold_05 = pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_ReactTime_Hold_05.head()

##################################

data_RI_Hold_07 = pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_RI_Hold_07.head()

data_ReactTime_Hold_07 = pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_ReactTime_Hold_07.head()

##################################

data_RI_Hold_09 = pd.read_csv('<insert path>', delimiter = ';',decimal=",")
data_RI_Hold_09.head()

data_ReactTime_Hold_09 = pd.read_csv('<insert path>',na_values='-', delimiter = ';',decimal=",")
data_ReactTime_Hold_09.head()

##################################

#dopa-->sero 0.1
vec_mean_RI_Hold_01_elem_0=np.mean(data_RI_Hold_01['elem_0'])
vec_mean_RI_Hold_01_elem_1=np.mean(data_RI_Hold_01['elem_1'])
vec_mean_RI_Hold_01_elem_2=np.mean(data_RI_Hold_01['elem_2'])
vec_mean_RI_Hold_01_elem_3=np.mean(data_RI_Hold_01['elem_3'])
vec_mean_RI_Hold_01=[vec_mean_RI_Hold_01_elem_0, vec_mean_RI_Hold_01_elem_1, vec_mean_RI_Hold_01_elem_2, vec_mean_RI_Hold_01_elem_3]

vec_std_RI_Hold_01_elem_0=np.std(data_RI_Hold_01['elem_0'])
vec_std_RI_Hold_01_elem_1=np.std(data_RI_Hold_01['elem_1'])
vec_std_RI_Hold_01_elem_2=np.std(data_RI_Hold_01['elem_2'])
vec_std_RI_Hold_01_elem_3=np.std(data_RI_Hold_01['elem_3'])
vec_std_RI_Hold_01=[vec_std_RI_Hold_01_elem_0, vec_std_RI_Hold_01_elem_1, vec_std_RI_Hold_01_elem_2, vec_std_RI_Hold_01_elem_3]

vec_mean_ReactTime_Hold_01_elem_0=np.mean(data_ReactTime_Hold_01['elem_0'])
vec_mean_ReactTime_Hold_01_elem_1=np.mean(data_ReactTime_Hold_01['elem_1'])
vec_mean_ReactTime_Hold_01_elem_2=np.mean(data_ReactTime_Hold_01['elem_2'])
vec_mean_ReactTime_Hold_01_elem_3=np.mean(data_ReactTime_Hold_01['elem_3'])
vec_mean_ReactTime_Hold_01=[vec_mean_ReactTime_Hold_01_elem_0, vec_mean_ReactTime_Hold_01_elem_1, vec_mean_ReactTime_Hold_01_elem_2, vec_mean_ReactTime_Hold_01_elem_3]

vec_std_ReactTime_Hold_01_elem_0=np.std(data_ReactTime_Hold_01['elem_0'])
vec_std_ReactTime_Hold_01_elem_1=np.std(data_ReactTime_Hold_01['elem_1'])
vec_std_ReactTime_Hold_01_elem_2=np.std(data_ReactTime_Hold_01['elem_2'])
vec_std_ReactTime_Hold_01_elem_3=np.std(data_ReactTime_Hold_01['elem_3'])
vec_std_ReactTime_Hold_01=[vec_std_ReactTime_Hold_01_elem_0, vec_std_ReactTime_Hold_01_elem_1, vec_std_ReactTime_Hold_01_elem_2, vec_std_ReactTime_Hold_01_elem_3]

#regression RI
data_regr_RI_Hold_01 = data_RI_Hold_01.to_numpy()
coeff_RI_01 = np.zeros((40,2))
vector_delay_RI_01=np.array(range(0,31,10))
vec_r_square_RI_01=np.zeros((40))

def func(x, a, b):
    return a * x + b 
for i in list(range(40)):
    print(i)
    temp_RI_01=data_regr_RI_Hold_01[i,[1,2,3,4]]
    print(temp_RI_01)
    popt_RI_01, pcov_RI_01= curve_fit(func, vector_delay_RI_01,temp_RI_01)
    coeff_RI_01[i,0] = popt_RI_01[1]
    coeff_RI_01[i,1] = popt_RI_01[0]
    #residui 
    residuals_RI_01=temp_RI_01-func(vector_delay_RI_01,*popt_RI_01)
    ss_res_RI_01=np.sum(residuals_RI_01**2)
    ss_tot_RI_01=np.sum((temp_RI_01-np.mean(temp_RI_01))**2)
    vec_r_square_RI_01[i]=1-(ss_res_RI_01/ss_tot_RI_01)
    
vec_mean_regr_RI_Hold_01_elem_0=np.mean(coeff_RI_01[:,1])
vec_mean_regr_RI_Hold_01_elem_1=np.mean(coeff_RI_01[:,0])

vec_sem_regr_RI_Hold_01_elem_0=np.std(coeff_RI_01[:,1])/np.sqrt(40)
vec_sem_regr_RI_Hold_01_elem_1=np.std(coeff_RI_01[:,0])/np.sqrt(40)

#tscore
t_score_RI_01=vec_mean_regr_RI_Hold_01_elem_0/vec_sem_regr_RI_Hold_01_elem_0
pvalue_RI_01= (t.sf(np.abs(t_score_RI_01),39))*2

vec_mean_r_square_RI_Hold_01=np.mean(vec_r_square_RI_01)
pearson_RI_01=np.sqrt(vec_mean_r_square_RI_Hold_01)
vec_sem_r_square_RI_Hold_01=np.std(vec_r_square_RI_01)/np.sqrt(40)

x_RI_01=np.arange(0,35,5)
y_RI_01= x_RI_01*vec_mean_regr_RI_Hold_01_elem_0+vec_mean_regr_RI_Hold_01_elem_1

#regression ReactTime 
data_regr_ReactTime_Hold_01 = data_ReactTime_Hold_01.to_numpy()
coeff_ReactTime_01 = np.zeros((40,2))
vector_delay_ReactTime_01=np.array(range(0,31,10))
vec_r_square_ReactTime_01=np.zeros((40))

def func(x, a, b):
    return a * x + b 
for i in list(range(40)):
    print(i)
    temp_ReactTime_01=data_regr_ReactTime_Hold_01[i,[1,2,3,4]]
    print(temp_ReactTime_01)
    popt_ReactTime_01, pcov_ReactTime_01 = curve_fit(func, vector_delay_ReactTime_01,temp_ReactTime_01)
    coeff_ReactTime_01[i,0] = popt_ReactTime_01[1]
    coeff_ReactTime_01[i,1] = popt_ReactTime_01[0]
    #residui 
    residuals_ReactTime_01=temp_ReactTime_01-func(vector_delay_ReactTime_01,*popt_ReactTime_01)
    ss_res_ReactTime_01=np.sum(residuals_ReactTime_01**2)
    ss_tot_ReactTime_01=np.sum((temp_ReactTime_01-np.mean(temp_ReactTime_01))**2)
    vec_r_square_ReactTime_01[i]=1-(ss_res_ReactTime_01/ss_tot_ReactTime_01)
    
vec_mean_regr_ReactTime_Hold_01_elem_0=np.mean(coeff_ReactTime_01[:,1])
vec_mean_regr_ReactTime_Hold_01_elem_1=np.mean(coeff_ReactTime_01[:,0])

vec_sem_regr_ReactTime_Hold_01_elem_0=np.std(coeff_ReactTime_01[:,1])/np.sqrt(40)
vec_sem_regr_ReactTime_Hold_01_elem_1=np.std(coeff_ReactTime_01[:,0])/np.sqrt(40)

#tscore
t_score_ReactTime_01=vec_mean_regr_ReactTime_Hold_01_elem_0/vec_sem_regr_ReactTime_Hold_01_elem_0
pvalue_ReactTime_01= (t.sf(np.abs(t_score_ReactTime_01),39))*2

vec_mean_r_square_ReactTime_Hold_01=np.mean(vec_r_square_ReactTime_01)
pearson_ReactTime_01=np.sqrt(vec_mean_r_square_ReactTime_Hold_01)
vec_sem_r_square_ReactTime_Hold_01=np.std(vec_r_square_ReactTime_01)/np.sqrt(40)

x_ReactTime_01=np.arange(0,35,5)
y_ReactTime_01=x_ReactTime_01* vec_mean_regr_ReactTime_Hold_01_elem_0+vec_mean_regr_ReactTime_Hold_01_elem_1

np.savetxt('coeff_RI_Hold_01_elem1.txt', coeff_RI_01[:,0])
np.savetxt('coeff_RI_Hold_01_elem0.txt', coeff_RI_01[:,1])

np.savetxt('coeff_ReactTime_correct_Hold_01_elem1.txt', coeff_ReactTime_01[:,0])
np.savetxt('coeff_ReactTime_correct_Hold_01_elem0.txt', coeff_ReactTime_01[:,1])

#dopa-->sero 0.3
vec_mean_RI_Hold_03_elem_0=np.mean(data_RI_Hold_03['elem_0'])
vec_mean_RI_Hold_03_elem_1=np.mean(data_RI_Hold_03['elem_1'])
vec_mean_RI_Hold_03_elem_2=np.mean(data_RI_Hold_03['elem_2'])
vec_mean_RI_Hold_03_elem_3=np.mean(data_RI_Hold_03['elem_3'])
vec_mean_RI_Hold_03=[vec_mean_RI_Hold_03_elem_0, vec_mean_RI_Hold_03_elem_1, vec_mean_RI_Hold_03_elem_2, vec_mean_RI_Hold_03_elem_3]

vec_std_RI_Hold_03_elem_0=np.std(data_RI_Hold_03['elem_0'])
vec_std_RI_Hold_03_elem_1=np.std(data_RI_Hold_03['elem_1'])
vec_std_RI_Hold_03_elem_2=np.std(data_RI_Hold_03['elem_2'])
vec_std_RI_Hold_03_elem_3=np.std(data_RI_Hold_03['elem_3'])
vec_std_RI_Hold_03=[vec_std_RI_Hold_03_elem_0, vec_std_RI_Hold_03_elem_1, vec_std_RI_Hold_03_elem_2, vec_std_RI_Hold_03_elem_3]

vec_mean_ReactTime_Hold_03_elem_0=np.mean(data_ReactTime_Hold_03['elem_0'])
vec_mean_ReactTime_Hold_03_elem_1=np.mean(data_ReactTime_Hold_03['elem_1'])
vec_mean_ReactTime_Hold_03_elem_2=np.mean(data_ReactTime_Hold_03['elem_2'])
vec_mean_ReactTime_Hold_03_elem_3=np.mean(data_ReactTime_Hold_03['elem_3'])
vec_mean_ReactTime_Hold_03=[vec_mean_ReactTime_Hold_03_elem_0, vec_mean_ReactTime_Hold_03_elem_1, vec_mean_ReactTime_Hold_03_elem_2, vec_mean_ReactTime_Hold_03_elem_3]

vec_std_ReactTime_Hold_03_elem_0=np.std(data_ReactTime_Hold_03['elem_0'])
vec_std_ReactTime_Hold_03_elem_1=np.std(data_ReactTime_Hold_03['elem_1'])
vec_std_ReactTime_Hold_03_elem_2=np.std(data_ReactTime_Hold_03['elem_2'])
vec_std_ReactTime_Hold_03_elem_3=np.std(data_ReactTime_Hold_03['elem_3'])
vec_std_ReactTime_Hold_03=[vec_std_ReactTime_Hold_03_elem_0, vec_std_ReactTime_Hold_03_elem_1, vec_std_ReactTime_Hold_03_elem_2, vec_std_ReactTime_Hold_03_elem_3]

#regression RI
data_regr_RI_Hold_03 = data_RI_Hold_03.to_numpy()
coeff_RI_03 = np.zeros((40,2))
vector_delay_RI_03=np.array(range(0,31,10))
vec_r_square_RI_03=np.zeros((40))

def func(x, a, b):
    return a * x + b 
for i in list(range(40)):
    print(i)
    temp_RI_03=data_regr_RI_Hold_03[i,[1,2,3,4]]
    print(temp_RI_03)
    popt_RI_03, pcov_RI_03= curve_fit(func, vector_delay_RI_03,temp_RI_03)
    coeff_RI_03[i,0] = popt_RI_03[1]
    coeff_RI_03[i,1] = popt_RI_03[0]
    #residui 
    residuals_RI_03=temp_RI_03-func(vector_delay_RI_03,*popt_RI_03)
    ss_res_RI_03=np.sum(residuals_RI_03**2)
    ss_tot_RI_03=np.sum((temp_RI_03-np.mean(temp_RI_03))**2)
    vec_r_square_RI_03[i]=1-(ss_res_RI_03/ss_tot_RI_03)
    
vec_mean_regr_RI_Hold_03_elem_0=np.mean(coeff_RI_03[:,1])
vec_mean_regr_RI_Hold_03_elem_1=np.mean(coeff_RI_03[:,0])

vec_sem_regr_RI_Hold_03_elem_0=np.std(coeff_RI_03[:,1])/np.sqrt(40)
vec_sem_regr_RI_Hold_03_elem_1=np.std(coeff_RI_03[:,0])/np.sqrt(40)

#tscore
t_score_RI_03=vec_mean_regr_RI_Hold_03_elem_0/vec_sem_regr_RI_Hold_03_elem_0
pvalue_RI_03= (t.sf(np.abs(t_score_RI_03),39))*2

vec_mean_r_square_RI_Hold_03=np.mean(vec_r_square_RI_03)
pearson_RI_03=np.sqrt(vec_mean_r_square_RI_Hold_03)
vec_sem_r_square_RI_Hold_03=np.std(vec_r_square_RI_03)/np.sqrt(40)

x_RI_03=np.arange(0,35,5)
y_RI_03= x_RI_03*vec_mean_regr_RI_Hold_03_elem_0+vec_mean_regr_RI_Hold_03_elem_1

#regression ReactTime 
data_regr_ReactTime_Hold_03 = data_ReactTime_Hold_03.to_numpy()
coeff_ReactTime_03 = np.zeros((40,2))
vector_delay_ReactTime_03=np.array(range(0,31,10))
vec_r_square_ReactTime_03=np.zeros((40))

def func(x, a, b):
    return a * x + b 
for i in list(range(40)):
    print(i)
    temp_ReactTime_03=data_regr_ReactTime_Hold_03[i,[1,2,3,4]]
    print(temp_ReactTime_03)
    popt_ReactTime_03, pcov_ReactTime_03 = curve_fit(func, vector_delay_ReactTime_03,temp_ReactTime_03)
    coeff_ReactTime_03[i,0] = popt_ReactTime_03[1]
    coeff_ReactTime_03[i,1] = popt_ReactTime_03[0]
    #residui 
    residuals_ReactTime_03=temp_ReactTime_03-func(vector_delay_ReactTime_03,*popt_ReactTime_03)
    ss_res_ReactTime_03=np.sum(residuals_ReactTime_03**2)
    ss_tot_ReactTime_03=np.sum((temp_ReactTime_03-np.mean(temp_ReactTime_03))**2)
    vec_r_square_ReactTime_03[i]=1-(ss_res_ReactTime_03/ss_tot_ReactTime_03)
    
vec_mean_regr_ReactTime_Hold_03_elem_0=np.mean(coeff_ReactTime_03[:,1])
vec_mean_regr_ReactTime_Hold_03_elem_1=np.mean(coeff_ReactTime_03[:,0])

vec_sem_regr_ReactTime_Hold_03_elem_0=np.std(coeff_ReactTime_03[:,1])/np.sqrt(40)
vec_sem_regr_ReactTime_Hold_03_elem_1=np.std(coeff_ReactTime_03[:,0])/np.sqrt(40)

#tscore
t_score_ReactTime_03=vec_mean_regr_ReactTime_Hold_03_elem_0/vec_sem_regr_ReactTime_Hold_03_elem_0
pvalue_ReactTime_03= (t.sf(np.abs(t_score_ReactTime_03),39))*2

vec_mean_r_square_ReactTime_Hold_03=np.mean(vec_r_square_ReactTime_03)
pearson_ReactTime_03=np.sqrt(vec_mean_r_square_ReactTime_Hold_03)
vec_sem_r_square_ReactTime_Hold_03=np.std(vec_r_square_ReactTime_03)/np.sqrt(40)

x_ReactTime_03=np.arange(0,35,5)
y_ReactTime_03=x_ReactTime_03* vec_mean_regr_ReactTime_Hold_03_elem_0+vec_mean_regr_ReactTime_Hold_03_elem_1

np.savetxt('coeff_RI_Hold_03_elem1.txt', coeff_RI_03[:,0])
np.savetxt('coeff_RI_Hold_03_elem0.txt', coeff_RI_03[:,1])

np.savetxt('coeff_ReactTime_correct_Hold_03_elem1.txt', coeff_ReactTime_03[:,0])
np.savetxt('coeff_ReactTime_correct_Hold_03_elem0.txt', coeff_ReactTime_03[:,1])

#dopa-->sero 0.5
vec_mean_RI_Hold_05_elem_0=np.mean(data_RI_Hold_05['elem_0'])
vec_mean_RI_Hold_05_elem_1=np.mean(data_RI_Hold_05['elem_1'])
vec_mean_RI_Hold_05_elem_2=np.mean(data_RI_Hold_05['elem_2'])
vec_mean_RI_Hold_05_elem_3=np.mean(data_RI_Hold_05['elem_3'])
vec_mean_RI_Hold_05=[vec_mean_RI_Hold_05_elem_0, vec_mean_RI_Hold_05_elem_1, vec_mean_RI_Hold_05_elem_2, vec_mean_RI_Hold_05_elem_3]

vec_std_RI_Hold_05_elem_0=np.std(data_RI_Hold_05['elem_0'])
vec_std_RI_Hold_05_elem_1=np.std(data_RI_Hold_05['elem_1'])
vec_std_RI_Hold_05_elem_2=np.std(data_RI_Hold_05['elem_2'])
vec_std_RI_Hold_05_elem_3=np.std(data_RI_Hold_05['elem_3'])
vec_std_RI_Hold_05=[vec_std_RI_Hold_05_elem_0, vec_std_RI_Hold_05_elem_1, vec_std_RI_Hold_05_elem_2, vec_std_RI_Hold_05_elem_3]

vec_mean_ReactTime_Hold_05_elem_0=np.mean(data_ReactTime_Hold_05['elem_0'])
vec_mean_ReactTime_Hold_05_elem_1=np.mean(data_ReactTime_Hold_05['elem_1'])
vec_mean_ReactTime_Hold_05_elem_2=np.mean(data_ReactTime_Hold_05['elem_2'])
vec_mean_ReactTime_Hold_05_elem_3=np.mean(data_ReactTime_Hold_05['elem_3'])
vec_mean_ReactTime_Hold_05=[vec_mean_ReactTime_Hold_05_elem_0, vec_mean_ReactTime_Hold_05_elem_1, vec_mean_ReactTime_Hold_05_elem_2, vec_mean_ReactTime_Hold_05_elem_3]

vec_std_ReactTime_Hold_05_elem_0=np.std(data_ReactTime_Hold_05['elem_0'])
vec_std_ReactTime_Hold_05_elem_1=np.std(data_ReactTime_Hold_05['elem_1'])
vec_std_ReactTime_Hold_05_elem_2=np.std(data_ReactTime_Hold_05['elem_2'])
vec_std_ReactTime_Hold_05_elem_3=np.std(data_ReactTime_Hold_05['elem_3'])
vec_std_ReactTime_Hold_05=[vec_std_ReactTime_Hold_05_elem_0, vec_std_ReactTime_Hold_05_elem_1, vec_std_ReactTime_Hold_05_elem_2, vec_std_ReactTime_Hold_05_elem_3]

#regression RI
data_regr_RI_Hold_05 = data_RI_Hold_05.to_numpy()
coeff_RI_05 = np.zeros((40,2))
vector_delay_RI_05=np.array(range(0,31,10))
vec_r_square_RI_05=np.zeros((40))

def func(x, a, b):
    return a * x + b 
for i in list(range(40)):
    print(i)
    temp_RI_05=data_regr_RI_Hold_05[i,[1,2,3,4]]
    print(temp_RI_05)
    popt_RI_05, pcov_RI_05= curve_fit(func, vector_delay_RI_05,temp_RI_05)
    coeff_RI_05[i,0] = popt_RI_05[1]
    coeff_RI_05[i,1] = popt_RI_05[0]
    #residui 
    residuals_RI_05=temp_RI_05-func(vector_delay_RI_05,*popt_RI_05)
    ss_res_RI_05=np.sum(residuals_RI_05**2)
    ss_tot_RI_05=np.sum((temp_RI_05-np.mean(temp_RI_05))**2)
    vec_r_square_RI_05[i]=1-(ss_res_RI_05/ss_tot_RI_05)
    
vec_mean_regr_RI_Hold_05_elem_0=np.mean(coeff_RI_05[:,1])
vec_mean_regr_RI_Hold_05_elem_1=np.mean(coeff_RI_05[:,0])

vec_sem_regr_RI_Hold_05_elem_0=np.std(coeff_RI_05[:,1])/np.sqrt(40)
vec_sem_regr_RI_Hold_05_elem_1=np.std(coeff_RI_05[:,0])/np.sqrt(40)

#tscore
t_score_RI_05=vec_mean_regr_RI_Hold_05_elem_0/vec_sem_regr_RI_Hold_05_elem_0
pvalue_RI_05= (t.sf(np.abs(t_score_RI_05),39))*2

vec_mean_r_square_RI_Hold_05=np.mean(vec_r_square_RI_05)
pearson_RI_05=np.sqrt(vec_mean_r_square_RI_Hold_05)
vec_sem_r_square_RI_Hold_05=np.std(vec_r_square_RI_05)/np.sqrt(40)

x_RI_05=np.arange(0,35,5)
y_RI_05= x_RI_05*vec_mean_regr_RI_Hold_05_elem_0+vec_mean_regr_RI_Hold_05_elem_1

#regression ReactTime
data_regr_ReactTime_Hold_05 = data_ReactTime_Hold_05.to_numpy()
coeff_ReactTime_05 = np.zeros((40,2))
vector_delay_ReactTime_05=np.array(range(0,31,10))
vec_r_square_ReactTime_05=np.zeros((40))

def func(x, a, b):
    return a * x + b 
for i in list(range(40)):
    print(i)
    temp_ReactTime_05=data_regr_ReactTime_Hold_05[i,[1,2,3,4]]
    print(temp_ReactTime_05)
    popt_ReactTime_05, pcov_ReactTime_05 = curve_fit(func, vector_delay_ReactTime_05,temp_ReactTime_05)
    coeff_ReactTime_05[i,0] = popt_ReactTime_05[1]
    coeff_ReactTime_05[i,1] = popt_ReactTime_05[0]
    #residui 
    residuals_ReactTime_05=temp_ReactTime_05-func(vector_delay_ReactTime_05,*popt_ReactTime_05)
    ss_res_ReactTime_05=np.sum(residuals_ReactTime_05**2)
    ss_tot_ReactTime_05=np.sum((temp_ReactTime_05-np.mean(temp_ReactTime_05))**2)
    vec_r_square_ReactTime_05[i]=1-(ss_res_ReactTime_05/ss_tot_ReactTime_05)
    
vec_mean_regr_ReactTime_Hold_05_elem_0=np.mean(coeff_ReactTime_05[:,1])
vec_mean_regr_ReactTime_Hold_05_elem_1=np.mean(coeff_ReactTime_05[:,0])

vec_sem_regr_ReactTime_Hold_05_elem_0=np.std(coeff_ReactTime_05[:,1])/np.sqrt(40)
vec_sem_regr_ReactTime_Hold_05_elem_1=np.std(coeff_ReactTime_05[:,0])/np.sqrt(40)

#tscore
t_score_ReactTime_05=vec_mean_regr_ReactTime_Hold_05_elem_0/vec_sem_regr_ReactTime_Hold_05_elem_0
pvalue_ReactTime_05= (t.sf(np.abs(t_score_ReactTime_05),39))*2

vec_mean_r_square_ReactTime_Hold_05=np.mean(vec_r_square_ReactTime_05)
pearson_ReactTime_05=np.sqrt(vec_mean_r_square_ReactTime_Hold_05)
vec_sem_r_square_ReactTime_Hold_05=np.std(vec_r_square_ReactTime_05)/np.sqrt(40)

x_ReactTime_05=np.arange(0,35,5)
y_ReactTime_05=x_ReactTime_05* vec_mean_regr_ReactTime_Hold_05_elem_0+vec_mean_regr_ReactTime_Hold_05_elem_1

np.savetxt('coeff_RI_Hold_05_elem1.txt', coeff_RI_05[:,0])
np.savetxt('coeff_RI_Hold_05_elem0.txt', coeff_RI_05[:,1])

np.savetxt('coeff_ReactTime_correct_Hold_05_elem1.txt', coeff_ReactTime_05[:,0])
np.savetxt('coeff_ReactTime_correct_Hold_05_elem0.txt', coeff_ReactTime_05[:,1])

#dopa-->sero 0.7
vec_mean_RI_Hold_07_elem_0=np.mean(data_RI_Hold_07['elem_0'])
vec_mean_RI_Hold_07_elem_1=np.mean(data_RI_Hold_07['elem_1'])
vec_mean_RI_Hold_07_elem_2=np.mean(data_RI_Hold_07['elem_2'])
vec_mean_RI_Hold_07_elem_3=np.mean(data_RI_Hold_07['elem_3'])
vec_mean_RI_Hold_07=[vec_mean_RI_Hold_07_elem_0, vec_mean_RI_Hold_07_elem_1, vec_mean_RI_Hold_07_elem_2, vec_mean_RI_Hold_07_elem_3]

vec_std_RI_Hold_07_elem_0=np.std(data_RI_Hold_07['elem_0'])
vec_std_RI_Hold_07_elem_1=np.std(data_RI_Hold_07['elem_1'])
vec_std_RI_Hold_07_elem_2=np.std(data_RI_Hold_07['elem_2'])
vec_std_RI_Hold_07_elem_3=np.std(data_RI_Hold_07['elem_3'])
vec_std_RI_Hold_07=[vec_std_RI_Hold_07_elem_0, vec_std_RI_Hold_07_elem_1, vec_std_RI_Hold_07_elem_2, vec_std_RI_Hold_07_elem_3]

vec_mean_ReactTime_Hold_07_elem_0=np.mean(data_ReactTime_Hold_07['elem_0'])
vec_mean_ReactTime_Hold_07_elem_1=np.mean(data_ReactTime_Hold_07['elem_1'])
vec_mean_ReactTime_Hold_07_elem_2=np.mean(data_ReactTime_Hold_07['elem_2'])
vec_mean_ReactTime_Hold_07_elem_3=np.mean(data_ReactTime_Hold_07['elem_3'])
vec_mean_ReactTime_Hold_07=[vec_mean_ReactTime_Hold_07_elem_0, vec_mean_ReactTime_Hold_07_elem_1, vec_mean_ReactTime_Hold_07_elem_2, vec_mean_ReactTime_Hold_07_elem_3]

vec_std_ReactTime_Hold_07_elem_0=np.std(data_ReactTime_Hold_07['elem_0'])
vec_std_ReactTime_Hold_07_elem_1=np.std(data_ReactTime_Hold_07['elem_1'])
vec_std_ReactTime_Hold_07_elem_2=np.std(data_ReactTime_Hold_07['elem_2'])
vec_std_ReactTime_Hold_07_elem_3=np.std(data_ReactTime_Hold_07['elem_3'])
vec_std_ReactTime_Hold_07=[vec_std_ReactTime_Hold_07_elem_0, vec_std_ReactTime_Hold_07_elem_1, vec_std_ReactTime_Hold_07_elem_2, vec_std_ReactTime_Hold_07_elem_3]

#regression RI
data_regr_RI_Hold_07 = data_RI_Hold_07.to_numpy()
coeff_RI_07= np.zeros((40,2))
vector_delay_RI_07=np.array(range(0,31,10))
vec_r_square_RI_07=np.zeros((40))

def func(x, a, b):
    return a * x + b 
for i in list(range(40)):
    print(i)
    temp_RI_07=data_regr_RI_Hold_07[i,[1,2,3,4]]
    print(temp_RI_07)
    popt_RI_07, pcov_RI_07= curve_fit(func, vector_delay_RI_07,temp_RI_07)
    coeff_RI_07[i,0] = popt_RI_07[1]
    coeff_RI_07[i,1] = popt_RI_07[0]
    #residui 
    residuals_RI_07=temp_RI_07-func(vector_delay_RI_07,*popt_RI_07)
    ss_res_RI_07=np.sum(residuals_RI_07**2)
    ss_tot_RI_07=np.sum((temp_RI_07-np.mean(temp_RI_07))**2)
    vec_r_square_RI_07[i]=1-(ss_res_RI_07/ss_tot_RI_07)
    
vec_mean_regr_RI_Hold_07_elem_0=np.mean(coeff_RI_07[:,1])
vec_mean_regr_RI_Hold_07_elem_1=np.mean(coeff_RI_07[:,0])

vec_sem_regr_RI_Hold_07_elem_0=np.std(coeff_RI_07[:,1])/np.sqrt(40)
vec_sem_regr_RI_Hold_07_elem_1=np.std(coeff_RI_07[:,0])/np.sqrt(40)

#tscore
t_score_RI_07=vec_mean_regr_RI_Hold_07_elem_0/vec_sem_regr_RI_Hold_07_elem_0
pvalue_RI_07= (t.sf(np.abs(t_score_RI_07),39))*2

vec_mean_r_square_RI_Hold_07=np.mean(vec_r_square_RI_07)
pearson_RI_07=np.sqrt(vec_mean_r_square_RI_Hold_07)
vec_sem_r_square_RI_Hold_07=np.std(vec_r_square_RI_07)/np.sqrt(40)

x_RI_07=np.arange(0,35,5)
y_RI_07= x_RI_07*vec_mean_regr_RI_Hold_07_elem_0+vec_mean_regr_RI_Hold_07_elem_1

#regression ReactTime 
data_regr_ReactTime_Hold_07 = data_ReactTime_Hold_07.to_numpy()
coeff_ReactTime_07 = np.zeros((40,2))
vector_delay_ReactTime_07=np.array(range(0,31,10))
vec_r_square_ReactTime_07=np.zeros((40))

def func(x, a, b):
    return a * x + b 
for i in list(range(40)):
    print(i)
    temp_ReactTime_07=data_regr_ReactTime_Hold_07[i,[1,2,3,4]]
    print(temp_ReactTime_07)
    popt_ReactTime_07, pcov_ReactTime_07 = curve_fit(func, vector_delay_ReactTime_07,temp_ReactTime_07)
    coeff_ReactTime_07[i,0] = popt_ReactTime_07[1]
    coeff_ReactTime_07[i,1] = popt_ReactTime_07[0]
    #residui 
    residuals_ReactTime_07=temp_ReactTime_07-func(vector_delay_ReactTime_07,*popt_ReactTime_07)
    ss_res_ReactTime_07=np.sum(residuals_ReactTime_07**2)
    ss_tot_ReactTime_07=np.sum((temp_ReactTime_07-np.mean(temp_ReactTime_07))**2)
    vec_r_square_ReactTime_07[i]=1-(ss_res_ReactTime_07/ss_tot_ReactTime_07)
    
vec_mean_regr_ReactTime_Hold_07_elem_0=np.mean(coeff_ReactTime_07[:,1])
vec_mean_regr_ReactTime_Hold_07_elem_1=np.mean(coeff_ReactTime_07[:,0])

vec_sem_regr_ReactTime_Hold_07_elem_0=np.std(coeff_ReactTime_07[:,1])/np.sqrt(40)
vec_sem_regr_ReactTime_Hold_07_elem_1=np.std(coeff_ReactTime_07[:,0])/np.sqrt(40)

#tscore
t_score_ReactTime_07=vec_mean_regr_ReactTime_Hold_07_elem_0/vec_sem_regr_ReactTime_Hold_07_elem_0
pvalue_ReactTime_07= (t.sf(np.abs(t_score_ReactTime_07),39))*2

vec_mean_r_square_ReactTime_Hold_07=np.mean(vec_r_square_ReactTime_07)
pearson_ReactTime_07=np.sqrt(vec_mean_r_square_ReactTime_Hold_07)
vec_sem_r_square_ReactTime_Hold_07=np.std(vec_r_square_ReactTime_07)/np.sqrt(40)

x_ReactTime_07=np.arange(0,35,5)
y_ReactTime_07=x_ReactTime_07* vec_mean_regr_ReactTime_Hold_07_elem_0+vec_mean_regr_ReactTime_Hold_07_elem_1

np.savetxt('coeff_RI_Hold_07_elem1.txt', coeff_RI_07[:,0])
np.savetxt('coeff_RI_Hold_07_elem0.txt', coeff_RI_07[:,1])

np.savetxt('coeff_ReactTime_correct_Hold_07_elem1.txt', coeff_ReactTime_07[:,0])
np.savetxt('coeff_ReactTime_correct_Hold_07_elem0.txt', coeff_ReactTime_07[:,1])

#dopa-->sero 0.9
vec_mean_RI_Hold_09_elem_0=np.mean(data_RI_Hold_09['elem_0'])
vec_mean_RI_Hold_09_elem_1=np.mean(data_RI_Hold_09['elem_1'])
vec_mean_RI_Hold_09_elem_2=np.mean(data_RI_Hold_09['elem_2'])
vec_mean_RI_Hold_09_elem_3=np.mean(data_RI_Hold_09['elem_3'])
vec_mean_RI_Hold_09=[vec_mean_RI_Hold_09_elem_0, vec_mean_RI_Hold_09_elem_1, vec_mean_RI_Hold_09_elem_2, vec_mean_RI_Hold_09_elem_3]

vec_std_RI_Hold_09_elem_0=np.std(data_RI_Hold_09['elem_0'])
vec_std_RI_Hold_09_elem_1=np.std(data_RI_Hold_09['elem_1'])
vec_std_RI_Hold_09_elem_2=np.std(data_RI_Hold_09['elem_2'])
vec_std_RI_Hold_09_elem_3=np.std(data_RI_Hold_09['elem_3'])
vec_std_RI_Hold_09=[vec_std_RI_Hold_09_elem_0, vec_std_RI_Hold_09_elem_1, vec_std_RI_Hold_09_elem_2, vec_std_RI_Hold_09_elem_3]

vec_mean_ReactTime_Hold_09_elem_0=np.mean(data_ReactTime_Hold_09['elem_0'])
vec_mean_ReactTime_Hold_09_elem_1=np.mean(data_ReactTime_Hold_09['elem_1'])
vec_mean_ReactTime_Hold_09_elem_2=np.mean(data_ReactTime_Hold_09['elem_2'])
vec_mean_ReactTime_Hold_09_elem_3=np.mean(data_ReactTime_Hold_09['elem_3'])
vec_mean_ReactTime_Hold_09=[vec_mean_ReactTime_Hold_09_elem_0, vec_mean_ReactTime_Hold_09_elem_1, vec_mean_ReactTime_Hold_09_elem_2, vec_mean_ReactTime_Hold_09_elem_3]

vec_std_ReactTime_Hold_09_elem_0=np.std(data_ReactTime_Hold_09['elem_0'])
vec_std_ReactTime_Hold_09_elem_1=np.std(data_ReactTime_Hold_09['elem_1'])
vec_std_ReactTime_Hold_09_elem_2=np.std(data_ReactTime_Hold_09['elem_2'])
vec_std_ReactTime_Hold_09_elem_3=np.std(data_ReactTime_Hold_09['elem_3'])
vec_std_ReactTime_Hold_09=[vec_std_ReactTime_Hold_09_elem_0, vec_std_ReactTime_Hold_09_elem_1, vec_std_ReactTime_Hold_09_elem_2, vec_std_ReactTime_Hold_09_elem_3]

#regression RI
data_regr_RI_Hold_09 = data_RI_Hold_09.to_numpy()
coeff_RI_09 = np.zeros((40,2))
vector_delay_RI_09=np.array(range(0,31,10))
vec_r_square_RI_09=np.zeros((40))

def func(x, a, b):
    return a * x + b 
for i in list(range(40)):
    print(i)
    temp_RI_09=data_regr_RI_Hold_09[i,[1,2,3,4]]
    print(temp_RI_09)
    popt_RI_09, pcov_RI_09= curve_fit(func, vector_delay_RI_09,temp_RI_09)
    coeff_RI_09[i,0] = popt_RI_09[1]
    coeff_RI_09[i,1] = popt_RI_09[0]
    #residui 
    residuals_RI_09=temp_RI_09-func(vector_delay_RI_09,*popt_RI_09)
    ss_res_RI_09=np.sum(residuals_RI_09**2)
    ss_tot_RI_09=np.sum((temp_RI_09-np.mean(temp_RI_09))**2)
    vec_r_square_RI_09[i]=1-(ss_res_RI_09/ss_tot_RI_09)
    
vec_mean_regr_RI_Hold_09_elem_0=np.mean(coeff_RI_09[:,1])
vec_mean_regr_RI_Hold_09_elem_1=np.mean(coeff_RI_09[:,0])

vec_sem_regr_RI_Hold_09_elem_0=np.std(coeff_RI_09[:,1])/np.sqrt(40)
vec_sem_regr_RI_Hold_09_elem_1=np.std(coeff_RI_09[:,0])/np.sqrt(40)

#tscore
t_score_RI_09=vec_mean_regr_RI_Hold_09_elem_0/vec_sem_regr_RI_Hold_09_elem_0
pvalue_RI_09= (t.sf(np.abs(t_score_RI_09),39))*2

vec_mean_r_square_RI_Hold_09=np.mean(vec_r_square_RI_09)
pearson_RI_09=np.sqrt(vec_mean_r_square_RI_Hold_09)
vec_sem_r_square_RI_Hold_09=np.std(vec_r_square_RI_09)/np.sqrt(40)

x_RI_09=np.arange(0,35,5)
y_RI_09= x_RI_09*vec_mean_regr_RI_Hold_09_elem_0+vec_mean_regr_RI_Hold_09_elem_1

#regression ReactTime 
data_regr_ReactTime_Hold_09 = data_ReactTime_Hold_09.to_numpy()
coeff_ReactTime_09 = np.zeros((40,2))
vector_delay_ReactTime_09=np.array(range(0,31,10))
vec_r_square_ReactTime_09=np.zeros((40))

def func(x, a, b):
    return a * x + b 
for i in list(range(40)):
    print(i)
    temp_ReactTime_09=data_regr_ReactTime_Hold_09[i,[1,2,3,4]]
    print(temp_ReactTime_09)
    popt_ReactTime_09, pcov_ReactTime_09 = curve_fit(func, vector_delay_ReactTime_09,temp_ReactTime_09)
    coeff_ReactTime_09[i,0] = popt_ReactTime_09[1]
    coeff_ReactTime_09[i,1] = popt_ReactTime_09[0]
    #residui 
    residuals_ReactTime_09=temp_ReactTime_09-func(vector_delay_ReactTime_09,*popt_ReactTime_09)
    ss_res_ReactTime_09=np.sum(residuals_ReactTime_09**2)
    ss_tot_ReactTime_09=np.sum((temp_ReactTime_09-np.mean(temp_ReactTime_09))**2)
    vec_r_square_ReactTime_09[i]=1-(ss_res_ReactTime_09/ss_tot_ReactTime_09)
    
vec_mean_regr_ReactTime_Hold_09_elem_0=np.mean(coeff_ReactTime_09[:,1])
vec_mean_regr_ReactTime_Hold_09_elem_1=np.mean(coeff_ReactTime_09[:,0])

vec_sem_regr_ReactTime_Hold_09_elem_0=np.std(coeff_ReactTime_09[:,1])/np.sqrt(40)
vec_sem_regr_ReactTime_Hold_09_elem_1=np.std(coeff_ReactTime_09[:,0])/np.sqrt(40)

#tscore
t_score_ReactTime_09=vec_mean_regr_ReactTime_Hold_09_elem_0/vec_sem_regr_ReactTime_Hold_09_elem_0
pvalue_ReactTime_09= (t.sf(np.abs(t_score_ReactTime_09),39))*2

vec_mean_r_square_ReactTime_Hold_09=np.mean(vec_r_square_ReactTime_09)
pearson_ReactTime_09=np.sqrt(vec_mean_r_square_ReactTime_Hold_09)
vec_sem_r_square_ReactTime_Hold_09=np.std(vec_r_square_ReactTime_09)/np.sqrt(40)

x_ReactTime_09=np.arange(0,35,5)
y_ReactTime_09=x_ReactTime_09* vec_mean_regr_ReactTime_Hold_09_elem_0+vec_mean_regr_ReactTime_Hold_09_elem_1

np.savetxt('coeff_RI_Hold_09_elem1.txt', coeff_RI_09[:,0])
np.savetxt('coeff_RI_Hold_09_elem0.txt', coeff_RI_09[:,1])

np.savetxt('coeff_ReactTime_correct_Hold_09_elem1.txt', coeff_ReactTime_09[:,0])
np.savetxt('coeff_ReactTime_correct_Hold_09_elem0.txt', coeff_ReactTime_09[:,1])

plt.figure()
plt.scatter([0,10,20,30],vec_mean_RI_Hold_01,s=40, color='black', alpha=1, marker='o', label='0.1')
plt.errorbar([0,10,20,30],vec_mean_RI_Hold_01, yerr= vec_std_RI_Hold_01/np.sqrt(40),fmt='o',color='black', alpha=1)
plt.scatter([0,10,20,30],vec_mean_RI_Hold_03,s=40, color='#9a0200', alpha=1, marker='o',label='0.3')
plt.errorbar([0,10,20,30],vec_mean_RI_Hold_03, yerr= vec_std_RI_Hold_03/np.sqrt(40),fmt='o',color='#9a0200',alpha=1)
plt.scatter([0,10,20,30],vec_mean_RI_Hold_05,s=40,  color='red', alpha=1, marker='o',label='0.5')
plt.errorbar([0,10,20,30],vec_mean_RI_Hold_05, yerr= vec_std_RI_Hold_05/np.sqrt(40),fmt='o',color='red', alpha=1)
plt.scatter([0,10,20,30],vec_mean_RI_Hold_07,s=40, color='tomato', alpha=1, marker='o', label='0.7')
plt.errorbar([0,10,20,30],vec_mean_RI_Hold_07, yerr= vec_std_RI_Hold_07/np.sqrt(40),fmt='o',color='tomato', alpha=1)
plt.scatter([0,10,20,30],vec_mean_RI_Hold_09,s=40,  color='darkorange', alpha=1, marker='o', label='0.9')
plt.errorbar([0,10,20,30],vec_mean_RI_Hold_09, yerr= vec_std_RI_Hold_09/np.sqrt(40),fmt='o',color='darkorange', alpha=1)
plt.xlabel("Delay Hold Trials [samples]", size=17)
plt.ylabel("RI Hold [a.u.]",size=17)
plt.plot(x_RI_01, y_RI_01,color='black', alpha=1,  label='0.1')
plt.plot(x_RI_03, y_RI_03,color='#9a0200', alpha=1,label='0.3')
plt.plot(x_RI_05, y_RI_05,color='red', alpha=1,label='0.5')
plt.plot(x_RI_07, y_RI_07,color='tomato', alpha=1,label='0.7')
plt.plot(x_RI_09, y_RI_09,color='darkorange', alpha=1,label='0.9')
plt.ylim(0,1)
plt.show()

X1= [0, 10, 20, 30]
Y1 = [0.1,0.3,0.5,0.7,0.9]

vec_mean_RI_Hold_01=np.array(vec_mean_RI_Hold_01)
vec_mean_RI_Hold_01=vec_mean_RI_Hold_01[:,np.newaxis]
vec_mean_RI_Hold_03=np.array(vec_mean_RI_Hold_03)
vec_mean_RI_Hold_03=vec_mean_RI_Hold_03[:,np.newaxis]
vec_mean_RI_Hold_05=np.array(vec_mean_RI_Hold_05)
vec_mean_RI_Hold_05=vec_mean_RI_Hold_05[:,np.newaxis]
vec_mean_RI_Hold_07=np.array(vec_mean_RI_Hold_07)
vec_mean_RI_Hold_07=vec_mean_RI_Hold_07[:,np.newaxis]
vec_mean_RI_Hold_09=np.array(vec_mean_RI_Hold_09)
vec_mean_RI_Hold_09=vec_mean_RI_Hold_09[:,np.newaxis]
Z1= np.concatenate((vec_mean_RI_Hold_01, vec_mean_RI_Hold_03, vec_mean_RI_Hold_05, vec_mean_RI_Hold_07,vec_mean_RI_Hold_09),axis=1)
Z1=(np.transpose(Z1)).ravel()
X1,Y1=np.meshgrid(X1,Y1)
X1=X1.ravel()
Y1=Y1.ravel()
plotx1,ploty1, = np.meshgrid(np.linspace(np.min(X1),np.max(X1),40),\
                           np.linspace(np.min(Y1),np.max(Y1),40))
plotz1 = interp.griddata((X1,Y1),Z1,(plotx1,ploty1),method='linear')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf1=ax.plot_surface(plotx1,ploty1,plotz1,cstride=1,rstride=1,cmap='viridis',alpha=0.7, linewidth=0, antialiased=False, zorder=1)
ax.view_init(azim=-35)
ax.set_zlim3d(np.min(Z1), np.max(Z1))
x_label='Delay Hold Trials[samples]'
y_label='Dopamine'
z_label='RI Hold [samples]'
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
fig.colorbar(surf1, label=z_label)
ax.plot(x_RI_01,0.1*np.ones(7), y_RI_01,color='black', alpha=1,label='0.1',linewidth=1.3, zorder=3)
ax.plot(x_RI_03,0.3*np.ones(7), y_RI_03,color='#9a0200', alpha=1,label='0.3',linewidth=1.3, zorder=3)
ax.plot(x_RI_05,0.5*np.ones(7), y_RI_05,color='red', alpha=1,label='0.5',linewidth=1.3, zorder=3)
ax.plot(x_RI_07,0.7*np.ones(7), y_RI_07,color='tomato', alpha=1,label='0.7',linewidth=1.3, zorder=3)
ax.plot(x_RI_09,0.9*np.ones(7), y_RI_09,color='darkorange', alpha=1,label='0.9',linewidth=1.3, zorder=3)
plt.show()

plt.figure()
plt.scatter([0,10,20,30],vec_mean_ReactTime_Hold_01,s=40, color='black', alpha=1, marker='o',label='0.1')
plt.errorbar([0,10,20,30],vec_mean_ReactTime_Hold_01, yerr= vec_std_ReactTime_Hold_01/np.sqrt(40), fmt='o',color='black', alpha=1)
plt.scatter([0,10,20,30],vec_mean_ReactTime_Hold_03,s=40, color='#9a0200', alpha=1, marker='o',label='0.3')
plt.errorbar([0,10,20,30],vec_mean_ReactTime_Hold_03, yerr= vec_std_ReactTime_Hold_03/np.sqrt(40), fmt='o',color='#9a0200', alpha=1)
plt.scatter([0,10,20,30],vec_mean_ReactTime_Hold_05,s=40, color='red', alpha=1, marker='o',label='0.5')
plt.errorbar([0,10,20,30],vec_mean_ReactTime_Hold_05, yerr= vec_std_ReactTime_Hold_05/np.sqrt(40), fmt='o',color='red', alpha=1)
plt.scatter([0,10,20,30],vec_mean_ReactTime_Hold_07,s=40, color='tomato', alpha=1, marker='o',label='0.7')
plt.errorbar([0,10,20,30],vec_mean_ReactTime_Hold_07, yerr= vec_std_ReactTime_Hold_07/np.sqrt(40),fmt='o', color='tomato', alpha=1)
plt.scatter([0,10,20,30],vec_mean_ReactTime_Hold_09,s=40, color='darkorange', alpha=1, marker='o',label='0.9')
plt.errorbar([0,10,20,30],vec_mean_ReactTime_Hold_09, yerr= vec_std_ReactTime_Hold_09/np.sqrt(40),fmt='o', color='darkorange', alpha=1)
plt.xlabel("Delay Hold Trials [samples]", size=17)
plt.ylabel("Reaction Time Hold [samples]",size=17)
plt.plot(x_ReactTime_01, y_ReactTime_01,color='black', alpha=1,   label='0.1')
plt.plot(x_ReactTime_03, y_ReactTime_03,color='#9a0200', alpha=1, label='0.3')
plt.plot(x_ReactTime_05, y_ReactTime_05,color='red', alpha=1, label='0.5')
plt.plot(x_ReactTime_07, y_ReactTime_07,color='tomato', alpha=1, label='0.7')
plt.plot(x_ReactTime_09, y_ReactTime_09,color='darkorange', alpha=1, label='0.9')
plt.show()

   
X = [0, 10, 20, 30]
Y = [0.1,0.3,0.5,0.7,0.9]

vec_mean_ReactTime_Hold_01=np.array(vec_mean_ReactTime_Hold_01)
vec_mean_ReactTime_Hold_01=vec_mean_ReactTime_Hold_01[:,np.newaxis]
vec_mean_ReactTime_Hold_03=np.array(vec_mean_ReactTime_Hold_03)
vec_mean_ReactTime_Hold_03=vec_mean_ReactTime_Hold_03[:,np.newaxis]
vec_mean_ReactTime_Hold_05=np.array(vec_mean_ReactTime_Hold_05)
vec_mean_ReactTime_Hold_05=vec_mean_ReactTime_Hold_05[:,np.newaxis]
vec_mean_ReactTime_Hold_07=np.array(vec_mean_ReactTime_Hold_07)
vec_mean_ReactTime_Hold_07=vec_mean_ReactTime_Hold_07[:,np.newaxis]
vec_mean_ReactTime_Hold_09=np.array(vec_mean_ReactTime_Hold_09)
vec_mean_ReactTime_Hold_09=vec_mean_ReactTime_Hold_09[:,np.newaxis]
Z= np.concatenate((vec_mean_ReactTime_Hold_01, vec_mean_ReactTime_Hold_03, vec_mean_ReactTime_Hold_05, vec_mean_ReactTime_Hold_07,vec_mean_ReactTime_Hold_09),axis=1)
Z=(np.transpose(Z)).ravel()
X,Y=np.meshgrid(X,Y)
X=X.ravel()
Y=Y.ravel()
plotx,ploty, = np.meshgrid(np.linspace(np.min(X),np.max(X),40),\
                           np.linspace(np.min(Y),np.max(Y),40))
plotz = interp.griddata((X,Y),Z,(plotx,ploty),method='linear')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf=ax.plot_surface(plotx,ploty,plotz,cstride=1,rstride=1,cmap='viridis',alpha=0.7, linewidth=0, antialiased=False, zorder=1)
ax.view_init(azim=145)
ax.set_zlim3d(np.min(Z), np.max(Z))
x_label='Delay Hold Trials[samples]'
y_label='Dopamine'
z_label='Reaction Time Hold [samples]'
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
fig.colorbar(surf, label=z_label)

ax.plot(x_ReactTime_01,0.1*np.ones(7), y_ReactTime_01,color='black', alpha=1,label='0.1',linewidth=1.3, zorder=3)
ax.plot(x_ReactTime_03,0.3*np.ones(7), y_ReactTime_03,color='#9a0200', alpha=1,label='0.3',linewidth=1.3,zorder=3)
ax.plot(x_ReactTime_05,0.5*np.ones(7), y_ReactTime_05,color='red', alpha=1,label='0.5',linewidth=1.3,zorder=3)
ax.plot(x_ReactTime_07,0.7*np.ones(7), y_ReactTime_07,color='tomato', alpha=1,label='0.7',linewidth=1.3,zorder=3)
ax.plot(x_ReactTime_09,0.9*np.ones(7), y_ReactTime_09,color='darkorange', alpha=1,label='0.9',linewidth=1.3,zorder=3)
ax.set_facecolor('white')
plt.show()

