solucao_todas(_, [], _) :- !.
solucao_todas(Q, [V|VS], N) :-
	N0 is N + 1,
	QV0 is Q + N,
	QV1 is Q - N,
	V \= QV0,
	V \= QV1,
	V \= Q,
	solucao_todas(Q, VS, N0).

solucao(Q, VS) :-
	solucao_todas(Q, VS, 1).

solucao([Q,V|VS]) :-
	solucao_todas(Q, [V|VS], 1).

rainhas([], _).
rainhas([Q|QS], N) :-
	rainhas(QS, N),
	findall(X, between(1, N, X), L),
	member(Q0, L),
	Q = Q0,
	solucao(Q, QS).

rainhas_p(QS, N) :-
	nonvar(N),
	findall(X, between(1, N, X), L),
	permutation(L, QS),
	solucao(QS).

rainhas_r(QS, N) :-
	nonvar(N),
	length(QS, N),
	rainhas(QS, N).
