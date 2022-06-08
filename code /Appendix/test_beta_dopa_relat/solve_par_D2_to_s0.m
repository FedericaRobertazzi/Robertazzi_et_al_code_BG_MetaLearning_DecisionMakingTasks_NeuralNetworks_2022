function F = solve_par_D2_to_s0(x)
         F(1) = x(1)/(1 + exp(-x(2)*x(3))) - 1;
         F(2) = x(1)/(1 + exp(x(2)*(0.5 - x(3)))) - 0.6;
         F(3) = x(1)/(1 + exp(x(2)*(1 - x(3)))) - 0.2;        
end