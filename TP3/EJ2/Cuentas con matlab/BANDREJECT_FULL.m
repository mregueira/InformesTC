R = 1000; 
C = 470e-9;
Rg = 100;
Cg = 1e-9;
Zg = 510e3;
BWP = 3e6 * 2 * pi;

s=tf('s');
L = Rg*Cg*Zg;

%H =(BWP + s + C*Rg*s^2 + Cg*Rg*s^2 + Cg*Zg*s^2 + BWP*C*Rg*s + BWP*Cg*Rg*s + C*Cg*Rg*Zg*s^3 + BWP*C*Cg*Rg*Zg*s^2)/(C*Cg*(R*Rg + R*Zg + Rg*Zg)*s^3 + (C*R + C*Rg + Cg*Rg + Cg*Zg + BWP*C*Cg*R*Rg + BWP*C*Cg*Rg*Zg)*s^2 + (BWP*C*R + BWP*C*Rg + BWP*Cg*Rg + 1)*s + BWP);

Haux = ((C*L)*s^2+s*(Rg*C)+1)/(C*L*s^2+(C*(R+Rg))*s+1);
bode(Haux)
Haux2 =((C*L)*s^2+s*(Rg*C)+1)/(C*L*s^2+(C*(R))*s+1);
hold on;
bode(Haux2)
