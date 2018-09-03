function datos = levantar_raw(filename, variable_to_plot)

%antes de usar levantas el .raw con  LTspice2matlab.m -> ej: raw_data = LTspice2Matlab('simulacion.RAW');
%miras raw_data.variable_name_list y te fijas cúal es la que queres plotear
%le mandas el nombre del archivo .raw como 'simulacion.raw' y variable_to_plot el num de la variable de la lista.

simulation = LTspice2Matlab (filename);

datos.magnitud = 20*log10(abs(simulation.variable_mat(variable_to_plot,:)));

datos.fase = angle(simulation.variable_mat(variable_to_plot,:))*180/pi;

datos.frecuencia = simulation.freq_vect;


end