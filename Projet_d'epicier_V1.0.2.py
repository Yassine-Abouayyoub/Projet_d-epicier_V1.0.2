print("Le programme est en cours de développement!")
print("BONJOUR")
S = 0
while True:
    try:
        print("\nGuid: \n", "- Tapez 0 si vous souhaitez terminer \n","- Tapez la lettre « n » si vous souhaitez supprimer la valeur d'un élément.(En développement)" )
        P = input(" ecrire le prix: ")
        if P == "":
            raise ValueError("Aucune valeur entrée !")
        P = float(P)
        if P > 0:
            S = S + P
            print(S, " DH")
            continue
        if P == 0:
            print("Montant total est ", S, " DH")
            break
        else:
            raise ValueError("La valeur que vous avez saisie est inférieure à 0.")
    except ValueError as e:
        print("⚠️ Erreur: ", e)
        continue
    except KeyboardInterrupt:
        continue
