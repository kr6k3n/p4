import random as rnd


def grille_vide():
    return [[0]*7 for l in range(6)]

def affiche(g):
    for l in range(5,-1,-1):
        for c in range(0,7):
            if g[l][c ] == 0:
                print('_', end = ' | ')
            elif g[l][c] == 1:
                print('O', end = ' | ')
            else :
                print('X', end = ' | ')
        print(' ')
    print(' ')

def coup_possible(g,c):
    return not (g[5][c] != 0)
    
def jouer(g,j,c):
    l = 0;
    while g[l][c] != 0:
        l = l+1
    g[l][c] = j

def horiz(g,j,l,c):
    for i in range(4):
        if g[l][c+i] != j:
            return False
    return True

def vert(g,j,l,c):
    for i in range(4):
        if g[l+i][c] != j :
            return False
    return True

def diag1(g,j,l,c):
    for i in range(4):
        if g[l+i][c+i] != j:
            return False
    return True

def diag2(g,j,l,c):
    for i in range(4):
        if g[l+i][c-i] !=j:
            return False
    return True

def victoire(g,j):
    for l in range(6):
        for c in range(7):
            if c<4 and horiz(g,j,l,c) :
                return True
            if l<3 and vert(g,j,l,c):
                return True
            if c<4 and l<3 and diag1(g,j,l,c) :
                return True
            if l<3 and c>2 and diag2(g,j,l,c):
                return True
    return False

def match_nul(g):
    for i in range(7):
        if g[5][i] == 0:
            return False
    return True

def coup_aleatoire(g,j):
    while True :
        c = rnd.randint(0,6)
        if coup_possible(g,c):
            jouer(g,j,c)
            return


def coup_utilisateur(g,j):
    while True :
        c = int(input("Entre le numéro de la colonne, entre 0 et 6: "))
        if coup_possible(g,c):
            jouer(g,j,c)
            return
        else:
            print("Non, ce n'est pas possible.")


def partie_aleatoire():
    g = grille_vide()
    
    for i in range(3):
        for j in range(1,3):
            coup_aleatoire(g,j)
            affiche(g)
            
    while match_nul(g) == False :
        coup_aleatoire(g,1)
        affiche(g)
        if victoire(g,1) :
            print("Le joueur 1 a gagné")
            break
        coup_aleatoire(g,2)
        affiche(g)
        if victoire(g,2):
            print("Le joueur 2 a gagné")
            break  

def partie_contre_ordi():
    g = grille_vide()
    affiche(g)
    
    while match_nul(g) == False :
        coup_aleatoire(g,1)
        affiche(g)
        if victoire(g,1) :
            print("L'ordinateur a gagné")
            break
        coup_utilisateur(g,2)
        affiche(g)
        if victoire(g,2):
            print("Bravo, tu as gagné")
            break  

