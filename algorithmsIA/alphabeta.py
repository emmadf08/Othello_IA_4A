import copy
import os
import sys
from .fct_eval import *
import othello
import obj.pion

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

def alpha_beta(gameBoard: othello.Plateau, profondeur: int, alpha: float, beta: float, is_maximizing: bool, couleur_maximisant: int, fct_eval):
    """
    Fonction Alpha-Beta pour le jeu d'Othello.

    :param gameBoard: état actuel du plateau (Plateau)
    :param profondeur: profondeur maximale de recherche (int)
    :param alpha: meilleure valeur trouvée pour le joueur maximisant (float)
    :param beta: meilleure valeur trouvée pour le joueur minimisant (float)
    :param is_maximizing: True si le joueur courant maximise (bool)
    :return: score évalué de la position (float)
    """

    # Cas terminal : profondeur atteinte ou pas de coup disponible
    if profondeur == 0 or (not gameBoard.position_jouable(1) and not gameBoard.position_jouable(0)):
        return fct_eval(gameBoard, couleur_maximisant)  

    if is_maximizing:
        max_eval = float('-inf')

        # Parcourt les coups possibles pour le joueur maximisant (0 = Blanc)
        for move in gameBoard.position_jouable(couleur_maximisant):
            new_board = copy.deepcopy(gameBoard)
            pion_max = obj.pion.Pion(0, move)
            new_board.poser(pion_max, move)

            eval = alpha_beta(new_board, profondeur - 1, alpha, beta, False, couleur_maximisant, fct_eval)

            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)

            if beta <= alpha:
                break

        return max_eval

    else:
        min_eval = float('inf')

        # Parcourt les coups possibles pour le joueur minimisant (1 = Noir)
        for move in gameBoard.position_jouable(1 - couleur_maximisant):
            new_board = copy.deepcopy(gameBoard)
            pion_min = obj.pion.Pion(1 - couleur_maximisant, move)
            new_board.poser(pion_min, move)

            eval = alpha_beta(new_board, profondeur - 1, alpha, beta, True, couleur_maximisant, fct_eval)

            min_eval = min(min_eval, eval)
            beta = min(beta, eval)

            if beta <= alpha:
                break

        return min_eval