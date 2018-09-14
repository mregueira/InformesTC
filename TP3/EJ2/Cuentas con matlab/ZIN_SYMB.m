clear;
clc;
%s= tf('s');
syms s;
syms Rg;
syms Zg;
syms Cg;
syms BWP;
Vin = 1;
K = 1 / (1 +(s/BWP)); 
Vmas=Vin * ( Zg /(Zg+ (1/(s*Cg))));
Vmenos= K*(Vmas) ;
Iin = (Vmas / Zg) + (Vin - Vmenos)/Rg;
Zin = Vin/(Iin);
Zin = simplify(Zin)
