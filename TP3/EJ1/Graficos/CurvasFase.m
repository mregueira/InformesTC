pha = pha;
pic = semilogx(freq,pha,'color','red','linewidth',2);
hold on;
set(gca, 'FontName', 'Times New Roman', 'FontSize', 12);
xlabel('Frecuencia [Hz]');         
ylabel('Fase H(S) [°]');
str = {'Frec: ', 'Fase: '};
[max_medido,xMax_medido] = max(pha);
[min_medido,xMin_medido] = min(pha);
datatip(pic, xMax_medido, str, 'r', 'topright','hold');
datatip(pic, xMin_medido, str, 'r', 'topleft','hold');

for i=1:5001
    temp = sscanf(Vvo{i},'%f,%f');
    pha_Sim(i) = (atan(temp(2)/temp(1)))*180/pi;
    if temp(1)<0
        pha_Sim(i) = pha_Sim(i) + 180;
    end
end
pic = semilogx(freq_Sim,pha_Sim,'color','blue','linewidth',2);
[max_Sim,xMax_Sim] = max(pha_Sim);
[min_Sim,xMin_Sim] = min(pha_Sim);
datatip(pic, xMax_Sim, str, 'b', 'bottomleft','hold');
datatip(pic, xMin_Sim, str, 'b', 'topright','hold');

k = sqrt((2*(10^(-0.2))) - 1);
q = 2;
wp = 13000;
s = tf('s');
H = (2/(1+(k^2)))*(((s^2) + ((k*wp)^2))/((s^2) + (s*wp/q) + (wp^2)));
win = (2*pi*10):10:(2*pi*1000000);
[mag, pha_Teo, wout] = bode(H,win);
pha_Teo = squeeze(pha_Teo);
pic = semilogx(win/(2*pi),pha_Teo,'color','green','linewidth',2);
[max_Teo,xMax_Teo] = max(pha_Teo);
[min_Teo,xMin_Teo] = min(pha_Teo);
datatip(pic, xMax_Teo, str, 'g', 'topleft','hold');
datatip(pic, xMin_Teo, str, 'g', 'bottomleft','hold');


legend('Medido','Simulado','Teorico');
set(gcf,'PaperOrientation','landscape');
print('GIC_Bode_Pha','-dpdf','-fillpage');