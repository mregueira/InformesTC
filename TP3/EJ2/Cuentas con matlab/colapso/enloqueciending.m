clear;
clc;


R = 12000
C = 2.2e-9
Rg = 47
Cg = 10e-9
Zg = 200e3
BWP = 3e6*2*pi
L=Rg*Cg*Zg

s=tf('s')

H=1/(C*L*s^2+C*R*s+1)
bode(H)

s=sqrt(1/(L*C))
H=1/(C*R*s)

nasde= 20*log10(H)
