# Entraînement sur https://cscircles.cemc.uwaterloo.ca/fr/

# Ecrivez un programme qui affiche : Hello world!

print("Hellow world")!

# Ecrivez un extrait de code (une petite partie d'un programme Python) qui compte les têtes, les épaules, les genoux et les orteils à une fête. Le correcteur va automatiquement définir une variable personnes pour vous, elle contiendra le nombre de personnes à la fête. Votre code doit définir quatre variables, une appelée tetes, une appelée epaules, une appelée genoux et une appelée orteils, égales au nombre de têtes, épaules, genoux et orteils à la fête. Votre programme ne doit pas générer de sortie.

tetes = 1 * personnes
epaules = 2 * personnes
genoux = 2 * personnes
orteils = 10 * personnes

# Ecrivez un programme pour inverser les valeurs de deux variables. Le correcteur va automatiquement définir les variables x et y pour vous, avec des valeurs numériques. Vous devez écrire le code qui va échanger leurs valeurs : la valeur de x après que votre code soit exécuté doit être égale à la valeur que y avait avant que votre code s'exécute, et la valeur de y après que votre code s'exécute doit être celle de x avant que votre code s'exécute. Votre programme ne doit pas générer de sortie.

xOriginal = x
x = y
y = xOriginal

# Il y a une seule route entre les deux villes. La route a trois ponts avec des limites de poids a, b, c. Pour pouvoir conduire sur cette route, le camion doit d'abord passer la pont avec avec une limite de poids a, puis celui avec avec une limite de poids b, et enfin celui avec avec une limite de poids c. Votre camion aura un accident s'il dépasse l'une des trois limites. Ecrivez un programme qui affiche le poids maximum qui peut être transporté sur cette route. Votre code utilisera le fait que les variables a, b, and c contiennent déjà les valeurs des poids limites pour les ponts.

print(min(a,b,c))

