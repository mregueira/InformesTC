clc;
R1 = 560;
R2 = 10000;
R3 = 100000;
k = 1; %Aca depende porque hay que hacer 3 casos:
% 0 , 0.5 , 1
s = tf('s');
C1 = 1000e-9;
C2 = 100e-9;

a1 = C1*C2*R1*R2*(R1 + 2*R2*k -2*R2*(k^2) + R3);
a2 = (C2*(((R1)^2) + ((R2)^2)*k - ((R2)^2)*(k^2) + R1*R2 + R1*R3 + R2*R3 - R2*R3*k)) + (2*C1*R1*R2);
a3 = 2*R1 + R2;
b1 = C1*C2*R1*R2*(R1 + 2*R2*k -2*R2*(k^2) + R3);
b2 = (C2*(((R1)^2) + ((R2)^2)*k - ((R2)^2)*(k^2) + R1*R2 + R1*R3 + R2*R3*k)) + (2*C1*R1*R2);
b3 = 2*R1 + R2; 

HBajos = -((a1)*(s^2) + (a2)*s + a3)/((b1)*(s^2) + (b2)*s + b3);

C1 = 100e-9;
C2 = 10e-9;

a1 = C1*C2*R1*R2*(R1 + 2*R2*k -2*R2*(k^2) + R3);
a2 = (C2*(((R1)^2) + ((R2)^2)*k - ((R2)^2)*(k^2) + R1*R2 + R1*R3 + R2*R3 - R2*R3*k)) + (2*C1*R1*R2);
a3 = 2*R1 + R2;
b1 = C1*C2*R1*R2*(R1 + 2*R2*k -2*R2*(k^2) + R3);
b2 = (C2*(((R1)^2) + ((R2)^2)*k - ((R2)^2)*(k^2) + R1*R2 + R1*R3 + R2*R3*k)) + (2*C1*R1*R2);
b3 = 2*R1 + R2; 

HMedios = -((a1)*(s^2) + (a2)*s + a3)/((b1)*(s^2) + (b2)*s + b3);

C1 = 10e-9;
C2 = 1e-9;

a1 = C1*C2*R1*R2*(R1 + 2*R2*k -2*R2*(k^2) + R3);
a2 = (C2*(((R1)^2) + ((R2)^2)*k - ((R2)^2)*(k^2) + R1*R2 + R1*R3 + R2*R3 - R2*R3*k)) + (2*C1*R1*R2);
a3 = 2*R1 + R2;
b1 = C1*C2*R1*R2*(R1 + 2*R2*k -2*R2*(k^2) + R3);
b2 = (C2*(((R1)^2) + ((R2)^2)*k - ((R2)^2)*(k^2) + R1*R2 + R1*R3 + R2*R3*k)) + (2*C1*R1*R2);
b3 = 2*R1 + R2; 

HAltos = -((a1)*(s^2) + (a2)*s + a3)/((b1)*(s^2) + (b2)*s + b3);

HFinal = -(5/9)*(HBajos + HMedios + HAltos);

bode(HFinal)
% H es la de cada filtro, NO la que se usa
% R1 = 560
% R2 = 10K
% R3 = 100K
% BAJOS
% C1 = 1000n
% C2 = 100n
% MEDIOS
% C1 = 100n
% C2 = 10n
% ALTOS
% C1 = 10n
% C2 = 1n
% La transferencia final a la que se le hace el bode es:
% HFinal = -(5/9)*(HBajos + HMedios + HAltos)
% Haciendo una H para cada filtro con los valores indicados