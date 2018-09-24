
clc;
clear;
R = 1000;
C = 5.6e-9;
Rg = 100;
Cg = 470e-12;
Zg = 510e3;
BWP = 3e6 * 2 * pi;
s = tf('s');
H =(Cg*Rg*Zg*s^2 + (Rg + BWP*Cg*Rg*Zg)*s + BWP*Rg)/(C*Cg*R*Rg*Zg*s^3 + (C*R*Rg + Cg*R*Rg + Cg*R*Zg + Cg*Rg*Zg + BWP*C*Cg*R*Rg*Zg)*s^2 + (R + Rg + BWP*C*R*Rg + BWP*Cg*R*Rg + BWP*Cg*Rg*Zg)*s + BWP*R + BWP*Rg);
L = Rg * Cg * Zg;
%Haux = ((1/R)*sqrt(L/C))*(((L*C)^(0.5))*s)/( ( (Rg*C*R+L)/R)*s+R );
%Haux = ((Cg*Rg*Zg)*s)/ (C*Cg*R*Rg*Zg*s^2+((C*R*Rg+Cg*Rg*Zg))*s+R+Rg) ;
Haux =sqrt(L/C)*(1/R)* sqrt(L*C)*s / ( C*L*s^2+((Rg*C*R+L)/R)*s+1 );

bode(H)
hold on;
bode(Haux)

