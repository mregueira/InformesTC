

s = tf('s');

H = (4*s^2+1) / (4*s^2 + 8*s+1); 

[mag, pha , w] = bode(H);

mag = squeeze(mag);
xlabel('freq (1/s)');
ylabel('|H(s)| (db)');
semilogx(w , 20 * log10(mag) );