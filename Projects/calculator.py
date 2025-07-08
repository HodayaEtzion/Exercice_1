import math

# Dictionnaire des fonctions autorisées
allowed_names = {
    k: v for k, v in math.__dict__.items() if not k.startswith("__")
}

# Ajout de fonctions supplémentaires si besoin
allowed_names.update({
    "abs": abs,
    "round": round
})
fff

print("=== Calculatrice Scientifique ===")
print("Tapez 'quit' pour quitter.")

while True:
    expr = input(">>> ")
    
    if expr.lower() in ["quit", "exit"]:
        print("Au revoir !")
        break

    try:
        # Evaluation sécurisée de l'expression
        result = eval(expr, {"__builtins__": {}}, allowed_names)
        print("Résultat:", result)
    except Exception as e:
        print("Erreur :", e)


  