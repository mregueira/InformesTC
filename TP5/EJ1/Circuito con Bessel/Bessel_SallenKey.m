% PB de orden 5 - Aproximado con Bessel%
clc;
s = tf('s');

% T1 = 1/(SLP^2 + 5.79242*SLP + 9.14013);
% T2 = 1/(SLP^2 + 4.20758*SLP + 11.4878);
% T3 = 1/(SLP + 3.64674);

% De la T1
wo1 = sqrt(3.772e11/0.001472);
Q1 = wo1*1472/4.514e7;
K1 = 3-(1/Q1);

% C1 = C2 = C
C_T1 = 1e-9
% R1 = R2 = R
R_T1 = 1/(wo1*C_T1)
RA_T1 = 2.2e3
RB_T1 = RA_T1*(2-(1/Q1))


% De la T2
wo2 = sqrt(4.741e11/0.001472);
Q2 = wo2*1472/3.279e7;
K2 = 3-(1/Q2);

% C1 = C2 = C
C_T2 = 1e-9
% R1 = R2 = R
R_T2 = 1/(wo2*C_T2)
RA_T2 = 2.2e3
RB_T2 = RA_T2*(2-(1/Q2))

% De la T3
wo3 = 1.26e4/0.0006526;
C_T3 = 1e-9
R_T3 = 1/(wo3*C_T3)