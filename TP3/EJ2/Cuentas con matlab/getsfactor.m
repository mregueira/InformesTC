function [ H] = getsfactor( H )
% La funcion getsfactor expande el numerador y denominador y luego en cada
% uno hace factor comun s, s^2 ... etc... para poder llegar a una expresion
% más amigable
    syms s;
    [N,D] = numden(H);
    N = expand(N);
    N = collect(N,s);
    D = expand(D);
    D = collect(D,s);
    H= N/D;
    H=simplify(H);
end

