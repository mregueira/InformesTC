    clc;
    clear all 
    close all
    
    ComponentType = 'cap';
    
    
    nominalValue=zeros(0);
    if strcmp(ComponentType,'res')
    nominalValuecore = [1,1.2,1.5,1.8,2.2,2.7,3.3,3.9,4.7,5.1,5.6,6.8,8.2];        
        for i = -1:6
            for j=1:length(nominalValuecore)
                nominalValue=[nominalValue,nominalValuecore(j)*(10.0^i) ];
            end
        end    
    elseif strcmp(ComponentType,'cap')
    nominalValuecore = [1,1.2,2.2,3.3,4.7,5.6,6.7,8.2];
        for i = -12:-1
            for j=1:length(nominalValuecore)
                nominalValue=[nominalValue,nominalValuecore(j)*(10.0^i)];
            end
        end
    end
    
    %el caso j==0 es para ver si con R1 ya me alcanza
    
    if strcmp(ComponentType,'res')
         fileID = fopen('StoredResValues.txt','w');
    elseif strcmp(ComponentType,'cap')
         fileID = fopen('StoredCapValues.txt','w');
    end
    
    for i=1:length(nominalValue)
        for j=1:length(nominalValue)
            if j==0
                r1 = nominalValue(i);
                r2 = 0;
            else
                r1 = nominalValue(i);
                r2 = nominalValue(j);
            end
                store=BasicClass;
                store.r1=r1;
                store.r2=r2;
                store.req_series = r1+r2;
                if j==0 
                    store.req_parallel = realmax('single');
                else
                    store.req_parallel = (r1*r2)/(r1+r2);
                end
                if strcmp(ComponentType,'res')
                      fprintf(fileID,'%f %f %f %f\n',store.r1,store.r2,store.req_series,store.req_parallel);
                 elseif strcmp(ComponentType,'cap')
                      fprintf(fileID,'%4.16f %4.16f %4.16f \n',store.r1,store.r2,store.req_series,store.req_parallel);
                end
        end
    end
    
    if(strcmp(ComponentType,'res') || strcmp(ComponentType,'cap'))
    fclose(fileID);
    end
    
    