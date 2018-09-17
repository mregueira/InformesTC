clear;
close all;
clc;
s=tf('s');

R=680;
C=470e-9;
Rg = 100;
Cg = 6.8e-9;
Zg = 51e3;
BWP = 2*pi*3e6;

num = C*Rg*s*(Cg*Zg*s+1);
den =(C*Cg*Rg*(R+Zg))*s^2+(C*(R+Rg)+Cg*Rg)*s+1;

H=num/den;

[mag, phase,w ]= bode(H);
mag= squeeze(mag);
phase= squeeze(phase);
w= squeeze(w);
f= w./(2*pi);
mag = 20*log10(mag);
figure(1);
semilogx(f,mag);
hold on;
title('Bode');
xlim([500 1e5]);

