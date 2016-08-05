arad-[zerind/75, arad/118, sibiu/140].
bucharest-[urziceni/85, giurgiu/90, pitesti/101, fagaras/211].
craiova-[dobreta/120, pitesti/138, rimnicu_vilcea/146].
dobreta-[mehadia/75, craiova/120].
eforie-[hirsova/86].
fagaras-[sibiu/99, bucharest/211].
giurgiu-[bucharest/90].
hirsova-[eforie/86, urziceni,98].
iasi-[neamt/87, vaslui/92].
lugoj-[mehadia/70, timisoara/111].
mehadia-[lugoj/70, dobreta/75].
neamt-[iasi/87].
oradea-[zerind/71, sibiu/151].
pitesti-[rimnicu_vilcea/97, bucharest/90, craiova/138].
rimnicu_vilcea-[sibiu/80, pitesti/97, craiova/146].
sibiu-[rimnicu_vilcea/80, fagaras/90, oradea/151, arad/140].
timisoara-[arad/118, lujog/111].
urziceni-[bucharest/85, hirsova/98, vaslui/142].
vaslui-[iasi/92, urziceni/142].
zerind-[oradea/71, arad/75].

h(arad, 366).
h(bucharest, 0).
h(craiova, 160).
h(dobreta, 242).
h(eforie, 161).
h(fagaras, 178).
h(giurgiu, 77).
h(hirsova, 226).
h(iasli, 226).
h(lugoj, 244).
h(mehadia, 241).
h(neamt, 234).
h(oradea, 380).
h(pitesti, 98).
h(rimnicu_vilcea, 193).
h(sibiu, 253).
h(timisoara, 329).
h(urziceni, 80).
h(vaslui, 199).
h(zerind, 374).

menor_vizinho(V1/H1, _/H2, V) :-
	H1 < H2,
	V = V1.

menor_vizinho(_/H1, V2/H2, V) :-
	H2 =< H1,
	V = V2.

melhor_vizinho([V/_], V).
melhor_vizinho([VC|VR], V) :-
	melhor_vizinho(VR, V1),
	V2/_ = VC,
	h(V1, H1),
	h(V2, H2),
	menor_vizinho(V1/H1, V2/H2, V).

melhor_caminho(bucharest, [bucharest]) :- !.
melhor_caminho(O, [O|C]) :-
	O-VS,
	melhor_vizinho(VS, V),
	melhor_caminho(V, C),
	!.



