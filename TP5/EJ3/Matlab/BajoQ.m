clear;
clc;
%--TP Pablo--%
%con Ap = 1db, As = 45db, wp = 11000, ws = 20500 -0.5db
wz = 31779.0;
w0 = 220935.8;
Q = 0.81;
% estas cosas no dependen de n2
n2 = 10^(1.73/20);
%---Esto lo fijo yo-%
Q0 = (1/2.50)*Q;
%Q0 = (1/3)*Q; % Q0
C = 300e-9;
Gb = 1/1000;
%------------%
for i = 0.1:0.01:0.4
    Q0 = i;
    nominalVal = 6.8e-9;
    [Gb,G1,Ga1,Ga2,G41,G42,C21,C22,C3] = getCompValues(Q,w0,wz, n2 , Q0, C , Gb);
    %nominalValC21 = C-nominalVal;
    %nominalValC21 = 3.3e-9; 
    %&& (abs(C21-nominalValC21)< nominalValC21*5/100)
    %if((abs(C22-nominalVal)< nominalVal*5/100) )
    fprintf('Gb = %e KOhm G1 = %e KOhm \n Ga1= %e KOhm Ga2= %e KOhm \n G41= %e KOhm G42= %e KOhm \n C21= %e nf C22=%e nf C3= %e nf \n',1/Gb/1e3,1/G1/1e3,1/Ga1/1e3,1/Ga2/1e3,1/G41/1e3,1/G42/1e3,C21/1e-9,C22/1e-9,C3/1e-9);
    disp(20*log10(abs(((Ga1+Ga2+Gb)/Gb)* (C22/C)-(Ga2/Gb))));
    %end
end


%n2 = );
% Gb = 1.000000e+00 KOhm G1 = 7.300325e-01 KOhm 
%  Ga1= 3.246431e-01 KOhm Ga2= 7.612111e+00 KOhm 
%  G41= 2.914631e-01 KOhm G42= 7.546341e+00 KOhm 
%  C21= 6.790438e+00 nf C22=3.209562e+00 nf C3= 1.000000e+01 nf 