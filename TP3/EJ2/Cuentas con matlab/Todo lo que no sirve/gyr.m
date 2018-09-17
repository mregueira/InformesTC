clear;
clc;
s = tf('s');
Rg = 10;
Zg = 200e3;
Cg = 10e-9; 
% BWP=3e6*2*pi;
% K= 1/ (1+s*(1/BWP));
% ZINNUM = Rg*((1/(s*Cg)) +Zg);
% ZINDEN = Rg + (1/(s*Cg)) + Zg - K*Zg;
% 
% ZIN = ZINNUM/ZINDEN;

Vin = 1;
BWP = 3e6*2*pi;
K = 1 / (1 +(s/BWP)); 
Vmas=Vin * ( Zg /(Zg+ (1/(s*Cg))));
Vmenos= K*(Vmas) ;

Iin = (Vmas / Zg) + (Vin - Vmenos)/Rg;

ZIN = Vin/(Iin);

%bode(Zin,{1e2,1e6})
R1= 1200;
C2= 100e-9;
ZC2 = 1/ (s * C2);
H =  ZIN /( ZIN + ZC2 + R1);
[mag, phase,w ]= bode(H);
%[mag, phase,w ]= bode(ZIN);
mag= squeeze(mag);
phase= squeeze(phase);
w= squeeze(w);
f= w./(2*pi);
mag = 20*log10(mag);
figure(1);
semilogx(f,mag);
hold on;
title('Bode');
xlim([100 1e7]);
