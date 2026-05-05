from tarifs import obtenir_tarif

#Fonction pour lire un nombre entier avec gestion d'erreur
def lire_entier(message, message_erreur="Veuillez entrer un nombre entier.", min_value=None, max_value=None):
    while True:
        try:
            nombre = int(input(message))
            if (min_value is not None and nombre < min_value) or (max_value is not None and nombre > max_value):
                if min_value is not None and max_value is not None:
                    print(f"Veuillez entrer un nombre entier entre {min_value} et {max_value}.")
                elif min_value is not None:
                    print(f"Veuillez entrer un nombre entier supérieur ou égal à {min_value}.")
                elif max_value is not None:
                    print(f"Veuillez entrer un nombre entier inférieur ou égal à {max_value}.")
            else: return nombre
        except ValueError:
            print(message_erreur)
if __name__ == "__main__":
    #On demande à l'utilisateur combien de voyageurs ils sont et on stocke cette information dans une variable
    nombre_voyageurs = lire_entier("Combien de voyageurs êtes vous? ", "Veuillez entrer un nombre entier pour le nombre de voyageurs.", 1,250)

    #Listes servant à stocker les information des différents voyageurs
    ages = []
    tarifs = []
    categories = []

    #On boucle pour chaque voyageur
    for i in range(nombre_voyageurs):
        age = lire_entier(f"Quel est l'âge du voyageur {i+1}? ", "Veuillez entrer un nombre entier pour l'âge du voyageur.", 0, 122)
        tarif, categorie = obtenir_tarif(age)
        print(f"Voyageur {i+1} : {age} ans -> tarif {categorie} : {tarif:.2f} €")
        ages.append(age)
        tarifs.append(tarif)
        categories.append(categorie)
    #Fin de boucle for
    #On affiche le tarif total pour tous les voyageurs²
    print(f" \nTarif total pour {nombre_voyageurs} voyageur(s): {sum(tarifs):.2f} € ")
    
# Tarif réduit senior
tarif_senior = 0.75
print(f"Tarif senior : {tarif_senior} €")
