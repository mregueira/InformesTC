syms C3;
syms R5;
syms R6;
syms C4;
syms R7;
syms s;
 
ZB= R6+R5 + (1/(s*C3));
ZAUX= (1/(s*C4));
ZC = (R7*ZAUX)/(R7+ZAUX);
H= ZC/(ZB+ZC);
pretty(simplify(H))