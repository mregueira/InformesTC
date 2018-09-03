clear all;
close all;
clc;
syms C3;
syms R5;
syms R6;
syms C4;
syms R7;
syms s;
 
ZB = ((R5+R6)*s*C3 + 1)/(s*C3);
ZC =  R7/(s*C4*R7+1);

ZD=ZC/(ZB+ZC);

polinomio= C3 * C4 * (R5+R6)* s^2 +( (C3*(R5+R6+R7))/(R7)+C4)*s +1 ;
a=C3 * C4 * (R5+R6);
b=( (C3*(R5+R6+R7))/(R7)+C4);
S1=(-b+(b^2-4*a)^(0.5))/(2*a);

S2=(-b-(b^2-4*a)^(0.5))/(2*a);


