pot=500;
R8=pot:-1:1;
R9=1:1:pot;
Rparalelo=(R9*8)./(R9+8);
Vout = Rparalelo./(Rparalelo+R8);

%plot(R9,Vout)
semilogx(R9,Vout);



%hold on;
%semilogx(R9,R8);
% Resistencia=1000:1000:100000;
% plot(Resistencia,Rparalelo);
% hold on;
% plot(R8,R8+Rparalelo);