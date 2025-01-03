# treejsonapp

> **Affiche l’arborescence d’un fichier JSON via une interface graphique Tkinter.**

## Sommaire
1. [Aperçu](#aperçu)  
2. [Installation](#installation)  
3. [Utilisation](#utilisation)  

---

## Aperçu

**treejsonapp** est un petit package Python permettant de visualiser l’arborescence (structure) de fichiers JSON à l’aide d’une interface Tkinter.  
- Chargement d’un fichier JSON via un bouton « Ouvrir ».  
- Affichage sous forme d’arbre (TreeView) répliquant la hiérarchie (objets, listes, clés/valeurs).  
- Simplifie la lecture et l’exploration de documents JSON volumineux.

### Structure du projet

```
.
├── setup.py
└── treejsonapp
    ├── __init__.py
    └── gui.py
```

1. **treejsonapp/** : dossier contenant le cœur du package.  
   - **`__init__.py`** : indique que `treejsonapp` est un package Python.  
   - **`gui.py`** : contient le code principal pour créer la fenêtre Tkinter et afficher la structure JSON.  
2. **`setup.py`** : configuration d’installation du package.

---

## Installation

### 1) Récupérer le code

- **Option A :** Cloner ce dépôt, puis installer en mode « editable » :

  ```bash
  git clone https://github.com/n-pizzetta/treejsonapp.git
  cd treejsonapp
  pip install -e .
  ```

- **Option B :** Installer directement depuis GitHub (sans cloner) :

  ```bash
  pip install git+https://github.com/n-pizzetta/treejsonapp.git
  ```

### 2) Vérifier les dépendances

- Python 3.7+
- Tkinter est habituellement inclus nativement avec Python, mais au besoin, on a aussi la mention `tk==0.1.0` dans `setup.py`.

---

## Utilisation

Une fois installé, la commande d'utilisation est la suivante :

  ```bash
  treejsonapp
  ```

Une fois la fenêtre lancée, le bouton **« Ouvrir un fichier JSON »** permet de charger un fichier `.json`. L’arborescence s’affichera dans la `TreeView`.

---

**Merci d’utiliser treejsonapp !**