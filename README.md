# Othello AI Project

## Description

Ce projet vise à développer une IA pour jouer au jeu d'Othello contre un joueur humain ou une autre IA. L'IA utilise des **algorithmes de recherche** (Minimax, NegaMax) et différentes **stratégies d'évaluation** pour déterminer les meilleurs coups à jouer. Le projet inclut aussi un mini-tournoi pour tester et comparer différentes stratégies d'évaluation.

## Algorithmes et Stratégies

### 1. Algorithmes de recherche
- **Minimax** : Recherche de l’arbre de jeu sans optimisation.
- **NegaMax** : Variante de Minimax simplifiée, plus facile à implémenter.
- **Élagage Alpha-Bêta** : Optimisation des algorithmes Minimax et NegaMax pour réduire le temps de calcul.

### 2. Stratégies d'évaluation
- **Mobilité** : Évalue la capacité de l'IA à avoir un grand nombre de coups disponibles.
- **Différence de score** : Évalue la différence entre le nombre de pions du joueur et de l’adversaire.
- **Heuristique positionnelle** : Utilisation d’une grille pondérée pour évaluer l’importance des positions sur le plateau.

## Validation et Résultats

### Critères d'évaluation
- **Temps de calcul** : Mesuré pour chaque coup joué.
- **Taux de victoire** : Nombre de victoires et de défaites pour chaque stratégie d'évaluation.

### Mini-Tournoi
Nous avons effectué un tournoi de **30 matchs** entre différentes stratégies d’évaluation, avec les résultats suivants :

1. **Absolu vs Positionnel**  
   19 victoires pour Absolu, 9 victoires pour Positionnel, 2 égalités.
   
2. **Positionnel vs Mobilité**  
   12 victoires pour Positionnel, 18 victoires pour Mobilité.
   
3. **Mobilité vs Absolu**  
   23 victoires pour Mobilité, 7 victoires pour Absolu.

En conclusion, l'IA utilisant la stratégie **Mobilité** a montré les meilleures performances.

## Fonctionnalités

- **Jeu contre une IA** : Le joueur humain peut affronter une IA avec des stratégies d’évaluation variées.
- **Mode tournoi** : Teste différentes stratégies d’IA dans un mini-tournoi pour analyser les performances.
- **Algorithmes optimisés** : Utilisation de NegaMax avec élagage alpha-bêta pour améliorer les performances.


