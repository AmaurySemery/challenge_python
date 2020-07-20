# Exercice 1 : Ecrire un programme en langage Python qui demande à l’utilisateur de saisir son nom et de lui afficher son nom avec un message de bienvenue !

name = input("Tu t'appelles comment ? ")
print("Bienvenue", name, "!")

# Exercice 2 : Ecrire un programme en Python qui demande à l’utilisateur de saisir deux nombres a et b et de lui afficher leur somme : a + b

a = input("Donne moi un premier chiffre : ")
b = input("Donne moi un second chiffre (tu vas voir, c'est magique) : ")
c = int(a) + int(b)
print("Ce qui nous fait la modique somme de...", c, "!")

# Exercice 3 : Ecrire un programme en Python qui demande à l’utilisateur de saisir deux nombres a et b et de lui afficher leur maximum.
# &
# Exercice 7 : Ecrire un programme en Python qui demande à l’utilisateur de saisir 3 nombre x, y et z et de lui afficher leur maximum.

print("On va maintenant saisir trois chiffres et définir le maximum.")
h = int(input("Entrez le premier nombre : "))
i = int(input("Entrez le deuxième nombre : "))
j = int(input("Entrez le troisième nombre : "))
def max(h,i,j):
    if h>i and j:
        return(h)
    if i>j and h:
        return(i)
    if j>h and i:
        return(j)
print("Le nombre maximum est", max(h,i,j), "!")

# Exercice 4 : Ecrire un programme en langage Python qui affiche les 100 premiers nombres entiers
# &
# Exercice 5 : Ecrire un programme en langage Python qui demande à l’utilisateur de saisir son nombre entier et de lui afficher si ce nombre est pair ou impair

def int_numbers():
    f = input("Donne moi un nombre entier entre 1 et 100 : ")
    if int(f) <= 100 and int(f) >= 0:
        print("Votre nombre de", f, "fait partie des 100 premiers entiers, bravo !")
    else:
        print("Votre nombre ne fait pas partie des 100 premiers entiers.")
    print("Mais attention, tu n'as encore rien vu !")
    n = int(f)
    if (n % 2) == 0:
        print("{0} est pair".format(n),"!!!!")
    else:
        print("{0} est impair".format(n),"!!!!")

int_numbers()

# Exercice 6 : Ecrire un programme en langage Python qui demande à l’utilisateur de saisir son âge et de lui afficher le message « vous êtes Majeur ! » si l’âge tapé est supérieur ou égale à 18 et le message « vous êtes mineur ! » si l’âge tapé est inférieur à 18

def age():
    g = int(input("D'ailleurs, t'as quel âge ? "))
    if g < 18:
        print("Mais...", name, "... Tu es mineur ! La belle époque !")
    if g >= 18 and g < 130:
        print("Oh ! Tu es majeur", name, "! Les responsabilités, toussa...")
        print("La vie de famille peut-être !")
    if g > 130:
        print(g, "ans ?! Tu ne te payerais pas ma tête Nosfératu ?!")

age()

# Exercice 8 : Ecrire un programme en Python qui demande à l’utilisateur de saisir un nombre entier n et de lui afficher la valeur de la somme 1 + 2 + … + n =

k = int(input("Tu veux bien me donner un nombre entier ? "))
print("Merci à toi !")
l = 0
for i in range(1,k+1):
    l = l + i
print("La valeur de la somme  1 + 2 + 3 + ... + ",k,"vaut donc", l)

# Exercice 9 : Ecrire un programme en Python qui demande à l’utilisateur de saisir un nombre entier n et de lui afficher n !

m = int(input("Bon, j'ai l'impression de radoter, mais tu veux bien me prêter un nombre entier ? Allez, n'importe lequel : "))
print("P'tit", m, "rendu !")

# Exercice 10 : Ecrire un programme en Python qui demande à l’utilisateur de saisir le rayon d’un cercle et de lui renvoyer la surface et le périmètre.

rayon = int(input("Imagine un cercle, son rayon vaut combien ? "))
from math import*
def aire(rayon):
    A=pi*rayon**2
    return(A)

import math    

def perimetre(rayon):
    diametre = 2 * rayon
    return math.pi * diametre
    
print("Ton cercle a une surface de", aire(rayon), "et un périmètre de", perimetre(rayon))