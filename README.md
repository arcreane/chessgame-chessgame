♟️ Jeu d'Échecs en Python

Projet réalisé dans le cadre du module I1 – Projet Informatique (2025/2026).

👥 Équipe

-Nicolas - Player/AIPlayer
-Ahmed - Timer/Deplacement
-Tom - Deplacement
-Clément - Board
-Tidjani - Pion

📋 Description

Implémentation d'un jeu d'échecs en Python avec une approche orientée objet.  
Le jeu se joue à deux joueurs (humain vs humain, ou humain vs IA) sur un plateau 8×8.

🚀 Lancement

```bash
python main.py
```

> Python 3.x requis. Aucune dépendance externe nécessaire pour la version texte.  
> Si vous utilisez une interface graphique (Tkinter / Pygame), installez les dépendances ci-dessous.

Dépendances (optionnelles)

```bash
pip install pygame   # si interface Pygame
```

🗂️ Structure du projet
🎮 Règles implémentées

- ✅ Déplacements standards des 6 types de pièces
- ✅ Détection des cases occupées (même couleur / prise adverse)
- ✅ Vérification de l'échec et mat
- ✅ Sauvegarde et restauration de partie (fichier JSON)
- ✅ Mode IA (déplacement aléatoire)
- ❌ Roque
- ❌ Prise en passant
- ❌ Promotion des pions

💾 Sauvegarde / Restauration

La partie en cours peut être sauvegardée et rechargée via le menu du jeu.  
Le fichier de sauvegarde est stocké au format JSON dans le dossier `saves/`.

🧪 Tests unitaires

Les tests sont écrits avec le framework `unittest`.

```bash
python -m unittest discover tests/
```

📌 Fonctionnement

Au lancement, le jeu demande le nom des deux joueurs.  
Saisir `AI` comme nom pour jouer contre l'intelligence artificielle.

Les coups sont saisis au format : `[Pièce][Case origine] [Case destination]`  
Exemples :
- `Nb1 Nc3` → le Cavalier en b1 se déplace en c3
- `Pe2 Pe4` → le Pion en e2 avance en e4

(a été changé)

🏗️ Améliorations envisagées

- [ ] Interface graphique (Pygame)
- [ ] Timer
- [ ] IA améliorée
- [ ] Roque et prise en passant

📄 Licence

Projet académique – ISEP – 2025/2026

📄Trello

https://trello.com/b/pjK3Ocrg/echec

