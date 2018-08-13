N = 10000;
T = 1/8000; 
F = 1 / T;

t = 0:T/N:(T-T/N);

duty = 0.5;

x = rectangularPulse(0,T * duty,t) - 0.5;

y = fft(x)/N;

t2 = 1:100;

coef_abs = abs(y(1:100) );


ydata = [];
xdata = [];


for i=1:100
    ydata = [ydata,0];
    ydata = [ydata,coef_abs(i)];
    ydata = [ydata,0];
    xdata = [xdata, (i-1)*F-0.01*F];
    xdata = [xdata, (i-1)*F ];
    xdata = [xdata, (i-1)*F+0.01*F];
end

ans = [xdata,ydata];

plot(xdata,ydata);

