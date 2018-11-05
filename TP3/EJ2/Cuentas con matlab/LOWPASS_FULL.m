R = 12000
C = 2.2e-9
Rg = 47
Cg = 10e-9
Zg = 200e3
BWP = 3e6 * 2 * pi
s=tf('s');

% DEN1 =(C*Cg*(C*R*Rg+R*Zg+Rg*Zg))*s^3+(C*(BWP*(Cg*Rg*(R*C+Zg))+Cg*Rg+R+Rg+Cg*Zg))*s^2;
% DEN2 = (BWP*C*Cg*Rg+BWP*C*R+BWP*C*Rg+1)*s+BWP;
% H= (C*Cg*Rg*s^2+BWP*C*Cg*Rg*s+BWP)/(DEN1+DEN2);
% bode(H)


sys = tf([C*Cg*Rg, BWP*C*Cg*Rg, BWP],[C^2*Cg*R*Rg + C*Cg*R*Zg + C*Cg*Rg*Zg, BWP*C^2*Cg*R*Rg + BWP*C*Cg*Rg*Zg + C*Cg*Rg + C*R + C*Rg + Cg*Zg, BWP*C*Cg*Rg + BWP*C*R + BWP*C*Rg + 1, BWP])
[mag, phase,w ]= bode(sys);
%[mag, phase,w ]= bode(ZIN);
mag= squeeze(mag);
phase= squeeze(phase);
w= squeeze(w);
f= w./(2*pi);
mag = 20*log10(mag);
figure(1);
semilogx(f,mag);
hold on;
title('Bode');
xlim([100 2e7]);
L = Cg*Rg*Zg
bode(1/((C*L)*s^2+(C*(R+Rg)+1)*s+1))
grid on