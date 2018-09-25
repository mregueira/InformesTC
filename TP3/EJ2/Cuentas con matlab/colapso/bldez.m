clear;
clc;
R = 12000;
C = 2.2e-9;
Rg = 47;
Cg = 10e-9;
Zg = 200e3;
BWP = 3e6*2*pi;
L= 0.094

syms s;

denom=(((C*L)* s^2 + C*R*s+1));
Rexplicit = solve(denom,s,'MaxDegree',2)