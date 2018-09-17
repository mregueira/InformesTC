clear;
clc;
R=10000;
C=33e-9;

s= tf('s');
Rg = 530;
Zg = 10000;
Cg = 1e-9;
Vin = 1;
BWP = 3e6 * 2 * pi ;
K = 1 / (1 +(s/BWP)); 
Vmas=Vin * ( Zg /(Zg+ (1/(s*Cg))));
Vmenos= K*(Vmas) ;
Iin = (Vmas / Zg) + (Vin - Vmenos)/Rg;
Zin = Vin/(Iin);

H= Zin / (Zin + R + 1/(s*C));

bode(H)


L = Rg*Zg*Cg;
w0 = sqrt(BWP/(Cg*(Rg+Zg)));
xi = Rg*Cg*w0/2;

