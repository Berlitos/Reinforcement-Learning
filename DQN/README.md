# DQN

## Explication

* Q-Learning mais avec un réseau neuronal profond comme approximateur de fonction.
* L'utilisation d'un réseau neuronal profond non linéaire est puissante, mais l'entraînement est instable si on l'applique naïvement.

Solution :

1. **Experience Replay** : On stock l'expérience (S, A, R, S_next) dans une mémoire tampon de relecture et on échantillone des minibatchs pour entaîner le réseau. Cela permet de décoreller les données et d'en améliorer l'efficacité. Au début, le tampon de relecture est rempli d'expériences aléatoires.

2. **Target Network** : On utilise un réseau distinct pour estimer la TD cible (Temporal Difference). Ce réseau cible a la même architecture que l'approximateur de fonctions mais avec des paramètres figés. A chaque pas T (un hyperparamètre) les paramètres du réseau Q sont copiés sur le réseau cible. Cela conduit à un entraînement plus stable parce qu'il maintient la fonction cible fixe (pendant un certain temps).
