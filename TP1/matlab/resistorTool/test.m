fileID = fopen('nominalResValues.txt','w');
%fprintf(fileID,'%4.4f\n',x);

nominalValue=zeros(0);
nominalValuecore = [1,1.2,1.5,1.8,2.2,2.7,3.3,3.9,4.7,5.1,5.6,6.8,8.2];        
for i = -1:6
    for j=1:length(nominalValuecore)
        nominalValue=[nominalValue,nominalValuecore(j)*(10.0^i) ];
        
    end
end

fprintf(fileID,'%4.4f\n',nominalValue);
fclose(fileID);
