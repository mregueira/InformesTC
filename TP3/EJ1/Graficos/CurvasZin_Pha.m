pic = semilogx(freq,Zin_Pha,'color','red','linewidth',2);
hold on;
set(gca, 'FontName', 'Times New Roman', 'FontSize', 12);
xlabel('Frecuencia [Hz]');         
ylabel('Fase Zin [°]');
str = {'Frec: ', 'Fase: '};
[max_medido,xMax_medido] = max(Zin_Pha);
[min_medido,xMin_medido] = min(Zin_Pha);
datatip(pic, xMax_medido, str, 'r', 'topleft','hold');
datatip(pic, xMin_medido, str, 'r', 'bottomright','hold');

for i=1:501
    temp = sscanf(Vvo{i},'%f,%f');
    Zin_Sim(i) = 180*(atan(temp(2)/temp(1)))/pi;
end
pic = semilogx(freq_Sim,Zin_Sim,'color','blue','linewidth',2);
[max_Sim,xMax_Sim] = max(Zin_Sim);
[min_Sim,xMin_Sim] = min(Zin_Sim);
datatip(pic, xMax_Sim, str, 'b', 'topright','hold');
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

Zin_pha = (squeeze(Zin_pha));
pic = semilogx(win/(2*pi),Zin_pha,'color','green','linewidth',2);
[max_Teo,xMax_Teo] = max(Zin_pha);
[min_Teo,xMin_Teo] = min(Zin_pha);
datatip(pic, xMax_Teo, str, 'g', 'topleft','hold');
datatip(pic, xMin_Teo, str, 'g', 'bottomleft','hold');

legend('Medido','Simulado','Teorico');
set(gcf,'PaperOrientation','landscape');
print('GIC_Bode_Zin_Pha','-dpdf','-fillpage');