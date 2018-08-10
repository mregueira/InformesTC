clear all; 
n = 0:1:200;
fo = 8000;
R = 10000;
C = 1e-9;
f = (2.*n+1).*fo;
Xn = 10./((2.*n+1).*pi);
Yn = 10./sqrt(pi.^2.*(2.*n+1).^2+(2.*pi.^2.*fo.*R.*C.*(2.*n+1).^2).^2);
%stem(f,Xn,'filled','color','blue');
%hold on;
%stem(f,Yn,'filled','color','red','marker','diamond');
%xlabel('Frecuencia(Hz)');
%ylabel('Componentes de se�al');
%legend('|Xn|','|Yn|');
%set(gcf,'PaperOrientation','landscape');
%print('Diag_espectral_160_2','-dpdf','-fillpage');

ydata = [];
xdata = [];

for i=1:40
    ydata = [ydata,0];
    ydata = [ydata,Xn(i)];
    ydata = [ydata,Xn(i)];
    ydata = [ydata,Xn(i)];
    ydata = [ydata,0];
    xdata = [xdata, f(i)-fo*0.01];
    xdata = [xdata, f(i)-fo*0.01];
    xdata = [xdata, f(i)];
    xdata = [xdata, f(i)+fo*0.01];
    xdata = [xdata, f(i)+fo*0.01];
end

ans = [xdata,ydata];

plot(xdata,ydata);
