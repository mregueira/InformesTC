clear;
clc;
s=tf('s');

R=620;
C=470e-9;
Rg = 100;
Cg = 680e-12;
Zg = 510e3;
BWP = 2*pi*3e6;

H= (C*Rg*s*(BWP + s)*(Cg*Zg*s + 1))/(C*Cg*(R*Rg + R*Zg + Rg*Zg)*s^3 + (C*R + C*Rg + Cg*Rg + Cg*Zg + BWP*C*Cg*R*Rg + BWP*C*Cg*Rg*Zg)*s^2 + (BWP*C*R + BWP*C*Rg + BWP*Cg*Rg + 1)*s + BWP);

bode(H,{1e2,1e6})


