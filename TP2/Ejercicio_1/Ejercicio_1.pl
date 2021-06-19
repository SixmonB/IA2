/* EJERCICIO 1:  Sistema experto para mantenimiento de sistema de control 
    
    de valvula de seguridad en estacion de reduccion de presion de gas */

% ESTADOS POSIBLES : DESCONOCIDO , OK, NO



/* Axiomas (invariantes del dominio) */


% Rama IZQUIERDA
verificar(valvula_1) :-  
    thickness( valvula_1, Espesor ), threshold(valvula_1, Limite), Espesor < Limite , writeln('Espesor MAYOR que limite');
    thickness( valvula_1, Espesor ), threshold(valvula_1, Limite), Espesor >= Limite , writeln('Espesor MENOR que limite');
    

    (   thickness( valvula_1, desconocido ), 
        (   
            ( estado(valvula_components_having_effects, no ), writeln('Verificar Thickness valve') );
            verificar( valvula_components_having_effects )
        ) 
                
    ).

verificar(safety_valve_components_having_effects) :-  

    estado( safety_valve_components_having_effects, no ), writeln('Todo OK');
    estado( safety_valve_components_having_effects, no ), writeln('Todo MAL');
    
    estado( safety_valve_components_having_effects, desconocido ), writeln('Verificar safety valve components having effects').



% Rama CENTRAL izquierda
verificar(piloto) :- 
    estado(piloto, ok), writeln('Todo OK');
    estado(piloto, no), writeln('Todo MAL');
    (estado(piloto, desconocido), 
    ((estado(leakage_prevention_between_sit_and_orifice, ok), writeln('Verificar Pilot'));
    verificar(leakage_prevention_between_sit_and_orifice))).



verificar(leakage_prevention_between_sit_and_orifice) :- 
                estado(leakage_prevention_between_sit_and_orifice, desconocido), 
                ((estado(safety_valve_spring, ok), writeln('Verificar leakage prevention between sit and orifice')); 
                verificar(safety_valve_spring)).

verificar(safety_valve_spring) :- 
                estado(safety_valve_spring, desconocido), 
                ((estado(control_valve_sensors_blocked, no), writeln('Verificar safety valve spring')); 
                verificar(control_valve_sensors_blocked)).

verificar(control_valve_sensors_blocked) :- 
                estado(control_valve_sensors_blocked, desconocido), 
                ((estado(valve_status_closed, no), writeln('Verificar control valve sensors blocked')); 
                verificar(valve_status_closed)).
                
verificar(valve_status_closed) :- 
                estado(valve_status_closed, desconocido),
                ((estado(relief_valve_ok_with_10_percent_more_pressure, no), writeln('Verificar valve status "Close"'));
                verificar(relief_valve_ok_with_10_percent_more_pressure)).
                
verificar(relief_valve_ok_with_10_percent_more_pressure) :- 
                estado(relief_valve_ok_with_10_percent_more_pressure, desconocido),
                ((estado(safety_valve_has_continuous_evacuation, no), writeln('Verificar relief valve works correctly with +10% over regular pressure')); 
                verificar(safety_valve_has_continuous_evacuation)).
            
verificar(safety_valve_has_continuous_evacuation) :- 
                estado(safety_valve_has_continuous_evacuation, desconocido), 
                writeln('Verificar safety valve has continuous evacuation').


% Rama CENTRAL derecha
verificar(preventable_lackage_between_sit_and_orifice) :- 
                estado( preventable_lackage_between_sit_and_orifice, ok ), writeln('Todo OK');
                estado( preventable_lackage_between_sit_and_orifice, no ), writeln('Todo MAL');
                (
                estado( preventable_lackage_between_sit_and_orifice, desconocido ), 
                ((estado(safety_spring_effective, ok ), writeln('Verificar preventable lackage between sit and orifice'));
                verificar(safety_spring_effective))).

verificar(safety_spring_effective) :- 
                estado( safety_spring_effective, ok ), writeln('Todo OK');
                estado( safety_spring_effective, no ), writeln('Todo MAL');
                
                (estado( safety_spring_effective, desconocido ), 
                ((estado(control_and_sensor_pipes_blocked, no ), writeln('Verificar safety spring effective'));
                verificar(control_and_sensor_pipes_blocked  ))).



verificar(control_and_sensor_pipes_blocked) :-

        estado( control_and_sensor_pipes_blocked, ok ), writeln('Todo OK');
        estado( control_and_sensor_pipes_blocked, no ), writeln('Todo MAL');

        (   estado( control_and_sensor_pipes_blocked, desconocido ), 
            (( estado(line_gas_pressure_appropriate, ok ), writeln('Verificar si control and sensor pipes estan bloqueados'));
            verificar( line_gas_pressure_appropriate  )) ).
 


verificar(line_gas_pressure_appropriate) :-
    
    estado( line_gas_pressure_appropriate, ok ), writeln('Todo OK');
    estado( line_gas_pressure_appropriate, no ), writeln('Todo MAL');

    (   
        estado( line_gas_pressure_appropriate, desconocido ), 
       
        (   
            ( estado(safety_valve_has_continuous_evacuation, ok ), writeln('Verificar si control and sensor pipes estan bloqueados') );
            ( estado(safety_valve_has_continuous_evacuation, desconocido ), verificar( safety_valve_has_continuous_evacuation ) )
            
            %
        ) 
                
    ).


% --------- Rama IZQUIERDA ---------

verificar(leakage_fixed_with_wrench_at_joints) :- 

    estado(leakage_fixed_with_wrench_at_joints, ok), writeln('Todo OK');
    estado(leakage_fixed_with_wrench_at_joints, no), writeln('Todo MAL');
    (
        estado(leakage_fixed_with_wrench_at_joints, desconocido), 
        (
            (estado(gas_leakage_at_joint, ok), writeln('Verificar leakage fixed with wrench at joints'));
            verificar(gas_leakage_at_joint)
        )
    ).
verificar(gas_leakage_at_joint) :- 
    estado(leakage_fixed_with_wrench_at_joints, no), writeln('The safety valve joint are free of gas leakage.');
    estado(leakage_fixed_with_wrench_at_joints, desconocido), writeln('Verificar gas leakage at joint');



/* Ground Facts de instancia variables (podrian resolverse mediante sensado o agregando la informacion interactivamente a la base de conocimientos) */

estado(piloto, ok).
estado(leakage_prevention_between_sit_and_orifice, desconocido).
estado(safety_valve_spring, desconocido).
estado(control_valve_sensors_blocked, desconocido).
estado(valve_status_closed, desconocido).
estado(relief_valve_ok_with_10_percent_more_pressure, desconocido).
estado(safety_valve_has_continuous_evacuation, desconocido).




thickness(valvula_1, Esp) :-  Esp is 30.
threshold(valvula_1, Thres) :-  Thres is 20.