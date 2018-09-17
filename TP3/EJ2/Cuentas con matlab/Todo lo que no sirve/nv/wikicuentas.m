syms s;
syms C;
syms R;
syms RL;

PART1 = (s*C)/(R*s*C +1);
PART2 = -(RL*s*C)/(RL*s*C +1);
DEN= PART1 +1 +PART2;
ZINP= 1/DEN; 
ZINP = simplify(ZINP)
pretty(ZINP)
