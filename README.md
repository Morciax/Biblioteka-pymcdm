# Biblioteka-pymcdm
Python Multiple-Criteria Decision Making
Analiza metod MCDM z wykorzystaniem biblioteki pymcdm

Biblioteka pymcdm pomaga w podejmowaniu decyzji na podstawie wielu kryteriów. W tym projekcie wykorzystane zostały metody TOPSIS, SPOTIS, VIKOR oraz PROMETHEE II, aby ocenić różne opcje i porównać ich wyniki.

**Dane wejściowe** 
Porównaliśmy cztery alternatywy (A1, A2, A3, A4) według trzech kryteriów:
Alternatywa	Kryterium 1	Kryterium 2	Kryterium 3
A1	4	2	6
A2	7	9	3
A3	3	4	8
A4	5	6	5
•	Wagi kryteriów: [0.3, 0.5, 0.2]
•	Typy kryteriów: wszystkie kryteria powinny być maksymalizowane.
Normalizacja danych
Do normalizacji danych wykorzystano metodę Min-Max, aby wartości były w zakresie [0,1]: 		normalizacja = (value – min)/ (max-min)

**Zastosowane metody**
•	TOPSIS – ocenia, która alternatywa jest najbliżej rozwiązania idealnego.
•	SPOTIS – porównuje alternatywy do najlepszych i najgorszych wartości.
•	VIKOR – szuka rozwiązania kompromisowego.
•	PROMETHEE II – metoda porównawcza oparta na funkcjach preferencji.

Wyniki analizy
Metoda	A1	    A2	    A3	    A4	    Ranking
TOPSIS	0.2034	0.7446	0.3451	0.5360	A2 > A4 > A3 > A1
VIKOR	  1.0000	0.0000	0.6397	0.2588	A2 > A4 > A3 > A1
SPOTIS	0.8050	0.2000	0.6571	0.4843	A1 > A3 > A4 > A2
PROMETHEE II	
        -0.5333	0.6000	-0.2667	0.2000	A2 > A4 > A3 > A1
Aby lepiej zrozumieć różnice między metodami, przedstawiłam wyniki w formie wykresów.

**Wnioski**
•	Zbieżność wyników – Metody TOPSIS, VIKOR i PROMETHEE II wskazują, że A2 jest najlepszą opcją, natomiast SPOTIS wskazuje A1 jako najlepszą.
•	Różnice w metodach – SPOTIS działa inaczej niż pozostałe metody, co wpływa na ranking.
•	Stabilność metod – Wyniki dla TOPSIS, VIKOR i PROMETHEE II są spójne, co świadczy o ich podobnym działaniu.
•	Zastosowanie w praktyce – Takie analizy pomagają w podejmowaniu decyzji np. w finansach czy zarządzaniu projektami.

**Podsumowanie**
Projekt pokazał, jak metody MCDM mogą pomóc w ocenie różnych opcji. Wyniki różnych metod były częściowo zgodne, ale różnice w SPOTIS pokazują, że wybór metody ma znaczenie. Wizualizacje dodatkowo ułatwiły analizę wyników.
