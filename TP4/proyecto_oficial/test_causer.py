
from scipy.special import ellipkinc
from math import sqrt
from math import atan
from math import pi


k = 0.7
n = 5
ep = 0.5

v0 =  ellipkinc( atan(1/ep) ,(1-k**2) ) / n

print(v0)