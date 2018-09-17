clear;
clc;

s= tf('s');
Rg = 100;
Zg = 10000;
Cg = 1e-9;
Vin = 1;
BWP = (3e6) * 2 * pi ;
K = 1 / (1 +(s/BWP)); 
Vmas=Vin * ( Zg /(Zg+ (1/(s*Cg))));
Vmenos= K*(Vmas) ;
Iin = (Vmas / Zg) + (Vin - Vmenos)/Rg;
Zin = Vin/(Iin);
bode(Zin)
%hold on;
%IdealZin= Rg*(Cg* Zg * s + 1);
%bode(IdealZin,{1e3,1e7})
L = Rg*Zg*Cg;
w0 = sqrt(BWP/(Cg*(Rg+Zg)));
xi = Rg*Cg*w0/2;