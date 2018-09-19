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
ZPARALELO = (ZIN*ZC)/(ZIN+ZC);
H = ZPARALELO/(ZPARALELO + Z);
H = getsfactor(H)
