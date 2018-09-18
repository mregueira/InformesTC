clc;
clear;
syms Vin;
syms s;
syms Zg;
syms Rg;
syms Cg;
syms BWP;
%Ecuaciones
K = 1 / (1 +(s/BWP)); 
Vmas=Vin * ( Zg /(Zg+ (1/(s*Cg))));
Vmenos= K*(Vmas) ;
Iin = (Vmas / Zg) + (Vin - Vmenos)/Rg;
Zin = Vin/(Iin);
%obtengo expresion
Zin = getsfactor(Zin)
%(Cg*Rg*Zg*s^2 + (Rg + BWP*Cg*Rg*Zg)*s + BWP*Rg)/((Cg*Rg + Cg*Zg)*s^2 + (BWP*Cg*Rg + 1)*s + BWP)


