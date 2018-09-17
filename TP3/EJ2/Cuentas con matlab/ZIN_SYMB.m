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



