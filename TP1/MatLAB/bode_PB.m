s = tf('s');
R = 10000;
C = 1e-9;
H = 1/(s*R*C+1);
[absH,phaH,w] = bode(H,2*pi*freq);
absH = squeeze(absH);
phaH = squeeze(phaH);
absH = 20*log10(absH);
semilogx(freq,fase,'color','red');
hold on;
semilogx(freq,phaH,'color','blue');
xlabel('Frecuencia [Hz]');
ylabel('Fase [°]');
legend('Práctico','Teórico');
set(gcf,'PaperOrientation','landscape');
print('bode_PB_Fase','-dpdf','-fillpage');

