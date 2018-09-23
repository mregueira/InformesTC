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