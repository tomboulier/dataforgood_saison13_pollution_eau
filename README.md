# Rendre Visible la Pollution de l'Eau Potable 💧

## Contexte du Projet

Ce projet, développé par des bénévoles de [Data For Good](https://www.dataforgood.fr/) lors de la saison 13, vise à créer une carte interactive pour [Générations Futures](https://www.generations-futures.fr/).

L'objectif est de consolider, analyser et cartographier les données sur la qualité de l'eau potable en France à partir de sources de données ouvertes.

## Structure du Projet

- `pipelines/` : Consolidation et préparation des données
- `analytics/` : Analyse des données
- `webapp/` : Développement du site web interactif

## Installation

- [Installation de Python](#installation-de-python)

Ce projet utilise [uv](https://docs.astral.sh/uv/) pour la gestion des dépendances Python. Il est préréquis pour l'installation de ce projet.

Une fois installé, il suffit de lancer la commande suivante pour installer la version de Python adéquate, créer un environnement virtuel et installer les dépendances du projet.

```bash
uv sync
```

A l'usage, si vous utilisez VSCode, l'environnement virtuel sera automatiquement activé lorsque vous ouvrirez le projet. Sinon, il suffit de l'activer manuellement avec la commande suivante :

```bash
source .venv/bin/activate
```

Ou alors, utilisez la commande `uv run ...` (au lieu de `python ...`) pour lancer un script Python. Par exemple:

```bash
uv run pipelines/run.py run build_database
```

- [Installation de Node.js](#installation-de-nodejs) (pour le développement du site web et pour l'usage de Evidence)

Pour le développement du site web et pour l'usage de [Evidence](https://evidence.dev/), il est nécessaire d'installer Node.js. Pour cela, il suffit de suivre les instructions sur le [site officiel](https://nodejs.org/).

Pour installer les dépendances du site web, il suffit de lancer les commandes suivantes :

```bash
cd webapp
npm install
```
