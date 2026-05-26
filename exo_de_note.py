# exo_de_note.py — Analyse de notes
# Accepte des notes séparées par des virgules
# Calcule moyenne, max, pourcentage réussite, et message motivant

notes = input("Entrez vos notes separees par des virgules : ")
liste_notes = notes.split(",")

notes_rattrapages = []  # notes < 10
autres_notes = []       # notes ≥ 10

for note in liste_notes:
    note = int(note)
    if note < 10:
        notes_rattrapages.append(note)
    else:
        autres_notes.append(note)

def compteur_reussites(liste):
    """Compte le nombre de notes ≥ 10"""
    total = 0
    for note in liste:
        if note >= 10:
            total += 1
    return total

moyenne = sum(autres_notes + notes_rattrapages) / len(liste_notes)
meilleure_note = max(autres_notes + notes_rattrapages)

print(f"Votre moyenne est : {moyenne}")
print(f"Votre meilleure note est : {meilleure_note}")

if moyenne >= 16:
    print("❤️❤️❤️ Excellent travail ! Continue comme ça !")
elif moyenne >= 12:
    print("💚💚💚 Bon travail ! Tu peux encore progresser !")
elif moyenne >= 10:
    print("💛💛💛 C'est juste, mais tu peux mieux faire !")
elif moyenne >= 8:
    print("🤍🤍🤍 Encore un petit effort !")
else:
    print("🧡🧡🧡 Ne te décourage pas ! L'important c'est d'apprendre !")

# Stats supplémentaires
total_notes = len(liste_notes)
reussies = compteur_reussites(autres_notes)
pourcentage = (reussies / total_notes) * 100

print(f"Nombre de notes : {total_notes}")
print(f"Notes de rattrapage : {notes_rattrapages}")
print(f"Notes ≥ 10 : {autres_notes}")
print(f"Pourcentage de réussite : {pourcentage}%")
