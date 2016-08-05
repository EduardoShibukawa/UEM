vizinhos(R) :-
	length(R, 5),
	% casa(cor, nacionalidade, bebida, cigarro, animal).
	R = [casa(_, noruegues,_,_,_), casa(_,_,_,_,_),
	     casa(_,_,leite,_,_), casa(_,_,_,_,_),
	     casa(_,_,_,_,_)],
	member(casa(vermelho, ingles, _, _, _), R),
	member(casa(_, sueco, _, _, cachorros), R),
	member(casa(_, dinamarques, cha, _, _), R),
	a_esquerda(R, casa(branca, _, _, _, _),
		      casa(verde, _, _, _, _)),
	member(casa(verde, _, cafe, _, _), R),
	member(casa(_, _, _, pall_mall, passaros), R),
	member(casa(amarela, _, _, dunhill, _), R),
	ao_lado(R, casa(_, _, _, blends, _),
		   casa(_, _, _, _, gatos)),
	ao_lado(R, casa(_, _, _, _, cavalos),
		   casa(_, _, _, dunhill, _)),
	member(casa(_, _, cerveja, bluemaster, _), R),
	member(casa(_, alemao, _, prince, _), R),
	ao_lado(R, casa(_, noruegues, _, _, _),
		   casa(azul, _, _, _, _)),
	ao_lado(R, casa(_, _, _, blends, _),
		   casa(_, _, agua, _, _)),
	member(casa(_, _, _, _, peixes), R), !.

ao_lado([C1,C2|_], C1, C2).
ao_lado([C2,C1|_], C1, C2).
ao_lado([_|R], C1, C2) :-
	ao_lado(R, C1, C2).

a_esquerda([C|R], C, E) :-
	memberchk(E, R).
a_esquerda([_|R], C, E) :-
	a_esquerda(R, C, E).

