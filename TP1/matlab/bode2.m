
data_freq = test * 1000;

s = tf('s');

w0 = 16 * 10 ^3 * 2 * pi;

H = 1/(1+s/w0);

[mag, pha , w] = bode(H);

mag = squeeze(mag);
xlabel('freq (1/s)');
ylabel('|H(s)| (db)');

whz = w / (2 * pi) ;

semilogx(whz , 20 * log10(mag) );

hdb = 20 * log10(mag);