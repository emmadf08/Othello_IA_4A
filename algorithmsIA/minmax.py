# In order for the minmax algorithm to work, we have to give it as a parameter
# The available moves we can play so it can consider them (and also the function that returns the available moves)
# This function is supposed to return the best move that the AI player can do given a game board
import copy
import os
import sys
from .fct_eval import *
import othello
from obj.pion import *

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
# On va aussi définir une profondeur maximale standard de 6 (qu'on peut ensuite modifier selon les phases de jeu)
# A changer
def min_max(gameBoard:othello.Plateau, profondeur, is_maximizing):
    """
    Fonction Min-Max pour le jeu d'Othello.

    :param gameBoard: état actuel du plateau (grille)
    :param Profondeur: profondeur maximale de recherche
    :param is_maximizing: booléen, True si le joueur courant maximise
    :return: score évalué de la position
    """
    if (profondeur == 0 or (not gameBoard.position_jouable(1) and not gameBoard.position_jouable(0))):
        return positionnel(gameBoard)
    if is_maximizing:
        max_eval = float('-inf')
        for move in gameBoard.position_jouable(0):  # 'Max' correspond à la couleur 0 (blanc)
            new_board = copy.deepcopy(gameBoard)
            pion_max = Pion(0,move) # Crée un objet pion pour le joueur Max (blanc)
            new_board.poser(pion_max, move)  # Applique le coup
            eval = min_max(new_board, profondeur - 1, False)
            max_eval = max(max_eval, eval)
        #print("jexectue minmax")
        return max_eval
    else:
        min_eval = float('inf')
        for move in gameBoard.position_jouable(1):  # 'Min' correspond à la couleur 1 (noir)
            new_board = copy.deepcopy(gameBoard)
            pion_min = Pion(1,move)  # Crée un objet pion pour le joueur Min (noir)
            new_board.poser(pion_min, move)  # Applique le coup
            eval = min_max(new_board, profondeur - 1, True)
            min_eval = min(min_eval, eval)
        #print("jexectue minmax")
        return min_eval
