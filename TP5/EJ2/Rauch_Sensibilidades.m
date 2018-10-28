% Rauch - Sensibilidades%
clc;
R1 = sym('R1');
R2 = sym('R2');
C = sym('C');

wo = (2/(R2*C))*sqrt(R2/(4*R1));
dwo_R1 = diff(wo,R1);
dwo_R2 = diff(wo,R2);
dwo_C = diff(wo,C);
Swo_R1 = dwo_R1 * R1 / wo;
Swo_R2 = dwo_R2 * R2 / wo;
Swo_C = dwo_C * C / wo;

% Celda 1 %
R1 = 2280;
R2 = 20500;
C = 680e-12;

eval(Swo_R1)
eval(Swo_R2)
eval(Swo_C)

% Celda 2 %
% R1 = 1390;
% R2 = 12600;
% C = 1e-9;
% 
% eval(Swo_R1)
% eval(Swo_R2)
% eval(Swo_C)
K = sym('K');

Q = 1.5/(1-(2*1.5*1.5*K/(1-K)));
dQ_K = diff(Q,K);
SQ_K = dQ_K * K / Q;

K = 0.155;
eval(SQ_K)