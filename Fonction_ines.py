import os


def nom_president():
    L = []
    remplacement = "'!?123456789"
    for filename in os.listdir("speeches-20231124"):
        for i in range(len(remplacement)):
            filename = filename.replace(remplacement[i], "")
        filename = filename.replace("Nomination_", "")
        filename = filename.replace(".txt", "")
        if filename not in L:
            if filename == "Hollande":
                filename = " François" +" "+ filename
                L.append(filename)

            if filename == "Chirac":
                filename = " Jacques" +" "+ filename
                L.append(filename)

            if filename == "Sarkozy":
                filename = " Nicolas" +" "+ filename
                L.append(filename)

            if filename == "Giscard dEstaing":
                filename = " Valéry" +" "+ filename
                L.append(filename)

            if filename == "Mitterant":
                filename = " François" +" "+ filename
                L.append(filename)

            if filename == "Macron":
                filename = " Emmanuel" +" "+ filename
                L.append(filename)
    return L


#print(nom_president())

def clean(): # fonction qui enlève les majuscules et la ponctuation de chaque discours
    for filename in os.listdir("speeches-20231124"): # récupère les fichier
        mon_fichier = "speeches-20231124/" + filename # ajoute un nom à chacun d'eux
        f1 = open(mon_fichier, "r", encoding="utf-8") #ouvre le fichier avec l'encodage utf-8 pour éviter les problèmes d'accents
        repertoire_nom_fichier = "cleaned/" + filename # prend le fichier et ajoute cleaned pour l'ouvrir
        f = open(repertoire_nom_fichier, "w", encoding="utf-8") #ouvre le fichier de manière à pouvoir le modifier
        ligne = f1.readline() #parcours la première ligne
        while ligne != "":
            l = list(ligne)  #prend en liste la ligne
            for i in range(len(ligne)):
                if 65 <= ord(l[i]) <= 90: # si la lettre est une majuscule
                    l[i] = chr(ord(l[i]) + 32)# on ajoute 32 à son code ascii pour que ca devienne une minuscule
                if (33 <= ord(l[i]) <= 47) or (58 <= ord(l[i]) <= 64) or (91 <= ord(l[i]) <= 96) or (123 <= ord(l[i]) <= 126 ) :# si le caractère est une ponctuation
                    if ord(l[i])== 45 or 44: # si c'ets un - ou une '
                        l[i] = chr(32) # alors on met un espace pour éviter qe le mot composé devienne un seul mot
                    else:
                        l[i]= chr(0)# sinon on fait juste disparaitre le caractère de ponctuation
            ligne = "".join(l) # on ajoute ce qu'on a modifié au texte
            f.write(ligne)
            ligne = f1.readline() #on change de ligne



#clean()


def TF(name): #fonction qui permet d'avoir le dictionnaire comprenant tous les mots prononcés par un président dans un discours et l'itération de ces mots
    dic = {} # création du dictionnaire
    a = 0 #création d'un compteur
    f1 = open(name, "r", encoding="utf-8")# ouvre le fichier choisi et avec l'encodage utf-8 pour éviter les problèmes d'accents et donc un mauvais affichage
    ligne = f1.readline() #parcours la première ligne du fichier
    while ligne != "": #tant qu'il y a de l'écriture sur chaque ligne
        L1 = ligne.split(" ")#liste comprenant tous les mot de la  ligne
        for i in range(len(L1)): #pour la longueur de cette liste
            if L1[i] in dic:# si le mot existe deja dans le dico
                dic[L1[i]] = dic[L1[i]] + 1# on ajoute juste +1 à son itération
            else:
                for j in range(i, len(L1)): #sinon on part du mot et on regrade dans toute la liste(ligne) s'il y est
                    if L1[j] == L1[i]:
                        a += 1 #dès qu'il y est le compteur augmente
                dic[L1[i]] = a #le mot apprend son itération
                a = 0 # on remet le compteur à 0 pour éviter l'accumulation
        ligne = f1.readline()# on change de ligne

    return(dic)


