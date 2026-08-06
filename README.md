# ⚡ Observatoire du mix énergétique français

Pipeline de données et dashboard interactif basé sur l'API [éco2mix](https://www.rte-france.com/eco2mix) de RTE, retraçant l'évolution du mix électrique français et de son intensité carbone depuis 2012.

**🔗 Démo en ligne :** _à venir (Streamlit Community Cloud)_

---

## 🎯 Problématique

> Quelle place occupent encore les énergies fossiles dans le mix électrique français, et comment cela se reflète-t-il dans la trajectoire d'intensité carbone depuis 2012 ?

Ce projet répond à cette question à travers trois angles de lecture :

1. **Évolution de la part des fossiles** (fioul, charbon, gaz) dans le mix de production depuis 2012
2. **Trajectoire de l'intensité carbone** (`taux_co2`) sur la même période
3. **Mise en regard des deux** — dans quels contextes (saison, disponibilité du nucléaire, heure de la journée) le poids des fossiles se traduit en pics d'intensité carbone

---

## 📊 Aperçu

_Captures d'écran du dashboard à ajouter ici une fois la Phase 4 livrée._

---

## 🏗️ Architecture

```
Récupération (API éco2mix, cron 15 min)
        │
        ▼
Stockage brut (CSV récent → Parquet archive, Cloudflare R2)
        │
        ▼
Nettoyage (pandas : NaN, anomalies flaguées, datetime unifié)
        │
        ▼
Stockage propre (SQLite/Turso récent + Parquet agrégé ancien)
        │
        ▼
Visualisation (Plotly — fonctions pures, DataFrame → figure)
        │
        ▼
Dashboard (Streamlit, déployé sur Streamlit Community Cloud)
```

## 🛠️ Stack technique

| Couche          | Techno                                    | Pourquoi                                                                          |
| --------------- | ----------------------------------------- | --------------------------------------------------------------------------------- |
| Récupération    | Python, `requests`, GitHub Actions (cron) | Pas de serveur à maintenir, aligné sur le rythme de rafraîchissement de la source |
| Stockage brut   | CSV / Parquet, Cloudflare R2              | VM GitHub Actions éphémère → stockage objet externe nécessaire                    |
| Nettoyage       | pandas                                    | Standard du traitement tabulaire en Python                                        |
| Stockage propre | SQLite (Turso) + Parquet agrégé           | Un seul writer, lectures modestes, pas besoin d'un vrai serveur DB                |
| Visualisation   | Plotly                                    | Graphiques interactifs, fonctions découplées du dashboard                         |
| Dashboard       | Streamlit                                 | Progression pédagogique douce avant Django, déploiement gratuit et rapide         |

## 📁 Structure du repo

```
src/
  recovery/         → récupération des données (API, pagination)
  raw_storage/       → écriture des données brutes
  cleaning/          → nettoyage et normalisation
  clean_storage/      → écriture en base propre
  visualization/     → fonctions DataFrame → figure Plotly
  dashboard/         → application Streamlit
tests/
  (miroir de src/)
docs/
  architecture.md
  database.md
.github/
  workflows/
.env.example
.gitignore
requirements.txt
README.md
LICENSE
setup.py
Makefile
```

## 🚀 Installation locale

```bash
git clone https://github.com/lea-dieudonat/energy_mix_observatory_fr.git
cd energy_mix_observatory_fr
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # renseigner les clés si besoin
```

## 🧪 Tests

```bash
pytest tests/
```

## 📈 Résultats clés

_À renseigner une fois l'analyse menée (Phase 4) — ex. évolution en points de % de la part des fossiles dans le mix, contextes (saison, disponibilité du nucléaire) associés aux pics d'intensité carbone, etc._

## 🗺️ Roadmap

- [x] Pipeline de récupération avec pagination robuste
- [x] Nettoyage des données (`clean_data`)
- [ ] Gestion des anomalies flaguées
- [ ] Stockage propre (SQLite/Turso)
- [ ] Premier graphique Plotly
- [ ] Dashboard Streamlit déployé
- [ ] CI (lint + tests)
- [ ] Historisation multi-années
- [ ] Documentation `docs/architecture.md` et `docs/database.md`

## 📄 Licence

MIT — voir [LICENSE](./LICENSE)
