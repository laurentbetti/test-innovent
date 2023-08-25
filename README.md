# test-innovent

## BDD / Données :

- J'ai utilisé Docker pour la bdd (et l'interface Adminer), d'où le fichier `compose.yaml`
- Je n'ai pas voulu mettre les données sur le repo, vu qu'il va être public quelques temps :)
- A partir des fichiers que tu m'as donnés, j'ai créé les structures des trois tables via Adminer
- J'ai ensuite fait un import des fichiers CSV
- Plus tard, j'ai utilisé la commande `inspectdb` de Django pour générer les modèles correspondants (et mis
  le flag `managed=false`)

## Back (Django)

- `cd back/`
- (optionnel : se créer une environnement virtuel)
- `pip install -r requirements.tx`
- `python manage.py migrate`
- `python manage.py runserver`

## Front (Vue 3)

_J'ai utilisé Vue 3 car c'était plus facile de trouver de la doc à jour, mais comme je l'utilise en mode
`Options Api`, il n'y a quasiment rien qui change par rapport à Vue2_

- Dans un autre terminal : `cd front/`
- `yarn` ou `npm i`
- `yarn dev` ou `npm run dev`

## Visualisation du résultat :

se rendre sur `http://localhost:5173/` (ie, URL affichée dans le retour de la commande `yarn dev`)

Remarque de perf : dans du code que je n'ai pas commité, j'utilise `Django-debug-toolbar` qui me donne les stats suivantes :

- Nb de query sur la DB = 1
- Temps total de traitement de la requête HTTP = 378ms (dont 268ms sur la DB)
