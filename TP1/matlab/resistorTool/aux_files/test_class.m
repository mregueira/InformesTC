clc 
clear all
close all
a=BasicClass;
a.r1=1;
a.r2=2;
a.req_series = a.r1+a.r2;
a.req_parallel = (a.r1 * a.r2) / (a.r1+a.r2);

for i = 1:10 
    aux=BasicClass;
    aux.r1=rand(1);
    aux.r2=rand(1);
    aux.req_series = aux.r1+aux.r2;
    aux.req_parallel = (aux.r1 * aux.r2) / ( aux.r1+aux.r2);
    a=[a,aux];
end

fileID = fopen('vars.txt','w');
for i = 1:10
    fprintf(fileID,'%4.4f %4.4f %4.4f \n',a(i).r1,a(i).r2,a(i).req_series,a(i).req_parallel);
end
fclose(fileID);

