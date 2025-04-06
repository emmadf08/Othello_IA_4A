
import random
from obj.pion import Pion
from obj.plateau import *
from algorithmsIA.minmax import *
from algorithmsIA.alphabeta import *
from algorithmsIA.fct_eval import *
import copy


# Pour le jeu humain vs IA, on suppose toujours que l'IA c'est le joueur blanc (couleur 0)

class Jeu:
    gagnant = None # Variable qui prends la couleur du joueur qui a gagné la partie (prends -1 si egalité)
    nb_coups = 0

    def __init__(self):
        self.plateau = Plateau()  # Créer un plateau de jeu
        self.joueur_actuel = 0  # L'IA commence avec les blancs(0)

    def changer_joueur(self):
        """Change le joueur actif (noir -> blanc et vice versa)"""
        self.joueur_actuel = 1 - self.joueur_actuel

    def jouer(self, position):
        """Joue un coup pour le joueur actuel à la position donnée"""

        if position in self.plateau.position_jouable(self.joueur_actuel):
            pion = Pion(self.joueur_actuel, position)
            self.plateau.poser(pion, position)
            self.nb_coups = self.nb_coups + 1
            self.changer_joueur()
        else:
            print("Coup invalide, choisissez une position jouable.")

    def partie_terminee(self):
        """Vérifie si la partie est terminée"""
        if not self.plateau.position_jouable(0) and not self.plateau.position_jouable(1):
            return True
        return False

    @staticmethod
    def best_move(plateau:Plateau, profondeur):
        best_score=float('-inf')
        best_move_found=None
        for move in plateau.position_jouable(0):
            new_board=copy.deepcopy(plateau)
            pion_max=Pion(0,move)
            new_board.poser(pion_max,move)
            score=min_max(new_board,profondeur,False)
            if score>best_score:
                best_score=score
                best_move_found=move

        return best_move_found

    def best_move_alpha_beta(plateau: othello.Plateau, profondeur: int, couleur: int, fct_eval):
        """
        Fonction pour trouver le meilleur coup à jouer pour l'IA (couleur 0)
        en utilisant l'algorithme Alpha-Beta .

        :param plateau: état actuel du plateau (Plateau)
        :param profondeur: profondeur maximale de recherche (int)
        :return: meilleur coup trouvé (liste [x, y])
        """

        best_score = float('-inf')
        best_move_found = None
        best_moves_random = []
        # Parcourt tous les coups possibles pour l'IA 
        for move in plateau.position_jouable(couleur):
            new_board = copy.deepcopy(plateau)
            pion_max = obj.pion.Pion(couleur, move)
            new_board.poser(pion_max, move)

            # Appel à la fonction alpha_beta
            score = alpha_beta(new_board, profondeur - 1, float('-inf'), float('inf'), False, couleur, fct_eval)

            #print(f"Test du coup {move} => score obtenu : {score}")

            

            if score > best_score:
                best_score = score
                best_moves_random = [move]
            elif score == best_score: # Pour le cas ou il y'a plusieurs mouvements avec le meme score
                best_moves_random.append(move)

       # print(f"Meilleur coup choisi par Alpha-Beta : {best_move_found} avec un score de {best_score}")
        if best_moves_random: 
            return random.choice(best_moves_random)
        else:
            return None




    def jouer_ia(self, couleur, fct_eval):
        # ICI c'est best_move_alpha_beta utilisé à modifier selon la strat choisie
        position_jouable = Jeu.best_move_alpha_beta(self.plateau, 4, couleur, fct_eval)
        #print("IA joue actuellement...")
        if position_jouable:
            self.jouer(position_jouable)
            #print("IA prend la position :", position_jouable)
        else:
            #print("IA n'a pas trouvé de positions")
            self.changer_joueur()

    # Fonction pour jouer une partie avec un humain 
    def jouer_partie(self, fct_evalIA):
        """Boucle principale du jeu"""
        while not self.partie_terminee():
            self.plateau.afficher_plateau(self.joueur_actuel)
            if self.joueur_actuel == 1:  # Joueur humain
                print(self.plateau.position_jouable(self.joueur_actuel))
                x, y = map(int, input("Choisissez une position (x y): ").split())
                self.jouer([x, y])
            else:  # IA
                self.jouer_ia(0, fct_evalIA)

        print("La partie est terminée.")
        self.plateau.afficher_plateau(-1)

    # Fonction pour jouer une partie avec 2 IA 
    # Retourne le gagnant (0,1 ou 2) valeur qui sera utilisée comme indice 
    def jouer_partieIA(self, fct_evalIA1, fct_evalIA2):
        """Fonction pour jouer une partie avec 2 IA dont choisit les fonctions d'évaluations
         et qui retourne le gagnant sous forme d'entier qui servira d'indice pour le mini-tournoi """
        while not self.partie_terminee():
            #self.plateau.afficher_plateau(self.joueur_actuel)

            # On fait jouer les 2 IAs 
            if self.joueur_actuel == 1:
                #print("IA 1")
                self.jouer_ia(1, fct_evalIA1)
            else:
                #print("IA 2")
                self.jouer_ia(0, fct_evalIA2)
        print("la partie est terminée")
        nbr_pieces = self.plateau.retourner_nbr_pieces_black_white()
        print("Voici le resultat, Noirs : ", nbr_pieces[0], "Blancs : ", nbr_pieces[1])
        # On determine ici le gagnant de la partie entre IA 1 et IA 2 pour pouvoir faire des comparatifs 
        if nbr_pieces[0] > nbr_pieces[1]:
            self.gagnant = 0
        elif nbr_pieces[0] < nbr_pieces[1]:
            self.gagnant = 1
        else: # egalite
            self.gagnant = 2

        # On retourne le gagnant entre les 2 pour pouvoir comparer 
        return self.gagnant




def main():
    jeu = Jeu()
    print("Ca commence")
    jeu.plateau.afficher_plateau(0)
    #jeu.jouer_partie()
    jeu.jouer_partieIA(positionnel, positionnel)


# Pour pouvoir importer le module sans executer tout le code
if __name__ == "__main__":
    main()


