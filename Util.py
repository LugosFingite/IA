import random
import time


# Création d'une instance de la classe Random, ayant pour seed le nombre de secondes écoulées depuis... le 1er Janvier 1970 !
rand = random.Random(x = time.time())


# Création d'une fonction prenant pour argument une ligne de texte et un caractère | un mot,
# et renvoyant une liste contenant chaque partie de la ligne de texte qui se trouve entre deux séparateurs.
def separate(separating : str, separator : str):
    # Séparation | création de la liste
    sep = separating.split(separator)
    separated = []

    # Manipulations pour insérer le séparateur entre chaque partie de la liste.
    for s in range(len(sep) - 1):
        separated.append(sep[s])
        separated.append(separator)
    separated.append(sep[-1])

    return separated

# Création d'une fonction qui renvoie un élément choisi au hasard dans une liste.
def pickrandomly(box : list):
    p = rand.randrange(- 1, stop = len(box))

    return box[p]
