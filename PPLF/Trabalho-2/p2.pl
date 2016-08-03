solucao_peca(_, [], _) :- !.
solucao_peca(Q, [V|VS], N) :-
	QV0 is Q + N,
	QV1 is Q - N,
	V \= QV0,
	V \= QV1,
	V \= Q,
	N0 is N + 1,
	solucao_peca(Q, VS, N0).

solucao([]).

solucao([Q|QS]) :-
	solucao_peca(Q, QS, 1),
	solucao(QS).

solucao(Q, VS) :-
	solucao_peca(Q, VS, 1).

rainhas([], _).
rainhas([Q|QS], N) :-
	rainhas(QS, N),
	findall(X, between(1, N, X), L),
	member(Q0, L),
	solucao(Q0, QS),
	Q = Q0.

rainhas_p(QS, N) :-
	nonvar(N),
	findall(X, between(1, N, X), L),
	permutation(L, QS),
	solucao(QS).

rainhas_r(QS, N) :-
	nonvar(N),
	length(QS, N),
	rainhas(QS, N).
