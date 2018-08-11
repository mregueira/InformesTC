clc;
clear all
close all

answer=zeros([1 3]);

[a,b,c,t]=ResistorTool(123,'res');

answer(1)=a;
answer(2)=b;
answer(3)=c;

disp(answer)
disp(t)