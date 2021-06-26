/* EJERCICIO 1:  Sistema experto para mantenimiento de sistema de control 
    
    de valvula de seguridad en estacion de reduccion de presion de gas */

% ESTADOS POSIBLES : DESCONOCIDO , OK, NO



/* Axiomas (invariantes del dominio) */

action(X):-  verificar(X) .
% verificacion():- verificar(piloto);


% Rama IZQUIERDA
verificar(valvula_thickness) :-  
    
    thickness( valvula_thickness, Espesor ), threshold(valvula_thickness, Limite), Espesor < Limite , writeln('\nACCION NECESARIA: Equipment status will be reported to the Technical Inspection Unit immediately.');
    % thickness( valvula_thickness, Espesor ), threshold(valvula_thickness, Limite), Espesor >= Limite , writeln('\nThe condition of the equipment is suitable');

    

    (   thickness( valvula_thickness, desconocido ), 
        (   
            ( estado(valvula_components_having_effects, no ), writeln('\nVERIFICAR COMPONENTE: Thickness valve') );
            verificar( valvula_components_having_effects )
        ) 
                
    ).

verificar(safety_valve_components_having_effects) :-  

    estado( safety_valve_components_having_effects, yes ), writeln('\nACCION NECESARIA: Coordination is required in order to render and color the equipment.');   

    estado( safety_valve_components_having_effects, desconocido ), writeln('\nVERIFICAR COMPONENTE: safety valve components having effects').



% Rama CENTRAL izquierda
verificar(piloto) :- 
    estado(piloto, ok), writeln('\nACCION NECESARIA: Set the safety valve according to the instauctions');
    estado(piloto, no), writeln('\nACCION NECESARIA: Pilot full service and reinstallation');
    (
        estado(piloto, desconocido), 
        (
        (estado(leakage_prevention_between_sit_and_orifice, ok), writeln('\nVERIFICAR COMPONENTE: estado de Piloto'));
        verificar(leakage_prevention_between_sit_and_orifice)
        )
    
    ).



verificar(leakage_prevention_between_sit_and_orifice) :- 
                estado(leakage_prevention_between_sit_and_orifice, no), writeln('\nACCION NECESARIA: Replace Sit and Orifice and put the safety valve into circuit') ; 
                estado(leakage_prevention_between_sit_and_orifice, desconocido), 
                ((estado(safety_valve_spring, ok), writeln('\nVERIFICAR COMPONENTE: leakage prevention between sit and orifice')); 
                verificar(safety_valve_spring)).

verificar(safety_valve_spring) :- 
                estado(safety_valve_spring, no), writeln('\nACCION NECESARIA: Putting spring and safety in the service') ; 
                
                estado(safety_valve_spring, desconocido), 
                (
                    (estado(control_valve_sensors_blocked, no), writeln('\nVERIFICAR COMPONENTE: safety valve spring')); 
                    verificar(control_valve_sensors_blocked)
                ).

verificar(control_valve_sensors_blocked) :- 
                estado(control_valve_sensors_blocked, ok), writeln('\nACCION NECESARIA: Cleaning and troubleshooting of the sensing pipes') ; 
                estado(control_valve_sensors_blocked, desconocido), 
                ((estado(valve_status_closed, no), writeln('\nVERIFICAR COMPONENTE:  control valve sensors blocked')); 
                verificar(valve_status_closed)).
                
verificar(valve_status_closed) :- 
                estado(valve_status_closed, ok), writeln('\nACCION NECESARIA: Place the safety valve in open position') ; 

                estado(valve_status_closed, desconocido),
                (
                    (estado(relief_valve_ok_with_10_percent_more_pressure, no), writeln('\nVERIFICAR COMPONENTE: VALVE STATUS position'));
                    verificar(relief_valve_ok_with_10_percent_more_pressure)
                ).
                
% Verifciar si no hay que hacerlo aprecido al de threshold
verificar(relief_valve_ok_with_10_percent_more_pressure) :- 

                estado(relief_valve_ok_with_10_percent_more_pressure, ok), writeln('\nACCION NECESARIA: Safety function is appropriate') ; 

                estado(relief_valve_ok_with_10_percent_more_pressure, desconocido),
                ((estado(safety_valve_has_continuous_evacuation, no), writeln('\nVERIFICAR COMPONENTE: relief valve works correctly with +10% over regular pressure')); 
                verificar(safety_valve_has_continuous_evacuation)).
            
verificar(safety_valve_has_continuous_evacuation) :- 
                estado(safety_valve_has_continuous_evacuation, desconocido), 
                writeln('\nVERIFICAR COMPONENTE: safety valve has continuous evacuation').


