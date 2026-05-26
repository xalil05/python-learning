# --- Tes fonctions restent identiques ---
def print_welcome_message():
    print("Bienvenue sur la mini-calculatrice !")
    
def input_two_number():
    num1 = float(input("Entrez le premier nombre : "))
    num2 = float(input("Entrez le deuxième nombre : "))
    return num1, num2

def print_menu_and_get_choice():
    print("\n=== MENU ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter") # Ajout d'une option pour sortir proprement

    user_choice = input("Entrez votre choix (1-5) : ")
    while user_choice not in ["1", "2", "3", "4", "5"]:
        user_choice = input("Choix invalide. Entrez votre choix (1-5) : ")
    return user_choice

def sum(a, b): return a + b
def subtraction(a, b): return a - b
def multiplication(a, b): return a * b
def division(a, b):
    if b != 0:
        return a / b
    else:
        print("Erreur : division par zéro")
        return None

def run_calculation(user_choice):
    num1, num2 = input_two_number()
    match user_choice:
        case '1': result = sum(num1, num2)
        case '2': result = subtraction(num1, num2)
        case '3': result = multiplication(num1, num2)
        case '4': result = division(num1, num2)
        case _: result = None
    return result

# --- C'EST ICI QUE TOUT SE JOUE ---
if __name__ == '__main__':
    print_welcome_message()
    
    continuer = "oui"
    
    while continuer == "oui":
        user_choice = print_menu_and_get_choice()
        
        # Si l'utilisateur choisit 5, on arrête tout de suite
        if user_choice == "5":
            break
            
        result = run_calculation(user_choice)
        
        if result is not None:
            print(f"Le résultat est : {round(result, 2)}")
        
        # On demande si on veut recommencer
        continuer = input("\nVoulez-vous faire un autre calcul ? (oui/non) : ").lower()

    print("Fin du programme et au revoir !")