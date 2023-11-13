"""
Module regroupant les fonctions pour gérer et analyser l'inventaire des bornes de stationnement de
la ville de Québec.
"""

from math import sqrt


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
    latitude = float(borne_info_list[5])
    longitude = float(borne_info_list[6].strip())

    return creer_borne(borne_info_list[1],borne_info_list[2],borne_info_list[4],latitude,longitude)


def lire_fichier_bornes(nom_fichier):
    """
    Lit un fichier texte contenant l'inventaire des bornes avec une borne par ligne.

    Args:
        nom_fichier (str): Fichier .txt contenant l'inventaire des bornes. Les éléments sur chaque ligne sont
        séparées par une virgule

    Returns:
        list: Une liste de toutes les bornes contenues dans le fichier
    """
    bornes_list = []
    try:
        f = open(nom_fichier, "r", encoding="utf-8-sig")
        f.readline()# pour enlever la premiere ligne du fichier txt avec les noms de colonnes.
        line = f.readline()
        while line != '':
            bornes_list.append(creer_borne_avec_chaine(line))
            line = f.readline()
        f.close()
    except IOError:
        print("Le fichier", nom_fichier, "est introuvable.")

    return bornes_list


def nombre_de_bornes(inventaire):
    """
    Retourne le nombre de bornes contenu dans un « inventaire ».

    Args:
        inventaire (list): Une liste de bornes

    Returns:
        int: Le nombre de bornes contenues dans l'inventaire.
    """
    return len(inventaire)


def selectionner_bornes_par_rue(inventaire, rue):
    """
    Sélectionne toutes les bornes sur la rue spécifiée en argument parmi l'inventaire.

    Args:
        inventaire (list): La liste des bornes de l'inventaire
        rue (str): Nom de la rue

    Returns:
        list: Liste des bornes qui sont sur la rue donnée
    """
    list_recherche = []
    for borne in inventaire:
        if rue.lower() in borne['Rue'].lower():
            list_recherche.append(borne)
    
    return list_recherche


def selectionner_bornes_par_cote(inventaire, cote):
    """
    Sélectionne toutes les bornes du côté spécifié en argument parmi l'inventaire.

    Args:
        inventaire (list): La liste des bornes de l'inventaire
        cote (str): Le côté de la rue

    Returns:
        list: Liste des bornes qui sont sur le côté donné
    """
    list_recherche = []
    for borne in inventaire:
        if borne['Cote'] == cote:
            list_recherche.append(borne)
    
    return list_recherche


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
    borne_par_num = {'Numero': -1}
    for borne in inventaire:
        if int(borne['Numero']) == int(numero_borne):
            borne_par_num = borne

    return borne_par_num


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
    x1 = float(borne_1['Coordonnees'][0]) * 110.6
    x2 = float(borne_2['Coordonnees'][0]) * 110.6
    y1 = float(borne_1['Coordonnees'][1]) * 78.85
    y2 = float(borne_2['Coordonnees'][1]) * 78.85
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    

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
    inventaire_local = inventaire.copy() # pour ne pas changer la valeur d'inventaire.
    borne_initial = selectionner_borne_par_numero(inventaire, numero_borne)
    if borne_initial == {'Numero': -1}:
        return {'Numero': -1}

    borne_plus_pres = {'Numero': -1}
    min_distance = float('inf') # pour initialiser min_moyenne avec la plus grosse valeur possible

    if autre_rue:
        inventaire_temp = selectionner_bornes_par_rue(inventaire_local, borne_initial['Rue'])
        for borne in inventaire_temp:
            retirer_borne(inventaire_local, borne['Numero'])

    for borne_courante in inventaire_local:
        if borne_courante != borne_initial:
            if calculer_distance_bornes(borne_initial, borne_courante) < min_distance:
                borne_plus_pres = borne_courante
                min_distance = calculer_distance_bornes(borne_initial, borne_courante)
    return borne_plus_pres

