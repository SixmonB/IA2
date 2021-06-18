% alarma(X) :-  explota(X).

explota(Tuberia) :- tuberia(Tuberia), temperatura(Tuberia,Temp), presion(Tuberia,P), P > 100, Temp > 150,   writeln('Va a explotar').

presion(t1, X) :- X is 2105.
presion(t2, X) :- X is 105.

temperatura(t1, Temp) :- Temp is  2105.
temperatura(t2, Temp) :- Temp is  165.


tuberia(t1).
tuberia(t2).

