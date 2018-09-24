clear;
clc;
syms s;
C=2.2e-9;
Cg = 10e-9;
Rg = 47;
Zg = 200e3;
R = 12e3;
BWP = 2*pi*3e6;


DEN=(  ((C*Cg*R*Zg)/BWP)*s^3+ ((1/BWP)+C*Rg)*Cg*Zg*s^2+C*R*s+1 )

r = root(DEN,s)
Rexplicit = solve(DEN,s,'MaxDegree',3)