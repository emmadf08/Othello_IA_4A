# On veut faire jouer l'IA contre elle meme
# Le but est de pouvoir comparer les différentes stratégies utilisées pour savoir laquelle est la meilleur 

# Dans ce contexte là, on va faire jouer sur 10 matches chaque IA avec une stratégie différente 

#from Othello_IA_4A.algorithmsIA.fct_eval import *
#from Othello_IA_4A.othello import Jeu

import sys
import os

# Add the root project folder (Othello_IA_4A's parent) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from algorithmsIA.fct_eval import *
from othello import Jeu



# On aura 3 matches 
# Positionnel vs absolu (match 1)
# Positionnel vs mobilite (match 2)
# mobilite vs absolu (match 3)


# Pour chaque match 
nbr_victoires_1 = [0, 0, 0] # Chaque case correspond à un joueur (0 et 1) et la derniere c'est pour les égalités 
nbr_victoires_2 = [0, 0, 0]
nbr_victoires_3 = [0, 0, 0]

nbr_victoires_4 = [0, 0, 0]
nbr_victoires_5 = [0, 0, 0]
nbr_victoires_6 = [0, 0, 0]



for i in range(30):

    # jeu1 = Jeu()
    # jeu2 = Jeu()
    # jeu3 = Jeu()
    
   
    jeu4 = Jeu()
    jeu5 = Jeu()
    jeu6 = Jeu()
    
    res4 = jeu4.jouer_partieIA(mixte, positionnel)
    res5 = jeu5.jouer_partieIA(mixte, absolu)
    res6 = jeu6.jouer_partieIA(mixte, mobilite)

    nbr_victoires_4[res4] = nbr_victoires_4[res4] + 1
    nbr_victoires_5[res5] = nbr_victoires_5[res5] + 1
    nbr_victoires_6[res6] = nbr_victoires_6[res6] + 1

    # res1 = jeu1.jouer_partieIA(absolu, positionnel)
    # res2 = jeu2.jouer_partieIA(positionnel, mobilite)
    # res3 = jeu3.jouer_partieIA(mobilite, absolu)

    # On attribue les résultats 
    # resX c'est le resultat du match (victoire pour joueur 0 ou 1 ou egalité)
    # nbr_victoires_1[res1] = nbr_victoires_1[res1] + 1
    # nbr_victoires_2[res2] = nbr_victoires_2[res2] + 1
    # nbr_victoires_3[res3] = nbr_victoires_3[res3] + 1


# print("Resultats du match 1 : ", nbr_victoires_1)
# print("Resultats du match 2 : ", nbr_victoires_2)
# print("Resultats du match 3 : ", nbr_victoires_3)


print("Resultat du match 4 (mixte vs positionnel) : ", nbr_victoires_4)
print("Resultat du match 5 (mixte vs absolu) : ", nbr_victoires_5)
print("Resultat du match 6 (mixte vs mobilite) : ", nbr_victoires_6)


