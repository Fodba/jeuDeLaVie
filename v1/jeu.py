import tkinter as tk
import numpy as np
import time

# CONSTANTES
HEIGHT = 1000
WIDTH = 1000
NB_CELLULES_X = 25
NB_CELLULES_Y = 25
TAILLE_X = WIDTH / NB_CELLULES_X
TAILLE_Y = HEIGHT / NB_CELLULES_Y
VITESSE = 250

# VARIABLES GLOBALES
flag = 0
compteur_generation = 0
compteur_population = 0


# FONCTIONS
def colorie(tableau, canevas):
    '''
    Affiche une case blanche ou noir selon que la cellule soit vivante ou morte
    :param tableau: tableau des cellules vivantes
    :return:
    '''
    h = 0
    for ind, row in enumerate(tableau):
        l = 0
        for idx, c in enumerate(row):
            if c == 1:
                X = TAILLE_X * idx
                Y = TAILLE_Y * ind
                canevas.create_rectangle(X, Y, X + TAILLE_X, Y + TAILLE_Y, fill='black')
    canevas.pack()


def ligne_vertical(canevas):
    '''
    Crée les lignes verticales
    :return: None
    '''
    c_x = 0
    while c_x < WIDTH:
        canevas.create_line(c_x, 0, c_x, HEIGHT, fill='black')
        c_x += TAILLE_X


def ligne_horizontal(canevas):
    '''
    Crée les lignes verticales
    :return: None
    '''
    c_y = 0
    while c_y < HEIGHT:
        canevas.create_line(0, c_y, WIDTH, c_y, fill='black')
        c_y += TAILLE_Y


def damier(canevas):
    '''
    dessine un damier dans la surface
    :return:
    '''
    canevas.delete(tk.ALL)
    ligne_horizontal(canevas)
    ligne_vertical(canevas)
    canevas.pack()


def click_gauche(event):  # fonction rendant vivante la cellule cliquée
    global canevas1, tableau, compteur_population
    x = event.x - (event.x % TAILLE_X)
    y = event.y - (event.y % TAILLE_Y)
    X = int(event.x / TAILLE_X)
    Y = int(event.y / TAILLE_Y)
    canevas1.create_rectangle(x, y, x + TAILLE_X, y + TAILLE_Y, fill='black')
    tableau[Y, X] = 1
    print(X, ' - ', Y)
    compteur_population = np.sum(tableau)
    chaine2.configure(text="Population: {}".format(compteur_population))


def click_droit(event):  # fonction rendant vivante la cellule cliquée
    global canevas1, tableau, compteur_population
    x = event.x - (event.x % TAILLE_X)
    y = event.y - (event.y % TAILLE_Y)
    X = int(event.x / TAILLE_X)
    Y = int(event.y / TAILLE_Y)
    canevas1.create_rectangle(x, y, x + TAILLE_X, y + TAILLE_Y, fill='white')
    tableau[Y, X] = 0
    print(X, ' - ', Y)
    compteur_population = np.sum(tableau)
    chaine2.configure(text="Population: {}".format(compteur_population))


