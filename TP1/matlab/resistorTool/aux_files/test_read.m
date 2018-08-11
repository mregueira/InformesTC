clear all
close all
fileID = fopen('vars.txt','r');
formatSpec = '%f';
sizeA = [4 Inf];
%A=fscanf(fileID,formatSpec,sizeA);
A=fscanf(fileID,formatSpec,sizeA);
whos('A')