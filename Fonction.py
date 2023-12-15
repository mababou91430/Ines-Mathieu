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


def TF():
    dic = {}
    a = 0
    b = 0
    for filename in os.listdir("cleaned"):
        text = "cleaned/" + filename
        f1 = open(text, "r")
        ligne = f1.readline()
        p = True
        while ligne != "":
            L1 = ligne.split(" ")
            for i in range(len(L1)):
                if L1[i] in dic:
                    dic[L1[i]] = dic[L1[i]] + 1

                else:
                    for j in range(i, len(L1)):
                        if L1[j] == L1[i]:
                            a += 1
                    dic[L1[i]] = a
                    a = 0
            ligne = f1.readline()
        print(dic)


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


def vecteur_TF_IDF(text):
    g = {}
    l = Tokenisation(text)
    nb_mots = 0
    for i in range(len(l)):
        if l[i] != "" and l[i] !=" ":
            nb_mots += 1
    for i in range(len(l)):
        if l[i] != "" and l[i] !=" ":
            g[l[i]] = l.count(l[i])
    for i in g.keys():
        g[i] = g[i]/nb_mots
    d = IDF()
    for i in g.keys():
        for j in d.keys():
            if i == j:
                g[i] = d[i]*g[i]
    return g

text = "Ceci est une queston de test pour savoir si le code que j'ai fait marche une question est une question"
print(vecteur_TF_IDF(text))