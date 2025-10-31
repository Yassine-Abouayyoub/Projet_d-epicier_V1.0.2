# Projet_d-epicier_V1.0.2
## Description:
Cette version du programme permet à l'utilisateur d'entrer plusieurs prix, d’obtenir le sous-total à chaque opération, et d'afficher le montant total. Elle met l'accent sur la robustesse: toutes les erreurs de saisie sont gérées de manière contrôlée, ce qui rend le programme très stable et prêt pour des évolutions futures.

## 1. Fonctionnalités:
- Saisie des prix un à un (format nombre réel accepté).

- Affichage du sous-total après chaque ajout de prix.

- Instruction claire pour arrêter la saisie en tapant « 0 ».

- Affichage du montant total à la fin.

## 2. Gestion avancée des erreurs:

- Message adapté si aucune valeur n'est saisie.

- Message clair si l'utilisateur entre une valeur négative.

- Message d’erreur explicite si la saisie n’est pas un chiffre valide.

- Interruption clavier (Ctrl+C) gérée sans crash.

- Guidance pour les fonctionnalités à venir (“n” pour suppression – en développement).

## 3. Améliorations apportées par rapport à la version précédente:

- Plus aucune entrée ne provoque le crash du programme.

- Erreurs différenciées selon le contexte et expliquées à l’utilisateur.

- Saisie vide, caractères spéciaux et opérations inattendues entièrement sécurisées.

- Affichage amélioré (guides et sous-totaux) pour plus de clarté.

## 4. Limitations connues:
- La fonctionnalité “suppression d’un élément saisi” (taper « n ») n’est pas encore active – mentionnée à titre d’information.

- Les cas très spécifiques de format (ex : virgule à la place du point selon le clavier) ne sont pas totalement gérés.

- Pas encore de gestion de fichiers ou d’interface graphique.

## 5. Prochaines étapes envisagées:
- Activer la fonctionnalité de suppression d’une valeur saisie (passage à V1.1.0).

- Ajouter un historique ou un système d’annulation.
