"""
Module regroupant les fonctions pour gérer et analyser l'inventaire des bornes de stationnement de
la ville de Québec.
"""


def creer_borne(no_borne, cote_rue, nom_topographique, longitute, latitude):
    """
    Construit un dictionnaire contenant les informations pertinentes décrivant une borne

    Args:
        no_borne (int): Le numéro unique de la borne
        cote_rue (str): Le côté de la rue où se trouve la borne
        nom_topographique (str): Le nom de la rue où se trouve la borne
        longitute (float): La postion géographique de la borne (degré longitudinal)
        latitude (float): La postion géographique de la borne (degré latitudinal)

    Returns:
        dict: Un dictionnaire contenant l'information d'une borne
    """
    borne = {}
    borne['Numero'] = no_borne
    borne['Cote'] = cote_rue
    borne['Rue'] = nom_topographique
    borne['Coordonnees'] = (latitude, longitute)
    return borne


def afficher_inventaire(inventaire):
    """
    Affiche l'inventaire des bornes sous la forme d'un tableau dans la console.

    Args:
        inventaire (list): Une liste contenant des bornes. Chacune des bornes est un dictionnaire.
    """
    ligne = '-' * 100
    print(ligne)
    print(f"| {'Numero':6} | {'Cote':4} | {'Rue':35} | {'Coordonnees':42} |")
    print(ligne)
    for borne in inventaire:
        print(f"| {borne['Numero']:6} | {borne['Cote']:4} | {borne['Rue']:35} | {str(borne['Coordonnees']):42} |")
    print(ligne)


def creer_borne_avec_chaine(chaine):
    """
    Construit un dictionnaire contenant les informations pertinentes décrivant une borne, à partir d'une chaîne de
    caractère correspondant à une ligne du fichier contenant l'information sur les bornes. Pensez à utiliser la
    fonction creer_borne().

    Args:
        chaine (str): Une chaîne de caractères contenant les informations sur la borne, séparées par des virgules

    Returns:
        dict: Un dictionnaire contenant les informations sur la borne, tel que retourné par la fonction creer_borne()
    """
    borne_info_list = chaine.split(",")
    return creer_borne(borne_info_list[1],borne_info_list[2],borne_info_list[4],borne_info_list[5],borne_info_list[6])


def lire_fichier_bornes(nom_fichier):
    """
    Lit un fichier texte contenant l'inventaire des bornes avec une borne par ligne.

    Args:
        nom_fichier (str): Fichier .txt contenant l'inventaire des bornes. Les éléments sur chaque ligne sont
        séparées par une virgule

    Returns:
        list: Une liste de toutes les bornes contenues dans le fichier
    """



def nombre_de_bornes(inventaire):
    """
    Retourne le nombre de bornes contenu dans un « inventaire ».

    Args:
        inventaire (list): Une liste de bornes

    Returns:
        int: Le nombre de bornes contenues dans l'inventaire.
    """



def selectionner_bornes_par_rue(inventaire, rue):
    """
    Sélectionne toutes les bornes sur la rue spécifiée en argument parmi l'inventaire.

    Args:
        inventaire (list): La liste des bornes de l'inventaire
        rue (str): Nom de la rue

    Returns:
        list: Liste des bornes qui sont sur la rue donnée
    """



def selectionner_bornes_par_cote(inventaire, cote):
    """
    Sélectionne toutes les bornes du côté spécifié en argument parmi l'inventaire.

    Args:
        inventaire (list): La liste des bornes de l'inventaire
        cote (str): Le côté de la rue

    Returns:
        list: Liste des bornes qui sont sur le côté donné
    """


def selectionner_borne_par_numero(inventaire, numero_borne):
    """
    Sélectionne une borne par son numéro.

    Args:
        inventaire (list): La liste des bornes de l'inventaire
        numero_borne (int): Numéro de la borne

    Returns:
        dict: Un dictionnaire contenant l'information de la borne avec le numéro donné
            Si le numéro de borne n'existe pas dans l'inventaire, retourner
            le dictionnaire {'Numero': -1}.
    """



def calculer_distance_bornes(borne_1, borne_2):
    """
    Calcule la distance en kilomètre entre deux bornes.

    Note: Pour calculer la distance approximative à partir des coordonnées géographique de la région de Québec,
    il faut d'abord multiplier la distance entre les degrés de lattitude par 110.6 km/degré et la distance entre
    les degrés de lattitude par 78.85 km/degré (cette dernière quantité varie selon la distance de l'équateur).

    Args:
        borne_1 (dict): Une première borne
        borne_2 (dict): Une deuxième borne

    Returns:
        float: La distance entre les deux bornes en kilomètres
    """



def trouver_borne_plus_pres(inventaire, numero_borne, autre_rue):
    """
    Trouve la borne dans l'inventaire qui est la plus près.

    Args:
        inventaire (list): La liste des bornes de l'inventaire
        numero_borne (int): Numéro de la borne pour laquelle on cherche la borne la plus proche
        autre_rue (bool): True si la borne retournée doit se trouver sur une autre rue, False sinon

    Returns:
        dict: Un dictionnaire contenant l'information de la borne la plus proche
    """




def trouver_bornes_plus_eloignees(inventaire):
    """
    Trouve les deux bornes les plus éloignées géographiquement parmi l'inventaire.

    Args:
        inventaire (list): La liste des bornes de l'inventaire

    Returns:
        tuple: Les deux dictionnaires contenant l'information des bornes les plus éloignées
    """




def trouver_borne_centrale(inventaire):
    """ Trouve la borne «centrale», c-a-d celle dont la moyenne des distances avec toutes les autres bornes de
    l'inventaire est minimale.

    Args:
        inventaire (list): La liste des bornes de l'inventaire

    Returns:
        dict: Dictionnaire contenant l'information de la borne centrale
    """



def ajouter_borne(inventaire, borne):
    """
    Ajoute une borne à l'inventaire.

    Args:
        inventaire (list): La liste des bornes de l'inventaire
        borne (dict): Dictionnaire contenant l'information de la borne à ajouter à l'inventaire

    Returns:
        bool: True si la borne a été ajoutée à l'inventaire, False si le numéro de borne existait déjà.
    """



def retirer_borne(inventaire, numero_borne):
    """
    Retire une borne de l'inventaire.

    Args:
        inventaire (list): La liste des bornes de l'inventaire
        numero_borne (int): Numéro de la borne à retirer de l'inventaire

    Returns:
        bool: True si la borne a été retirée de l'inventaire, False si le numéro de borne n'existait pas.
    """



if __name__ == '__main__':
    print('Exécution des tests...')
    print('-----------------------')
    inventaire = lire_fichier_bornes('vdq-bornestationnement.txt')

    borne = creer_borne(4, 'N', 'Ruelle Rouge', -71.23, 46.82)
    assert borne == {'Numero': 4, 'Cote': 'N', 'Rue': 'Ruelle Rouge', 'Coordonnees': (46.82, -71.23)}
    print('creer_borne: OK')


