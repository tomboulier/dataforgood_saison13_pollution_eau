## Présentation

Ce projet a pour objectif de consolider, analyser et créer une cartographie sur la qualité de l'eau potable en France à partir de données ouvertes.
Il est porté par des bénévoles de l'association [Data For Good](https://www.dataforgood.fr/) dans le cadre de la saison 13, pour le compte de l'association [Générations Futures](https://www.generations-futures.fr/).

Le projet est divisé en 3 parties :

- Consolidation des données, dans le dossier `pipelines`
- Analyse des données, dans le dossier `analytics`
- Création de la cartographie, dans le dossier `webapp`

Pour la gestion de projet, nous utilisons les outils de l'association, à savoir Slack, Outline et NocoDB.

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
