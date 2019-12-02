import numpy as np

def pt(texte=""):
    '''
    Parce que j'ai la flemme d'écrire "print"'
    :param texte: texte à afficher
    :return:
    '''
    print(texte)

# Création de tableaux
tableau = np.array([1,5,8,63,7,4], dtype='float32')
pt("tableau")
pt(tableau)
pt()

# tableau de tuples aléatoires
tableau_tuple = np.array([np.random.randint(0,100,2) for i in range(5)])
pt("tableau de tuples")
pt(tableau_tuple)
pt()

# tableau à plusieurs dimensions
tableau_2d = np.random.randint(0,100, size=(8,6))
pt("tableau à 2 dimensions")
pt(tableau_2d)
pt()

tableau_3d = np.random.randint(0,100, size=(5,4,7))
pt("tableau à 3 dimensions")
pt(tableau_3d)
pt()

# Opérations sur les tableaux
pt("tableau à 2 dimensions")
pt(tableau_2d)
pt()
pt("tableaux 2d triés")
tableau_trie1 = np.sort(tableau_2d)
pt(tableau_trie1)
pt()
tableau_trie2 = np.sort(tableau_3d[0][1])
pt(tableau_trie2)
pt()


# Afficher des elements du tableeau

pt("quelques element du tableau à 3 dimensions")
pt(tableau_3d[:2][:2][:2])
pt()

pt("tableau 2d")
pt(tableau_2d)
pt()
pt("élément de tableau 2d")
pt(tableau_2d[0:4,1:5])
pt()



