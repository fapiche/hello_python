# Calculateur de tarif v1
# Règle métier :
# 0-3 ans : gratuit
# 4-17 ans : tarif jeune (1.20€)
# 18-24 ans : tarif étudiant (1.00€)
# 25-63 ans : tarif plein (2.00€)
# 64 ans et + : tarif senior (1.50€)

#CONSTANTE DES TARIFS
TARIFS = [(4, 0.00, "gratuit"), (18, 1.20, "jeune"), (25, 1.00, "étudiant"), (64, 2.00, "plein"), (150, 1.50, "sénior")]

#Fonction permettant de récupérer le tarif en fonction de l'age du voyageur
def obtenir_tarif(age):
    for seuil, tarif, categorie in TARIFS:
        if age < seuil :
            return tarif, categorie