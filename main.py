import random

a = random.randint(1,100)

demande = int(input("devinez le nombre : "))


while demande != a :

    if demande < a :
        print("c'est plus !")

    if demande > a :
        print("c'est moins...")

    demande = int(input("devinez le nombre : "))

print("Gagné !")
