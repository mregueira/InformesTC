% Filtro final - Orden 10 Legendre - Intento 2 %
% Mas reestrictivo: Ap = 0.5dB y As = 50dB
% Resulta orden n = 12
clc;

Wo1 = 2*pi*12746; 
Q1 = 11.84; 
Wo2 = 2*pi*13642; 
Q2 = 3.73; 
Wo3 = 2*pi*15625;
Q3 = 2; 
Wo4 = 2*pi*19298; 
Q4 = 1.21;
Wo5 = 2*pi*25787; 
Q5 = 0.77;
Wo6 = 2*pi*34169; 
Q6 = 0.53;

% Circuito 1

C_1 = 1e-9;
R2_1 = 3*(Q1)/(Wo1*C_1);
R1_1 = 1/(((Wo1)^2) * R2_1 * (C_1)^2);
f_1 = Wo1 / (2*pi);

% Circuito 2

C_2 = 1.5e-9;
R2_2 = 3*(Q2)/(Wo2*C_2);
R1_2 = 1/(((Wo2)^2) * R2_2 * (C_2)^2);
f_2 = Wo2 / (2*pi);

% Circuito 3

C_3 = 5.6e-9;
R_3 = 1/(Wo3*C_3);
R_A3 = 1e3;
R_B3 = (2-(1/Q3))*R_A3;
f_3 = Wo3/(2*pi);

% Circuito 4

C_4 = 3.3e-9;
R_4 = 1/(Wo4*C_4);
R_A4 = 1.2e3;
R_B4 = (2-(1/Q4))*R_A4;
f_4 = Wo4/(2*pi);

% Circuito 5

C_5 = 3.3e-9;
R_5 = 1/(Wo5*C_5);
R_A5 = 10e3;
R_B5 = (2-(1/Q5))*R_A5;
f_5 = Wo5/(2*pi);

% Circuito 6

C_6 = 2.2e-9;
R_6 = 1/(Wo6*C_6);
R_A6 = 10e3;
R_B6 = (2-(1/Q6))*R_A6;
f_6 = Wo6/(2*pi);