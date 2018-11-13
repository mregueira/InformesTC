a=csvread('WIEN.txt');


%semilogx(a(:,1),10.^(a(:,2)/20),'LineWidth',1.5);

 plot(a(:,1),(a(:,2)),'LineWidth',1.5);


 hold on
 grid on 
 
 ylabel('Amplitud (V)')
 xlabel('Tiempo (s)')