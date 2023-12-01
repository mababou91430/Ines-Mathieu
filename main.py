from Fonction import *
from IDF import *
from Fonction_ines import *
import os

L1 = []
Dictionnaire_IDF = IDF()
for mot in Dictionnaire_IDF.keys():
    L2 = []
    L2.append(mot)
    for filename in os.listdir("cleaned")