def trouver_bornes_plus_eloignees(inventaire):
    """
    Trouve les deux bornes les plus éloignées géographiquement parmi l'inventaire.

    Args:
        inventaire (list): La liste des bornes de l'inventaire

    Returns:
        tuple: Les deux dictionnaires contenant l'information des bornes les plus éloignées
    """
    borne_1 = inventaire[0]
    borne_2 = inventaire[1]
    distance_max = 0

    for borne_courante_1 in inventaire:
        for borne_courante_2 in inventaire:
            if calculer_distance_bornes(borne_courante_1, borne_courante_2) > distance_max:
                borne_1 = borne_courante_1
                borne_2 = borne_courante_2
                distance_max = calculer_distance_bornes(borne_courante_1, borne_courante_2)

    return borne_1, borne_2


def trouver_borne_centrale(inventaire):
    """ Trouve la borne «centrale», c-a-d celle dont la moyenne des distances avec toutes les autres bornes de
    l'inventaire est minimale.

    Args:
        inventaire (list): La liste des bornes de l'inventaire

    Returns:
        dict: Dictionnaire contenant l'information de la borne centrale
    """
    min_moyenne = float('inf') # pour initialiser min_moyenne avec la plus grosse valeur possible
    borne_centrale = {'Numero': -1}

    for borne_courante_1 in inventaire:
        somme_distance = 0
        for borne_courante_2 in inventaire:
            somme_distance += calculer_distance_bornes(borne_courante_1, borne_courante_2)

        moyenne = somme_distance / nombre_de_bornes(inventaire)
        if moyenne < min_moyenne:
            borne_centrale = borne_courante_1
            min_moyenne = moyenne
    return borne_centrale


def ajouter_borne(inventaire, borne):
    """
    Ajoute une borne à l'inventaire.

    Args:
        inventaire (list): La liste des bornes de l'inventaire
        borne (dict): Dictionnaire contenant l'information de la borne à ajouter à l'inventaire

    Returns:
        bool: True si la borne a été ajoutée à l'inventaire, False si le numéro de borne existait déjà.
    """
    for borne_courante in inventaire:
        if borne['Numero'] == borne_courante['Numero']:
            return False

    inventaire.append(borne)
    return True


def retirer_borne(inventaire, numero_borne):
    """
    Retire une borne de l'inventaire.

    Args:
        inventaire (list): La liste des bornes de l'inventaire
        numero_borne (int): Numéro de la borne à retirer de l'inventaire

    Returns:
        bool: True si la borne a été retirée de l'inventaire, False si le numéro de borne n'existait pas.
    """
    for borne_courante in inventaire:
        if numero_borne == borne_courante['Numero']:
            inventaire.remove(borne_courante)
            return True

    return False


if __name__ == '__main__':
    print('Exécution des tests...')
    print('-----------------------')
    inventaire = lire_fichier_bornes('vdq-bornestationnement.txt')

    borne = creer_borne(4, 'N', 'Ruelle Rouge', -71.23, 46.82)
    assert borne == {'Numero': 4, 'Cote': 'N', 'Rue': 'Ruelle Rouge', 'Coordonnees': (46.82, -71.23)}
    print('creer_borne: OK')


# tests pour creer_borne_avec_chaine
    chaine = "100020,4060,N,102085,Rue De L'Espinay,-71.23586776648797,46.82775479224512"
    resultat1 = creer_borne_avec_chaine(chaine)
    assert resultat1["Numero"] == "4060"
    assert resultat1["Cote"] == "N"
    assert resultat1["Rue"] == "Rue De L'Espinay"
    assert resultat1["Coordonnees"] == (46.82775479224512, -71.23586776648797)

    chaine = "100277,2468,,100006,Rue Aberdeen,-71.22531187144521,46.80294840216365"
    resultat2 = creer_borne_avec_chaine(chaine)
    assert resultat2["Numero"] == "2468"
    assert resultat2["Cote"] == ""
    assert resultat2["Rue"] == "Rue Aberdeen"
    assert resultat2["Coordonnees"] == (46.80294840216365, -71.22531187144521)

    chaine = "300075,5001,,,Stationnement Gare-du-Palais,-71.21458772811069,46.81706543381666"
    resultat3 = creer_borne_avec_chaine(chaine)
    assert resultat3["Numero"] == "5001"
    assert resultat3["Cote"] == ""
    assert resultat3["Rue"] == "Stationnement Gare-du-Palais"
    assert resultat3["Coordonnees"] == (46.81706543381666, -71.21458772811069)


