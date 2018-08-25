clc

s=tf('s');
k = 10^3;

r1 = 1.2*k;
r2 = 12*k;
r3 = r1;
r4 = 4.99*k;
a0 = 10^5;
wp = 12 * 2 * pi;

q = r1*r2+r1*r3+r2*r3;
G_ac = a0*r2*r3 / (q + a0*r1*r3);


wpp = wp * (1+r1*r3*a0/q);
H=G_ac / (s/wpp + 1);
freq = logspace(2,8);

[magH,phaH,w] = bode(H,freq*2*pi);
magH = squeeze(magH);
phaH = squeeze(phaH);
semilogx(freq,20*log10(phaH),'color','blue');

hold on;

data = csvread('EJ_1_simulaciones_caso1.csv');

plot(data(:,1),data(:,2));




