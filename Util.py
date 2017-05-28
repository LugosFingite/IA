import random
import time


# Création d'une instance de la classe Random, ayant pour seed le nombre de secondes écoulées depuis... le 1er Janvier 1970 !
rand = random.Random(x = time.time())


# Création d'une fonction prenant pour argument une ligne de texte et un caractère | un mot,
# et renvoyant une liste contenant chaque partie de la ligne de texte qui se trouve entre deux séparateurs.
def separate(separating : str, separator : str):
    # Création de deux listes de caractères qui seront nos séparateurs et notre phrase à séparer.
    separator = list(separator)
    separating = list(separating)
    # Création de deux autres listes vides qui nous serviront à séparer.
    separated = []
    temp = []

    # Pour chaque caractère on va :
    # Vérifier si le caractère correspond à un séparateur. Si oui, si la liste temporaire contient quelque chose, on va ajouter son contenu a la phrase séparée, et on va rajouter le séparateur.
    # Si non, on va rajouter le caractère à la liste temporaire. Bien evidemment, si on passe le contenu de la liste temporaire dans la phrase séparée, on vide la liste temporaire.
    for char in separating:
        check = 0

        for s in separator:
            if char == s:
                if len(temp) > 0:
                    separated.append("".join(temp))
                separated.append(char)
                temp.append(char)
                break
            else:
                check += 1

        if check == len(separator):
            temp.append(char)
        else:
            temp.clear()
    separated.append("".join(temp))

    return separated

# Création d'une fonction qui renvoie un élément choisi au hasard dans une liste.
def pickrandomly(box : list):
    p = rand.randrange(- 1, stop = len(box))

    return box[p]