% Rama CENTRAL derecha
verificar(preventable_lackage_between_sit_and_orifice) :- 
                estado( preventable_lackage_between_sit_and_orifice, ok ), writeln('\nACCION NECESARIA: Set the safety valve according to the instructions ');
                estado( preventable_lackage_between_sit_and_orifice, no ), writeln('\nACCION NECESARIA: Replace Sit and Orifice and put the safety valve into circuit');
                (
                estado( preventable_lackage_between_sit_and_orifice, desconocido ), 
                ((estado(safety_spring_effective, ok ), writeln('\nVERIFICAR COMPONENTE: preventable lackage between sit and orifice'));
                verificar(safety_spring_effective))).

verificar(safety_spring_effective) :- 
                
                estado( safety_spring_effective, no ), writeln('\nACCION NECESARIA: Replace the safety spring in the service');
                
                (estado( safety_spring_effective, desconocido ), 
                (
                    (estado(control_and_pressuere_sensor_pipes_blocked, no ), writeln('\nVERIFICAR COMPONENTE: Verificar safety spring effective'));
                    verificar(control_and_pressuere_sensor_pipes_blocked  )
                )
                ).



verificar(control_and_pressuere_sensor_pipes_blocked) :-

        estado( control_and_pressuere_sensor_pipes_blocked, ok ), writeln('\nACCION NECESARIA: Clean up and fix the faults of the sensing pipes');

        (   
            estado( control_and_pressuere_sensor_pipes_blocked, desconocido ), 
            (
            (estado(line_gas_pressure_appropriate, ok ), writeln('\nVERIFICAR COMPONENTE: control and sensor pipes estan bloqueados'));
            verificar( line_gas_pressure_appropriate )
            ) 
        ).
 


verificar(line_gas_pressure_appropriate) :-
    
    estado( line_gas_pressure_appropriate, no ), writeln('\nACCION NECESARIA: Adjust the regulator according to the instructions');
    (   
        estado( line_gas_pressure_appropriate, desconocido ),        
        (   
            ( estado(safety_valve_has_continuous_evacuation, ok ), writeln('\nVERIFICAR COMPONENTE: si control and sensor pipes estan bloqueados') );
            ( verificar( safety_valve_has_continuous_evacuation ) )                        
        )           
    ).


% --------- Rama DERECHA ---------

verificar(leakage_fixed_with_wrench_at_joints) :- 

    estado(leakage_fixed_with_wrench_at_joints, ok), writeln('\nACCION NECESARIA: Report to Technical Insprection Unit');
    estado(leakage_fixed_with_wrench_at_joints, no), writeln('\nACCION NECESARIA: Send a report to the repair department to fix the fault');
    (
        estado(leakage_fixed_with_wrench_at_joints, desconocido), 
        (
            (estado(gas_leakage_at_joint, ok), writeln('\nVERIFICAR COMPONENTE: leakage fixed with wrench at joints'));
            verificar(gas_leakage_at_joint)
        )
    ).
verificar(gas_leakage_at_joint) :- 
    % estado(gas_leakage_at_joint, no), writeln('\nThe safety valve joint are free of gas leakage.');
    
    estado(gas_leakage_at_joint, desconocido), writeln('\nVERIFICAR COMPONENTE: gas leakage at joint').



/* Ground Facts de instancia variables (podrian resolverse mediante sensado o agregando la informacion interactivamente a la base de conocimientos) */

%RAMA IZQUIERDA
thickness(valvula_thickness, Espesor) :-  Espesor is 15.
threshold(valvula_thickness, Threshol) :-  Threshol is 20.
estado( safety_valve_components_having_effects, no ).


% RAMA CENTRAL izqueirda
estado(piloto, ok).
estado(leakage_prevention_between_sit_and_orifice, ok).
estado(safety_valve_spring, ok).
estado(control_valve_sensors_blocked, no).
estado(valve_status_closed, no).
estado(relief_valve_ok_with_10_percent_more_pressure, no).
estado(safety_valve_has_continuous_evacuation, no).


% RAMA CENTRAL izqueirda
estado( preventable_lackage_between_sit_and_orifice, no ).
estado( safety_spring_effective, ok ).
estado( control_and_pressuere_sensor_pipes_blocked, no ).
estado( line_gas_pressure_appropriate, ok ).


%RAMA DERECHA
estado(leakage_fixed_with_wrench_at_joints, no).
estado(gas_leakage_at_joint, ok).


