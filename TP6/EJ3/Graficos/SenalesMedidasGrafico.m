% Mediciones %
clc;
plot(time,volt,'linewidth',2,'Color','magenta');
legend('Frecuencia = 10KHz');
xlabel('Tiempo[s]');
ylabel('Tension[V]')


set(gcf,'PaperOrientation','landscape');
print('VCO_10K','-dpdf','-fillpage');