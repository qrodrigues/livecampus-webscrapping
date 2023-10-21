# Evaluation : Python
```
Expliquer la phrase :
 “Pensez à bien utiliser cette commande dans le même terminal que celui que vous utilisez pour exécuter vos fichiers .py.“
```
La phrase mentionne l'importance d'executer la commande pour afficher les versions utilisées dans le même terminal que là où à lieu l'exécution des scripts python.

En effet, pour être sûr que les versions utilisées pour l'exécution, et celles indiquées par la commande soient les mêmes, il faut être dans le même terminal.

Par exemple, en créant un nouveau terminal, nous perdons l'utilisation de l'environnement python si on utilise pas le script "activate". Ainsi, les versions différentes peuvent empêcher le code de bien fonctionner.

De plus, si on développe sur un version de python qui n'est pas la bonne, nous pouvons détruire une partie de notre système, qui utilise python.

 # Général
 

 # Scrapping [1/2]
 Pour le scrapping, nous avons choisi de créer une class nommée webscrapper. Qui est utilisable de cette manière :
 ```py
 scrapper = ScrapEpisodes(base_url, url)
 ```
Elle prend en paramètre l'url de base, et la route à scrapper. Le choix de séparer l'url nous permet de garder l'URL de base pour chercher dans les pages de chaque épisode.

Elle contient plusieurs méthodes.
```
__init__() : permet d'initialiser la méthode.
getSourceCode() : permet d'obtenir le code source de la page.
getAllEpisodes() : scrappe et retourne tous les épisodes dans un tableau d'objets.
```

Un objet épisode se présente comme ci-dessous :
```yml
{
    'air_date': '31-10-2023',
    'origin_country': 'Etats-Unis',
    'channel': 'BET',
    'series_name': 'The Oval',
    'episode_number': 3,
    'season_number': 5,
    'episode_url': 'episode03-411296-31102023-saison5-The-Oval.html',
    'duration': 42
}
```

 # Scrapping [2/2]
Afin de récupérer la durée d'un épisode, nous avons ajouté une fonction dans la class webscrapper. Cette fonction va scrapper la page de l'épisode et retourner sa durée.

La fonction est :
```
getEpisodeDuration () : permet d'obtenir la durée d'un épisode en scrappant sa page.
```

# Fichier CSV
Doc fichier csv...

 # Algorithmie [1/2]
```
 Indiquer dans le fichier README.md le nom des trois chaînes qui ont diffusé le plus d’épisodes. 
```
Les trois chaînes les plus diffusées sont : Netflix avec 108, Disney+ avec 34 et Prime Video avec 27.

```
Faire de même pour les pays (pensez à mutualiser votre code !)
```
Les trois pays les plus diffusés sont : Etats-Unis avec 355, France avec 76 et Canada avec 63.

```
Quels sont les 10 mots les plus présents dans les noms des séries ? 
```
1 - "The" utilisé 66 fois.  
2 - "of" utilisé 31 fois.  
3 - "de" utilisé 24 fois.  
4 - "(2023)" utilisé 19 fois.  
5 - "Pacto" utilisé 18 fois.  
6 - "Silencio" utilisé 18 fois.  
7 - "Les" utilisé 17 fois.  
8 - "the" utilisé 16 fois.  
9 - "(UK)" utilisé 12 fois.  
10 - "Everything" utilisé 11 fois.


 # Algorithmie [2/2]
```
Quelle est la chaîne de TV qui diffuse des épisodes pendant le plus grand nombre de jours consécutifs sur le mois d’Octobre ? 
```
Il y a beaucoup de chaîne de TV qui diffuse 2 jours consécutifs, c'est le maximum et la premiere à le faire au mois d'octobre est NBC.

# SQL [1/2]
# SQL [2/2]