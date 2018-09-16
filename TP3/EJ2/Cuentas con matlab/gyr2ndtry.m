clear;
clc;
s= tf('s');
Rg = 10;
Zg = 200e3;
Cg = 10e-9;
Vin = 1;

BWP = 3e6 * 2 * pi ;
K = 1 / (1 +(s/BWP)); 
Vmas=Vin * ( Zg /(Zg+ (1/(s*Cg))));
Vmenos= K*(Vmas) ;

Iin = (Vmas / Zg) + (Vin - Vmenos)/Rg;

Zin = Vin/(Iin);

bode(Zin,{1e2,1e6})




