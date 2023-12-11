from IDF import *
from Fonction_ines import *
import os



def nom_president():
    L = []
    remplacement = "'!?123456789"
    for filename in os.listdir("speeches-20231124"):
        for i in range(len(remplacement)):
            filename = filename.replace(remplacement[i],     "")
        filename = filename.replace("Nomination_", "")
        filename = filename.replace(".txt", "")
        if filename not in L:
            L.append(filename)
    return L


def clean():
    for filename in os.listdir("speeches-20231124"):
        mon_fichier = "speeches-20231124/" + filename
        f1 = open(mon_fichier, "r")
        repertoire_nom_fichier = "cleaned/" + filename
        f = open(repertoire_nom_fichier, "w")
        ligne = f1.readline()
        while ligne != "":
            l = list(ligne)
            for i in range(len(ligne)):
                if 65 <= ord(l[i]) <= 90:
                    l[i] = chr(ord(l[i]) + 32)
            ligne = "".join(l)
            f.write(ligne)
            ligne = f1.readline()


def Tokenisation(text):
    l = list(text)
    for i in range(len(l)):
        if 65 <= ord(l[i]) <= 90:
            l[i] = chr(ord(l[i]) + 32)
        if (33 <= ord(l[i]) <= 47) or (58 <= ord(l[i]) <= 64) or (91 <= ord(l[i]) <= 96) or (123 <= ord(l[i]) <= 126):
            if ord(l[i]) == 45 or 39:
                l[i] = chr(32)
            else:
                l.remove(l[i])
    question = "".join(l)
    question = question.split(" ")
    return question


def corpus(x):
    k=[]
    j=Tokenisation(x)
    print (j)
    for filename in os.listdir("cleaned"):
        text = "cleaned/" + filename
        f1 = open(text, "r",encoding="utf-8")
        ligne = f1.readline()
        d = TF(text)
        print(d)
        for elem in j:
            print (elem)
            if elem in d:
                    k.append(elem)
        return("les mots présents dans le corpus et la question sont :",k)


def vecteur_TF_IDF(x):
    j = Tokenisation(x)
    k = IDF()
    somme = 0
    nb = {}
    TF = {}
    vTF_IDF = []
    for i in range(len(j)):
        if j[i] != " " and j[i] != "":
            somme += 1
    for i in range(len(j)):
        if j[i] not in nb and j[i] != "":
            nb[j[i]] = j.count(j[i])
    for i in range(len(j)):
        TF[j[i]] = nb[j[i]]/somme
    for i in range(len(j)):

    return TF

z = "Quels présidents a répéter le plus de fois climat a son peuple dans son discours"
print(vecteur_TF_IDF(z))