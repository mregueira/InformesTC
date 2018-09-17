clc;
clear;
syms Vin;
syms s;
syms Zg;
syms Rg;
syms Cg;
syms BWP;

syms C;
syms R;

ZIN = (Cg*Rg*Zg*s^2 + (Rg + BWP*Cg*Rg*Zg)*s + BWP*Rg)/((Cg*Rg + Cg*Zg)*s^2 + (BWP*Cg*Rg + 1)*s + BWP);

Z = R + 1/(s*C); 

H= ZIN/(Z+ZIN);
H = getsfactor(H)