def get_voisins(tableau):
    '''
    definit le nombre de voisins immediat pour chaque cellule du tableau
    :param tableau: tableau à analyser
    :return:
    '''
    tab_voisin = np.zeros((NB_CELLULES_X, NB_CELLULES_Y))
    for idx, row in enumerate(tableau):  # idx = axe y
        for index, cell in enumerate(row):  # index = axe x

            # CAS PARTICULIER
            # Les Coins
            if idx == 0 and index == 0:
                if tableau[idx + 1, index] == 1:
                    tab_voisin[idx, index] += 1

                if tableau[idx + 1, index + 1] == 1:
                    tab_voisin[idx, index] += 1

                if tableau[idx, index + 1] == 1:
                    tab_voisin[idx, index] += 1

            elif idx == NB_CELLULES_Y - 1 and index == 0:
                if tableau[idx - 1, index] == 1:
                    tab_voisin[idx, index] += 1

                if tableau[idx - 1, index + 1] == 1:
                    tab_voisin[idx, index] += 1

                if tableau[idx, index + 1] == 1:
                    tab_voisin[idx, index] += 1

            elif index == NB_CELLULES_X - 1 and idx == 0:
                if tableau[idx, index - 1] == 1:
                    tab_voisin[idx, index] += 1

                if tableau[idx + 1, index - 1] == 1:
                    tab_voisin[idx, index] += 1

                if tableau[idx + 1, index] == 1:
                    tab_voisin[idx, index] += 1

            elif index == NB_CELLULES_X - 1 and idx == NB_CELLULES_Y - 1:
                if tableau[idx - 1, index - 1] == 1:
                    tab_voisin[idx, index] += 1

                if tableau[idx - 1, index] == 1:
                    tab_voisin[idx, index] += 1

                if tableau[idx, index - 1] == 1:
                    tab_voisin[idx, index] += 1

            # Les bordures
            elif index == 0:
                if tableau[idx - 1, index] == 1:
                    tab_voisin[idx, index] += 1
                if tableau[idx + 1, index] == 1:
                    tab_voisin[idx, index] += 1
                if tableau[idx - 1, index + 1] == 1:
                    tab_voisin[idx, index] += 1
                if tableau[idx, index + 1] == 1:
                    tab_voisin[idx, index] += 1
                if tableau[idx + 1, index + 1] == 1:
                    tab_voisin[idx, index] += 1

            elif index == NB_CELLULES_X - 1:
                if tableau[idx - 1, index - 1] == 1:
                    tab_voisin[idx, index] += 1
                if tableau[idx, index - 1] == 1:
                    tab_voisin[idx, index] += 1
                if tableau[idx + 1, index - 1] == 1:
                    tab_voisin[idx, index] += 1

                if tableau[idx - 1, index] == 1:
                    tab_voisin[idx, index] += 1
                if tableau[idx + 1, index] == 1:
                    tab_voisin[idx, index] += 1

            elif idx == 0:
                if tableau[idx, index - 1] == 1:
                    tab_voisin[idx, index] += 1
                if tableau[idx, index + 1] == 1:
                    tab_voisin[idx, index] += 1

                if tableau[idx + 1, index - 1] == 1:
                    tab_voisin[idx, index] += 1
                if tableau[idx + 1, index] == 1:
                    tab_voisin[idx, index] += 1
                if tableau[idx + 1, index + 1] == 1:
                    tab_voisin[idx, index] += 1

            elif idx == NB_CELLULES_Y - 1:
                if tableau[idx, index - 1] == 1:
                    tab_voisin[idx, index] += 1
                if tableau[idx, index + 1] == 1:
                    tab_voisin[idx, index] += 1

                if tableau[idx - 1, index - 1] == 1:
                    tab_voisin[idx, index] += 1
                if tableau[idx - 1, index] == 1:
                    tab_voisin[idx, index] += 1
                if tableau[idx - 1, index + 1] == 1:
                    tab_voisin[idx, index] += 1

            else:
                if tableau[idx - 1, index - 1] == 1:
                    tab_voisin[idx, index] += 1
                if tableau[idx - 1, index] == 1:
                    tab_voisin[idx, index] += 1
                if tableau[idx - 1, index + 1] == 1:
                    tab_voisin[idx, index] += 1

                if tableau[idx, index - 1] == 1:
                    tab_voisin[idx, index] += 1
                if tableau[idx, index + 1] == 1:
                    tab_voisin[idx, index] += 1

                if tableau[idx + 1, index - 1] == 1:
                    tab_voisin[idx, index] += 1
                if tableau[idx + 1, index] == 1:
                    tab_voisin[idx, index] += 1
                if tableau[idx + 1, index + 1] == 1:
                    tab_voisin[idx, index] += 1

    tab = tab_voisin
    # print(tab_voisin)
    return tab


