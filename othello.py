
from obj.pion import Pion
from algorithmsIA.minmax import *
from algorithmsIA.alphabeta import *
from algorithmsIA.fct_eval import *
import copy

class Plateau:
    HEIGHT = 8  # Taille du plateau de Othello (8x8)
    tableau = []
    listblack = [[3, 4], [4, 3]]
    listwhite = [[3, 3], [4, 4]]
    total_pieces = 4
    nb_coups= 0



    def __init__(self):
        # Création du plateau 8x8 initialisé avec -1 pour les cases vides
        self.tableau = [[-1 for _ in range(self.HEIGHT)] for _ in range(self.HEIGHT)]
        # Initialisation de la position de départ
        self.tableau[3][3], self.tableau[4][4] = 0, 0  # Pions blancs au début
        self.tableau[3][4], self.tableau[4][3] = 1, 1  # Pions noirs au début

    def poser(self, pion, position):
        """Place un pion sur le plateau et capture les pions adverses"""
        # Vérifier que la position est vide avant de poser un pion
        if self.tableau[position[0]][position[1]] == -1:  # Case vide
            self.tableau[position[0]][position[1]] = pion.couleur  # Placer le pion
            self.capturer_pions(pion.couleur, position)  # Capturer les pions adverses
            self.nb_coups+= 1  # Mettre à jour le nombre de coups
        else:
            print("La case est déjà occupée, choix invalide.")  # Gérer une position déjà occupée


    def capturer_pions(self, couleur, position):
        """Capture les pions adverses en fonction du coup posé"""
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        adversaire = 1 - couleur  # Couleur de l'adversaire

        # Pour chaque direction, vérifier s'il y a des pions adverses à capturer
        for d in directions:
            x, y = position[0], position[1]
            pions_a_retourner = []
            # Avancer dans la direction donnée tant qu'on rencontre des pions adverses
            while True:
                x, y = x + d[0], y + d[1]
                if not (0 <= x < self.HEIGHT and 0 <= y < self.HEIGHT):  # Sortie de la grille
                    break
                if self.tableau[x][y] == adversaire:
                    pions_a_retourner.append([x, y])
                elif self.tableau[x][y] == couleur:
                    # Si un pion de la même couleur est trouvé, on capture les pions entre
                    if pions_a_retourner:  # Vérifier si des pions ont été trouvés avant
                        for px, py in pions_a_retourner:
                            self.tableau[px][py] = couleur
                    break
                else:
                    break


    def afficher_plateau(self, couleur):
        """Affiche le plateau avec X pour noirs, O pour blancs, et . pour les cases vides"""
        print("  ", end="")
        for i in range(self.HEIGHT):
            print(i, end=" ")
        print()

        for i in range(self.HEIGHT):
            print(i, end=" ")  # Affichage de l'indice de ligne
            for j in range(self.HEIGHT):
                if self.tableau[i][j] == 1:
                    print("X", end=" ")
                elif self.tableau[i][j] == 0:
                    print("O", end=" ")
                elif [i, j] in self.position_jouable(couleur):
                    print("?", end=" ")
                else:
                    print(".", end=" ")
            print()
        print("------------------")
        print("nombre de coups :" + str(self.nb_coups))
        print()


# Tu peux stp ajouter le nbr de coup aussi, pour pouvoir implementer la heuristique mixte
# car apres un nbr de coup on change la fonction d evaluation
# T'as capté hh ?

# Si jamais tu parles je t'entends pas mdr,

    def position_jouable(self, couleur):
        """Retourne une liste des positions jouables pour le joueur donné"""
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        positions = []
        adversaire = 1 - couleur  # Couleur de l'adversaire

        # Parcourir toutes les cases vides
        for x in range(self.HEIGHT):
            for y in range(self.HEIGHT):
                if self.tableau[x][y] == -1:  # Si la case est vide
                    for d in directions:
                        pions_a_retourner = []
                        i, j = x, y
                        # Avancer dans chaque direction pour vérifier si une capture est possible
                        while True:
                            i, j = i + d[0], j + d[1]
                            if not (0 <= i < self.HEIGHT and 0 <= j < self.HEIGHT):
                                break
                            if self.tableau[i][j] == adversaire:  # Si on rencontre un pion adverse
                                pions_a_retourner.append([i, j])
                            elif self.tableau[i][j] == couleur:  # Si on rencontre un pion de la même couleur
                                if pions_a_retourner:  # Il doit y avoir des pions à retourner
                                    positions.append([x, y])  # Ajouter la position comme jouable
                                break
                            else:
                                break
        return positions




class Jeu:
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

    def best_move_alpha_beta(plateau: othello.Plateau, profondeur: int):
        """
        Fonction pour trouver le meilleur coup à jouer pour l'IA (couleur 0)
        en utilisant l'algorithme Alpha-Beta .

        :param plateau: état actuel du plateau (Plateau)
        :param profondeur: profondeur maximale de recherche (int)
        :return: meilleur coup trouvé (liste [x, y])
        """

        best_score = float('-inf')
        best_move_found = None

        # Parcourt tous les coups possibles pour l'IA (joueur 0)
        for move in plateau.position_jouable(0):
            new_board = copy.deepcopy(plateau)
            pion_max = obj.pion.Pion(0, move)
            new_board.poser(pion_max, move)

            # Appel à la fonction alpha_beta
            score = alpha_beta(new_board, profondeur - 1, float('-inf'), float('inf'), False)

            print(f"Test du coup {move} => score obtenu : {score}")

            if score > best_score:
                best_score = score
                best_move_found = move

        print(f"Meilleur coup choisi par Alpha-Beta : {best_move_found} avec un score de {best_score}")

        return best_move_found




    def jouer_ia(self):
        # ICI c'est best_move_alpha_beta utilisé à modifier selon la strat choisie
        position_jouable = Jeu.best_move_alpha_beta(self.plateau, 4)
        print("IA joue actuellement...")
        if position_jouable:
            self.jouer(position_jouable)
            print("IA prend la position :", position_jouable)
        else:
            print("IA n'a pas trouvé de positions")
            self.changer_joueur()

    def jouer_partie(self):
        """Boucle principale du jeu"""
        while not self.partie_terminee():
            self.plateau.afficher_plateau(self.joueur_actuel)
            if self.joueur_actuel == 1:  # Joueur humain
                print(self.plateau.position_jouable(self.joueur_actuel))
                x, y = map(int, input("Choisissez une position (x y): ").split())
                self.jouer([x, y])
            else:  # IA
                self.jouer_ia()

        print("La partie est terminée.")
        self.plateau.afficher_plateau(-1)

def main():
    jeu = Jeu()
    print("Ca commence")
    jeu.plateau.afficher_plateau(0)
    jeu.jouer_partie()


# Pour pouvoir importer le module sans executer tout le code
if __name__ == "__main__":
    main()


