clc
s=tf('s');
%syms s;
R=1500;
C=22*10^(-9);
H=(1+4*C^2*R^2*s^2)/(1+8*R*C*s+4*R^2*C^2*s^2);
[magH,phaH,w] = bode(H,freq*2*pi);
magH = squeeze(magH);
phaH = squeeze(phaH);
semilogx(freq,phaH,'color','blue');
hold on;
semilogx(freq,fase,'color','red');
xlabel('Frecuencia [Hz]');
ylabel('Fase [°]');
legend('Teorico','Practico');
set(gcf,'PaperOrientation','landscape');
print('bode_Notch_Fase','-dpdf','-fillpage');