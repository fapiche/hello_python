#Dictionnaire des lignes de bus et de leurs terminus
lignes_bus = {
    "L1" : "Centre-Ville -  Stade municipal",
    "L2" : "Gare - Université",
    "L3" : "Hôpital - Musée",
    "L4" : "Gare routière - Aéroport",
    "L5" : "Ferme pédagogique - Lycée camille Claudel"
}
#On affiche les clés de notre dictionnaire pour présenter les lignes disponibles et on les sépare par une virgule
lignes =", ".join(lignes_bus.keys())
#On récupère la ligne choisie par l'utilisateur en forçant la casse et en supprimant les espaces
ligne_choisie = input(f"Lignes disponibles : {lignes} \nQuelle ligne de bus souhaitez-vous emprunter ?  ").strip().upper()
#On vérifie l'existence de la ligne choisie dans notre dictionnaire et on affiche le résultat, sinon affiche un message d'erreur
terminus = lignes_bus.get(ligne_choisie, "INCONNUE")

if terminus == "INCONNUE" :
    print(f"{ligne_choisie} non présente dans notre réseau.")
else:
    print(f"Le terminus de la {ligne_choisie} est : {terminus}.")
