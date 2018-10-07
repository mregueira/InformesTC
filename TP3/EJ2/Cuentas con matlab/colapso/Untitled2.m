clear;
clc;
syms s;
syms dosrep;
syms modp2;
syms p
syms wo;
syms Q

% exp = s^2 - dosrep *s + modp2;
exp = s^2 -2* real(p) *s + abs(p)^2;
% exp = subs(exp,s,Q*(s/wo + wo/s));
exp = subs(exp,s,(Q*s^2+wo^2*Q)/(s*wo));
[N,D] = numden(exp);
D = D/Q^2;
N = N/Q^2;
collect(N,s)

