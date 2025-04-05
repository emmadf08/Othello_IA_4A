import copy
from .fct_eval import *
from othello import *
from obj.pion import *

def negamax(gameBoard: othello.Plateau, profondeur, couleur, alpha=float('-inf'), beta=float('inf')):
    """
    Implémentation de l'algorithme NegaMax avec élagage Alpha-Beta.

    :param gameBoard: état actuel du plateau
    :param profondeur: profondeur maximale de recherche
    :param couleur: couleur du joueur actuel (0 pour blanc, 1 pour noir)
    :param alpha: valeur alpha pour l'élagage alpha-beta
    :param beta: valeur beta pour l'élagage alpha-beta
    :return: score évalué de la position
    """
    if profondeur == 0 or (not gameBoard.position_jouable(0) and not gameBoard.position_jouable(1)):
        return positionnel(gameBoard) * (1 if couleur == 0 else -1)

    max_eval = float('-inf')
    for move in gameBoard.position_jouable(couleur):
        new_board = copy.deepcopy(gameBoard)
        pion = Pion(couleur, move)
        new_board.poser(pion, move)

        eval = -negamax(new_board, profondeur - 1, 1 - couleur, -beta, -alpha)
        max_eval = max(max_eval, eval)
        alpha = max(alpha, eval)

        if alpha >= beta:
            break  # Coupure beta

    return max_eval