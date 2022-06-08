function beta = build_func(DA,params,type)
%UNTITLED5 Summary of this function goes here
%   Detailed explanation goes here
switch type
    case 'mul'
        beta = params(1)./(1+exp(-params(2)*(DA-params(3))));
    case 'mul_rev'
        beta = params(1)./(1+exp(params(2)*(DA-params(3))));        
    case 'add'
        beta = params(1) + 1/(1+exp(-params(2)*(DA-params(3))));
    case 'mul2'
        beta = params(1)./(1+exp(params(2)*(1-DA)-params(3)));
end
end

