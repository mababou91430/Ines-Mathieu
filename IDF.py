import math
import os


def IDF():
    L = []
    for filename in os.listdir("cleaned"):
        text = "cleaned/" + filename
        f1 = open(text, "r")
        ligne = f1.readline()
        while ligne != "":
            L1 = ligne.split(" ")
            ligne = f1.readline()
            print(L1)

IDF()