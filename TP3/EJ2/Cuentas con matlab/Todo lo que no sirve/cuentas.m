clear;
clc;
close all;
clear all;
s=tf('s');
RL= 50;
L= 20e-3;
ffalla=1e6;
C= (1/(RL*ffalla))*0.1;
R=L/(C*RL);
Bobina = RL + s*L;
% $*RL*C << 1 
% despejando psi con psi>0.707 queda que R 
psi = 0.8;
Rext= 2* (psi) * (L/C)^0.5;

HP= (s*L)/(Rext+RL+ s*L + 1/(s*C));
bode(HP,{10e4,10e6})