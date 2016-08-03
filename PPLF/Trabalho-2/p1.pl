ana.
bruno.
carlos.
daniel.

disse_criminoso(ana, A) :- A \= ana.
disse_criminoso(bruno, carlos).
disse_criminoso(carlos, daniel).
disse_criminoso(daniel, A) :- A \= daniel.

disse_apenas_um(C, V) :-
        findall(X,  disse_criminoso(X, C), L),
	length(L, 1),
	member(V, L).

solucao(C, V) :-
	member(C, [ana, bruno, carlos, daniel]),
	disse_apenas_um(C, V), !.
