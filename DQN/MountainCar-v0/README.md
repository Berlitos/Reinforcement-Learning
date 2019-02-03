# MountainCar-v0

## Objectif

Amenez une voiture sous-alimentée au sommet d'une colline (sommet = 0,5 position).

## Source

Andrew Moore in his PhD thesis [Moore90].

## Environment

### Observation
Type: Box(2)

Num	Observation	Min	Max

0	position	-1.2	0.6

1	velocity	-0.07	0.07

| Num           |   Observation   |        Titre 3 |
| :------------ | :-------------: | -------------: |
| Colonne       |     Colonne     |        Colonne |
| Alignée à     |   Alignée au    |      Alignée à |
| Gauche        |     Centre      |         Droite |

### Actions
Type: Discrete(3)

Num	Action
0	push left
1	no push
2	push right