clc;
clear all
close all
clear;

answer=zeros([1 3]);

[a,b,c,t]=aux_res_tool(227,'res');

answer(1)=a;
answer(2)=b;
answer(3)=c;

disp(answer)
disp(t)