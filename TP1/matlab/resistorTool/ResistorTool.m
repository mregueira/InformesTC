function [ r1,r2,err,topologia] = ResistorTool(n,resorcap)
%resistorTool devuelve la combinación con menos error relativo de paralelo o serie
%segun corresponda.
%Aclaracion : Si devuelve r2=0 y topologia=serie significa que solo hay que usar una resistencia

%ERRORES DE INPUT:
%-Si resorcap no es ni 'res' ni 'cap' entonces la funcion devuelve:
% r1=r2=intmin('int64'),err=intmax('int64'),topologia=err_in_component_type_input
%-Si n<0 se devuelve:
% err=intmax('int64'),topologia='err_in_value_input'

%TO-DO LIST:
%Retornar mas de una combinacion posible.
%Incluir el calculo de error para las tolerancias de los componentes que se van a utilizar.

    nominalValue=zeros(0);
    if  strcmp(resorcap,'res')
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
    
    r1s=intmin('int64'); %valores absurdos para debugging 
    r2s=intmin('int64');
    errs=intmax('int64');
    r1p=intmin('int64');  
    r2p=intmin('int64');
    errp=intmax('int64');
    
    %CASO SERIE
    pushed_minSeries = zeros([1 3]); 
    minSeries = intmax('int64');
    %el caso j==0 es para ver si con R1 ya me alcanza
    for i=1:length(nominalValue)
        for j=0:length(nominalValue)
            if j==0
                actual = nominalValue(i);
            else
                actual=(nominalValue(i)+nominalValue(j));
            end
            if(abs(n-actual)<=abs(n-minSeries))
                minSeries=actual;
                r1s=nominalValue(i);
                if j==0
                    r2s=0;
                else
                    r2s=nominalValue(j);
                end
                aux = zeros([1 3]);
                aux(1)=r1s;
                aux(2)=r2s;
                aux(3)=actual;
                pushed_minSeries=[pushed_minSeries,aux];

            end
            
        end
    end
    errs = abs(n-(r1s+r2s));
   
    
    
    %CASO PARALELO
    pushed_minParallel=zeros([1 3]);
    minParallel=intmax('int64');
    for i=1:length(nominalValue)
        for j=1:length(nominalValue)
            actual=(nominalValue(i)*nominalValue(j))/(nominalValue(i)+nominalValue(j));
            %si el actual tiene menos error que el ultimo que se guardo con
            %menor error entonces pongo a actual como el menor de todos
            if(abs(n-actual)<=abs(n-minParallel))
                minParallel=actual;
                r1p=nominalValue(i);
                r2p=nominalValue(j);
                aux = zeros([1 3]);
                aux(1)=r1p;
                aux(2)=r2p;
                aux(3)=actual;
                pushed_minParallel=[pushed_minParallel,aux];
            end
        end
    end
    
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
    
    if(n<0)
        err=intmax('int64');
        topologia='err_in_value_input';
    end
    
    %notamos la dualidad de la asociacion de resistores y capacitores luego
    if strcmp(resorcap,'cap')
        if strcmp(topologia,'serie')
            topologia='paralelo';
            if(length(pushed_minSeries)>3)
                disp('otra comb')
                maxsz=length(pushed_minSeries);
                sz=3;
                found =0 ;
                while(sz<maxsz && ~found)
                    if pushed_minSeries(end-sz) ~= pushed_minSeries(end) && pushed_minSeries(end-sz-1) ~= pushed_minSeries(end-1) && pushed_minSeries(end-2) ~= pushed_minSeries(end-sz-2)
                        found = 1;
                        disp(pushed_minSeries(end-sz-2))
                        disp(pushed_minSeries(end-sz-1))
                        disp(abs(n-pushed_minSeries(end-sz)))
                    else
                        sz=sz+3;
                    end
                        
                end
            end
            
        elseif strcmp(topologia,'paralelo')
            topologia='serie';   
            if(length(pushed_minParallel)>3)
                disp('otra comb')
                maxsz=length(pushed_minParallel);
                sz=3;
                found =0 ;
                while(sz<maxsz && ~found)
                    if pushed_minParallel(end-sz) ~= pushed_minParallel(end) && pushed_minParallel(end-sz-1) ~= pushed_minParallel(end-1) && pushed_minParallel(end-2) ~= pushed_minParallel(end-sz-2)
                        found = 1;
                        disp(pushed_minParallel(end-sz-2))
                        disp(pushed_minParallel(end-sz-1))
                        disp(abs(n-pushed_minParallel(end-sz)))
                    else
                        sz=sz+3;
                    end
                        
                end
            end
        end
    elseif strcmp(resorcap,'res')
        %no hago nada
    else
         err=intmax('int64');
         topologia='err_in_component_type_input';
    end
    
    
end