# tests pour lire_fichier_bornes
    inventaire_test = lire_fichier_bornes("vdq-bornestationnement-reduit.txt")
    assert len(inventaire_test) == 5
    assert inventaire_test[0]["Numero"] == "4034"
    assert inventaire_test[1]["Numero"] == "4083"
    assert inventaire_test[2]["Numero"] == "3008"
    assert inventaire_test[3]["Cote"] == "N"
    assert inventaire_test[4]["Rue"] == "Rue Caron"
    assert inventaire_test[4]["Coordonnees"] == (46.81163827847973, -71.2275177088525)


# tests pour nombre_de_bornes
    assert nombre_de_bornes(inventaire_test) == 5
    assert nombre_de_bornes([]) == 0
    assert nombre_de_bornes(lire_fichier_bornes('vdq-bornestationnement.txt')) == 1793


# tests pour selectionner_bornes_par_rue
    resultat5 = selectionner_bornes_par_rue(inventaire_test, "Rue Ozanam")
    assert resultat5 == [{'Numero': '4083', 'Cote': 'E', 'Rue': 'Rue Ozanam', 'Coordonnees': (46.82738279722134, -71.2372202135681)}]

    resultat5 = selectionner_bornes_par_rue(inventaire_test, "Rue invalide")
    assert resultat5 == []

    resultat5 = selectionner_bornes_par_rue(inventaire_test, "rue caron") # recherche avec des lettres miniscule
    assert resultat5 == [{'Numero': '3170', 'Cote': 'E', 'Rue': 'Rue Caron', 'Coordonnees': (46.81163827847973, -71.2275177088525)}]


# tests pour selectionner_bornes_par_cote
    resultat5 = selectionner_bornes_par_cote(inventaire_test, "S")
    assert len(resultat5) == 2

    resultat5 = selectionner_bornes_par_cote(inventaire_test, "O")
    assert len(resultat5) == 0

    resultat5 = selectionner_bornes_par_cote(inventaire_test, "N")
    assert resultat5 == [{'Numero': '3060', 'Cote': 'N', 'Rue': 'Boulevard Charest Est', 'Coordonnees': (46.8141394906634, -71.22296230536146)}]


# tests pour selectionner_bornes_par_numero
    resultat5 = selectionner_borne_par_numero(inventaire_test, 4034)
    assert resultat5 == {'Numero': '4034', 'Cote': 'S', 'Rue': 'Boulevard Cardinal-Villeneuve', 'Coordonnees': (46.828893322195135, -71.23571580398136)}

    resultat5 = selectionner_borne_par_numero(inventaire_test, 5555)
    assert resultat5 == {'Numero': -1}

    resultat5 = selectionner_borne_par_numero(inventaire_test, 3060)
    assert resultat5 == {'Numero': '3060', 'Cote': 'N', 'Rue': 'Boulevard Charest Est', 'Coordonnees': (46.8141394906634, -71.22296230536146)}


