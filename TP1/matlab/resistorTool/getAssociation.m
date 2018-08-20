function [result] = getAssociation(r1,r2,assoc_res,n,ComponentType,Association)
%getAssociation recibe dos componentes con un error y asociaci�n, dependiendo ComponentType esta 
%funci�n devuelve un cell array con la informaci�n que recibe m�s la asociaci�n seg�n el componente que sea
%por ejemplo, si es un resistor y la asociacion es serie devuelve serie 
%y si era un capacitor devuelve paralelo
    result=cell(1,4);
    
    result{end+1,1}=r1;
    result{end,2}=r2;
    result{end,3}=assoc_res;
    if strcmp(Association,'serie')
        if strcmp(ComponentType,'cap') %notamos la dualidad de las asociaciones
            topology='paralelo';
        elseif strcmp(ComponentType,'res')
            topology='serie';
        end
    elseif strcmp(Association,'paralelo')

        if strcmp(ComponentType,'cap') %notamos la dualidad de las asociaciones
            topology='serie';
        elseif strcmp(ComponentType,'res')
            topology='paralelo';   
        end
    end 
    err=100*(abs(n-assoc_res)/n);
    result{end,4}=err;
    result{end,5}=topology; 
    
    result=result(~cellfun(@isempty, result(:,1)), :);
    
end