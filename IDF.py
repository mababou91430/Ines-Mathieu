from Fonction_ines import *
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


def TF_IDF():
    L1 = []
    Dictionnaire_IDF = IDF()
    for mot in Dictionnaire_IDF:
        L2 = []
        L2.append(mot)
        for filename in os.listdir("cleaned"):
            text = "cleaned/" + filename
            d = TF(text)
            if mot not in d:
                L2.append("9.9")
            else:
                g = d[mot]
                L2.append(format(g*Dictionnaire_IDF[mot], ".1f"))
        L1.append(L2)
    return L1
