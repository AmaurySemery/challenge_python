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
    if h>i and h>j:
        return(h)
    if i>j and i>h:
        return(i)
    if j>h and j>i:
        return(j)
print("Le nombre maximum est", max(h,i,j), "!")

# Exercice 4 : Ecrire un programme en langage Python qui affiche les 100 premiers nombres entiers
# &
# Exercice 5 : Ecrire un programme en langage Python qui demande à l’utilisateur de saisir son nombre entier et de lui afficher si ce nombre est pair ou impair

def int_numbers():
    f = input("Donne moi un nombre entier entre 1 et 100 : ")
    if int(f) <= 100 and int(f) >= 0:
        print("Le nombre", f, "fait partie des 100 premiers entiers, bravo !")
    else:
        print("Le nombre", f, "ne fait pas partie des 100 premiers entiers.")
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

# Exercice 11 : Ecrire un programme en Python qui demande à l’utilisateur de saisir un nombre entier n et de lui afficher tous les diviseurs de ce nombre.

o = int(input("Saisis moi un nombre entier que je te donne tous ses diviseurs : "))

def getFactors(n):
    factors=[];
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

print ("Voici la liste des diviseurs de", o, ":", getFactors(o))

# Exercice 12 : 1) – Ecrire un programme en Python qui demande à l’utilisateur de saisir un nombre entier n et de lui afficher la table de multiplication de ce nombre.
# 2) – Améliorez le programme afin qu’il affiche les tables de multiplications de tous les nombres compris entre 1 et 9

p = int(input("Donne moi un nouveau nombre entier compris entre 1 et 9 : "))

def multiplication(p, max=10):
    if int(p) > 0 and int(p) <= 9:
        print("Je t'affiche la table de multiplication du nombre", p, ":")
        for i in range(1, max + 1):
            print(p * i, end=" ")
            print()
    else:
        print("Le nombre que tu as choisis ne respecte pas les conditions de base. Navré.")
        print("Si tu veux réitérer l'essai, lis bien l'énoncé cette fois :)")

multiplication(p, max=10)

# Exercice 13 : Ecrire un programme en langage Python qui demande à l’utilisateur de saisir deux nombres entiers a et b et de lui afficher le quotient et le reste de la division euclidienne de a par b.

print("On va maintenant saisir deux entiers.")
print("Nous afficherons le quotient et le reste de leur division euclidienne.")
dividende = int(input("Donne moi un premier chiffre (dividende) : "))
diviseur = int(input("Donne moi le deuxième chiffre (diviseur) : "))

quotient = dividende // diviseur
reste = dividende % diviseur

print("Le quotient entre", dividende, "et", diviseur, "est", quotient)
print("Quant au reste entre les deux nombres susmentionnés, le résultat est de", reste)

# Exercice 14 : Ecrire un programme en langage Python qui demande à l’utilisateur de saisir un nombre entier n et de lui afficher si ce nombre est carré parfait ou non.

print("Quand on multiplie un nombre entier par lui-même, on obtient un carré parfait.")
print("Nous allons voir si le nombre sélectionné est un carré parfait ou non.")
q = int(input("Saisissez un nombre entier : "))
    
def car_parfait(q):
    rep = 0
    if q >= 0:
        while rep*rep < q:
            rep = rep + 1

        if rep*rep != q:
            print(q, "n'est pas un carré parfait.")
            return None
        else:
            print(q, "est un carré parfait.")
            return rep
    else:
        print(q, "n'est pas un nombre positif.")
        return None
    
car_parfait(q)

# Exercice 15 : Ecrire un programme en langage Python qui demande à l’utilisateur de saisir un nombre entier n et de lui afficher si ce nombre est premier ou non.

print("Un nombre premier est un entier naturel qui admet exactement deux diviseurs distincts entiers et positifs.")
print("Nous allons vérifier si le nombre suivant est premier ou non.")
r = int(input("Saisis un nombre entier : "))

i = 2
while i < r and r % i != 0 :
    i = i + 1
if i == r :
    print("Le nombre", r, "est premier !")
else :
    print("Le nombre", r, "n'est pas premier !")
    print("Les vingt-cinq nombres premiers inférieurs à 100 sont : 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, et 97.")
    
# Exercice 16 : Ecrire un programme en langage Python qui permet de parcourir et afficher les caractères d’une variable du type chaine de caractères. Exemple pour s = « Python » , le programme affiche les caractères : P y t h o n

mot = input("On arrête un peu avec les chiffres. Donne moi maintenant un mot : ")
mot = mot.upper()

print("Les caractères de ton mot sont :", mot.upper())

# Exercice 17 : Ecrire un programme en Python permettant d’afficher pour une chaine de caractères donnée, le nombre d’occurrences de chaque caractère dans la chaine. Exemple pour la chaine de caractère s = « Python.org » le programme doit afficher :
# Le caractère : ” P ” figure 1 fois dans la chaine s
# Le caractère : ” y ” figure 1 fois dans la chaine s
# Le caractère : ” t ” figure 1 fois dans la chaine s
# Le caractère : ” h ” figure 1 fois dans la chaine s
# Le caractère : ” o ” figure 2 fois dans la chaine s
# Le caractère : ” n ” figure 1 fois dans la chaine s
# Le caractère : ” . ” figure 1 fois dans la chaine s
# Le caractère : ” r ” figure 1 fois dans la chaine s
# Le caractère : ” g ” figure 1 fois dans la chaine s

from collections import Counter
expression = input("Là, tu peux me donner un mot ou une phrase si t'es inspiré Jean-Paul Rimbaud : ")
occurrences = Counter(expression)
print("Nombre d'occurrences de tous les caractères :")
for (key, value) in occurrences.items():
    print ("Nombres d'occurrences de", key, "est :",value)

# Exercice 18 : Ecrire un programme en Python qui demande à l’utilisateur de saisir une chaine de caractère s et de lui renvoyer un message indiquant si la chaine contient la lettre ‘a’ tout en indiquant sa position sur la chaine. Exemple si l’utilisateur tape la chaine s = ‘langage’ le programme lui renvoie : La lettre ‘a’ se trouve à la position : 1 La lettre ‘a’ se trouve à la position : 4