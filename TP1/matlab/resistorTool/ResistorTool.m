function [ minValues] = ResistorTool(n,ComponentType,Association)
%resistorTool devuelve la combinación con menos error relativo de paralelo o serie
%segun corresponda.
%Aclaracion : Si devuelve r2=0 y topologia=serie significa que solo hay que usar una resistencia

%ERRORES DE INPUT:
%-Si n no es numerico se retorna por topologia 'err_arg_value_not_numeric'
%-Si ComponentType no es ni 'res' ni 'cap' entonces la funcion devuelve:
% r1=r2=intmin('int64'),err=intmax('int64'),topologia=err_in_component_type_input
%-Si n<=0 se devuelve:
% err=intmax('int64'),topologia='err_arg_value_not_positive'

    r1s=intmin('int64'); %valores absurdos para debugging 
    r2s=intmin('int64');
    errs=intmax('int64');
    r1p=intmin('int64');  
    r2p=intmin('int64');
    errp=intmax('int64');
    

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
    Comb=cell(1,4);
    
    %genero todas las combinaciones posibles
    for i=1:length(nominalValue)
        for j=1:length(nominalValue)
            if j==0
                r1 = nominalValue(i);
                r2 = 0;
            else
                r1 = nominalValue(i);
                r2 = nominalValue(j);
            end
            if j==0 
                req_parallel = realmax('single');
            else
                req_parallel = (r1*r2)/(r1+r2);
            end
            Comb{end+1,1}=r1;
            Comb{end,2}=r2;
            Comb{end,3}=r1+r2;
            Comb{end,4}=req_parallel;
        end
    end
    
    minValues=cell(1,5); % 1x5
    minSeries=intmax('int64');
    minParallel=intmax('int64');
    topology = 'not_modified';
   
    %Chequeo de errores
    input_error=0;
    if(n<=0)
        input_error=1;
        minValues=[intmin('int64') intmin('int64') intmin('int64') intmax('int64') 'err_arg_value_not_positive'];
    end
    if(~isnumeric(n))
        input_error=1;
        minValues=[intmin('int64') intmin('int64') intmin('int64') intmax('int64') 'err_arg_value_not_numeric'];
    end
       
    if ~(strcmp(ComponentType,'cap') || strcmp(ComponentType,'res'))
        input_error=1;
         minValues=[intmin('int64') intmin('int64') intmin('int64') intmax('int64') 'err_in_component_type_input']; 
    end    
    
    if ~(strcmp(Association,'paralelo') || strcmp(Association,'serie') || strcmp(Association,'ambos'))
        input_error=1;
        minValues=[intmin('int64') intmin('int64') intmin('int64') intmax('int64') 'err_in_association_input']; 
    end     
    
    %Comb son todas las combinaciones posibles con los valores nominales
    %sigue el siguiente orden
    % Comb{i,1}=R1 Comb{i,2}=R2 Comb{i,3}=R1+R2 Comb{i,4}=R1//R2
    % la variable r1s r2s, representa las resistencias que seran asociadas en serie
    % y r1p r2p las que seran asociadas en paralelo
    
    if input_error~=1
        %primero vemos si no es un valor nominal
        for i=1:length(Comb)
           if(Comb{i,1}==n)
               r1s=Comb{i,1};
               r2s=0;
               minSeries=r1s+r2s;
               errs=0;      
           end
        end
        if r2s~=0 %si fuera un valor nominal r2s seria 0
            for i=1:length(Comb)        
                if(abs(n-Comb{i,3})<abs(n-minSeries))
                    r1s=Comb{i,1};
                    r2s=Comb{i,2};
                    minSeries= Comb{i,3};
                    errs=abs(n-Comb{i,3})/n;                   
                    %si el error es menor lo guardo
                    minValues{end+1,1}=r1s;
                    minValues{end,2}=r2s;
                    minValues{end,3}=minSeries; % minSeries=r1s +r2s
                    minValues{end,4}=errs;
                    if strcmp(ComponentType,'cap') %notamos la dualidad de las asociaciones
                        topology='paralelo';
                    elseif strcmp(ComponentType,'res')
                        topology='serie';   
                    end
                    minValues{end,5}=topology;
                end
                if(abs(n-Comb{i,4})<abs(n-minParallel))
                    r1p=Comb{i,1};
                    r2p=Comb{i,2};
                    minParallel = Comb{i,4};
                    errp=abs(n-Comb{i,4})/n;                    
                    minValues{end+1,1}=r1p;
                    minValues{end,2}=r2p;
                    minValues{end,3}=minParallel; %minParallel = r1p//r2p
                    minValues{end,4}=errp;                                       
                    if strcmp(ComponentType,'cap')
                        topology='serie';
                    elseif strcmp(ComponentType,'res')
                        topology='paralelo';   
                    end
                    minValues{end,5}=topology;
                end
            end
        elseif r2s==0
               minValues{end+1,1}=r1s;
               minValues{end,2}=r2s;
               minValues{end,3}=minSeries; % minSeries=r1s +r2s
               minValues{end,4}=errs;
               minValues{end,5}='serie';
        end

        %las siguientes dos lineas borran los empty values del cell array (ya
        %que sino sort no los puede ordenar)
        minValues=minValues(~cellfun(@isempty, minValues(:,1)), :);
        %ordeno segun el error
        minValues= sortrows(minValues,4);
 
        %y ahora agarro los 10 con menor error segun la asociacion que se
        %pidio
        selectedValues=cell(1,5);
        numberOfSelectedV=10;
        if length(minValues) > numberOfSelectedV
            i=1;
            while(numberOfSelectedV>=1 && i<=length(minValues)) 
                if strcmp(Association,'paralelo') && strcmp(minValues(i,5),'paralelo')
                    selectedValues(end+1,1)=minValues(i,1);
                    selectedValues(end,2)=minValues(i,2);
                    selectedValues(end,3)=minValues(i,3);
                    selectedValues(end,4)=minValues(i,4);
                    selectedValues(end,5)=minValues(i,5);
                    i=i+1;
                    numberOfSelectedV=numberOfSelectedV-1;
                else
                    i=i+1;
                end
                if strcmp(Association,'serie') && strcmp(minValues(i,5),'serie')
                    selectedValues(end+1,1)=minValues(i,1);
                    selectedValues(end,2)=minValues(i,2);
                    selectedValues(end,3)=minValues(i,3);
                    selectedValues(end,4)=minValues(i,4);
                    selectedValues(end,5)=minValues(i,5);
                    i=i+1;
                    numberOfSelectedV=numberOfSelectedV-1;
                else
                    i=i+1;
                end
                if strcmp(Association,'ambos')
                    selectedValues(end+1,1)=minValues(i,1);
                    selectedValues(end,2)=minValues(i,2);
                    selectedValues(end,3)=minValues(i,3);
                    selectedValues(end,4)=minValues(i,4);
                    selectedValues(end,5)=minValues(i,5);
                    numberOfSelectedV=numberOfSelectedV-1;
                    i=i+1;
                else
                    i=i+1;
                end
            end
            selectedValues=selectedValues(~cellfun(@isempty, selectedValues(:,1)), :); 
            minValues=selectedValues;
        end        
    end
end