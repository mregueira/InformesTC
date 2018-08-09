fileID = fopen('nominalCapValues.txt','w');

nominalValue=zeros(0);
nominalValuecore = [1,1.2,2.2,3.3,4.7,5.6,6.7,8.2];

for i = -12:-1
    for j=1:length(nominalValuecore)
        nominalValue=[nominalValue,nominalValuecore(j)*(10.0^i)];
    end
end

fprintf(fileID,'%4.16f\n',nominalValue);
fclose(fileID);