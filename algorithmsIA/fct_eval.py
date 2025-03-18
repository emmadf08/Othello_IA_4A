# Ce fichier contient les différentes fct d'évaluations (ou stratégies) qu'on utilise pour notre algorithme IA
# pour choisir la meilleure position

# Chaque fct ici prend une position et une seule position pour un joueur et lui attribue un score

# 0 pour les blancs
# 1 pour les noirs 

#On garde toujours cette heuristique
# Noir - Blanc 


# Assigne un score selon le tableau des positions vu en cours
# N-B: IL FAUT CONVERTIR LA POSITION EN TUPLE AVANT DE L'UTILISER POUR CETTE FCT

# On calcule la difference de poids entre la position des noirs et celle des blancs
def positionnel(game_board):
    # La grille des poids des positions 
    grid = {
        (0, 0): 500,  (0, 1): -150, (0, 2): 30,  (0, 3): 10,  (0, 4): 10,  (0, 5): 30,  (0, 6): -150, (0, 7): 500,
        (1, 0): -150, (1, 1): -250, (1, 2): 0,   (1, 3): 0,   (1, 4): 0,   (1, 5): 0,   (1, 6): -250, (1, 7): -150,
        (2, 0): 30,   (2, 1): 0,    (2, 2): 1,   (2, 3): 2,   (2, 4): 2,   (2, 5): 1,   (2, 6): 0,    (2, 7): 30,
        (3, 0): 10,   (3, 1): 0,    (3, 2): 2,   (3, 3): 16,  (3, 4): 16,  (3, 5): 2,   (3, 6): 0,    (3, 7): 10,
        (4, 0): 10,   (4, 1): 0,    (4, 2): 2,   (4, 3): 16,  (4, 4): 16,  (4, 5): 2,   (4, 6): 0,    (4, 7): 10,
        (5, 0): 30,   (5, 1): 0,    (5, 2): 1,   (5, 3): 2,   (5, 4): 2,   (5, 5): 1,   (5, 6): 0,    (5, 7): 30,
        (6, 0): -150, (6, 1): -250, (6, 2): 0,   (6, 3): 0,   (6, 4): 0,   (6, 5): 0,   (6, 6): -250, (6, 7): -150,
        (7, 0): 500,  (7, 1): -150, (7, 2): 30,  (7, 3): 10,  (7, 4): 10,  (7, 5): 30,  (7, 6): -150, (7, 7): 500,
    }

    # Récupérer les positions sur le plateau pour chaque joueur
    positions_noirs = game_board.position_jouable(1)
    positions_blancs = game_board.position_jouable(0)

    total_poids_noirs = sum(grid[tuple(position)] for position in positions_noirs)
    total_poids_blancs = sum(grid[tuple(position)] for position in positions_blancs)

    # Le score est la différence des sommes des poids des pions noirs et blancs
    score_posi = total_poids_noirs - total_poids_blancs

    return score_posi





# Prend en compte la difference du nombre de pions entre chaque joueur
# La différence dans notre cas est le nbr de pions noir - blanc
# Donc plus cette différence est croissante dans le sens positif, plus le mouvement est meilleur pour l'adversaire (pas IA)
def absolu(game_board):
    
    score_abs = len(game_board.listblack) - len(game_board.listwhite)
    return score_abs






# Maximise le nombre de mouvements pour le joueur tout en minimisant les coups de l'adversaire, tout en essayant de prendre les coins
# Concretement, on essaie de regarder la taille du tableau des positions jouables et on regarde les différents 
# résultat pour chaque mouvement

# Retourne le nbr de positions jouables pour les 2 joueurs 
# Si jamais y'a un corner dans les positions qu'on peut jouer on l'indique

# retourne un tableau [nbr_position_noir, nbr_position_blanc, isCorner] avec isCorner un boolean pour savoir si y'a un corner
# Dans les positions à joueur

def mobilite(game_board, couleur_joueur):

    
    positions_joueur = game_board.position_jouable(couleur_joueur) 
    positions_adversaire = game_board.position_jouable(1 - couleur_joueur)
    isCorner = False

    # On verifie l'existence de coins dans les positions jouables
    for e in positions_joueur:
        if e == [0,0] or e == [7,0] or e == [0,7] or e == [7,7]:
            isCorner = True
    
    score_mobilite = [len(positions_joueur), len(positions_adversaire), isCorner]

    return score_mobilite