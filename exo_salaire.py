"""
Exercice : Calcul de salaire avec commissions progressives

Règles :
- Salaire de base : 800€
- Ventes <= 5 000€   → 4% de commission (sur la tranche 0-5000)
- Ventes <= 10 000€  → 8% (sur la tranche 5000-10 000)
- Ventes > 10 000€   → 12% (sur la tranche >10 000)
- Bonus : +200€ si ventes > 12 000€
"""

ventes = float(input("Entrez le montant total des ventes (€) : "))

# --- Calcul progressif des commissions par tranche ---

# Tranche 1 : 0 → 5000€ à 4%
tranche1 = min(ventes, 5000)
commission1 = 0.04 * tranche1

# Tranche 2 : 5000 → 10000€ à 8%
tranche2 = min(max(ventes - 5000, 0), 5000)
commission2 = 0.08 * tranche2

# Tranche 3 : > 10000€ à 12%
tranche3 = max(ventes - 10000, 0)
commission3 = 0.12 * tranche3

total_commissions = commission1 + commission2 + commission3

# --- Bonus ---
bonus = 200 if ventes > 12000 else 0

# --- Salaire final ---
salaire = 800 + total_commissions + bonus

# --- Affichage ---
print("\n===== RÉCAPITULATIF SALAIRE =====")
print(f"Ventes totales          : {ventes:.2f} €")
print(f"Salaire de base         : 800.00 €")
print(f"Commission tranche 4%   : {commission1:.2f} €")
print(f"Commission tranche 8%   : {commission2:.2f} €")
print(f"Commission tranche 12%  : {commission3:.2f} €")
print(f"Total commissions       : {total_commissions:.2f} €")
print(f"Bonus                   : {bonus:.2f} €")
print(f"-----------------------------------")
print(f"SALAIRE FINAL           : {round(salaire, 2)} €")
