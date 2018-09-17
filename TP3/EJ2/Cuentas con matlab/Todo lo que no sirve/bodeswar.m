clear;
clc;
%s=tf('s');
%Rg = 530;
%Zg = 10000;
%Cg = 1e-9;
%Vin = 1;
%BWP = (3e6) * 2 * pi ;
syms s;
syms Rg;
syms Zg;
syms Cg;
syms BWP;
Z2 = (Rg*(BWP + s)*(Cg*Zg*s + 1))/(BWP + s + Cg*Rg*s^2 + Cg*Zg*s^2 + BWP*Cg*Rg*s);
[N,D] = numden(Z2);
N=collect(N);
D=collect(D);