# tests pour calculer_distance_bornes
    borne1 = {'Numero': '3060', 'Cote': 'N', 'Rue': 'Boulevard Charest Est', 'Coordonnees': (46.8141394906634, -71.22296230536146)}
    borne2 = {'Numero': '4034', 'Cote': 'S', 'Rue': 'Boulevard Cardinal-Villeneuve', 'Coordonnees': (46.828893322195135, -71.23571580398136)}
    borne3 = {'Numero': '3170', 'Cote': 'E', 'Rue': 'Rue Caron', 'Coordonnees': (46.81163827847973, -71.2275177088525)}

    distance1 = calculer_distance_bornes(borne1, borne1)
    assert abs(distance1) < 1e-9
    distance2 = calculer_distance_bornes(borne1, borne2)
    assert abs(distance2 - 1.9167534714) < 1e-4
    distance3 = calculer_distance_bornes(borne1, borne3)
    assert abs(distance3 - 0.453) < 0.001


# tests pour trouver_borne_plus_pres
    assert trouver_borne_plus_pres(inventaire_test, 3170, False)['Numero'] == '3008'
    assert trouver_borne_plus_pres(inventaire_test, 5555, False) == {'Numero': -1}
    assert trouver_borne_plus_pres(inventaire_test, 3170, True)['Numero'] == '3008'


# tests pour trouver_bornes_plus_eloignees
    assert trouver_bornes_plus_eloignees(inventaire_test) == (borne2, borne3)
    assert len(trouver_bornes_plus_eloignees(inventaire_test)) == 2

    borne4 = {'Numero': '4140', 'Cote': 'N', 'Rue': 'Boulevard Sainte-Anne', 'Coordonnees': (46.84520539397195, -71.21370767822152)}
    borne5 = {'Numero': '6111', 'Cote': 'O', 'Rue': 'Avenue Maguire', 'Coordonnees': (46.779296353862875, -71.25043521119333)}
    assert trouver_bornes_plus_eloignees(inventaire) == (borne4, borne5)


# tests pour trouver_borne_centrale
    assert trouver_borne_centrale(inventaire_test) == {'Numero': '3008', 'Cote': 'S', 'Rue': 'Boulevard Charest Est', 'Coordonnees': (46.812700620681355, -71.22626380380918)}

    inventaire_1 = [
        {'Numero': '1244', 'Cote': 'N', 'Rue': 'Boulevard Sainte-Anne', "Coordonnees": (12.345, 67.890)},
        {'Numero': '5124', 'Cote': 'N', 'Rue': 'Boulevard Sainte', "Coordonnees": (23.456, 45.678)},
        {'Numero': '6578', 'Cote': 'E', 'Rue': 'Boulevard Rene', "Coordonnees": (34.567, 56.789)}
    ]
    resultat6 = trouver_borne_centrale(inventaire_1)
    assert resultat6['Numero'] == '5124'

    inventaire_une_entree = [{'Numero': '7777', 'Cote': 'S', 'Rue': 'Boulevard Gascon', "Coordonnees": (12.345, 67.890)}]
    resultat7 = trouver_borne_centrale(inventaire_une_entree)
    assert resultat7["Numero"] == "7777"


# tests pour ajouter_borne
    borne_nouveau = {'Numero': '8888', 'Cote': 'N', 'Rue': 'Boulevard Ismail', "Coordonnees": (34.577, 56.999)}
    resultat8 = ajouter_borne(inventaire_1, borne_nouveau)
    assert resultat8 is True
    assert len(inventaire_1) == 4
    assert inventaire_1[-1]['Numero'] == '8888'

    borne_existante = {'Numero': '1244', 'Cote': 'S', 'Rue': 'Boulevard Ismail', "Coordonnees": (11.345, 87.890)}
    resultat9 = ajouter_borne(inventaire_1, borne_existante)
    assert resultat9 is False
    assert len(inventaire_1) == 4


# tests pour retirer_borne
    numero_borne = "1244"
    resultat10 = retirer_borne(inventaire_1, numero_borne)
    assert resultat10 is True
    assert len(inventaire_1) == 3
    assert inventaire_1[0]['Numero'] != '1244'

    numero_borne_non_existante = "1111"
    resultat11 = retirer_borne(inventaire_1, numero_borne_non_existante)
    assert resultat11 is False
    assert len(inventaire_1) == 3



