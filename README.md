# ObesityPrediction

Le dataset parle de l’obésité et de la relation entre l'âge (Age), le poids (Weight), la taille(Height), ainsi que d’autres questions posées au patient, pour en déduire son type d’obésité, qui peut varier:
Poids Insuffisant, Poids Normale, 
Surpoids de niveau I, Surpoids de niveau II, Surpoids de niveau III, 
Obésité de Type I, Obésité de Type II, Obésité de Type III

Nous cherchons donc à établir le meilleur modèle de prediction, et cela dans l'objectif de pouvoir determiner le plus efficacement possible le type d'obésité d'une personne à partir des attributs donnés.

Vous pouvez voir ici les attributs float ainsi que l'entier qui leur correspond lorsque l'on doit associer auxx float un int pour les modèles : 

- Genre : Female(0), Male(1)
- Family_history_with_overweight : no(0), yes(1)
- FAVC : no(0), yes(1)
- CAEC : always(0), frequently(1), sometimes(2), no(3)
- SMOKE : no(0), yes(1)
- SCC : no(0), yes(1)
- CALC : always(0), frequently(1), sometimes(2), no(3)
- MTRANS : Automobile(0), Bike(1), Motorbike(2), Public_Transportation(3), Walking(4)

Nous avons testé plusieurs modèles mais en conclusion, le plus efficace est celui dont la prédiction a été faite à partir de l'algorithme RandomForest
