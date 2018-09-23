pic = semilogx(freq,Zin,'color','red','linewidth',2);
hold on;
set(gca, 'FontName', 'Times New Roman', 'FontSize', 12);
xlabel('Frecuencia [Hz]');         
ylabel('|Zin| [Ohm]');
str = {'Frec: ', 'Zin: '};
[max_medido,xMax_medido] = max(Zin);
[min_medido,xMin_medido] = min(Zin);
datatip(pic, xMax_medido, str, 'r', 'topleft','hold');
datatip(pic, xMin_medido, str, 'r', 'topright','hold');

for i=1:501
    temp = sscanf(Vvo{i},'%f,%f');
    Zin_Sim(i) = temp(1);
end
pic = semilogx(freq_Sim,Zin_Sim,'color','blue','linewidth',2);
[max_Sim,xMax_Sim] = max(Zin_Sim);
[min_Sim,xMin_Sim] = min(Zin_Sim);
datatip(pic, xMax_Sim, str, 'b', 'bottomleft','hold');
datatip(pic, xMin_Sim, str, 'b', 'bottomright','hold');

k = sqrt((2*(10^(-0.2))) - 1);
q = 2;
R = 7500;
wp = 13000;
s = tf('s');

b1 = wp/q;
c1 = wp^2;
b2 = wp*( ((q*(1+(k^2))+(k^2))/(q*(1+(k^2)))) + q*(1-(k^2)) );
c2 = (wp^2)*(1-(k^2))*((k^2)+(q*(1+(k^2))))/(1+(k^2));

Zin_Teo = (1+(k^2))*q*R*((s^2) + s*b1 + c1)/((s^2) + s*b2 + c2);

win = (2*pi*10):10:(2*pi*1000000);
[Zin_mag, Zin_pha, wout] = bode(Zin_Teo,win);

Zin_mag = (squeeze(Zin_mag));
pic = semilogx(win/(2*pi),Zin_mag,'color','green','linewidth',2);
% [max_Teo,xMax_Teo] = max(mag);
[min_Teo,xMin_Teo] = min(Zin_mag);
% datatip(pic, xMax_Teo, str, 'g', 'bottomleft','hold');
datatip(pic, xMin_Teo, str, 'g', 'bottomleft','hold');

legend('Medido','Simulado','Teorico','Location','northwest');
set(gcf,'PaperOrientation','landscape');
print('GIC_Bode_Zin_PuntaX10','-dpdf','-fillpage');