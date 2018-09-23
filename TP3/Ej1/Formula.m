R1 = sym('R1');
R3 = sym('R3');
R4 = sym('R4');
R5 = sym('R5');
R6 = sym('R6');
R7 = sym('R7');
R8 = sym('R8');
C2 = sym('C2');
C6 = sym('C6');
s = sym('s');
k = (1/R4)+(1/R5)+(1/R8);
q = (1/R7)+(s*C6)+(1/R6)-(1/(s*C2*R1*R3));
H = ((1/R7)+(s*C6)-(q/(k*R8)))/((q/(k*R4))+(1/(s*C2*R1*R3)));
clc;
Zin = (1/((1-((1/k)*((1/R8) + (H/R4))))*((1/R7) + (1/R8) + (s*C6))));
F = simplify(Zin);
pretty(F)
latex(F)