clear;
clc;
syms s;
syms Cg;
syms C;
syms Rg;
syms R;
syms Zg;
syms BWP;


DEN=(  ((C*Cg*R*Zg)/BWP)*s^3+ (C*Rg)*Cg*Zg*s^2+C*R*s+1 )

r = root(DEN,s)

Rexplicit = solve(DEN,s,'MaxDegree',3)

simplify((s-Rexplicit(2))*(s-Rexplicit(3)))