nombre = input("Saisissez des nombres séparés par des virgules: ")
liste = nombre.split(",")
# transformons les éléments de la liste en entiers
liste_des_entiers = []
for nombre in liste:
    nombre_entier = int(nombre)
    liste_des_entiers.append(nombre_entier)
# Affichons la liste des entiers
print("Voici la liste des entiers:", liste_des_entiers)
# calculons et affichons la somme des nombres
somme = sum(liste_des_entiers)
print("La somme des nombres est:", somme)
# ou bien
# somme = 0
# for nombre_entier in liste_des_entiers:
#     somme += nombre_entier
# print("La somme des nombres est:", somme)
# Calculons et affichons la moyenne
moyenne = sum(liste_des_entiers) / len(liste_des_entiers)
print("La moyenne des nombres est:", moyenne)
# Nombres supérieurs à la moyenne
for nombre_entier in liste_des_entiers:
    if nombre_entier > moyenne:
        print("Le nombre", nombre_entier, "est supérieur à la moyenne.")
