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
    nominalValuecore=zeros(0);
    if  strcmp(resorcap,'res')
        nominalValuecore = [1,1.2,1.5,1.8,2.2,2.7,3.3,3.9,4.7,5.1,5.6,6.8,8.2];
        tolerancia       = [5,5,5,5  ,5  ,5  ,5  ,5  ,5  ,5  ,5  ,5  ,  5,  5];
        
        for i = -1:6
            for j=1:length(nominalValuecore)
                nominalValue=[nominalValue,nominalValuecore(j)*(10.0^i),tolerancia(j) ];
            end
        end
    elseif strcmp(resorcap,'cap')
        nominalValuecore = [1,1.2,2.2,3.3,4.7,5.6,6.7,8.2];
        tolerancia       = [5,5,5,5,5,5,5,5,5,5,5,5,5,5];
        for i = -12:-1
            for j=1:length(nominalValuecore)
                nominalValue=[nominalValue,nominalValuecore(j)*(10.0^i),tolerancia(j)];
            end
        end
    end
    
    r1s=intmin('int64'); %valores absurdos para debugging 
    r2s=intmin('int64');
    errs=intmax('int64');
    r1p=intmin('int64');  
    r2p=intmin('int64');
    errp=intmax('int64');
    
    
    %CASO SERIE
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
            end
        end
    end
    errs = abs(n-(r1s+r2s));
   
    %CASO PARALELO
    minParallelstack=zeros(0);
    aux={0,0,0};
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
        elseif strcmp(topologia,'paralelo')
            topologia='serie';   
        end
    elseif strcmp(resorcap,'res')
        %no hago nada
    else
         err=intmax('int64');
         topologia='err_in_component_type_input';
    end
end