clc;
clear;
syms s;
syms R;
syms C;
z1= 4*R+8*R^2*C*s;
z2=2*R+ 1/(s*C);
z3=z2;
z1p=2/(s*C) + 1/(s^2 * C^2 * R);
z2p=z2;
z3p=z2p;
z1par=(z1*z1p)/(z1+z1p);
z3par=simplify((z3*z3p)/(z3+z3p));
H= simplify(z3par/(z3par+z1par));
%u=ilaplace(H);
%plot(u)
[y,t]=impulse(H);
% matlab me hace las cuentas :)

