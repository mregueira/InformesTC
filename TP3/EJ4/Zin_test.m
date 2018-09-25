clc;
% General
%-----------------
R1 = sym('R1');
R2 = sym('R2');
k = sym('k');
R3 = sym('R3');
C1L = sym('C1L');
C1M = sym('C1M');
C1H = sym('C1H');
C2L = sym('C2L');
C2M = sym('C2M');
C2H = sym('C2H');
s = sym('s');
%-----------------
% Low Filter
ZA = (s*C2L*R2*k*(1-k)+1)/(s*C2L*(1-k));
ZB = s*C2L*((R2)^2)*k*(1-k)+R2;
ZC = (s*C2L*R2*k*(1-k)+1)/(s*C2L*k);

ZBB = (ZB/(s*C1L))/(ZB+(1/(s*C1L)));

q = ZA + ZBB + ZC;

Z1 = (ZA*ZBB)/q;
Z2 = (ZA*ZC)/q;
Z3 = (ZBB*ZC)/q;

Z11 = Z1 + R1;
Z33 = Z3 + R1;

Beta = Z11*Z2 + Z2*Z33 + Z33*Z11;

Za = Beta/Z33;
Zb = Beta/Z11;
ZcLow = Beta/Z2;
ZcLow = simplify(ZcLow);

ZrLow = (Za*R3)/(Za+R3);
ZrLow = simplify(ZrLow);
Zf = (Zb*R3)/(Zb+R3);

HLow = -Zf/ZrLow;
HLow = simplify(HLow);

% Med Filter
ZA = (s*C2M*R2*k*(1-k)+1)/(s*C2M*(1-k));
ZB = s*C2M*((R2)^2)*k*(1-k)+R2;
ZC = (s*C2M*R2*k*(1-k)+1)/(s*C2M*k);

ZBB = (ZB/(s*C1M))/(ZB+(1/(s*C1M)));

q = ZA + ZBB + ZC;

Z1 = (ZA*ZBB)/q;
Z2 = (ZA*ZC)/q;
Z3 = (ZBB*ZC)/q;

Z11 = Z1 + R1;
Z33 = Z3 + R1;

Beta = Z11*Z2 + Z2*Z33 + Z33*Z11;

Za = Beta/Z33;
Zb = Beta/Z11;
ZcMed = Beta/Z2;
ZcMed = simplify(ZcMed);

ZrMed = (Za*R3)/(Za+R3);
ZrMed = simplify(ZrMed);
Zf = (Zb*R3)/(Zb+R3);

HMed = -Zf/ZrMed;
HMed = simplify(HMed);

% High Filter
ZA = (s*C2H*R2*k*(1-k)+1)/(s*C2H*(1-k));
ZB = s*C2H*((R2)^2)*k*(1-k)+R2;
ZC = (s*C2H*R2*k*(1-k)+1)/(s*C2H*k);

ZBB = (ZB/(s*C1H))/(ZB+(1/(s*C1H)));

q = ZA + ZBB + ZC;

Z1 = (ZA*ZBB)/q;
Z2 = (ZA*ZC)/q;
Z3 = (ZBB*ZC)/q;

Z11 = Z1 + R1;
Z33 = Z3 + R1;

Beta = Z11*Z2 + Z2*Z33 + Z33*Z11;

Za = Beta/Z33;
Zb = Beta/Z11;
ZcHigh = Beta/Z2;
ZcHigh = simplify(ZcHigh);

ZrHigh = (Za*R3)/(Za+R3);
ZrHigh = simplify(ZrHigh);
Zf = (Zb*R3)/(Zb+R3);

HHigh = -Zf/ZrHigh;
HHigh = simplify(HHigh);

R1 = 560;
R2 = 10000;
R3 = 100000;
k = 0; %Aca depende porque hay que hacer 3 casos:
% 0 , 0.5 , 1
w = (2*pi*20):40:(2*pi*20000);
s = w*1i;
C1L = 1000e-9;
C1M = 100e-9;
C1H = 10e-9;
C2L = 100e-9;
C2M = 10e-9;
C2H = 1e-9;


Zin = 1/((1/ZrLow)+(1/ZrMed)+(1/ZrHigh)+((1-HLow)/ZcLow)+((1-HMed)/ZcMed)+((1-HHigh)/ZcHigh));
Zin = simplify(Zin);


Zin = subs(Zin);
%Zin

semilogx(w,abs(Zin));
