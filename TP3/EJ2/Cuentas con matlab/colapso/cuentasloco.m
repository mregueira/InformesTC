clear; 
clc;
C= 2.2e-9;
f = 10e3;
w = 2 * pi * f;
L= 1/(C*(w^2))
Cg = 10*C;
R = 12000;
Zg = R * 10; %esto podria bajarlo a 10
Rg = L / (Cg*Zg);

BWP = 2*pi*3e6;

FactorScubo = (((BWP/(C*Cg*R*Zg))^(1/3))/(2*pi))*0.1

xi = C*R*w/2

s=tf('s')

H=1 /(  ((C*Cg*R*Zg)/BWP)*s^3+ ((1/BWP)+C*Rg)*Cg*Zg*s^2+C*R*s+1 )

r = root(1/H,s)


