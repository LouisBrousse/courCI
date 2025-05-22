# courCI
Cours CI avec M. E. Sandre
groupe: Barbot Aymeric, Brousse Louis, Vitry Marie-Ornella, Vidal Samuel

# Choix de Github Actions

GitHub Actions est un outil d'intégration continue léger, directement intégré à GitHub, le client utilisé pour ce projet.
Son usage est plus pertinent que celui d’outils lourds comme Jenkins, dont la complexité serait injustifiée ici.
Bien que gratuit et soumis à certaines limites (VM partagées, 2 000 minutes par mois, écriture manuelle des fichiers de workflow en YAML), GitHub Actions reste largement suffisant pour automatiser les tests et tâches nécessaires.

Difficultés rencontrées : Dans Github Actions, le workflow est présent dans le projet sous forme de fichier YAML, ce qui pollue l'historique des branches jusqu'à ce que la CI fonctionne.

## workflow :
apres chaque CI réussi commandes à faire en local :
    git fetch origin
    git checkout main
    git pull origin main    # Met à jour main locale avec remote

    git checkout dev
    git pull origin dev     # Met à jour dev locale avec remote

création d'une nouvelle feature :
    git checkout dev         # Se baser sur la branche dev à jour
    git pull origin dev      # S'assurer que dev est à jour

    git checkout -b feature/<branche>

    ...FAIRE LA FEATURE...

    git commit -am "<message>"

    git push origin feature/<branche>

    sur Github, résoudre la pull request et **merger sur dev**