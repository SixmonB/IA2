/* Ejemplo parcial de sistema experto para mantenimiento de sistema de control 
    de valvula de seguridad en estacion de reduccion de presion de gas */

/* Axiomas (invariantes del dominio) */
verificar(piloto) :- 
    estado(piloto, ok), writeln('Todo OK').

verificar(piloto) :- 
                estado(piloto, desconocido), 
                ((estado(leakage_prevention_between_sit_and_orifice, ok), writeln('Verificar Pilot'));
                verificar(leakage_prevention_between_sit_and_orifice)).

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

/* Ground Facts de instancia variables (podrian resolverse mediante sensado o agregando la informacion interactivamente a la base de conocimientos) */
estado(piloto, desconocido).
estado(leakage_prevention_between_sit_and_orifice, desconocido).
estado(safety_valve_spring, desconocido).
estado(control_valve_sensors_blocked, desconocido).
estado(valve_status_closed, desconocido).
estado(relief_valve_ok_with_10_percent_more_pressure, desconocido).
estado(safety_valve_has_continuous_evacuation, desconocido).


