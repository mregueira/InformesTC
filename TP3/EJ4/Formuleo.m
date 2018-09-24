R1 = sym('R1');
R2 = sym('R2');
k = sym('k');
R3 = sym('R3');
C1 = sym('C1');
C2 = sym('C2');
s = sym('s');

ZA = (s*C2*R2*k*(1-k)+1)/(s*C2*(1-k));
ZB = s*C2*((R2)^2)*k*(1-k)+R2;
ZC = (s*C2*R2*k*(1-k)+1)/(s*C2*k);

ZBB = (ZB/(s*C1))/(ZB+(1/(s*C1)));

q = ZA + ZBB + ZC;

Z1 = (ZA*ZBB)/q;
Z2 = (ZA*ZC)/q;
Z3 = (ZBB*ZC)/q;

Z11 = Z1 + R1;
Z33 = Z3 + R1;

Beta = Z11*Z2 + Z2*Z33 + Z33*Z11;

Za = Beta/Z33;
Zb = Beta/Z11;
Zc = Beta/Z2;

Zr = (Za*R3)/(Za+R3);
Zf = (Zb*R3)/(Zb+R3);

H = -Zf/Zr;
F = simplify(H);
latex(F)
%Ahora con condiciones  
% ZA = (s*C2*R2*k*(1-k)+1)/(s*C2*(1-k));
% ZB = s*C2*((R2)^2)*k*(1-k)+R2;
% ZC = (s*C2*R2*k*(1-k)+1)/(s*C2*k);
% 
% ZBB = (ZB/(s*10*C2))/(ZB+(1/(s*10*C2)));
% 
% q = ZA + ZBB + ZC;
% 
% Z1 = (ZA*ZBB)/q;
% Z2 = (ZA*ZC)/q;
% Z3 = (ZBB*ZC)/q;
% 
% Z11 = Z1 + R1;
% Z33 = Z3 + R1;
% 
% Beta = Z11*Z2 + Z2*Z33 + Z33*Z11;
% 
% Za = Beta/Z33;
% Zb = Beta/Z11;
% Zc = Beta/Z2;
% 
% Zr = (Za*10*R2)/(Za+(10*R2));
% Zf = (Zb*10*R2)/(Zb+(10*R2));
% 
% H = -Zf/Zr;
% G = simplify(H);
% latex(G)