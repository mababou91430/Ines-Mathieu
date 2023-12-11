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
                if (33 <= ord(l[i]) <= 47) or (58 <= ord(l[i]) <= 64) or (91 <= ord(l[i]) <= 96) or (123 <= ord(l[i]) <= 126 ) :
                    if ord(l[i])== 45 or 44:
                        l[i] = chr(32)
                    else:
                        l[i]= chr(0)
            ligne = "".join(l)
            f.write(ligne)
            ligne = f1.readline()



#clean()


def TF(name):
    dic = {}
    a = 0
    b = 0
    f1 = open(name, "r")
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
    return(dic)


TF("cleaned/Nomination_Chirac1.txt")

import os
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


#text = input("saisir une question : ")
#print(Tokenisation(text))
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

u="quels présidents parlent de la nation ?"
print(corpus(u))

