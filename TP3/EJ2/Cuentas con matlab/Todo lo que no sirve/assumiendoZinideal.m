clear;
clc;

s=tf('s');
C = 330e-9;
R = 100;

Rg = 530;
Zg = 10000;
Cg = 1e-9;

IdealZin= Rg*(Cg* Zg * s + 1);

H = IdealZin / (IdealZin + R + (1/(s*C)));

Zgaux = logspace(1,4,20);
for i =1000:1000:10000
    Rg= i;
    IdealZin= Rg*(Cg* Zg * s + 1);
    H = IdealZin / (IdealZin + R + (1/(s*C)));
    bode(H);
    hold on;
end