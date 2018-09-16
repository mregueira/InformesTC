clear;
clc;
s= tf('s');
Rg = 100;
Zg = 10000;
Cg = 3.3e-9;
Vin = 1;
BWP = 3e6 * 2 * pi ;
K = 1 / (1 +(s/BWP)); 
Vmas=Vin * ( Zg /(Zg+ (1/(s*Cg))));
Vmenos= K*(Vmas) ;
Iin = (Vmas / Zg) + (Vin - Vmenos)/Rg;
Zin = Vin/(Iin);
bode(Zin,{1e3,1e7})