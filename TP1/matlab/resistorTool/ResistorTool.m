function [ r1,r2,err,topologia] = ResistorTool(n,ComponentType)
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
   
    pushed_minSeries=zeros([1 3]); % 1x3
    pushed_minParallel=zeros([1 3]);
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
                if(abs(n-Comb(3,i))<=abs(n-minSeries))
                    errs=abs(n-Comb(4,i));
                    aux = zeros([1 3]);
                    aux(1)=Comb(1,i);
                    aux(2)=Comb(2,i);
                    aux(3)=Comb(3,i);
                    r1s=aux(1);
                    r2s=aux(2);
                    minSeries= Comb(3,i);
                    pushed_minSeries=[pushed_minSeries,aux];
                end
                if(abs(n-Comb(4,i))<=abs(n-minParallel))
                    errp=abs(n-Comb(4,i));
                    aux = zeros([1 3]);
                    aux(1)=Comb(1,i);
                    aux(2)=Comb(2,i);
                    aux(3)=Comb(4,i);
                    r1p=aux(1);
                    r2p=aux(2);
                    minParallel = Comb(4,i);
                    pushed_minParallel=[pushed_minParallel,aux];
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