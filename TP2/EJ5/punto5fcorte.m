clear all;
close all;
clc;
clear;
C3=100e-9;
C4=820e-12;
R5=10000;
R6=680;
R7=10:10:500;

polo=1./(2*pi*(C3*C4*(R5+R6).*R7).^(0.5));
cero=1./(2*pi*C3.*R7);
semilogx(R7,polo)
hold on;
semilogx(R7,cero);