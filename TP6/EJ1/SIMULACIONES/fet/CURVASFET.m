a=csvread('Curvas_FET-0.txt');
plot(a(:,1),(a(:,2)),'LineWidth',1.5);
hold on

a=csvread('Curvas_FET-1.txt');
plot(a(:,1),(a(:,2)),'LineWidth',1.5);

a=csvread('Curvas_FET-2.txt');
plot(a(:,1),(a(:,2)),'LineWidth',1.5);

a=csvread('Curvas_FET-3.txt');
plot(a(:,1),(a(:,2)),'LineWidth',1.5);

a=csvread('Curvas_FET-4.txt');
plot(a(:,1),(a(:,2)),'LineWidth',1.5);

grid on 
legend('Vgs=0', 'Vgs=-1','Vgs=-2','Vgs=-3','Vgs=-4')
 title('Curvas caracterÝsticas MPF102')
 ylabel('Id (A)')
 xlabel('Vds(V)')