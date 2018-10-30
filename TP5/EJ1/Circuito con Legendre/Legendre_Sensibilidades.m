% Sallen-Key Legendre %
clc;
R1 = sym('R1');
R2 = sym('R2');
C = sym('C');
K = sym('K');
RA = sym('RA');
RB = sym('RB');
wo = sym('wo');

H = (K/(R1*R2*(C^2))) / ((1i*wo)^2 + 1i*wo*(((1/R1)+((2-K)/R2))/(C)) + (1/(R1*R2*(C^2))));
Habs = (K/(R1*R2*(C^2))) / sqrt((wo*(((1/R1)+((2-K)/R2))/(C)))^2 + ((1/(R1*R2*(C^2))) - wo^2)^2);

wof = sqrt(1/(R1*R2*(C^2)));
Q = sqrt(1/(R1*R2)) / ((1/R1) + ((1-(RB/RA))/R2));

dwof_R1 = diff(wof,R1);
dwof_R2 = diff(wof,R2);
dwof_C = diff(wof,C);

Swof_R1 = dwof_R1 * R1 / wof;
Swof_R2 = dwof_R2 * R2 / wof;
Swof_C = dwof_C * C / wof;
