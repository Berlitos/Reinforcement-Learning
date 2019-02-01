# Reinforcement-Learning

Avancement de mes propres recherches sur le Deep Reinforcement Learning. Le but est de comprendre et de mettre en place les algorithmes avancés du domaine. J'essaierai de mettre le lien de tous les articles, papiers scientifiques et repo GIT qui me seront utils. Je vois ce projet comme un support pour mes connaissances en Deep Reinforcement Learning. Il me servira également de base pour traiter un autre projet : "Reinforcement learning with musculoskeletal models in OpenSim".

## Pré-requis

Il y a peu de bonnes vidéos de vulgarisation sur l'apprentissage par renforcement. Pour vous faire [gagner du temps](https://www.youtube.com/playlist?list=PLXO45tsB95cIplu-fLMpUEEZTwrDNh6Ba)



## Algorithmes traités

Voici les différents algorithmes que je compte étudier et implémenter :

### DONE :

* [DQN](https://github.com/Berlitos/Reinforcement-Learning/tree/master/DQN) (2013) - [Article](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf)
* [DDPG](https://github.com/Berlitos/Reinforcement-Learning/tree/master/DDPG) (2015) - [Article](https://arxiv.org/pdf/1509.02971.pdf)

### TO DO :

* [A3C](#) (2016) - [Article](https://arxiv.org/pdf/1602.01783.pdf)
* [C51](#) (2017) - [Article](https://arxiv.org/pdf/1707.06887.pdf)
* [Rainbow](#) (2017) - [Article](https://arxiv.org/pdf/1710.02298.pdf)
* [D4PG](#) (2018) - [Article](https://arxiv.org/pdf/1804.08617.pdf)


## Librairie utilisée

Pour ce projet je me suis basé sur la librairie `keras-rl` de TensorFlow. J'utiliserai leur classe `Agent` pour construire mes propres agents. Pour les tests, j'utilise les environnements proposés par OpenAI gim.

## Méthodologie

Je procède de la même manière pour tous les algorithmes :
Dans un premier temps j'étudie le papier scientifique qui le présente afin de comprendre les choix effectués. 
Pour l'implémentation je regarde ce qui a déjà été fait et l'adapte à mon code. 
Je test mon algorithme sur différents environnements et enregistre les résultats.

## Auteur
**Jean-Baptiste SIX**