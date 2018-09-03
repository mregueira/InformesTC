function LTSpice2Csv(filename) 
    % States of the state machine
    START = 1;
    IDLE = 2;
    PARAM = 3;
    MEAS = 4;
    state = START;
    
    % Open file and read first line
    fid = fopen(filename);
    line = fgetl(fid);
    
    % Variables where the data and vector name are stored
    currData = 0;
    currName = '';
    
    % State machine loop
    
    while ischar(line)

        if state==START
            if length(line)>5 && strcmp(line(1:5),'.step')
                currName = line(strfind(line,' ')+1:strfind(line,'=')-1);
                currData = str2double(line(strfind(line,'=')+1:end));
                state=PARAM;
            end
            
        elseif state==PARAM
            if length(line) < 5
                assignin('base',currName,currData)
                currName = '';
                currData = 0;
                state = IDLE;
            else                
                currData = [currData; str2double(line(strfind(line,'=')+1:end))];
            end
            
        elseif state==IDLE      
            if length(line) > 11 && strcmp(line(1:11),'Measurement')
                currName = line(strfind(line,' ')+1:end);
                line = fgetl(fid);%Delete the line with names
                state = MEAS;
            end
                 
        elseif state==MEAS
            if length(line) < 5
                assignin('base',currName,currData)
                currName = '';
                currData = 0;
                state = IDLE;
            else
                nums = str2double(regexp(line,'\d*\.\d*|\d*|[+\-]?[^\w]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)','match'));
                if currData == 0
                    currData = nums(2);
                else
                    currData = [currData; nums(2)];
                end
            end
        end
        line = fgetl(fid);
    end
    fclose(fid);
end
    