def get_new_positions(tableau, voisins):
    '''
    Obtient les nouvelles positions de cellules à partir du nombre de voisins
    :param tableau: tableau à analyser
    :return:
    '''
    global compteur_population
    tab = np.zeros((NB_CELLULES_X, NB_CELLULES_Y))
    for idx, row in enumerate(voisins):
        for index, cell in enumerate(row):
            if cell == 2:
                if (tableau[idx, index] == 1):
                    tab[idx, index] = 1
            elif cell == 3:
                tab[idx, index] = 1
    # print(tab)
    compteur_population = np.sum(tab)
    return tab


def go():
    "demarrage de l'animation"
    global flag, compteur_generation
    if flag == 0:
        flag = 1
        play()


def stop():
    "arret de l'animation"
    global flag
    flag = 0


def remise_a_zero():
    global tableau, canevas1, flag, compteur_generation, compteur_population
    compteur_generation = 0
    flag = 0
    tableau = np.random.randint(0, 1, size=(NB_CELLULES_X, NB_CELLULES_Y))
    compteur_population = np.sum(tableau)
    damier(canevas1)
    colorie(tableau, canevas1)
    chaine1.configure(text="Génération: {}".format(compteur_generation))
    chaine2.configure(text="Population: {}".format(compteur_population))
    # chaine.pack(side=tk.RIGHT)


def aleatoire():
    global tableau, canevas1, flag, compteur_generation, compteur_population
    flag = 0
    stop()
    remise_a_zero()
    tableau = np.random.randint(0, 2, size=(NB_CELLULES_X, NB_CELLULES_Y))
    compteur_population = np.sum(tableau)
    damier(canevas1)
    colorie(tableau,canevas1)
    chaine1.configure(text="Génération: {}".format(compteur_generation))
    chaine2.configure(text="Population: {}".format(compteur_population))
    #play()



def play():
    global flag, tableau, compteur_generation
    colorie(tableau, canevas1)
    damier(canevas1)

    total = np.sum(tableau)
    tab = get_voisins(tableau)
    tableau = get_new_positions(tableau, tab)
    damier(canevas1)
    colorie(tableau, canevas1)

    if flag > 0:
        compteur_generation += 1
        chaine1.configure(text="Génération: {}".format(compteur_generation))
        chaine2.configure(text="Population: {}".format(compteur_population))
        fenetre1.after(VITESSE, play)


fenetre1 = tk.Tk()
canevas1 = tk.Canvas(fenetre1, width=WIDTH, height=HEIGHT, bg='white')

canevas1.bind("<Button-1>", click_gauche)
canevas1.bind("<Button-3>", click_droit)

damier(canevas1)

tableau = np.random.randint(0, 1, size=(NB_CELLULES_X, NB_CELLULES_Y))
colorie(tableau, canevas1)


b1 = tk.Button(fenetre1, text='PLAY!', command=go)
b1.pack(side=tk.LEFT, padx=3, pady=3)
b2 = tk.Button(fenetre1, text='STOP!', command=stop)
b2.pack(side=tk.LEFT, padx=3, pady=3)
b3 = tk.Button(fenetre1, text='remise à 0!', command=remise_a_zero)
b3.pack(side=tk.LEFT, padx=3, pady=3)
b3 = tk.Button(fenetre1, text='Aléatoire', command=aleatoire)
b3.pack(side=tk.LEFT, padx=3, pady=3)

chaine1 = tk.Label(fenetre1)
chaine1.configure(text="Génération: {}".format(compteur_generation))
chaine1.pack(side=tk.RIGHT)
chaine2 = tk.Label(fenetre1)
chaine2.configure(text="Population: {}".format(compteur_population))
chaine2.pack(side=tk.RIGHT)

fenetre1.mainloop()
