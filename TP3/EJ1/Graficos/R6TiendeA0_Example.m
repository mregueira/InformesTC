clc;
z3 = -0.5+(sqrt(3)/2)*1i;
z4 = -0.5-(sqrt(3)/2)*1i;
z5 = -(sqrt(2)/2)+(sqrt(2)/2)*1i;
z6 = -(sqrt(2)/2)-(sqrt(2)/2)*1i;
z7 = -(sqrt(3)/2)+0.5*1i;
z8 = -(sqrt(3)/2)-0.5*1i;
z9 = -1;
z10 = -2;
z11 = -0.5;
z12 = -3;
z13 = -0.25;

s = tf('s');
H = 1/((s-z3)*(s-z4)*(s-z5)*(s-z6)*(s-z7)*(s-z8)*(s-z9)*(s-z10)*(s-z11)*(s-z12)*(s-z13));
pzmap(H)
title('Polos con R6 tendiendo a 0 - Discriminante límite negativo');
set(gcf,'PaperOrientation','landscape');
print('Polos_R6TiendeA0_Neg','-dpng');
 