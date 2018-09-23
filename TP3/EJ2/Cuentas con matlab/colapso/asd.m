

C=2.2e-9;
Cg = 10e-9;
Rg = 47;
Zg = 200e3;
R = 12e3;
BWP = 2*pi*3e6;

sys = tf([1],[(C *Rg) * Cg*Zg , C * R, 1])

bode(sys)