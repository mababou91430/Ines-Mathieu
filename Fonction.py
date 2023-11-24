import os


def nom_president():
    for filename in os.listdir("speeches-20231124"):
        print(filename)

nom_president()