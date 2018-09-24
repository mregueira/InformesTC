k = sqrt((2*(10^(-0.2))) - 1);
q = 2;
wp = 13000;
s = tf('s');
H = (((s^2) + ((k*wp)^2))/((s^2) + (s*wp/q) + (wp^2)));
pzmap(H)
grid on

set(gcf,'PaperOrientation','landscape');
print('PZMap_Norm','-dpdf','-fillpage');