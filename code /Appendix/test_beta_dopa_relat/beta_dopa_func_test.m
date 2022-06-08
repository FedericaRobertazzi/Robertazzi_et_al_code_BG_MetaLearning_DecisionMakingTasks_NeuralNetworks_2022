n_actions = 4; %actions 
actions = 1:n_actions;
% test eq: y = a0/(1+exp(-a1(x-a2)))
n_DA = 11;
DA = linspace(0,1,n_DA); % level of dopamina normalized between 0 and 1

Q = [0.2 0.8 0.2 0.2]; % q-values of actions, in una situazione dove si ha una azione che è privilegiata,
%non sono i valori iniziali, si mettono dei q-value dove si ha una azione
%favorita,quando si è in exploitation, si deve avere un picco, quindi un
%q-value deve essere alto, non basta il beta per avere un picco nella
%probabilità,
%in questo caso l'azione 2 è favorita, quando è deterministico
%tenderà a fare l'azione 2.

%matrice delle combinazioni dei parametri, si hanno tre parametri quindi 3
%colonne e nelle righe si hanno tutte le combinazini, ogni volta si legge
%una riga
%3 parametri che vanno da 0 a 2
a0 = 3:0.5:10;
a1 = 1:0.5:15;
a2 = 2:0.5:11;
type = 'add';
%ndgrud crea tutte le combinazioni possibili da questi 3 vettori
[ca0, ca1, ca2] = ndgrid(a0', a1', a2');
combs = [ca0(:), ca1(:), ca2(:)];
%si calcola il numero delle combinazioni
n_combs = size(combs,1);
H_probB = zeros(n_combs,n_DA);%entropy init, per ogni combinazione e per ogni livello di dopamina si ha un valore di entropia
probB = zeros(n_combs,n_DA,n_actions);%probability distribution of actions init, è una matrice 3D, per ogni combinazione, per 
%ogni livello di dopamina si ha un vettore,perchè il risultato di prob_beta è un vettore 

%per ogni combinazione per ogni livello di dopamina si ha un valore di beta
%prendendo il valore attuale di dopamina e la combinazione attuale 
figure('renderer','painters')
for comb_i = 1 : n_combs
    for DA_i = 1 : n_DA
        beta = build_func(DA(DA_i),combs(comb_i,:),type);%secondo input è un vettore perche si hanno 3 parametri, quindi legge ogni riga della matrice di permutazione dei parameti
        prob_beta = boltzmann_eq(Q,beta);%prende il Q value definito a priori ed il beta corrente 
        % calcolare entropia di prob_beta
        H=myentropy(prob_beta);
        probB(comb_i,DA_i,:)=prob_beta;
        H_probB(comb_i,DA_i)=H;
%plottare ogni riga della matrice H_probB

    end
    plot(DA,H_probB(comb_i,:))
    title(sprintf('parameters: a0 = %2f, a1 = %2f and a2 = %2f',combs(comb_i,1),combs(comb_i,2),combs(comb_i,3)))
    ylim([0 2])
    
end
xlabel("dopamine")
ylabel("entropy")

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
