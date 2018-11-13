% Filtro final - Orden 10 Legendre %
clc;
s = tf('s');
wp = 2*pi*13250;
SHP = wp/s;

H1 = 1/(SHP^2 + SHP*0.5548 + 0.2702);
H2 = 1/(SHP^2 + SHP*0.0918 + 0.9870);
H3 = 1/(SHP^2 + SHP*0.4284 + 0.5282);
H4 = 1/(SHP^2 + SHP*0.2650 + 0.8013);
H5 = 1/(SHP^2 + SHP*0.6344 + 0.1218);

H = H1*H2*H3*H4*H5;