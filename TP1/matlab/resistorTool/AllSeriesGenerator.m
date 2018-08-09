    clear all 
    close all
    
    nominalValue=zeros(0);
    resorcap = 'res';
    
    if strcmp(resorcap,'res')
    fileID = fopen('nominalResValues.txt','r');
    formatSpec = '%f';
    nominalValue=fscanf(fileID,formatSpec);
    fclose(fileID);
    
    elseif strcmp(resorcap,'cap')
    fileID = fopen('nominalCapValues.txt','r');
    formatSpec = '%f';
    nominalValue=fscanf(fileID,formatSpec);
    fclose(fileID);
    end
    
    %el caso j==0 es para ver si con R1 ya me alcanza
    
 
    fileID;
    if strcmp(resorcap,'res')
         fileID = fopen('StoredResValues.txt','w');
    elseif strcmp(resorcap,'cap')
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
                if strcmp(resorcap,'res')
                      fprintf(fileID,'%f %f %f %f\n',store.r1,store.r2,store.req_series,store.req_parallel);
                 elseif strcmp(resorcap,'cap')
                      fprintf(fileID,'%4.16f %4.16f %4.16f \n',store.r1,store.r2,store.req_series,store.req_parallel);
                 end
   
                    
                

        end
    end

    fclose(fileID);
    
    