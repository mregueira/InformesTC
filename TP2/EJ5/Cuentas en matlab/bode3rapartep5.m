
s= tf('s');
C1=100e-9;
C2=0.82e-9;
R=10680;
Pot=10000;
H=(C1* Pot *s)/(C1 *Pot* s + C2 *Pot *s + C1* R* s + C1* C2* Pot *R* s^2  + 1);
bode(H,{10,1000000})