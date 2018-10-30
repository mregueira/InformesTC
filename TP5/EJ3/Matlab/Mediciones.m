clear;
clc;

s = tf('s');

min = 1000;
max = 500e3;



%bajo Q
w0 = 220935.8;
Q = 0.81;
R1 = 750;
Ra1	= 330;
Ra2 = 7500;
R41	= 300;
R42	=7500;
C21	= 6.8e-9;
C22	= 3.3e-9;
C3 = 10e-9;
Gb = 1/1000;

G1 = 1/R1;
Ga1 = 1 / Ra1;
Ga2 = 1/Ra2;
G41 = 1/ R41;
G42 = 1/ R42;


n2 = ((Ga1+Ga2+Gb)/Gb) * (C22 / (C21+C22))  - Ga2/Gb;
n1 = ((Ga1+Ga2+Gb)/Gb)*G42* ((1/(C21+C22)) + 1 / C3) -(Ga2/Gb)*((G1/(C21+C22))+(G41+G42)*((1/(C21+C22)) + 1 / C3));
n0 = (G1 *(G41+G42)/(C3* (C21+C22)))*((G42/(G41+G42)) * ((Ga1+Ga2+Gb)/(Gb)) -Ga2/Gb);
T1 = (n2* s ^2 + n1*s + n0) /(s^2 + s * (w0 / Q) + w0^2);

w0 = 129062.66;
Q = 4.41;
R1	=	180;
Ra1	=	3300;
Ra2	=	4700;
R41	=	4300;
R42	=	15000;
C21	= 3.3e-9;
C22	= 6.8e-9;
C3 = 10e-9;

Gb = 1/100;
G1 = 1/ R1;
Ga1 = 1 / Ra1;
Ga2 = 1/ Ra2;
G41 = 1/ R41;
G42 = 1/ R42;

n2 = ((Ga1+Ga2+Gb)/Gb) * (C22 / (C21+C22))  - Ga2/Gb;
n1 = ((Ga1+Ga2+Gb)/Gb)*G42* ((1/(C21+C22)) + 1 / C3) -(Ga2/Gb)*((G1/(C21+C22))+(G41+G42)*((1/(C21+C22)) + 1 / C3));
n0 = (G1 *(G41+G42)/(C3* (C21+C22)))*((G42/(G41+G42)) * ((Ga1+Ga2+Gb)/(Gb)) -Ga2/Gb);

T2 = (n2* s ^2 + n1*s + n0) /(s^2 + s * (w0 / Q) + w0^2);

T = T1*T2;

wx=((min*2*pi):(20*pi):((max)*(2*pi)));
[mag, fase]= bode(T, wx);
mag2=squeeze(mag);
fase1 = squeeze(fase);
fase2=squeeze(fase);
fase2= fase2-360;
for i=1:size(fase2)
    if(fase2(i)<(-200))
        fase2(i)= fase2(i)+360;
    end

end
magDB= 20*log10(mag2);
f=wx./(2*pi);
semilogx(f, magDB);
hold on;
%semilogx(f, fase1); %Esto podria ser fase 1 o fase 2

filename = 'bodecompleto.csv';
R1= 1 ;
C1 = 0 ;
data = csvread(filename,R1,C1);
data_Freq = data(:,1);
data_Mag = data(:,3);
data_Phase = data(:,4);

semilogx(data_Freq,data_Mag);
hold on;

filename = 'Sedra.csv';
R1= 1 ;
C1 = 0 ;
sim = csvread(filename,R1,C1);
sim_Freq = sim(:,1);
sim_Mag = sim(:,2);
sim_Phase = sim(:,3);

semilogx(sim_Freq,sim_Mag);
hold off ;

title('Diagrama de Bode (Módulo)');
xlim([min max])
legend('Teórico','Medido','Simulación');

