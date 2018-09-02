clear all;
close all;
clc;
s=tf('s');
wc=2*pi*24000;

C2=1e-6;
R3=10000;
R4=220000;
R1=220000;
C1=100e-9;
R5=1000;
R6=1000;
R7=100000;
C3=100e-9;
C4=3.3e-9;

H1 =(s/(2/(R1*C1)))/((s/(2/(R1*C1)))+1);
H2= ((s/(1/(C2*(R3+R4))))+1) / ((s/(1/(C2*(R3))))+1);
H3num=s/(1/(R7*C3));
H3den=C3*C4*(R5+R6)*R7*s^2+(C3*(R5+R6+R7)+C4*R7)*s+1;
H3=H3num/H3den;

A0=100000;
BWP=4e6;
wp=BWP/2;

H2posta=(A0)/((1+s/wp)*(1+ (A0)/(  (1+(R4/(R3+(1/(s*C2))))) *(1+s/wp) )   ));

H=H1*H2posta*H3;

[num,den]=tfdata(H);
bode(H)
