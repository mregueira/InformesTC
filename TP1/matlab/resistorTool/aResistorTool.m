function [ pushed_minParallel,pushed_minSeries] = aResistorTool(n,ComponentType)
%resistorTool devuelve la combinación con menos error relativo de paralelo o serie
%segun corresponda.
%Aclaracion : Si devuelve r2=0 y topologia=serie significa que solo hay que usar una resistencia

%ERRORES DE INPUT:
%-Si n no es numerico se retorna por topologia 'err_arg_value_not_numeric'
%-Si ComponentType no es ni 'res' ni 'cap' entonces la funcion devuelve:
% r1=r2=intmin('int64'),err=intmax('int64'),topologia=err_in_component_type_input
%-Si n<=0 se devuelve:
% err=intmax('int64'),topologia='err_arg_value_not_positive'

%TO-DO LIST:
%Retornar mas de una combinacion posible.
%Incluir el calculo de error para las tolerancias de los componentes que se van a utilizar.


    r1s=intmin('int64'); %valores absurdos para debugging 
    r2s=intmin('int64');
    errs=intmax('int64');
    r1p=intmin('int64');  
    r2p=intmin('int64');
    errp=intmax('int64');
    
    if strcmp(ComponentType,'res')
        fileID = fopen('StoredResValues.txt','r');
        formatSpec = '%f %f %f %f\n';
        sizeComb = [4 Inf];
        Comb=fscanf(fileID,formatSpec,sizeComb);
        fclose(fileID);
    elseif strcmp(ComponentType,'cap')
        fileID = fopen('StoredResValues.txt','r');
        formatSpec = '%4.16f %4.16f %4.16f \n';
        sizeComb = [4 Inf];
        Comb=fscanf(fileID,formatSpec,sizeComb);
        fclose(fileID);
    end
   
    pushed_minSeries=cell(1,4); % 1x3
    pushed_minParallel=cell(1,4);
    minSeries=intmax('int64');
    minParallel=intmax('int64');
    
    if (strcmp(ComponentType,'res') || strcmp(ComponentType,'cap')) && isnumeric(n)
        for i=1:length(Comb)
           if(Comb(1,i)==n)
               r1s=Comb(1,i);
               r2s=0;
           end
        end
        if r2s~=0 
            for i=1:length(Comb)        
                if(abs(n-Comb(3,i))<abs(n-minSeries))
                    errs=abs(n-Comb(4,i));
                    aux = zeros([1 3]);
                    aux(1)=Comb(1,i);
                    aux(2)=Comb(2,i);
                    aux(3)=Comb(3,i);
                    r1s=aux(1);
                    r2s=aux(2);
                    minSeries= Comb(3,i);
                    pushed_minSeries{end+1,1}=aux(1);
                    pushed_minSeries{end,2}=aux(2);
                    pushed_minSeries{end,3}=aux(3);
                    pushed_minSeries{end,4}=abs(n-Comb(3,i));
                    
                end
                if(abs(n-Comb(4,i))<abs(n-minParallel))
                    errp=abs(n-Comb(4,i));
                    aux = zeros([1 3]);
                    aux(1)=Comb(1,i);
                    aux(2)=Comb(2,i);
                    aux(3)=Comb(4,i);
                    r1p=aux(1);
                    r2p=aux(2);
                    minParallel = Comb(4,i);

                    pushed_minParallel{end+1,1}=aux(1);
                    pushed_minParallel{end,2}=aux(2);
                    pushed_minParallel{end,3}=aux(3);
                    pushed_minParallel{end,4}=abs(n-Comb(4,i));
                end
            end
        end    
        errs = abs(n-(r1s+r2s));
        errp=abs(n-((r1p*r2p)/(r1p+r2p)));
        if(errp>errs)
            r1=r1s;
            r2=r2s;
            err=errs;
            topologia='serie';
        else
            r1=r1p;
            r2=r2p;
            err=errp;
            topologia='paralelo';
        end
    %las siguientes dos lineas borran los empty values del cell array
        pushed_minSeries=pushed_minSeries(~cellfun(@isempty, pushed_minSeries(:,1)), :);
        pushed_minParallel=pushed_minParallel(~cellfun(@isempty, pushed_minParallel(:,1)), :);
    %ordeno segun el error
        pushed_minSeries= sortrows(pushed_minSeries,4);
        pushed_minParallel= sortrows(pushed_minParallel,4);
        
        fivepms=cell(1,3);
        fivepmp=cell(1,3);
        for i = 1:5
            fivepms(end+1,1)=pushed_minSeries(i,1);
            fivepms(end,2)=pushed_minSeries(i,2);
            fivepms(end,3)=pushed_minSeries(i,3);
            fivepms(end,4)=pushed_minSeries(i,4);
            
            fivepmp(end+1,1)=pushed_minParallel(i,1);
            fivepmp(end,2)=pushed_minParallel(i,2);
            fivepmp(end,3)=pushed_minParallel(i,3);
            fivepmp(end,4)=pushed_minParallel(i,4);
        end
        
        fivepms=fivepms(~cellfun(@isempty, fivepms(:,1)), :);
        fivepmp=fivepmp(~cellfun(@isempty, fivepmp(:,1)), :);
        
        pushed_minSeries=fivepms;
        pushed_minParallel=fivepmp;
    end
   
    
    
    %Chequeo de errores
    if(n<=0)
        err=intmax('int64');
        r1=intmin('int64'); %valores absurdos para debugging 
        r2=intmin('int64');
        topologia='err_arg_value_not_positive';
    end
    if(~isnumeric(n))
        err=intmax('int64');
        r1=intmin('int64'); 
        r2=intmin('int64');
        topologia='err_arg_value_not_numeric';
    end
       
    %notamos la dualidad de la asociacion de resistores y capacitores luego
    if strcmp(ComponentType,'cap')
        if strcmp(topologia,'serie')
            topologia='paralelo';
        elseif strcmp(topologia,'paralelo')
            topologia='serie';   
        end
    elseif strcmp(ComponentType,'res')
        %no hago nada
    else
         err=intmax('int64');
         topologia='err_in_component_type_input';
    end
end