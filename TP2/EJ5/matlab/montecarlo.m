

k = 10^3;
m = 10^6;
datos_circuito =[
    [5,-8.9,209-360];
    [6,-4.7,205-360];
    [8,1.9,170-360];
    [10,6.5,162-360];
    [15,13.8,149-360];
    [20,17.9,125-360];
    [30,22,95-360];
    [50,24.8,62-360];
    [70,26,45-360];
    [100,26.3,32-360];
    [150,26.6,22-360];
    [200,26.7,16-360];
    [300,26.8,11-360];
    [400,26.8,7-360];
    [500,26.8,5-360];
    [700,26.8,3-360];
    [k,26.8,0-360];
    [1.5*k,26.8,-2-360];
    [2*k,26.8,-4-360];
    [3*k,26.7,-8-360];
    [5*k,26.6,-14-360];
    [7*k,26.5,-19-360];
    [9*k,26.3,-24-360];
    [11*k,26,-28-360];
    [15*k,25.4,-38-360];
    [17*k,25.1,-43-360];
    [19*k,24.7,-46-360];
    [20*k,24.5,-49-360];
    [22*k,24.2,-52-360];
    [25*k,23.6,-59-360];
    [30*k,22.7,-65-360];
    [50*k,19.1,-89-360];
    [70*k,15.9,-102-360];
    [100*k,12,-121-360];
    [150*k,6.7,-140-360];
    [200*k,2.4,-146-360];
    [300*k,-4.1,-162-360];
    [500*k,-13.1,-190-360]];


% for i=1:length(mc(:,3))
%     if mc(i,3)>0
%         mc(i,3) = mc(i,3)- 360;
%     end
% end
% semilogx(mc(:,1),mc(i,3));
% xlim([5 500e3]);

for i=1:length(Phase)
    if isnumeric(Phase(i)) 
        if Freq(i)>7.15 
            Phase(i) = Phase(i)- 360;
        end
        if Freq(i)<9 && Freq(i)>6.5
            Phase(i) = Phase(i-1)-10;            
        end
    end
end
semilogx(Freq,Vout);
xlim([5 500e3]);

hold on;
semilogx(datos_circuito(:,1),datos_circuito(:,2),'LineWidth',1.5)
%semilogx(datos_circuito(:,1),datos_circuito(:,3),'red')
