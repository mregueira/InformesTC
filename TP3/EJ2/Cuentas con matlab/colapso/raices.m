clear;
clc;
C=2.2e-9;
Cg = 10e-9;
Rg = 47;
Zg = 200e3;
R = 12e3;
BWP = 2*pi*3e6;

s=tf('s')


s1=((BWP^2*Rg^2)/(9*R^2) - BWP/(3*Cg*Zg))/((((BWP^3*Rg^3)/(27*R^3) + BWP/(2*C*Cg*R*Zg) - (BWP^2*Rg)/(6*Cg*R*Zg))^2 - ((BWP^2*Rg^2)/(9*R^2) - BWP/(3*Cg*Zg))^3)^(1/2) - (BWP^3*Rg^3)/(27*R^3) - BWP/(2*C*Cg*R*Zg) + (BWP^2*Rg)/(6*Cg*R*Zg))^(1/3) + ((((BWP^3*Rg^3)/(27*R^3) + BWP/(2*C*Cg*R*Zg) - (BWP^2*Rg)/(6*Cg*R*Zg))^2 - ((BWP^2*Rg^2)/(9*R^2) - BWP/(3*Cg*Zg))^3)^(1/2) - (BWP^3*Rg^3)/(27*R^3) - BWP/(2*C*Cg*R*Zg) + (BWP^2*Rg)/(6*Cg*R*Zg))^(1/3) - (BWP*Rg)/(3*R)
s2= - ((BWP^2*Rg^2)/(9*R^2) - BWP/(3*Cg*Zg))/(2*((((BWP^3*Rg^3)/(27*R^3) + BWP/(2*C*Cg*R*Zg) - (BWP^2*Rg)/(6*Cg*R*Zg))^2 - ((BWP^2*Rg^2)/(9*R^2) - BWP/(3*Cg*Zg))^3)^(1/2) - (BWP^3*Rg^3)/(27*R^3) - BWP/(2*C*Cg*R*Zg) + (BWP^2*Rg)/(6*Cg*R*Zg))^(1/3)) - (3^(1/2)*(((BWP^2*Rg^2)/(9*R^2) - BWP/(3*Cg*Zg))/((((BWP^3*Rg^3)/(27*R^3) + BWP/(2*C*Cg*R*Zg) - (BWP^2*Rg)/(6*Cg*R*Zg))^2 - ((BWP^2*Rg^2)/(9*R^2) - BWP/(3*Cg*Zg))^3)^(1/2) - (BWP^3*Rg^3)/(27*R^3) - BWP/(2*C*Cg*R*Zg) + (BWP^2*Rg)/(6*Cg*R*Zg))^(1/3) - ((((BWP^3*Rg^3)/(27*R^3) + BWP/(2*C*Cg*R*Zg) - (BWP^2*Rg)/(6*Cg*R*Zg))^2 - ((BWP^2*Rg^2)/(9*R^2) - BWP/(3*Cg*Zg))^3)^(1/2) - (BWP^3*Rg^3)/(27*R^3) - BWP/(2*C*Cg*R*Zg) + (BWP^2*Rg)/(6*Cg*R*Zg))^(1/3))*1i)/2 - ((((BWP^3*Rg^3)/(27*R^3) + BWP/(2*C*Cg*R*Zg) - (BWP^2*Rg)/(6*Cg*R*Zg))^2 - ((BWP^2*Rg^2)/(9*R^2) - BWP/(3*Cg*Zg))^3)^(1/2) - (BWP^3*Rg^3)/(27*R^3) - BWP/(2*C*Cg*R*Zg) + (BWP^2*Rg)/(6*Cg*R*Zg))^(1/3)/2 - (BWP*Rg)/(3*R)
s3= - ((BWP^2*Rg^2)/(9*R^2) - BWP/(3*Cg*Zg))/(2*((((BWP^3*Rg^3)/(27*R^3) + BWP/(2*C*Cg*R*Zg) - (BWP^2*Rg)/(6*Cg*R*Zg))^2 - ((BWP^2*Rg^2)/(9*R^2) - BWP/(3*Cg*Zg))^3)^(1/2) - (BWP^3*Rg^3)/(27*R^3) - BWP/(2*C*Cg*R*Zg) + (BWP^2*Rg)/(6*Cg*R*Zg))^(1/3)) + (3^(1/2)*(((BWP^2*Rg^2)/(9*R^2) - BWP/(3*Cg*Zg))/((((BWP^3*Rg^3)/(27*R^3) + BWP/(2*C*Cg*R*Zg) - (BWP^2*Rg)/(6*Cg*R*Zg))^2 - ((BWP^2*Rg^2)/(9*R^2) - BWP/(3*Cg*Zg))^3)^(1/2) - (BWP^3*Rg^3)/(27*R^3) - BWP/(2*C*Cg*R*Zg) + (BWP^2*Rg)/(6*Cg*R*Zg))^(1/3) - ((((BWP^3*Rg^3)/(27*R^3) + BWP/(2*C*Cg*R*Zg) - (BWP^2*Rg)/(6*Cg*R*Zg))^2 - ((BWP^2*Rg^2)/(9*R^2) - BWP/(3*Cg*Zg))^3)^(1/2) - (BWP^3*Rg^3)/(27*R^3) - BWP/(2*C*Cg*R*Zg) + (BWP^2*Rg)/(6*Cg*R*Zg))^(1/3))*1i)/2 - ((((BWP^3*Rg^3)/(27*R^3) + BWP/(2*C*Cg*R*Zg) - (BWP^2*Rg)/(6*Cg*R*Zg))^2 - ((BWP^2*Rg^2)/(9*R^2) - BWP/(3*Cg*Zg))^3)^(1/2) - (BWP^3*Rg^3)/(27*R^3) - BWP/(2*C*Cg*R*Zg) + (BWP^2*Rg)/(6*Cg*R*Zg))^(1/3)/2 - (BWP*Rg)/(3*R)

aux = (s-s2)*(s-s3)

bode((BWP/(C*Cg*R*Zg))/((s-s1)*aux))

s-s1

