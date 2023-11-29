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
                for j in Dictionnaire.keys():
                    if j == L1[i]:
                        p = False
                        temp = L1[i]
            if p == True:



            ligne = f1.readline()
            print(L1)

IDF()