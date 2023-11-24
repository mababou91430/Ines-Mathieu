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
        ligne = f1.readline()
        while ligne != "":
            for i in range(len(ligne)):
                if 65 <= ord(ligne[i]) <= 90:
                    l = list(ligne)
                    l[i] = chr(ord(l[i]) + 32)
            ligne = f1.readline()
        text = "cleaned/" + filename


clean()