class Plateau:
    HEIGHT = 8  # Taille du plateau de Othello (8x8)
    tableau = [] # Tableau sur lequel on pose et qui contient les pieces 
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
        """Affiche le plateau avec N pour noirs, B pour blancs, et . pour les cases vides"""
        print("  ", end="")
        for i in range(self.HEIGHT):
            print(i, end=" ")
        print()

        for i in range(self.HEIGHT):
            print(i, end=" ")  # Affichage de l'indice de ligne
            for j in range(self.HEIGHT):
                if self.tableau[i][j] == 1:
                    print("N", end=" ")
                elif self.tableau[i][j] == 0:
                    print("B", end=" ")
                elif [i, j] in self.position_jouable(couleur):
                    print("?", end=" ")
                else:
                    print(".", end=" ")
            print()
        print("------------------")
        print("nombre de coups :" + str(self.nb_coups))
        print()




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
    

    def retourner_nbr_pieces_black_white(self):
        compteBlack = 0
        compteWhite = 0
        for i in range(8):
            for j in range(8):
                if self.tableau[i][j] == 1:
                    compteBlack = compteBlack + 1 
                elif self.tableau[i][j] == 0:
                    compteWhite = compteWhite + 1
        return [compteBlack, compteWhite]
                


