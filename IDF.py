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
                if L1[i] not in Dictionnaire:
                    Dictionnaire[L1[i]] = 1
                else:
                    Dictionnaire[L1[i]] =+ 1
            ligne = f1.readline()
            print(Dictionnaire)


IDF()