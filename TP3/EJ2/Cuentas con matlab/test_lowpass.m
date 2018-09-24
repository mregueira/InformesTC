R = 12000
C = 2.2e-9
Rg = 47
Cg = 10e-9
Zg = 200e3
BWP = 3e6 * 2 * pi
s=tf('s');

%sys = tf([C*Cg*Rg, BWP*C*Cg*Rg, BWP],[(C^2)*Cg*R*Rg + C*Cg*R*Zg + C*Cg*Rg*Zg, BWP*(C^2)*Cg*R*Rg + BWP*C*Cg*Rg*Zg + C*Cg*Rg + C*R + C*Rg + Cg*Zg, BWP*C*Cg*Rg + BWP*C*R + BWP*C*Rg + 1, BWP])
sys = tf([C*Cg*Rg, BWP*C*Cg*Rg, BWP],[(C^2)*Cg*R*Rg + C*Cg*R*Zg + C*Cg*Rg*Zg, BWP*(C^2)*Cg*R*Rg + BWP*C*Cg*Rg*Zg + C*Cg*Rg + C*R + C*Rg + Cg*Zg, BWP*C*Cg*Rg + BWP*C*R + BWP*C*Rg + 1, BWP]);
bode(sys)
hold on
NUM= 1
DEN1 =(C*(Cg*Rg*Zg))*s^2 
DEN2 = C*R*s+1
bode(NUM/(DEN1+DEN2))
grid on