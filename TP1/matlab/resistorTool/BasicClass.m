classdef BasicClass
   properties
      r1
      r2
      req_series
      req_parallel
   end
   methods
       function obj = ObjectArray(F)
         if nargin ~= 0
            m = size(F);
            obj(m) = ObjectArray;
            for i = 1:m
                  obj(i).r1 = F(i).r1;
                  obj(i).r2 = F(i).r2;
                  obj(i).req_series = F(i).req_series;
                  obj(i).req_parallel = F(i).req_parallel;
            end
         end
      end
   end
end