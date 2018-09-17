clear;
clc;
syms s;
syms R;
syms L;
syms C;

Z1 = s*L;
Z2 = 1/(s*C);
Z= (Z1*Z2)/(Z1+Z2);

H= Z/(Z+R);
[N,D]= numden(H);
N=collect(N,s);
D=collect(D,s);
N=N/R;
D=D/R;
H= N/D

w0 = 1/sqrt(L*C);
xi= (L/R)*w0/2;

xi= expand(xi);
xi= simplify(xi);
Q= 1 / (2*xi)

Q= R * (C)^(1/2) * (1/(L)^(1/2))