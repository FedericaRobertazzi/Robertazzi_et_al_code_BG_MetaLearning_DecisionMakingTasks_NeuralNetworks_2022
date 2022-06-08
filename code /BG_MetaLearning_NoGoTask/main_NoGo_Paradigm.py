#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: federicarobertazzi
"""
import numpy as np
#import matplotlib.pyplot as plt

from neurons import PPC,ACC_Q,ACC,LPFC,Striatum,SNr,Thalamus,PMC
from synapses import synapse,synaptic_plasticity
from action_probability import action_probability
from parameters_meta_learning import parameters
from utility import visual_input,check_salience,check_pcc,motor_output,compute_reward,stationary_stochastic_reward,reset_Q,reset_beta
from utility import get_activity,prevent_Qstack,get_QAct,get_QPrev,random_distr,action_vec_to_mat,update_metavalue,hold_react
from mechanisms_meta_learning import rel_D1_beta,serotonin_to_dopamine,compute_TD_meta_learning,compute_forgetting
from parameters_and_metrics_computation import compute_net_parameters,compute_right_inhibition,compute_global_accuracy

params = parameters()

#neurons 
#PPC layer
PPC_Neu0 = PPC(params.tau_PPC_Neu,params.x0_PPC_Neu,params.s0_PPC_Neu,params.slope_PPC_Neu)
PPC_Neu1 = PPC(params.tau_PPC_Neu,params.x0_PPC_Neu,params.s0_PPC_Neu,params.slope_PPC_Neu)
PPC_Neu2 = PPC(params.tau_PPC_Neu,params.x0_PPC_Neu,params.s0_PPC_Neu,params.slope_PPC_Neu)
PPC_Neu3 = PPC(params.tau_PPC_Neu,params.x0_PPC_Neu,params.s0_PPC_Neu,params.slope_PPC_Neu)
PPC_Neu =[[PPC_Neu0, PPC_Neu1], [PPC_Neu2, PPC_Neu3]]

#ACC action values
ACC_Q0 = ACC_Q(params.alpha,params.Q0)
ACC_Q1 = ACC_Q(params.alpha,params.Q0)
ACC_Q2 = ACC_Q(params.alpha,params.Q0)
ACC_Q3 = ACC_Q(params.alpha,params.Q0)
ACC_Q =[[ACC_Q0, ACC_Q1], [ACC_Q2, ACC_Q3]]

#ACC layer 
ACC_Neu0 = ACC(params.tau_ACC_Neu,params.x0_ACC_Neu,params.s0_ACC_Neu,params.slope_ACC_Neu)
ACC_Neu1 = ACC(params.tau_ACC_Neu,params.x0_ACC_Neu,params.s0_ACC_Neu,params.slope_ACC_Neu)
ACC_Neu2 = ACC(params.tau_ACC_Neu,params.x0_ACC_Neu,params.s0_ACC_Neu,params.slope_ACC_Neu) 
ACC_Neu3 = ACC(params.tau_ACC_Neu,params.x0_ACC_Neu,params.s0_ACC_Neu,params.slope_ACC_Neu)
ACC_Neu =[[ACC_Neu0, ACC_Neu1], [ACC_Neu2, ACC_Neu3]]

#LPFC layer 
LPFC_Neu0 = LPFC(params.tau_LPFC_Neu,params.x0_LPFC_Neu,params.s0_LPFC_Neu,params.slope_LPFC_Neu,params.prob0)
LPFC_Neu1 = LPFC(params.tau_LPFC_Neu,params.x0_LPFC_Neu,params.s0_LPFC_Neu,params.slope_LPFC_Neu,params.prob0)
LPFC_Neu2 = LPFC(params.tau_LPFC_Neu,params.x0_LPFC_Neu,params.s0_LPFC_Neu,params.slope_LPFC_Neu,params.prob0)
LPFC_Neu3 = LPFC(params.tau_LPFC_Neu,params.x0_LPFC_Neu,params.s0_LPFC_Neu,params.slope_LPFC_Neu,params.prob0)
LPFC_Neu =[[LPFC_Neu0, LPFC_Neu1], [LPFC_Neu2, LPFC_Neu3]]

#Striatum layer 
Striatum_Neu0 = Striatum(params.tau_Striatum_Neu,params.x0_Striatum_Neu,params.s0_Striatum_Neu,params.slope_Striatum_Neu)
Striatum_Neu1 = Striatum(params.tau_Striatum_Neu,params.x0_Striatum_Neu,params.s0_Striatum_Neu,params.slope_Striatum_Neu)
Striatum_Neu2 = Striatum(params.tau_Striatum_Neu,params.x0_Striatum_Neu,params.s0_Striatum_Neu,params.slope_Striatum_Neu)
Striatum_Neu3 = Striatum(params.tau_Striatum_Neu,params.x0_Striatum_Neu,params.s0_Striatum_Neu,params.slope_Striatum_Neu)
Striatum_Neu =[[Striatum_Neu0, Striatum_Neu1], [Striatum_Neu2, Striatum_Neu3]]

#SNr layer 
SNr_Neu0 = SNr(params.tau_SNr_Neu,params.x0_SNr_Neu,params.s0_SNr_Neu,params.slope_SNr_Neu)
SNr_Neu1 = SNr(params.tau_SNr_Neu,params.x0_SNr_Neu,params.s0_SNr_Neu,params.slope_SNr_Neu)
SNr_Neu2 = SNr(params.tau_SNr_Neu,params.x0_SNr_Neu,params.s0_SNr_Neu,params.slope_SNr_Neu)
SNr_Neu3 = SNr(params.tau_SNr_Neu,params.x0_SNr_Neu,params.s0_SNr_Neu,params.slope_SNr_Neu)
SNr_Neu =[[SNr_Neu0, SNr_Neu1], [SNr_Neu2, SNr_Neu3]]

#Thalamus layer 
Thalamus_Neu0 = Thalamus(params.tau_Thalamus_Neu,params.x0_Thalamus_Neu,params.s0_Thalamus_Neu,params.slope_Thalamus_Neu)
Thalamus_Neu1 = Thalamus(params.tau_Thalamus_Neu,params.x0_Thalamus_Neu,params.s0_Thalamus_Neu,params.slope_Thalamus_Neu)
Thalamus_Neu2 = Thalamus(params.tau_Thalamus_Neu,params.x0_Thalamus_Neu,params.s0_Thalamus_Neu,params.slope_Thalamus_Neu)
Thalamus_Neu3 = Thalamus(params.tau_Thalamus_Neu,params.x0_Thalamus_Neu,params.s0_Thalamus_Neu,params.slope_Thalamus_Neu)
Thalamus_Neu =[[Thalamus_Neu0, Thalamus_Neu1], [Thalamus_Neu2, Thalamus_Neu3]]

#PMC layer
PMC_Neu0 = PMC(params.tau_PMC_Neu,params.x0_PMC_Neu,params.s0_PMC_Neu,params.slope_PMC_Neu)
PMC_Neu1 = PMC(params.tau_PMC_Neu,params.x0_PMC_Neu,params.s0_PMC_Neu,params.slope_PMC_Neu)
PMC_Neu2 = PMC(params.tau_PMC_Neu,params.x0_PMC_Neu,params.s0_PMC_Neu,params.slope_PMC_Neu)
PMC_Neu3 = PMC(params.tau_PMC_Neu,params.x0_PMC_Neu,params.s0_PMC_Neu,params.slope_PMC_Neu)
PMC_Neu =[[PMC_Neu0, PMC_Neu1], [PMC_Neu2, PMC_Neu3]]

# beta init
beta = []
beta.append(np.random.uniform(0,5))

# action probability
P0 = action_probability(params.beta0,params.prob0,[0,0])
P1 = action_probability(params.beta0,params.prob0,[0,1])
P2 = action_probability(params.beta0,params.prob0,[1,0])
P3 = action_probability(params.beta0,params.prob0,[1,1])
P = [[P0,P1],[P2,P3]]

#synapses 
#from PPC
PPC_to_ACC = synapse(params.weight_PPC_to_ACC)
PPC_to_LPFC = synapse(params.weight_PPC_to_LPFC)
PPC_to_Striatum = synapse(params.weight_PPC_to_Striatum)

#from ACC 
ACC_to_LPFC = synapse(params.weight_ACC_to_LPFC)
#ACC_to_VTA = synapse(params.weight_ACC_to_VTA)

#from LPFC
#plasticity
LPFC_to_Striatum_0 = synaptic_plasticity(params.weight_LPFC_to_Striatum,params.Q0)
LPFC_to_Striatum_1 = synaptic_plasticity(params.weight_LPFC_to_Striatum,params.Q0)
LPFC_to_Striatum_2 = synaptic_plasticity(params.weight_LPFC_to_Striatum,params.Q0)
LPFC_to_Striatum_3 = synaptic_plasticity(params.weight_LPFC_to_Striatum,params.Q0)
LPFC_to_Striatum=[[ LPFC_to_Striatum_0,LPFC_to_Striatum_1],[LPFC_to_Striatum_2, LPFC_to_Striatum_3]]

#from Striatum
Striatum_to_SNr = synapse(params.weight_Striatum_to_SNr)

#from SNr 
SNr_to_Thalamus = synapse(params.weight_SNr_to_Thalamus)

#from Thalamus 
Thalamus_to_PMC = synapse(params.weight_Thalamus_to_PMC)

#from PMC 
PMC_to_ACC = synapse(params.weight_PMC_to_ACC)
PMC_to_Striatum = synapse(params.weight_PMC_to_Striatum)

# visual input
inp = visual_input(params.niter,params.inp_start,params.inp_stop)

#salience input 
sal = check_salience(inp,params.salience0)

firing_PPC = np.zeros((params.size, params.size, params.niter))
firing_ACC = np.zeros((params.size, params.size, params.niter))
firing_LPFC = np.zeros((params.size, params.size, params.niter))
firing_Striatum = np.zeros((params.size, params.size, params.niter))
firing_SNr = np.zeros((params.size, params.size, params.niter))
firing_Thalamus = np.zeros((params.size, params.size, params.niter))
firing_PMC = np.zeros((params.size, params.size, params.niter))

PPC_to_ACC_matrix = np.zeros((params.size,params.niter))
PPC_to_LPFC_matrix = np.zeros((params.size,params.niter))
PPC_to_Striatum_matrix = np.zeros((params.size,params.niter))
ACC_to_LPFC_matrix = np.zeros((params.size,params.niter))
LPFC_to_Striatum_matrix = np.zeros((params.size,params.niter))
Striatum_to_SNr_matrix = np.zeros((params.size,params.niter))
SNr_to_Thalamus_matrix = np.zeros((params.size,params.niter))
Thalamus_to_PMC_matrix = np.zeros((params.size,params.niter))
PMC_to_ACC_matrix = np.zeros((params.size,params.niter))
PMC_to_Striatum_matrix = np.zeros((params.size,params.niter))

#parameters init
Pmax =[]
action_vec =[]
reward_vec = []
flag_updateTD = []
TD_memory = []
delta_rew = []
time_hold = []
time_crucial_trial = []
count_problem=[]
trial_type_vec = []

MetaValue_Direction = [0,0]
MetaValue_Hold = [0,0]
action=0
reward = 0
cont_salient = 0
TD = 0
count_ppc = 0
l=np.random.randint(0,2)
#trial type (Go 50% or NoGo 50%)
trial_type_set = [0,1]
prob_trial_type = [0.5,0.5]
trial_type = 1 #init

#reward
r_values_Go = params.matrix[l]
r_values_No_Go = [0,0,1,0]
print('r values Go',r_values_Go)
print('r values NoGo',r_values_No_Go)

n_problems = 0
n_success = 0

n_trials_block = 10
n_trials_block_counter = 0

count_ppc = 0
flag_hold = False
done_crucial = 0

# parameters ML init
Sero = []
Sero.append(params.serotonin)
DopaD1 = []
D1, D2 = serotonin_to_dopamine(params.serotonin, params.k_VTA_D1, params.k_SNc_D2)
DopaD1.append(D1)
DopaD2 = []
DopaD2.append(D2)

No_Go_failure_type=[]#NoGo failure trials : omol or eter 

print('Sero:', Sero)
print('D1:', DopaD1)
print('D2:', DopaD2)

count_step_delay=0
vector_delay=np.zeros(4)#no delay 
print('vector delay:', vector_delay)
delay_type=[]
print('delay type:',delay_type)

for n in range(params.niter-1): 
    count_step_delay=count_step_delay+1
    if count_ppc != 4:
        trial_type = 1
    if count_ppc==5:
       done_crucial = 0
       flag_hold = False
       count_ppc = 0
       beta = reset_beta(beta)
       ACC_Q = reset_Q(ACC_Q)
       l=np.random.randint(0,2)
       if params.rew_method == 'deterministic':
          r_values = params.matrix[l]
       elif params.rew_method == 'random':
            #this function is equal to deterministic case if there are 1 and 0, 
            #change this values for custom probability
            r_values = stationary_stochastic_reward(params.matrix[l],params.matrix)  
    if count_ppc == 4 and done_crucial == 0: # target detection 
           done_crucial = 1
           print('START CRUCIAL TRIAL ########################################')
           print('ppc 4 yes')
           trial_type = random_distr(trial_type_set, prob_trial_type)
           trial_type_vec.append(trial_type)        
           if trial_type == 0:
                flag_hold = True
                r_values = r_values_No_Go
    D1,D2 = serotonin_to_dopamine(Sero[-1], params.k_VTA_D1, params.k_SNc_D2)
    DopaD1.append(D1)
    DopaD2.append(D2)

    # compute input
    for i in range(len(PPC_Neu)):
        for j in range(len(PPC_Neu[0])):
            #PPC connections 
             PPC_to_ACC.connect(PPC_Neu[i][j])
             PPC_to_ACC_matrix[i][j]=PPC_to_ACC.inp*ACC_Q[i][j].Q
             
             PPC_to_LPFC.connect(PPC_Neu[i][j])
             PPC_to_LPFC_matrix[i][j]=PPC_to_LPFC.inp
             
             PPC_to_Striatum.connect(PPC_Neu[i][j])
             PPC_to_Striatum_matrix[i][j]=PPC_to_Striatum.inp
             
             #ACC connections
             ACC_to_LPFC.connect(ACC_Neu[i][j])
             ACC_to_LPFC_matrix[i][j]=ACC_to_LPFC.inp
             
             #ACC_to_VTA.connect(ACC_Neu[i][j])
             #ACC_to_VTA_matrix[i][j]=ACC_to_VTA.inp
           
             #LPFC connections
             LPFC_to_Striatum[i][j].update(P[i][j])             
             LPFC_to_Striatum[i][j].connect(LPFC_Neu[i][j])
             LPFC_to_Striatum_matrix[i][j]=LPFC_to_Striatum[i][j].inp
             
             if i == 1 and j == 1:
                LPFC_to_Striatum_matrix[i][j]=LPFC_to_Striatum[i][j].inp*5
           
             #Striatum connections 
             Striatum_to_SNr.connect(Striatum_Neu[i][j])
             Striatum_to_SNr_matrix[i][j]= Striatum_to_SNr.inp
             
             #SNr connections 
             SNr_to_Thalamus.connect(SNr_Neu[i][j])
             SNr_to_Thalamus_matrix[i][j]= SNr_to_Thalamus.inp
             
             #Thalamus connections
             Thalamus_to_PMC.connect(Thalamus_Neu[i][j])
             Thalamus_to_PMC_matrix[i][j] = Thalamus_to_PMC.inp 
          
             #PMC connections 
             PMC_to_ACC.connect(PMC_Neu[i][j])
             PMC_to_ACC_matrix[i][j]= PMC_to_ACC.inp
             
             PMC_to_Striatum.connect(PMC_Neu[i][j])
             PMC_to_Striatum_matrix[i][j]= PMC_to_Striatum.inp
             
    for i in range(len(P)):
        for j in range(len(P[0])):
             P[i][j].set_values(beta[-1],ACC_Q)
             P[i][j].probab()
    if sal[n]  == 1:
        cont_salient = cont_salient + 1     
        if (cont_salient%2) != 0:
            print('ACC INP LEFT:',PPC_to_ACC_matrix[0][0])
            print('ACC INP RIGHT:',PPC_to_ACC_matrix[0][1])
            print('ACC INP HOLD:',PPC_to_ACC_matrix[1][0])
            if count_ppc!=4:
                time_crucial_trial.append(0)
            else:
                time_crucial_trial.append(1)
            print('check ppc 2:',count_ppc)
            QAct = get_QAct(ACC_Q)
            var=np.random.randint(0,4)
            delay=vector_delay[var]
            print('delay:',delay)
            if flag_hold:
                delay_type.append(delay)
            else: 
                delay_type.append(-1)      
            if flag_hold and count_step_delay >= round(params.deltaT*delay):
                count_step_delay=0
                ACC_Q, beta = hold_react(MetaValue_Direction,MetaValue_Hold,beta,ACC_Q, params.MetaValue_Thr)
                for i in range(len(P)):
                    for j in range(len(P[0])):
                        P[i][j].set_values(beta[-1],ACC_Q)
                        P[i][j].probab()                   
                print('hold react yes')
                print('beta {} and 1P test {}, 2P test {} and 3P test HOLD {}:'.format(beta[-1], P[0][0].probability, P[0][1].probability, P[1][0].probability))
                time_hold.append(1)
            else:
                time_hold.append(0)
            if cont_salient < 4:
               QPrev = QAct
            else:
               QPrev = get_QPrev(ACC_Q)
            print('Beta {} and 1Q test {}, 2Q test {} and 3Q test {}:'.format(beta[-1], ACC_Q[0][0].Q, ACC_Q[0][1].Q, ACC_Q[1][0].Q))               
            print('1P test {}, 2P test {} and 3P test {}:'.format(P[0][0].probability, P[0][1].probability, P[1][0].probability))
            print('trial type:',trial_type)
            if trial_type == 1:   
               r_values = stationary_stochastic_reward(params.matrix[l],params.matrix)      
               print('r value impo:',r_values)
            else:
                r_values = r_values_No_Go
        elif (cont_salient%2) == 0:      
             curr_PMC = get_activity(PMC_Neu)
             print('1PMC test {}, 2PMC test {} and 3PMC test {}:'.format(curr_PMC[0][0], curr_PMC[0][1], curr_PMC[1][0]))            
             Pmax.append(motor_output(curr_PMC)[0])
             action = (motor_output(curr_PMC)[1])  
             print('action: ',action)
             if action == 3:
                 action = 2
             action_conv_i, action_conv_j = action_vec_to_mat(action)
             action_vec.append(action)
             print('r values:',r_values)
             reward = compute_reward(action,r_values)
             reward_vec.append(reward)
             
             if reward==0 and trial_type==0:
                 if l==action:
                    No_Go_failure_type.append(1) #omol
                 else:
                     No_Go_failure_type.append(0) #eter
             
             print('flag hold: ',flag_hold)
             MetaValue_Direction,MetaValue_Hold,delta_rew_out = update_metavalue(MetaValue_Direction,MetaValue_Hold,reward_vec,params.eta,flag_hold)
             delta_rew.append(delta_rew_out)
             flag_hold = False
             count_ppc = check_pcc(reward,count_ppc)
             if count_ppc == 4:
                 n_problems = n_problems + 1    
             print('action i', action_conv_i)
             print('action j', action_conv_j)
             print('QAct',QAct[action_conv_i][ action_conv_j])
             print('QPrev',QPrev[action_conv_i][action_conv_j])
             print('Sero',Sero[-1])
             print('Dopa',DopaD1[-1])
             print('count ppc: ', count_ppc)
             [TD,flagSalient] = compute_TD_meta_learning(reward, QAct[action_conv_i][action_conv_j], QPrev[action_conv_i][action_conv_j], Sero[-1], DopaD1[-1] )
             print('delta reward:',delta_rew_out)
             print('end trial')
             TD_memory.append(TD)
             
             # compute beta from D1 
             beta.append(rel_D1_beta(params.a0_D1_to_beta,DopaD1[-1]*TD))
             # be sure that useless neuron is always 0
             ACC_Q[1][1].Q = 0
             ACC_Q[action_conv_i][action_conv_j].update(TD,1)          
             ACC_Q = compute_forgetting(ACC_Q,[action_conv_i, action_conv_j], params.forget_factor)
             print('1Q test {}, 2Q test {} and 3Q test {}:'.format(ACC_Q[0][0].Q, ACC_Q[0][1].Q, ACC_Q[1][0].Q))
             
    for i in range(len(PPC_Neu)):
        for j in range(len(PPC_Neu[0])): 
            if i == 0 and  j ==0:    
                if l == 0:
                    PPC_Neu[i][j].update(params.deltaT,inp[0][n])
                else:
                    PPC_Neu[i][j].update(params.deltaT,0)                        
            elif i == 0 and j ==1:
                if l == 1:
                    PPC_Neu[i][j].update(params.deltaT,inp[1][n])
                else:
                    PPC_Neu[i][j].update(params.deltaT,0)                     
            elif i == 1 and j ==0 and flag_hold == True:    
                 PPC_Neu[i][j].update(params.deltaT,inp[2][n])
            elif i == 1 and j ==1:    
                 PPC_Neu[i][j].update(params.deltaT,inp[3][n])           
            else:
                PPC_Neu[i][j].update(params.deltaT,0)     
                
            PPC_Neu[i][j].sigmoid() 
            l_PPC=PPC_Neu[i][j].out
            firing_PPC[i][j][n+1]=l_PPC
            
            ACC_Neu[i][j].update(params.deltaT,PPC_to_ACC_matrix[i][j]) #+PMC_to_ACC_matrix[i][j]) 
            ACC_Neu[i][j].store()
            l_ACC=ACC_Neu[i][j].out
            firing_ACC[i][j][n]=l_ACC
            
            LPFC_Neu[i][j].update(params.deltaT, ACC_to_LPFC_matrix[i][j]) #+PPC_to_LPFC_matrix[i][j])
            LPFC_Neu[i][j].sigmoid()
            l_LPFC=LPFC_Neu[i][j].out
            firing_LPFC[i][j][n+1]=l_LPFC
            
            Striatum_Neu[i][j].update_s0(DopaD2[-1], params.a0_D2_to_s0)
            Striatum_Neu[i][j].update(params.deltaT, LPFC_to_Striatum_matrix[i][j]) #+ PMC_to_Striatum_matrix[i][j])# PPC_to_Striatum_matrix[i][j]
            Striatum_Neu[i][j].sigmoid()
            l_Striatum=Striatum_Neu[i][j].out
            firing_Striatum[i][j][n+1]=l_Striatum
            
            SNr_Neu[i][j].update(params.deltaT,Striatum_to_SNr_matrix[i][j]+ params.tonic_input_SNr)
            SNr_Neu[i][j].sigmoid()
            l_SNr=SNr_Neu[i][j].out
            firing_SNr[i][j][n+1]=l_SNr
            
            Thalamus_Neu[i][j].update(params.deltaT,SNr_to_Thalamus_matrix[i][j]+params.tonic_input_Thal)
            Thalamus_Neu[i][j].sigmoid()
            l_Thalamus=Thalamus_Neu[i][j].out
            firing_Thalamus[i][j][n+1]=l_Thalamus
        
            PMC_Neu[i][j].update(params.deltaT,Thalamus_to_PMC_matrix[i][j]) 
            PMC_Neu[i][j].sigmoid()
            l_PMC=PMC_Neu[i][j].out
            firing_PMC[i][j][n+1]=l_PMC
              
    ACC_Q = prevent_Qstack(ACC_Q)

print('##############################################')
print(' Simulation settings:')
print(' level of serotonin:', np.mean(Sero))
print(' Level of D1:', np.mean(DopaD1))
print(' Level of D2:', np.mean(DopaD2))
print('##############################################')

print('##############################################')
print(' Check variables: ')
print(' len reward: ',len(reward_vec))
print(' len time hold: ',len(time_hold))
print(' len stimuli: ',len(params.inp_start[0]))
print(' len delta rew: ',len(delta_rew))
print(' len meta value hold ',len(MetaValue_Hold))
print(' len meta value direction ',len(MetaValue_Direction))
print(' len action ',len(action_vec))
print('##############################################')

#time to reach threshold
MetaValue_Hold = np.array(MetaValue_Hold)
try:
    time_tothr = np.argwhere(MetaValue_Hold <= params.MetaValue_Thr).min()
    print('trials needed to learn hold meta-value:',time_tothr)
    time_toend=params.nstim-time_tothr
    print('trials from learn hold meta-value and the end:',time_toend)
except:
    print('Metavalue of holds always greater than -0.25')

when_hold= np.argwhere(np.array(time_hold) == 1)

when_hold_training = when_hold[when_hold <= time_tothr]
when_hold_test = when_hold[when_hold > time_tothr]

firing_PMC_training=np.zeros((2,2,params.inp_start[0][time_tothr]))
firing_PMC_test=np.zeros((2,2,params.niter-params.inp_start[0][time_tothr]))

for i in range(2):
    for j in range(2):
        firing_PMC_training[i,j,:]=firing_PMC[i,j,0:params.inp_start[0][time_tothr]]
        firing_PMC_test[i,j,:]=firing_PMC[i,j,(params.inp_start[0][time_tothr]):]

count_inp_start=time_tothr  
print('count inp start:',count_inp_start)

delay_type_training1=delay_type[0:(count_inp_start)]
delay_type_training=np.array(delay_type_training1)
print('delay type training:',delay_type_training)
print('delay type training size:', np.shape(delay_type_training))

time_crucial_trial_training1=time_crucial_trial[0:(count_inp_start)]
time_crucial_trial_training=list(map(bool,time_crucial_trial_training1))
print('time crucial trial training:', time_crucial_trial_training)
print('time crucial trial training size:', np.shape(time_crucial_trial_training))

reward_vec_training1=reward_vec[0:(count_inp_start)]
reward_vec_training=np.array(reward_vec_training1)
print('reward vec training:',reward_vec_training)
print('reward vec training size:', np.shape(reward_vec_training))

action_vec_training1=action_vec[0:(count_inp_start)]
action_vec_training=np.array(action_vec_training1)
print('action vec training:',action_vec_training)
print('action vec training size:', np.shape(action_vec_training))

inp_start_training1=params.inp_start[1][0:(count_inp_start)]
inp_start_training=np.array(inp_start_training1)
print('inp start training:',inp_start_training)
print('inp start training size:', np.shape(inp_start_training))

Pmax_training1=Pmax[0:(count_inp_start)]
Pmax_training=np.array(Pmax_training1)

summa=np.sum(time_crucial_trial_training)
print('summa:',summa)

trial_type_training1=trial_type_vec[0:(summa)]
trial_type_training=np.array(trial_type_training1)
print('trial type training:',trial_type_training)
print('trial type training size:', np.shape(trial_type_training))

print('####################################################################')
print('time tothtr:',time_tothr)
#print('firing PMC training:',firing_PMC_training )
print('firing PMC training size:',np.shape(firing_PMC_training))
#print('firing PMC test:',firing_PMC_test)
print('firing PMC test size:',np.shape(firing_PMC_test))
print('####################################################################')

delay_type_test1=delay_type[(count_inp_start):]
delay_type_test=np.array(delay_type_test1)
print('delay type test:',delay_type_test)
print('delay type test size:', np.shape(delay_type_test))

time_crucial_trial_test1=time_crucial_trial[(count_inp_start):]
time_crucial_trial_test=list(map(bool,time_crucial_trial_test1))
print('time crucial trial test:', time_crucial_trial_test)
print('time crucial trial test size:', np.shape(time_crucial_trial_test))

reward_vec_test1=reward_vec[(count_inp_start):]
reward_vec_test=np.array(reward_vec_test1)
print('reward vec test:',reward_vec_test)
print('reward vec test size:', np.shape(reward_vec_test))

action_vec_test1=action_vec[(count_inp_start):]
action_vec_test=np.array(action_vec_test1)
print('action vec test:',action_vec_test)
print('action vec test size:', np.shape(action_vec_test))

inp_start_test1=params.inp_start[1][(count_inp_start):]
inp_start_test=np.array(inp_start_test1)
print('inp start test:',inp_start_test)
print('inp start test size:', np.shape(inp_start_test))

Pmax_test1=Pmax[(count_inp_start):]
Pmax_test=np.array(Pmax_test1)

trial_type_test1=trial_type_vec[(summa):]
trial_type_test=np.array(trial_type_test1)
print('trial type test:',trial_type_test)
print('trial type test size:', np.shape(trial_type_test))

n_Go_training,n_No_Go_training,n_No_Go_correct_training, react_time_Go_training_1,react_time_No_Go_total_training_1, react_time_No_Go_training_1,react_time_No_Go_correct_training_1, max_PMC_Go_training,max_PMC_No_Go_total_training, max_PMC_No_Go_training,max_PMC_No_Go_correct_training,Pmax_Go_training,Pmax_No_Go_total_training, Pmax_No_Go_training, Pmax_No_Go_correct_training =compute_net_parameters(firing_PMC,inp_start_training,trial_type_training,action_vec_training,time_crucial_trial_training,delay_type_training,Pmax_training,reward_vec_training)

No_Go_failure_type_training=np.array(No_Go_failure_type[0:(n_No_Go_training)])
No_Go_failure_type_test=np.array(No_Go_failure_type[(n_No_Go_training):])

freq_1_No_Go_failure_type_training=np.mean(No_Go_failure_type_training)*100
freq_0_No_Go_failure_type_training=100-freq_1_No_Go_failure_type_training

freq_1_No_Go_failure_type_test=np.mean(No_Go_failure_type_test)*100
freq_0_No_Go_failure_type_test=100-freq_1_No_Go_failure_type_test

num_1_No_Go_failure_type_training=sum(No_Go_failure_type_training)
num_0_No_Go_failure_type_training=len(No_Go_failure_type_training)-num_1_No_Go_failure_type_training

num_1_No_Go_failure_type_test=sum(No_Go_failure_type_test)
num_0_No_Go_failure_type_test=len(No_Go_failure_type_test)-num_1_No_Go_failure_type_test

mean_react_time_Go_training_1=np.mean(react_time_Go_training_1)
std_react_time_Go_training_1=np.std(react_time_Go_training_1)

mean_react_time_No_Go_total_training_1=np.mean(react_time_No_Go_total_training_1)
std_react_time_No_Go_total_training_1=np.std(react_time_No_Go_total_training_1)

mean_react_time_No_Go_training_1=np.mean(react_time_No_Go_training_1)
std_react_time_No_Go_training_1=np.std(react_time_No_Go_training_1)

mean_react_time_No_Go_training_1_eter=np.mean(react_time_No_Go_training_1[No_Go_failure_type_training==0])
std_react_time_No_Go_training_1_eter=np.std(react_time_No_Go_training_1[No_Go_failure_type_training==0])

mean_react_time_No_Go_training_1_omol=np.mean(react_time_No_Go_training_1[No_Go_failure_type_training==1])
std_react_time_No_Go_training_1_omol=np.std(react_time_No_Go_training_1[No_Go_failure_type_training==1])

mean_react_time_No_Go_correct_training_1=np.mean(react_time_No_Go_correct_training_1)
std_react_time_No_Go_correct_training_1=np.std(react_time_No_Go_correct_training_1)

mean_max_PMC_Go_training=np.mean(max_PMC_Go_training)
std_max_PMC_Go_training=np.std(max_PMC_Go_training)

mean_max_PMC_No_Go_total_training=np.mean(max_PMC_No_Go_total_training)
std_max_PMC_No_Go_total_training=np.std(max_PMC_No_Go_total_training)

mean_max_PMC_No_Go_training=np.mean(max_PMC_No_Go_training)
std_max_PMC_No_Go_training=np.std(max_PMC_No_Go_training)

mean_max_PMC_No_Go_training_eter=np.mean(max_PMC_No_Go_training[No_Go_failure_type_training==0])
std_max_PMC_No_Go_training_eter=np.std(max_PMC_No_Go_training[No_Go_failure_type_training==0])

mean_max_PMC_No_Go_training_omol=np.mean(max_PMC_No_Go_training[No_Go_failure_type_training==1])
std_max_PMC_No_Go_training_omol=np.std(max_PMC_No_Go_training[No_Go_failure_type_training==1])

mean_max_PMC_No_Go_correct_training=np.mean(max_PMC_No_Go_correct_training)
std_max_PMC_No_Go_correct_training=np.std(max_PMC_No_Go_correct_training)

mean_Pmax_Go_training=np.mean(Pmax_Go_training)
std_Pmax_Go_training=np.std(Pmax_Go_training)

mean_Pmax_No_Go_total_training=np.mean(Pmax_No_Go_total_training)
std_Pmax_No_Go_total_training=np.std(Pmax_No_Go_total_training)

mean_Pmax_No_Go_training=np.mean(Pmax_No_Go_training)
std_Pmax_No_Go_training=np.std(Pmax_No_Go_training)

mean_Pmax_No_Go_training_eter=np.mean(Pmax_No_Go_training[No_Go_failure_type_training==0])
std_Pmax_No_Go_training_eter=np.std(Pmax_No_Go_training[No_Go_failure_type_training==0])

mean_Pmax_No_Go_training_omol=np.mean(Pmax_No_Go_training[No_Go_failure_type_training==1])
std_Pmax_No_Go_training_omol=np.std(Pmax_No_Go_training[No_Go_failure_type_training==1])

mean_Pmax_No_Go_correct_training=np.mean(Pmax_No_Go_correct_training)
std_Pmax_No_Go_correct_training=np.std(Pmax_No_Go_correct_training)

right_inhibition_training=compute_right_inhibition(reward_vec_training,trial_type_training,time_crucial_trial_training)

accuracy_training=compute_global_accuracy(reward_vec_training,time_crucial_trial_training)

n_Go_test,n_No_Go_test,n_No_Go_correct_test,react_time_Go_test_1,react_time_No_Go_total_test_1,react_time_No_Go_test_1,react_time_No_Go_correct_test_1,max_PMC_Go_test,max_PMC_No_Go_total_test, max_PMC_No_Go_test,max_PMC_No_Go_correct_test,Pmax_Go_test,Pmax_No_Go_total_test, Pmax_No_Go_test, Pmax_No_Go_correct_test=compute_net_parameters(firing_PMC,inp_start_test,trial_type_test, action_vec_test,time_crucial_trial_test,delay_type_test,Pmax_test,reward_vec_test)

mean_react_time_Go_test_1=np.mean(react_time_Go_test_1)
std_react_time_Go_test_1=np.std(react_time_Go_test_1)

mean_react_time_No_Go_total_test_1=np.mean(react_time_No_Go_total_test_1)
std_react_time_No_Go_total_test_1=np.std(react_time_No_Go_total_test_1)

mean_react_time_No_Go_test_1=np.mean(react_time_No_Go_test_1)
std_react_time_No_Go_test_1=np.std(react_time_No_Go_test_1)

mean_react_time_No_Go_test_1_eter=np.mean(react_time_No_Go_test_1[No_Go_failure_type_test==0])
std_react_time_No_Go_test_1_eter=np.std(react_time_No_Go_test_1[No_Go_failure_type_test==0])

mean_react_time_No_Go_test_1_omol=np.mean(react_time_No_Go_test_1[No_Go_failure_type_test==1])
std_react_time_No_Go_test_1_omol=np.std(react_time_No_Go_test_1[No_Go_failure_type_test==1])

mean_react_time_No_Go_correct_test_1=np.mean(react_time_No_Go_correct_test_1)
std_react_time_No_Go_correct_test_1=np.std(react_time_No_Go_correct_test_1)

mean_max_PMC_Go_test=np.mean(max_PMC_Go_test)
std_max_PMC_Go_test=np.std(max_PMC_Go_test)

mean_max_PMC_No_Go_total_test=np.mean(max_PMC_No_Go_total_test)
std_max_PMC_No_Go_total_test=np.std(max_PMC_No_Go_total_test)

mean_max_PMC_No_Go_test=np.mean(max_PMC_No_Go_test)
std_max_PMC_No_Go_test=np.std(max_PMC_No_Go_test)

mean_max_PMC_No_Go_test_eter=np.mean(max_PMC_No_Go_test[No_Go_failure_type_test==0])
std_max_PMC_No_Go_test_eter=np.std(max_PMC_No_Go_test[No_Go_failure_type_test==0])

mean_max_PMC_No_Go_test_omol=np.mean(max_PMC_No_Go_test[No_Go_failure_type_test==1])
std_max_PMC_No_Go_test_omol=np.std(max_PMC_No_Go_test[No_Go_failure_type_test==1])

mean_max_PMC_No_Go_correct_test=np.mean(max_PMC_No_Go_correct_test)
std_max_PMC_No_Go_correct_test=np.std(max_PMC_No_Go_correct_test)

mean_Pmax_Go_test=np.mean(Pmax_Go_test)
std_Pmax_Go_test=np.std(Pmax_Go_test)

mean_Pmax_No_Go_total_test=np.mean(Pmax_No_Go_total_test)
std_Pmax_No_Go_total_test=np.std(Pmax_No_Go_total_test)

mean_Pmax_No_Go_test=np.mean(Pmax_No_Go_test)
std_Pmax_No_Go_test=np.std(Pmax_No_Go_test)

mean_Pmax_No_Go_test_eter=np.mean(Pmax_No_Go_test[No_Go_failure_type_test==0])
std_Pmax_No_Go_test_eter=np.std(Pmax_No_Go_test[No_Go_failure_type_test==0])

mean_Pmax_No_Go_test_omol=np.mean(Pmax_No_Go_test[No_Go_failure_type_test==1])
std_Pmax_No_Go_test_omol=np.std(Pmax_No_Go_test[No_Go_failure_type_test==1])

mean_Pmax_No_Go_correct_test=np.mean(Pmax_No_Go_correct_test)
std_Pmax_No_Go_correct_test=np.std(Pmax_No_Go_correct_test)

right_inhibition_test=compute_right_inhibition(reward_vec_test,trial_type_test, time_crucial_trial_test)

accuracy_test=compute_global_accuracy(reward_vec_test,time_crucial_trial_test)

print('##############################################')
print(' Model output during training phase:')

print('mean reaction time Go Trials training 1 :', mean_react_time_Go_training_1)
print('std reaction time Go Trials training 1 :', std_react_time_Go_training_1)

print('mean reaction time NoGo total Trials training 1:',mean_react_time_No_Go_total_training_1 )
print('std reaction time NoGo total Trials training 1:',std_react_time_No_Go_total_training_1 )

print('mean reaction time NoGo Trials training 1 :',mean_react_time_No_Go_training_1 )
print('std reaction time NoGo Trials training 1 :',std_react_time_No_Go_training_1 )

print('mean reaction time NoGo Trials correct training 1 :',mean_react_time_No_Go_correct_training_1 )
print('std reaction time NoGo Trials correct training 1 :',std_react_time_No_Go_correct_training_1 )

print('mean max PMC Go training:',mean_max_PMC_Go_training)
print('std max PMC Go training:',std_max_PMC_Go_training)

print('mean max PMC NoGo total training:',mean_max_PMC_No_Go_total_training)
print('std max PMC NoGo total training:',std_max_PMC_No_Go_total_training)

print('mean max PMC NoGo training:',mean_max_PMC_No_Go_training)
print('std max PMC NoGo training:',std_max_PMC_No_Go_training)

print('mean max PMC NoGo correct training:',mean_max_PMC_No_Go_correct_training)
print('std max PMC NoGo correct training:',std_max_PMC_No_Go_correct_training)

print('mean Pmax Go training:',mean_Pmax_Go_training)
print('std Pmax Go training:',std_Pmax_Go_training)

print('mean Pmax NoGo total training:',mean_Pmax_No_Go_total_training)
print('std Pmax NoGo total training:',std_Pmax_No_Go_total_training)

print('mean Pmax NoGo training:',mean_Pmax_No_Go_training)
print('std Pmax NoGo training:',std_Pmax_No_Go_training)

print('mean Pmax NoGo correct training:',mean_Pmax_No_Go_correct_training)
print('std Pmax NoGo correct training:',std_Pmax_No_Go_correct_training)

print('% right inibiton trials before and after meta_value_hold thr training:',right_inhibition_training)

print('global accuracy before and after meta_value_hold thr training:',accuracy_training)
print('##############################################')

print('##############################################')
print(' Model output during test phase:')

print('mean reaction time Go Trials test 1 :', mean_react_time_Go_test_1)
print('std reaction time Go Trials test 1 :', std_react_time_Go_test_1)

print('mean reaction time NoGo total Trials test 1:',mean_react_time_No_Go_total_test_1 )
print('std reaction time NoGo total Trials test 1:',std_react_time_No_Go_total_test_1 )

print('mean reaction time NoGo Trials test 1 :',mean_react_time_No_Go_test_1 )
print('std reaction time NoGo Trials test 1 :',std_react_time_No_Go_test_1 )

print('mean reaction time NoGo Trials correct test: 1 ',mean_react_time_No_Go_correct_test_1 )
print('std reaction time NoGo Trials correct test 1 :',std_react_time_No_Go_correct_test_1 )

print('mean max PMC Go test:',mean_max_PMC_Go_test)
print('std max PMC Go test:',std_max_PMC_Go_test)

print('mean max PMC NoGo total test:',mean_max_PMC_No_Go_total_test)
print('std max PMC NoGo total test:',std_max_PMC_No_Go_total_test)

print('mean max PMC NoGo test:',mean_max_PMC_No_Go_test)
print('std max PMC NoGo test:',std_max_PMC_No_Go_test)

print('mean max PMC NoGo test correct :',mean_max_PMC_No_Go_correct_test)
print('std max PMC NoGo test correct :',std_max_PMC_No_Go_correct_test)

print('mean Pmax Go test:',mean_Pmax_Go_test)
print('std Pmax Go test:',std_Pmax_Go_test)

print('mean Pmax NoGo total test:',mean_Pmax_No_Go_total_test)
print('std Pmax NoGo total test:',std_Pmax_No_Go_total_test)

print('mean Pmax NoGo test:',mean_Pmax_No_Go_test)
print('std Pmax NoGo test:',std_Pmax_No_Go_test)

print('mean Pmax NoGo correct  test:',mean_Pmax_No_Go_correct_test)
print('std Pmax NoGo correct test:',std_Pmax_No_Go_correct_test)

print('% right inibiton trials before and after meta_value_hold thr test:',right_inhibition_test)

print('global accuracy before and after meta_value_hold thr test:',accuracy_test)
print('##############################################')

print('freq omol NoGo failure type training :', freq_1_No_Go_failure_type_training )
print('freq eter NoGo failure type training :',freq_0_No_Go_failure_type_training )

print('num omol NoGo failure type training:', num_1_No_Go_failure_type_training)
print('num eter NoGo failure type training:', num_0_No_Go_failure_type_training)

print('freq omol NoGo failure type test:',freq_1_No_Go_failure_type_test )
print('freq eter NoGo failure type test:',freq_0_No_Go_failure_type_test )

print('num omol NoGo failure type test:',num_1_No_Go_failure_type_test )
print('num eter NoGo failure type test', num_0_No_Go_failure_type_test)
print('##############################################')

print('mean react time NoGo training 1 eter:', mean_react_time_No_Go_training_1_eter)
print('std react time NoGo training 1 eter', std_react_time_No_Go_training_1_eter)

print('mean react time NoGo training 1 omol:', mean_react_time_No_Go_training_1_omol)
print('std react time NoGo training 1 omol', std_react_time_No_Go_training_1_omol)

print('mean max PMC NoGo training eter:',mean_max_PMC_No_Go_training_eter )
print('std max PMC NoGo training eter',std_max_PMC_No_Go_training_eter )

print('mean max PMC NoGo training omol:',mean_max_PMC_No_Go_training_omol )
print('std max PMC NoGo training omol',std_max_PMC_No_Go_training_omol )

print('mean Pmax NoGo training eter:',mean_Pmax_No_Go_training_eter)
print('std Pmax NoGo training eter:',std_Pmax_No_Go_training_eter)

print('mean Pmax NoGo training omol:',mean_Pmax_No_Go_training_omol)
print('std Pmax NoGo training omol:',std_Pmax_No_Go_training_omol)

print('mean react time NoGo test 1 eter:', mean_react_time_No_Go_test_1_eter )
print('std react time NoGo test 1 eter:', std_react_time_No_Go_test_1_eter)

print('mean react time NoGo test 1 omol:', mean_react_time_No_Go_test_1_omol )
print('std react time NoGo test 1 omol:', std_react_time_No_Go_test_1_omol)

print('mean max PMC NoGo test eter:',mean_max_PMC_No_Go_test_eter )
print('std max PMC NoGo test eter:', std_max_PMC_No_Go_test_eter)

print('mean max PMC NoGo test omol:',mean_max_PMC_No_Go_test_omol )
print('std max PMC NoGo test omol:', std_max_PMC_No_Go_test_omol)

print('mean Pmax NoGo test eter:',mean_Pmax_No_Go_test_eter )
print('std Pmax NoGo test eter:',std_Pmax_No_Go_test_eter )

print('mean Pmax NoGo test omol:',mean_Pmax_No_Go_test_omol )
print('std Pmax NoGo test omol:',std_Pmax_No_Go_test_omol)

print('##############################################')

num_problems_training=np.sum(time_crucial_trial_training1)
num_problems_test=np.sum(time_crucial_trial_test1)

#training
num_problems_training_Go=0
num_problems_training_No_Go=0
for i in range(num_problems_training):
    if trial_type_training[i]==1:
        num_problems_training_No_Go=num_problems_training_No_Go+1
    else:
        num_problems_training_Go=num_problems_training_Go+1
        
#test
num_problems_test_Go=0
num_problems_test_No_Go=0
for i in range(num_problems_test):
    if trial_type_test[i]==1:
        num_problems_test_No_Go=num_problems_test_No_Go+1
    else:
        num_problems_test_Go=num_problems_test_Go+1

num_trials_between_two_problems_training=(len(time_crucial_trial_training1)-4*num_problems_training)/num_problems_training
num_trials_between_two_problems_test=(len(time_crucial_trial_test1)-4*num_problems_test)/num_problems_test

print('num problems training:',num_problems_training)
print('num problems training Go:',num_problems_training_Go)
print('num problems training NoGo:',num_problems_training_No_Go)
print('num trials between two problems training:',num_trials_between_two_problems_training)

print('num problems test:',num_problems_test)
print('num problems test Go:',num_problems_test_Go)
print('num problems test NoGo:',num_problems_test_No_Go)
print('num trials between two problems test:',num_trials_between_two_problems_test)

print('###############################')

print('trials needed to learn hold meta-value:',time_tothr)
print('trials from learn hold meta-value and the end:',time_toend)
print(' meta-value hold at time_tothr: ',MetaValue_Hold[time_tothr])
print(' meta-value hold at time_to the end: ',MetaValue_Hold[time_toend])
print(' meta-value slope:', MetaValue_Hold[time_tothr]/time_tothr)

ACC_Q_hold_train=ACC_Q[1][0].memory[1:(count_inp_start+1)]
ACC_Q_hold_test=ACC_Q[1][0].memory[(count_inp_start+1):]

print('###############################')

print('Qvalue max train mean:',max(ACC_Q_hold_train))
print('Qvalue max train median:',np.median(ACC_Q_hold_train))

print('Qvalue max test mean: ',max(ACC_Q_hold_test))
print('Qvalue max test median: ',np.median(ACC_Q_hold_test))

print('###############################')

print('min TD:', min(TD_memory))
print('max TD:', max(TD_memory))

print('min S0:', min(Striatum_Neu0.s0_memory))
print('max S0:', max(Striatum_Neu0.s0_memory))









































