R1=(100e3)/2;
ZINP=2e6;
R1= (R1*ZINP)/(R1+ZINP);
C1=100e-9;
s=tf('s');
H= (R1)/(R1+(1/(s*C1)));
bode(H)
