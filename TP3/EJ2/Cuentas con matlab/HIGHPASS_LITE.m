clear;
clc;
s=tf('s');

R=620;
C=470e-9;
Rg = 100;
Cg = 680e-12;
Zg = 510e3;
BWP = 2*pi*3e6;

num = C*Rg*s*(Cg*Zg*s+1);
den =(C*Cg*Rg*(R+Zg))*s^2+(C*(R+Rg)+Cg*Rg)*s+1;

H=num/den;

bode(H,{1e2,1e6})


