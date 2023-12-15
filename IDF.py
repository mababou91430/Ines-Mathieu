import math
import os


def IDF():
    Dictionnaire = {}
    for filename in os.listdir("cleaned"):
        text = "cleaned/" + filename
        f1 = open(text, "r")
        ligne = f1.readline()
        temp = ""
        p = True
        while ligne != "":
            L1 = ligne.split(" ")
            for i in range(len(L1)):
                if L1[i] not in Dictionnaire and L1[i] != "\n" and L1[i] != "" and L1[i] != " ":
                    Dictionnaire[L1[i]] = 0
            ligne = f1.readline()
    for filename1 in os.listdir("cleaned"):
        text1 = "cleaned/" + filename1
        f2 = open(text1, "r")
        ligne = f2.readline()
        L2 = []
        while ligne != "":
            L2.append(ligne.split(" "))
            ligne = f2.readline()
        for mot in Dictionnaire.keys():
            already = False
            for i in range(len(L2)):
                if mot in L2[i] and already == False:
                    Dictionnaire[mot] = Dictionnaire[mot] + 1
                    already = True
    for mot in Dictionnaire.keys():
        Dictionnaire[mot] = math.log(8/Dictionnaire[mot])
    return Dictionnaire


IDF()

def TF_IDF():
    L1 = []
    Dictionnaire_IDF = IDF() #création d'une variable qui prend le dictionnaire IDF comme valeur
    for mot in Dictionnaire_IDF:
        L2 = [] #création d'une liste L2 qui va nous servir a remplir la liste L1
        L2.append(mot)  #ajout du mot qu'on va calculer sa valeur TF-IDF dans le tableau
        for filename in os.listdir("cleaned"):
            text = "cleaned/" + filename #création d'une variable qui va prendre le nom du fichier et ajout de "cleaned/" devant pour pouvoir ouvrir les fichier
            d = TF(text) #création d'une variable qui va prendre le TF comme valeur
            if mot not in d:
                L2.append("0")   #si le mot n'est pas dans le dictionnaire TF de ce texte on lui mets 0 comme valeur
            else:
                g = d[mot]  #création d'une variable g qui va prendre la valeur TF du mot
                L2.append(format(g*Dictionnaire_IDF[mot], ".1f")) #calcul du TF-IDF de ce mot
        L1.append(L2) #ajout de la liste L2 a la liste L1
    return L1 #retour de la matrice TF-IDF

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