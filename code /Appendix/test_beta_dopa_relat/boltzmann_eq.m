function prob = boltzmann_eq(Q,beta)
prob = exp(beta*Q)/(sum(exp(Q.*beta)));
end

