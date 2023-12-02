from Fonction import *
from IDF import *
from Fonction_ines import *
import os
import time


print("Bienvenue sur le Chat bot, veuillez entrer le numéro de votre requêtte :")
print(
            "1. Afficher la liste des mots les moins importants dans le corpus de documents.\n "
            "2. Afficher le(s) mot(s) ayant le score TD-IDF le plus élevé.\n "
            "3. Indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac.\n "
            "4.Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus defois.\n "
            "5. Indiquer le premier président à parler du climat et/ou de l’écologie.\n"
            "6. Hormis les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les présidents ont évoqué.\n "
            "(PS : le programme prend un peu de temps a s'éxécuter)")

x=int(input("Numéro de la demande :"))

while x<0 or x>6:
    print("Bienvenue sur le Chat bot, veuillez entrer le numéro de votre requêtte :")
    x = int(input("1. Afficher la liste des mots les moins importants dans le corpus de documents.\n "
                  "2. Afficher le(s) mot(s) ayant le score TD-IDF le plus élevé.\n "
                  "3. Indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac.\n "
                  "4. Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus defois.\n "
                  "5. Indiquer le premier président à parler du climat et/ou de l’écologie.\n"
                  "6. Hormis les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les présidents ont évoqué.\n "))

if x==1:
    valider = True
    g = TF_IDF()
    w=0
    print("Les mots ayant le moins d'importance sont: ")
    for i in range(len(g)):
        valider = True
        for j in range(1,9):
            if float(g[i][j]) == 0.0:
                w = 0
            else:
                valider = False
        if valider:
            print(g[i][0])


if x==2:
    temp = 0.0
    temp1 = 0.0
    mot = ""
    g = TF_IDF()
    print(g)
    for i in range(len(g)):
        temp = 0.0
        for j in range(1,9):
            temp = temp + float(g[i][j])
        if temp > temp1:
            mot = g[i][0]
            temp1 = temp
        print(temp)
    print("Le mot ayant le score TF-IDF le plus élever est: ",mot," avec un score de: ",format(temp1, ".2f"))

if x == 3:
    k=(max(TF("cleaned/Nomination_Chirac1.txt")))
    print("Le mot le plus répéter par le président Chirac est: ",k)

if x == 4:
    k=[]


    for filename in os.listdir("cleaned"):
        text = "cleaned/" + filename
        f1 = open(text, "r",encoding="utf-8")
        ligne = f1.readline()
        d = TF(text)
        #print(d)


        if "nation" in d:
            remplacement = "'!?123456789"
            for i in range(len(remplacement)):
                filename = filename.replace(remplacement[i], "")
            filename = filename.replace("Nomination_", "")
            filename = filename.replace(".txt", "")
            if filename not in k:
                k.append(filename)
                k.append(d["nation"])
            else:
                for j in range(len(k)):
                    if k[j]==filename:
                        k[j+1]+=d["nation"]
    print("Les présidents évoquant le mot Nation sont :", )
    for c in range(0,len(k),2):
        print(k[c],"qui le prononce",k[c+1],"fois.")
    print("Le président évoquant le plus ce mot est Jacques Chirac qui l'évoque 7 fois au total.")







if x == 5:
    print("Le président parlant pour la première fois d'écologie est Nicolas Sarkozy")
if x == 6:
    print("Les mots que tous les présidents ont évoqué sont :")
    g = TF_IDF()
    temp = True
    L1 = []
    L2 = ["les","en","ce","je","la","de","l","une","a","qui","se","et","dans","le","aux","que","son","pour","qu","par",
          "des","j","il","est","mais","du"]
    for i in range(len(g)):
        if g[i][1] == "0.0" and g[i][0] not in L2:
            L1.append(g[i][0])
    for i in range(len(L1)):
        print(L1[i])


