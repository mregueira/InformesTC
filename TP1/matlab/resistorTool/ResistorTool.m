function [ minValues] = ResistorTool(n,ComponentType,Association,numberOfSelectedV)
%resistorTool devuelve la combinación con menos error relativo de paralelo o serie
%segun corresponda.

%ERRORES DE INPUT:
%-Si n no es numerico se retorna por topologia 'err_arg_value_not_numeric'
%-Si ComponentType no es ni 'res' ni 'cap' entonces la funcion devuelve:
% r1=r2=-realmax,err=realmax,topologia=err_in_component_type_input
%-Si n<=0 se devuelve:
% err=realmax,topologia='err_arg_value_not_positive'


    r1s=-realmax; %valores absurdos para debugging 
    r2s=-realmax;
    errs=realmax;
    r1p=-realmax;  
    r2p=-realmax;
    errp=realmax;
    

    nominalValue=zeros(0);
    if strcmp(ComponentType,'res')
    nominalValuecore = [1,1.2,1.5,1.8,2.2,2.7,3.3,3.9,4.7,5.6,6.8,8.2];        
        for i = -1:6
            for j=1:length(nominalValuecore)
                nominalValue=[nominalValue,nominalValuecore(j)*(10.0^i) ];
            end
        end    
   elseif strcmp(ComponentType,'cap')
        nominalValuecore = [10,12,15,18,22,27,33,39,47,56,68,82];
        for i = -12:-7
            for j=1:length(nominalValuecore)
                nominalValue=[nominalValue,nominalValuecore(j)*(10.0^i)];
            end
        end
        nominalValue=[nominalValue,10*(10.0^-6)];
        nominalValue=[nominalValue,10*(22.0^-6)];
        nominalValue=[nominalValue,10*(33.0^-6)];
        nominalValue=[nominalValue,10*(47.0^-6)];
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
    minSeries=realmax;
    minParallel=realmax;
    topology = 'not_modified';
   
    %Chequeo de errores
    input_error=0;
    
    if(~isnumeric(n) || ~isfinite(n) ||  n<=0)
        input_error=1;
        minValues=[-realmax -realmax -realmax realmax 'err_arg_value_of_n'];
    end
       
    if ~(strcmp(ComponentType,'cap') || strcmp(ComponentType,'res'))
        input_error=1;
         minValues=[-realmax -realmax -realmax realmax 'err_in_component_type_input']; 
    end    
    
    if ~(strcmp(Association,'paralelo') || strcmp(Association,'serie') || strcmp(Association,'ambos'))
        input_error=1;
        minValues=[-realmax -realmax -realmax realmax 'err_in_association_input']; 
    end     
    if ~isnumeric(numberOfSelectedV) || ~(isfinite(numberOfSelectedV) && numberOfSelectedV==floor(numberOfSelectedV))|| numberOfSelectedV <= 0
         input_error=1;
         minValues=[-realmax -realmax -realmax realmax 'err_in_numberOfSelectedV']; 
    end     
    
    %Comb son todas las combinaciones posibles con los valores nominales
    %sigue el siguiente orden
    % Comb{i,1}=R1 Comb{i,2}=R2 Comb{i,3}=R1+R2 Comb{i,4}=R1//R2
    % la variable r1s r2s, representa las resistencias que seran asociadas en serie
    % y r1p r2p las que seran asociadas en paralelo
    cant_series=0;
    cant_parallel=0;
    finding_nominal=1;
    
    if input_error~=1
        %primero vemos si no es un valor nominal
        for i=1:length(Comb)
           if(Comb{i,1}==n)
               if(finding_nominal)
                   r1s=Comb{i,1};
                   r2s=0;
                   minSeries=r1s+r2s;
                   errs=0;
                   cant_series=cant_series+1;
                   minValues{end+1,1}=r1s;
                   minValues{end,2}=r2s;
                   minValues{end,3}=minSeries; % minSeries=r1s +r2s
                   minValues{end,4}=errs;
                   minValues{end,5}='serie';
                   finding_nominal=0;
               end
           end
        end
         %si fuera un valor nominal r2s seria 0
        for i=1:length(Comb)        
            if(abs(n-Comb{i,3})<abs(n-minSeries))
                cant_series=cant_series+1;
                r1s=Comb{i,1};
                r2s=Comb{i,2};
                minSeries= Comb{i,3};
                errs=100*abs(n-Comb{i,3})/n;                   
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
                cant_parallel=cant_parallel+1;
                r1p=Comb{i,1};
                r2p=Comb{i,2};
                minParallel = Comb{i,4};
                errp=100*abs(n-Comb{i,4})/n;                    
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
        %las siguientes dos lineas borran los empty values del cell array (ya
        %que sino sort no los puede ordenar)
        minValues=minValues(~cellfun(@isempty, minValues(:,1)), :);
        %ordeno segun el error
        minValues= sortrows(minValues,4);
 
        %y ahora agarro los 10 con menor error segun la asociacion que se
        %pidio
        selectedValues=cell(1,5);
        totalSelected=numberOfSelectedV;
        if length(minValues) < totalSelected
            totalSelected=length(minValues); % satura
        end    
        i=1;
        while(numberOfSelectedV>=1 && i<=length(minValues))
            if strcmp(Association,'paralelo')
                if strcmp(minValues(i,5),'paralelo')
                    if cant_parallel < totalSelected
                        totalSelected=cant_parallel; % satura
                    end    
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
            end
            if strcmp(Association,'serie')
                if strcmp(minValues(i,5),'serie')
                    if cant_series < totalSelected
                        totalSelected=cant_series; % satura
                    end    
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
            end

            if strcmp(Association,'ambos')
                selectedValues(end+1,1)=minValues(i,1);
                selectedValues(end,2)=minValues(i,2);
                selectedValues(end,3)=minValues(i,3);
                selectedValues(end,4)=minValues(i,4);
                selectedValues(end,5)=minValues(i,5);
                i=i+1;
                numberOfSelectedV=numberOfSelectedV-1;
            end
        end
            selectedValues=selectedValues(~cellfun(@isempty, selectedValues(:,1)), :); 
            minValues=selectedValues;
        
    end
end