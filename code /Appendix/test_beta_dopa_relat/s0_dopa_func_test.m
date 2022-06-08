% s0 deve andare da 0.2 a 1


% test eq: y = a0/(1+exp(-a1(x-a2)))
n_DA = 11;
DA = linspace(0,1,n_DA); % level of dopamina normalized between 0 and 1

%matrice delle combinazioni dei parametri, si hanno tre parametri quindi 3
%colonne e nelle righe si hanno tutte le combinazini, ogni volta si legge
%una riga
%3 parametri che vanno da 0 a 2
% a0 = 3:0.5:10;
% a1 = 1:0.5:15;
% a2 = 2:0.5:11;
type = 'mul_rev';
%ndgrud crea tutte le combinazioni possibili da questi 3 vettori
% [ca0, ca1, ca2] = ndgrid(a0', a1', a2');
% combs = [ca0(:), ca1(:), ca2(:)];
% %si calcola il numero delle combinazioni
% n_combs = size(combs,1);

%% 

fun = @solve_par_D2_to_s0;

x0 = [1;4;0.9];


[a_opt,fval] = fsolve(fun,x0);


%% plot optimum secondo il solver
type = 'mul_rev';
s0 = build_func(DA,a_opt,type);%secondo input è un vettore perche si hanno 3 parametri, quindi legge ogni riga della matrice di permutazione dei parameti

% check plot

figure('renderer','painters')
plot(DA,s0)
hold on
plot(DA, build_func(DA,a_opt + [-0.19;3.5;0],type))  % ricorda [0;3;0]
xlabel('DA [a.u.]')
ylabel('s0 [a.u.]')
axis([0 1 0 1])
set(gca,'fontsize',15)
%%
% salvare a0_opt = [a0,a1,a2] = [1.2, 3.22, 0.5]

%%


%ogni livello di dopamina si ha un vettore,perchè il risultato di prob_beta è un vettore 

%per ogni combinazione per ogni livello di dopamina si ha un valore di beta
%prendendo il valore attuale di dopamina e la combinazione attuale 

%3 parametri che vanno da 0 a 2
a0 = a;
a1 = 10;
a2 = 0.5;
type = 'mul_rev';
%ndgrud crea tutte le combinazioni possibili da questi 3 vettori
[ca0, ca1, ca2] = ndgrid(a0', a1', a2');
combs = [ca0(:), ca1(:), ca2(:)];
% %si calcola il numero delle combinazioni
n_combs = size(combs,1);
s0 = zeros(n_combs,n_DA);

figure('renderer','painters')
for comb_i = 1 : n_combs
    for DA_i = 1 : n_DA
        s0(comb_i, DA_i) = build_func(DA(DA_i),combs(comb_i,:),type);%secondo input è un vettore perche si hanno 3 parametri, quindi legge ogni riga della matrice di permutazione dei parameti
%plottare ogni riga della matrice H_probB
    end
    plot(DA,s0(comb_i,:))
    title(sprintf('parameters: a0 = %2f, a1 = %2f and a2 = %2f',combs(comb_i,1),combs(comb_i,2),combs(comb_i,3)))
    ylim([0 1])
    pause()
end
xlabel("dopamine")
ylabel("s0")

% aumento params(1) ---> aumenta pendenza e trasla a sinistra
% aumento params(2) ----> aumenta leggermente pendenza
% aumento params(3) -----> trasla a destra 
 
% A good combination for DA = [0,1] a.u. and H = [0,2] Bits is a0 = 10, a1 = 9.5 and a2 = 0.5 
% using a multiplicative model mul

% A good combination for DA = [0,1] a.u. and H = [0,2] Bits is a0 = 10, a1 = 11 and a2 = 4.5 
% using a multiplicative model mul2


%% check chosen models
figure('renderer','painters')
plot(DA,build_func(DA,[10,9.5,0.5],'mul'))
hold on
plot(DA,build_func(DA,[10,11,4.5],'mul2'))
legend({'mul','mul2'})
xlabel('DA [a.u.]')
ylabel('\beta [a.u.]')
set(gca,'fontsize',15)
