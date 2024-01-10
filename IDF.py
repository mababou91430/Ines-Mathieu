from Fonction_ines import *
import math
import os



def IDF():
    Dictionnaire = {}
    for filename in os.listdir("cleaned"):  #ouverture et récupérage des noms de fichier un à un
        text = "cleaned/" + filename    #création d'une variable qui va prendre le nom du fichier et ajout de "cleaned/" devant pour pouvoir ouvrir les fichier
        f1 = open(text, "r", encoding="utf-8")  #ouverture du fichier text avec l'encodage utf-8 pour éviter les problèmes avec les accents
        ligne = f1.readline()   #lecture de la première ligne du fichier
        temp = ""   #variable qui sert en cas de débuggage
        p = True    #variable qui sert en cas de débuggage
        while ligne != "":
            L1 = ligne.split(" ")   #création d'un tableau avec tous les mots de la ligne actuelle
            for i in range(len(L1)):
                if L1[i] not in Dictionnaire and L1[i] != "\n" and L1[i] != "" and L1[i] != " ":
                    Dictionnaire[L1[i]] = 0 #ajout de tous les mots contenu dans les texte dans un dictionnaire
            ligne = f1.readline()   #mise a jour de la variable ligne
    for filename1 in os.listdir("cleaned"):
        text1 = "cleaned/" + filename1  #création d'une variable qui va prendre le nom du fichier et ajout de "cleaned/" devant pour pouvoir ouvrir les fichier
        f2 = open(text1, "r", encoding="utf-8") #ouverture du fichier text avec l'encodage utf-8 pour éviter les problèmes avec les accents
        ligne = f2.readline()   #création d'une variable qui va contenir la première ligne du texte
        L2 = [] #création d'un tableau
        while ligne != "":
            L2.append(ligne.split(" ")) #ajout de tous les mots de la première ligne dans le tableau
            ligne = f2.readline()   #mise a jour de la variable ligne
        for mot in Dictionnaire.keys():
            already = False #création d'une variable qui va nous permettre d'arréter le "if" après une éxécution
            for i in range(len(L2)):
                if mot in L2[i] and already == False:   #test pour savoir si les mots sont dans le tableau et si c'est leur première éxécution ou pas
                    Dictionnaire[mot] = Dictionnaire[mot] + 1   #si le mot est dans le tableau donc dans le texte on ajoute 1 a la valeur qui correspond a ce mot dans le dictionnaire
                    already = True  #pour éviter d'éxécuter le programme le test plusieurs fois
    for mot in Dictionnaire.keys():
        Dictionnaire[mot] = math.log(8/Dictionnaire[mot]) #calcul de l'IDF est ajout de la valeur dans le dictionnaire
    return Dictionnaire #retour du Dictionnaire IDF



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
                L2.append(format(g*Dictionnaire_IDF[mot])) #calcul du TF-IDF de ce mot
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

                L2.append(format(g*Dictionnaire_IDF[mot], ".1f")) #calcul du TF-IDF de ce mot
        L1.append(L2) #ajout de la liste L2 a la liste L1
    return L1 #retour de la matrice TF-IDF

