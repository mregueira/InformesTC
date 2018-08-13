N = 10000;
T = 1/8000; 

t = 0:T/N:(T-T/N);

duty = 0.5;

x = rectangularPulse(0,T * duty,t) - 0.5;

y = fft(x)/N;


t2 = 0:8000:8000*100-8000;

%stem(  t2, abs(y(1:100) ));

vals = abs(y(1:100) );

%stem(t2,vals);


