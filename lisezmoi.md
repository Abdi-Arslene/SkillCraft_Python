# SkillCraft

Mini-project


## Aperçu

Dans le jeu vidéo StarCraft, il existe une certaine relation entre la Ligue dans laquelle un joueur peut accéder et les mouvements de son écran lorsqu'il joue au jeu. Ce projet essaie de trouver le meilleur modèle et les meilleures fonctionnalités pour prédire la Ligue du joueur en fonction de ses mouvements d'écran.

## Dataset

L'ensemble de données utilisé dans ce projet est l' [ensemble de données SkillCraft1 Master Table](http://archive.ics.uci.edu/ml/datasets/SkillCraft1+Master+Table+Dataset) de [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets.html). Il a agrégé les mouvements d'écran en fixations d'écran à l'aide d'un algorithme de seuil de dispersion de Salvucci & Goldberg (2000) et a défini les cycles d'action de perception (PAC) comme des fixations avec au moins une action.

Il y a 3395 observations et 20 variables, où `LeagueIndex` est la valeur à prédir et les autres variables sont des caractéristiques. 


## Usage

Ouvrez le Jupyter Notebook [analysis.ipynb](https://github.com/Abdi-Arslene/SkillCraft_Python/blob/master/SkillCraft.ipynb).


## Dépendences

- Python
- Jupyter Notebook
- Python Packages:
	- `numpy`
	- `pandas`
	- `matplotlib`
	- `sklearn`
