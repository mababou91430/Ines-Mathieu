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
            "6. Hormis les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les présidents ont évoqué.\n ")

x=int(input("Numéro de la demande :"))

while x<0 or x>6:
    print("Bienvenue sur le Chat bot, veuillez entrer le numéro de votre requêtte :")
    x = int(input("1. Afficher la liste des mots les moins importants dans le corpus de documents.\n "
                  "2. Afficher le(s) mot(s) ayant le score TD-IDF le plus élevé.\n "
                  "3. Indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac.\n "
                  "4. Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus defois.\n "
                  "5. Indiquer le premier président à parler du climat et/ou de l’écologie.\n"
                  "6. Hormis les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les présidents ont évoqué.\n "))

#if x==1:


#if x==2:

if x == 3:
    k=(max(TF("cleaned/Nomination_Chirac1.txt")))
    print(k)

if x == 4:
    k=[]
    for filename in os.listdir("cleaned"):

        text = "cleaned/" + filename
        f1 = open(text, "r")
        ligne = f1.readline()
        p = True
        while ligne != "":
            L1 = ligne.split(" ")
            if "Nation" in L1:
                k.append(filename)
    print(k)






if x == 5:
    a = 0
    j = []
    for filename in os.listdir("cleaned"):
        print(filename)
        file= nom_president()
        for i in range(len(file)):
            a=file[i]
            H=TF(a)
        print(H)
        #if "ecologie" or "climat" in H:
            #print(filename)




    ligne = f1.readline()


    print(j)


#if x == 6:



