clc;
clear;
syms Vin;
syms s;
syms R;
syms C;
syms Zg;
syms Rg;
syms Cg;
syms BWP;

Z = R;
ZC = 1/(s*C);
ZIN = (Cg*Rg*Zg*s^2 + (Rg + BWP*Cg*Rg*Zg)*s + BWP*Rg)/((Cg*Rg + Cg*Zg)*s^2 + (BWP*Cg*Rg + 1)*s + BWP);

ZSERIE = ZIN  + R;

%H=ZC/(ZC+ZSERIE);

H=(BWP*C*Cg*Rg*s + BWP + C*Cg*Rg*s^2)/(C*Rg*s*(BWP*Cg*Zg*s + BWP + Cg*Zg*s^2 + s) + (C*R*s + 1)*(BWP*C*Cg*Rg*s + BWP + C*Cg*Rg*s^2 + Cg*Zg*s^2 + s))


H = getsfactor(H)
