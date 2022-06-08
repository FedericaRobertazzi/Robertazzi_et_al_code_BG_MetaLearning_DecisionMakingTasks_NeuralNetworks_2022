% sero_to_dopa test

clc
clear all
close all

n_Sero = 11;
Sero = linspace(0,1,n_Sero); % level of serotonine normalized between 0 and 1

k_VTA_D1 = [1/log(2); 1];
k_VTA_D2 = [1/log(2); 1];

D1 = log_func(Sero,k_VTA_D1);
D2 = log_func(Sero,k_VTA_D2);

% prova migliori parametri k_VTA_D1 = [1.44; 1] e k_VTA_D2 = [1.44; 1];
% check test

figure('renderer','painters')
plot(Sero,D1)
hold on
plot(Sero, D2)  % ricorda [0;3;0]
xlabel('Sero [a.u.]')
ylabel('Dopa [a.u.]')
axis([0 1 0 1])
set(gca,'fontsize',15)