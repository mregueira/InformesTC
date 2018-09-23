for i=1:501
    temp = sscanf(Vvo{i},'%f,%f');
    Zout_Sim(i) = temp(1);
end
pic = semilogx(freq_Sim,Zout_Sim,'color','blue','linewidth',2);
set(gca, 'FontName', 'Times New Roman', 'FontSize', 12);
xlabel('Frecuencia [Hz]');         
ylabel('|Zoutput| [Ohm]');

legend('Simulado');
set(gcf,'PaperOrientation','landscape');
print('GIC_ZoutSim','-dpdf','-fillpage');