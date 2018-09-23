ratio = amp;
pic = semilogx(freq,ratio,'color','red','linewidth',2);
hold on;
set(gca, 'FontName', 'Times New Roman', 'FontSize', 12);
xlabel('Frecuencia [Hz]');         
ylabel('|H(S)| [dB]');
str = {'Frec: ', '|H(S)|: '};
[max_medido,xMax_medido] = max(ratio);
[min_medido,xMin_medido] = min(ratio);
datatip(pic, xMax_medido, str, 'r', 'topright','hold');
datatip(pic, xMin_medido, str, 'r', 'bottomright','hold');

for i=1:5001
    temp = sscanf(Vvo{i},'%f,%f');
    ratio_Sim(i) = 20*log10(sqrt((temp(1))^2 + (temp(2))^2));
end
pic = semilogx(freq_Sim,ratio_Sim,'color','blue','linewidth',2);
[max_Sim,xMax_Sim] = max(ratio_Sim);
[min_Sim,xMin_Sim] = min(ratio_Sim);
datatip(pic, xMax_Sim, str, 'b', 'topleft','hold');
datatip(pic, xMin_Sim, str, 'b', 'bottomleft','hold');

k = sqrt((2*(10^(-0.2))) - 1);
q = 2;
wp = 13000;
s = tf('s');
H = (2/(1+(k^2)))*(((s^2) + ((k*wp)^2))/((s^2) + (s*wp/q) + (wp^2)));
win = (2*pi*10):10:(2*pi*1000000);
[mag, pha, wout] = bode(H,win);
mag = 20*log10(squeeze(mag));
pic = semilogx(win/(2*pi),mag,'color','green','linewidth',2);
[max_Teo,xMax_Teo] = max(mag);
[min_Teo,xMin_Teo] = min(mag);
datatip(pic, xMax_Teo, str, 'g', 'bottomleft','hold');
datatip(pic, xMin_Teo, str, 'g', 'topleft','hold');


legend('Medido','Simulado','Teorico');
set(gcf,'PaperOrientation','landscape');
print('Borrar','-dpdf','-fillpage');