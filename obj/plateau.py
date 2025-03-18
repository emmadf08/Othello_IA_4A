class Plateau: 
    # -1 pour des cases vides
    # 0 pour les cases blanches
    # 1 pour les cases noires


    # We have to also keep track of the number of black and white pieces on the board
    # In that sense, it will make it easier for us to see the available spots and also count the number of them
    # So that we can display them to the screen 
    # Having this can also help us get if the game is finished or not

    HEIGHT = 8
    tableau = []

    # Be wary, here the positions are stored in the array format, so don't forget to add one to each to get the actual 
    # position on the board
    listblack = [[4,3], [3,4]]
    listwhite = [[3,3], [4,4]]
    total_pieces = 4

    def __init__(self):
        # Normally we should modify this so that it can 
        self.tableau = [[-1, -1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1, -1]]
    
    # Position is an array [x, y] with x and y being the positions of the matrix 
    def poser(self, pion, position):
        self.tableau[position[0]][position[1]] = pion.couleur

    # A function to print the state of the board 
    def afficher_plateau(self):
        for i in range(self.HEIGHT + 1):
            for j in range(self.HEIGHT + 1):
                print(self.tableau[i][j], " - ")
            print("\n")
            print("----------------------------------")

    # A function that returns a list of available moves for a certain player
    #(The empty squares that a user can choose from and the AI also)
    # couleur is either 0 or 1
    def position_jouable(self, couleur):
        worklist = [] # the list of pieces on the board for a specific color
        if couleur == 1:
            worklist = self.listblack
        else:
            worklist = self.listwhite
        
        # Now we selected the working list based on our color code
        # We iterate throught each position in this list
        # We see the 6 pieces surronding it

    # A function that returns true or false to see if the game is over 
    # Useful for our minmax algorithm
    def is_game_finished():
        return True