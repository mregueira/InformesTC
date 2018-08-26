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
