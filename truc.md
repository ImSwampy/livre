# Python #

---

## Sommaire ##

### [1. Introduction et concepts](#1-introduction-et-concepts)
  * [1.1. Fonctionnement d'un ordinateur](#11-fonctionnement-dun-ordinateur)
    * [1.1.1. Les composants](#les-composants)
    * [1.1.2. Mémoire RAM](#mémoire-ram)
    * [1.1.3. CPU](#processeur)
      * [1.1.3.1. Threads](#threads)
      * [1.1.3.2. Cache](#cache)
    * [1.1.4. GPU](#carte-graphique)
      * [1.1.4.1. Traitement des données](#traitement-des-données)
  * [1.2. Python et ses applications](#12-python-et-ses-applications)
    * [1.2.1. Les domaines adaptés](#les-domaines-adaptés)
    * [1.2.1. Les domaines non-adaptés](#les-domaines-non-adaptés)
  * [1.3. Python et son environnement](#13-python-et-son-environnement)
    * [1.3.1. Package Manager](#le-package-manager)
    * [1.3.2. Les librairies](#les-librairies)
      * [1.3.2.1. Les librairies standards](#les-libraries-standards)
      * [1.3.2.2. Les librairies populaires](#les-libraries-populaires)
    * [1.3.3. Conda](#conda)
  * [1.4. Langage interprété vs. compilé vs. Byte-code](#14-langage-interprété-vs-compilé-vs-byte-code)
    * [1.4.1. Langage Interprété](#langage-interprété)
    * [1.4.2. Langage Compilé](#langage-compilé)
    * [1.4.3. Langage Byte-code](#langage-byte-code)
    * [1.4.4. Comparaison](#comparaison)
  * [1.5. Types statiques et Types dynamiques](#15-types-statiques-vs-types-dynamiques)
    * [1.5.1. Types statiques](#types-statiques)
    * [1.5.2. Types dynamiques](#types-dynamiques)
    * [1.5.3. Conclusion sur les types](#conclusion-sur-les-types)
  * [1.6. L'algorithmie et les mathématiques dans la programmation](#16-lalgorithmie-et-les-mathématiques-dans-la-programmation)
  * [1.7. Les conventions](#17-les-conventions)

### [2. Les outils](#2-les-outils)
  * 2.2. Les IDEs
  * 2.3. Les éditeurs de texte
  * 2.4. Les debuggers
  * 2.1. IDE vs. éditeur de texte
  * 2.5. Environnement Python
    * 2.5.1. Pipenv
    * 2.5.2. Virtualenv
    * 2.5.3. Conda env
  * 2.6. Le Package Manager

### 3. Les bases
  * 3.1. Les notations / particularitées syntaxique
  * 3.2. Les variables et ses types
  * 3.3. Les commentaires
  * 3.4. Les boucles
    * 3.4.1. For loop
    * 3.4.2. While loop
  * 3.5. Les conditions
    * 3.5.1. Les comparaisons
    * 3.5.2. If
    * 3.5.3. Elif
    * 3.5.4. Else
    * 3.5.5. Switch
  * 3.6. Les fonctions
  * 3.7. Les classes
- __Projet : créé une carte d'identité__

### 4. Python dans son ensemble
  * 4.1. L'importation de library
  * 4.2. Les library de base
  * 4.3. L'aléatoire
  * 4.4. Ouvrir et fermer des fichiers
  * 4.5. Les dictionnaires et JSON
  * 4.6. Les Listes
  * 4.7. Les classes : avancé
    * 4.7.1. Inhéritance
    * 4.7.2. Encapsulation
    * 4.7.3. Polymorphisme
- __Projet : créer un fichier d'identité avancé__

### 5. Python avancé : plongé dans le threading, l'asynchrone et le web
  * 5.1. Les library web
  * 5.2. Le front-end vs. back-end
  * 5.3. L'API
  * 5.4. Les bases de données SQL
  * 5.5. Les bases de données no-SQL
  * 5.6. Envoyer et recevoir des informations avec les websockets
  * 5.7. Faire un serveur API
  * 5.8. Utiliser une API tierce
- __Projet : faire un site de création et distribution de fiche d'identité__

___


# 1. INTRODUCTION ET CONCEPTS

## 1.1. Fonctionnement d'un ordinateur.

### Les composants

Un ordinateur est une machine complexe, qui, a l'aide de calculs, nous aident au quotidien. Que ce soit au travaille, a l'école, à la bibliothèque, ou que vous vouliez acheter un article en ligne, ou même regarder une vidéo, vous utiliserez un ordinnateur.

Pour commencer, parlons des composants :
- CPU : _Central Processing Unit_, c'est l'élément principal qui va nous permettre de faire ces calculs. Elle est composée d'une `horloge` qui est définie en _Hz_, et qui définie le nombre d'actions réalisé/réalisable par seconde. Il est aussi composé de `coeurs`, qui vont être cadencé et ordonné par l'`horloge`, qui effectueront leurs tâches associées. Les `threads` peuvent être représenté comme une boite, qui sera dépendante d'un `coeur`, qui effectuera le travaille envoyé par l'`horloge` a son coeur associé.


- GPU : _Graphics Processing Unit_, celle-ci n'est pas obligatoire, mais généralement nécessaire pour les ordinateurs de travail ou autre. Elle permet de faire de nombreux calculs en temps réel simultanément. Elle fonctionne en couche appelée `layer`, empilé les une sur les autres, commandé par de complexe calculs de vecteur et de matrices.


- RAM : _Random Access Memory_, un élément très important dans la programmation, car c'est généralement a l'utilisateur de décider de comment l'utilisé, en revanche, cela est moins importante en Python. Elle est stock les données de manière temporaire, par exemple, les valeurs d'une variable dans un programme. Elle est différente du stockage physique (disque dur, etc.), parce qu'elle permet d'accéder très rapidement à une valeur, mais a pour inconvénient d'être réinitialisé lorsqu'elle n'est plus alimenté.


- Carte Mère : _MotherBoard_, c'est le composant qui relie tous ceux précédents entre eux. Elle n'a pas tant de fonctionnalité en elle-même, mais peut tout de même être couplé a une carte wifi par exemple, qui captera les réseaux wifis, et d'autre encore.



### Mémoire RAM

La mémoire RAM est composé de 2 éléments pour chaque emplacement : l'`adresse` et la `valeur`. En réalité, dans beaucoup de language de programmation, si ce n'est tous, la mémoire utilisé est une `mémoire virtuelle`, qui sera entièrement gérée par le système d'exploitation; celui-ci va alors décider de l'organisation dans la `mémoire physique`. Ce processus permet d'éviter les erreurs de mémoire (exemple : 2 programme qui veulent accéder a la même adresse), et donc ajouté une couche de protection pour l'utilisateur et les applications elles même. 

Prenons ce tableau en exemple :

| Adresse Virtuelle | Adresse Physique  | Valeur | Valeur réel | 
|:-----------------:|:-----------------:|:------:|:-----------:|
|     0x73B1FF      |     0x093F82      |   73   |  01001001   |
|     0x73B200      |     0x2F783A      |  `s`   |  01110011   |
|     0x73B201      |     0xB3E012      |  True  |  00000001   |

Voici ce comment on accèderait a une valeur :
```
valeur(0x73B1FF) -> 73
```

Alors qu'en réalité :
```
valeur(0x73B1FF) -> physique(0x093F82) -> valeur(01001001) en chiffre -> 73
```

### Processeur

Comme vu précédemment, le processeur est constitué d'une horloge et de coeurs, qui sont eux même composé de threads.
On peut imaginer un processeur tel une entreprise :
 * L'horloge est comme une horloge dans une entreprise qui définit le rythme de travail, mais ne prend pas de décisions.
 * Les coeurs sont des employés capables d'exécuter des tâches de manière indépendante, et c'est le système d'exploitation (un manager) qui leur assigne des tâches.
 * Les threads sont des sous-équipes au sein de chaque employé (coeur), qui divisent les tâches pour être effectuées simultanément dans un même coeur.

Pour résumer, voici l'arbre hiérarchique du processeur :

```
Horloge --- rythme de travail ---> coeur --- instructions ---> threads (si Hyper-Threading) --- sous-tâches
```

##### Threads

Les threads sont souvent utilisés dans des applications ou projets à charge lourde, qui ont un besoin critique de performance ou de parallélisme dans les taches effectuées (simultanées).
En programmation, on affecte fréquemment des fonctions complexes ou longue aux threads, afin de ne pas ralentir le programme entier.
Par exemple, en Python :

Considérons cette fonction
```python
def prime_numbers(n: int, start: int = 2) -> list[int]:
    # éviter les erreurs de paramètres
    if n <= 1:
        print("Erreur, chiffre trop petit")
        return []
    if start < 2:
        print("Erreur, début trop petit")
        return []
    
    # le "coeur" de la fonction
    result: list[int] = [] # le resultat qu'on renverra 
    for i in range(start, n):
        for j in range(start, i):
            if (i % j) == 0: # si le nombre est un multiple entier autre que 1 ou le même
                break
        else:
            result.append(i) # ajouter ce nombre au resultat
    return result
```

Cette fonction renvoi une liste des nombres premiers compris entre `start` et `n`. Elle n'est pas optimisé, et peut prendre beaucoup de temps a éxecuter lors de paramètre plus élevés.

```python
import time

goal: int = 100_000 # le nombre maximal

curr = time.time() # le temps avant le lancement des fonctions
prime_numbers(goal) # les nombres premier compris entre 2 et 100,000
print(time.time() - curr) # affiche le temps actuelle - celui avant la fonction afin de déterminé son temps d'éxectution
```
```
17.05051851272583
```
Soit 17 secondes pour trouver tous les nombres premiers de 2 à 100,000.

Maintenant, éxecutons cette fonction 2 fois, simultanément.

```python
import time
import threading    

goal: int = 100_000 # le nombre maximal

thread1 = threading.Thread(target=prime_numbers, args=(goal//2, 2)) # le 1er thread executera la fonction de 2 à 50,000
thread2 = threading.Thread(target=prime_numbers, args=(goal - goal//2, goal//2)) # le deuxième executera la fonction de 50,000 à 100,000

curr = time.time() # le temps avant le lancement des fonctions

# lancer les threads
thread1.start() 
thread2.start()

# attendre la fin de leurs opérations
thread1.join()
thread2.join()

print(time.time() - curr) # le temps entre le lancement des fonctions et leurs fin
```
```
4.005001544952393
```

Comme on peut le constater, le fait d'avoir réparti cette fonction sur 2 threads simultanés donne un résultat bien plus rapidement que sans le multithreading.

Le code ci-dessus est une illustration seulement, il n'est pas nécessaire de comprendre entièrement le code, mais uniquement de comprendre l'importance de l'utilisation de threads.


### Cache

Le cache constitue la mémoire inclut directement dans le processeur. Du fait de sa proximité avec les coeurs, il est bien plus rapide que la RAM. Les données dessus ne sont rarement chargé plus de quelques millisecondes, voire quelques microsecondes. C'est ici qu'atterrissent les données de la RAM demandée par un programme, telle une sorte de "fil d'attente".

### Carte Graphique

La carte graphique est un composant essentiel, et fréquemment utilisé, mais n'est pas indispensable. Elle permet d'afficher l'interface de l'ordinateur, dans le plus courant des cas. Elle est aussi utilisé pour sa puissance de calculs intense. Elle n'est pas requise dans les serveurs web par exemple, car seulement l'envoie et la récéption de données est utile. 

De plus en plus, les cartes graphiques sont considéré comme un des composants le plus important, principalement a cause du secteur du jeu vidéo ou encore de la crypto-monnaie.

Un GPU en lui-même est une sorte d'ordinateur compacte, en effet, elle possède une carte principale, similaire a une carte mère, BEAUCOUP de coeurs (2560 pour une NVIDIA GTX 1080), tels les processeurs, et une mémoire.
Elles sont designé pour le calcul intensif simultané, grace a leurs milliers de coeurs, malgré leurs faibles performances.

### Traitement des données

Généralement, les données utilisées par la carte graphique sont fait de matrices :

$$
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
$$


Telle celle-ci dessus, et peut subir de complexe calculs comme la rotation, addition, multiplication, et division de matrices, ou encore même des calculs de vecteurs. 

## 1.2. Python et ses applications

### Les domaines adaptés

Le langage Python est très populaire dans de multiples secteurs, et continue de croitre au fil des années. Du fait de sa simplicité, popularité et de sa grande diversité de librairies, il est commun de retrouver Python dans :
 * l'IA et la science des données : les libraries d'IA et de _Machine Learning_ (a.k.a. l'apprentissage des machines) sont faites en C++ du fait de sa rapidité, mais son ré-adapté en Python, et compose la plupart des grandes IA tel que Copilot ou ChatGPT.
 * le web, plus spécifiquement le _backend_ soit le côté serveur. Il est utilisé pour des sites modérément grands, et permet une approche simple et rapide de la conception d'un serveur web.
 * l'apprentissage, beaucoup d'école (comme la France) apprennent aux élèves les principes de l'algorithmie via Python, grace a sa simplicité et sa syntaxe très "humaine".
 * les applications, de taille petite pour la plupart, tel qu'un générateur de mot de passe, ou un _pierre, feuille, ciseaux_.

### Les domaines non-adaptés

Cependant, Python a tendance à être lent comparé à d'autre langage tel que _Java_, _C_, _C++_ ou _Go_. Cette grande faiblesse fait que Python est moins adapté dans :
 * le secteur du jeu vidéo. Les jeux vidéos en 3D demande beaucoup de puissance de calcul afin de générer la lumière, sa refraction, la physique, etc.
 * les applications hautes performances, telles que les applications de montages photo et vidéo. En revanche, certaines parties de ces applications sont codé en Python, car elle ne nécessite pas de puissance de calcul.


## 1.3. Python et son environnement

### Le Package Manager

Le package manager est un terme anglais, 
qui désigne un outil permettant entre autre l'installation de bibliothèque
ou encore de mettre en place un environnement local au projet.
Le package manager officiel de Python s'appelle `pip`.
L'installation de `packets` (des bibliothèques) nécessite une connexion internet, et ont plusieurs répertoires d'installation par défaut.
Il est possible de créer un environnement local dans notre projet, ce qui permettra à nos libraries d'être utilisable seulement par ce projet.
Ces packets (ou _packages_) sont fait en Python, et permettent au développeur d'utiliser des fonctions ou classe déjà existante.

Plusieurs moyens existent afin d'utiliser `pip`, voici une liste complète :
```shell
pip <...args>
pip3 <...args>
python -m pip <...args>
python -m pip3 <...args>
```

> &#8505;&#65039; &nbsp; Vérifiez bien que Python et (si possible) `pip` soit dans les variables d'environnement système, ou `%PATH%`, afin que la commande puisse être utilisée. Vous pouvez aussi utiliser la commande directement à partir de l'éxecutable `pip` à partir de son répertoire comme ceci : ```<chemin_vers_pip> <commande_pip>```, par exemple ```"C:\python312\Scripts\pip.exe" pip --version```.

### Les librairies

#### Les libraries standards

Python à par défaut une vingtaine de `package`, qui rassemble un large éventail de fonctionnalités. Dans la [liste officiel](https://docs.python.org/3.12/py-modindex.html) des `Standard Library` de python, les plus populaires sont :
 * `datetime` : manipulation de dates.
 * `json` : manipulation d'objets et fichier json.
 * `asyncio` : fonctions asynchrone et autre.
 * `threading` : pour le multi-threading.
 * `typing` : pour la gestion de type, et la programmation statique.
 * `math` : pour les fonctions mathématiques telles que la racine carrée.
 * `requests` : recevoir et envoyer des données par HTTP.
 * `hashlib` : fonctions de hashing.
 * `os` : fonctionnalités du système d'exploitation.
 * `sys` : fonctionnalité du système.
 * `random` : pour les opérations aléatoires.
 * `sockets` : pour la gestion de socket web.

#### Les libraries populaires

Les librairies externes les plus courantes dépendent de leurs cas d'utilisation :
 * REST API et serveurs Web :
   * `Flask` : une bibliothèque solide pour les projets de petite a grande échelle. 
   * `Django` : spécifiquement prévu pour les plus gros projets, ayant des règles plus strictes et complexes. 
   * `FastAPI` : adapté à de petits projets, son manque de fonctionnalités est compensé par ses hautes performances. 
 * IA et Science des Données :
   * `numpy` : large librarie permettant de faire des array à deux dimensions, des formules de maths complexes, et autre. (est rarement utilisé seul). 
   * `pytorch` : bibliothèque pour le _Machine Learning_. Accessible au débutant, mais tout de même puissant. 
   * `tensorflow` : équivalent de `pytorch` mais plus complex et professionnel. 
   * `scipy` : complète `numpy`.
 * Bases de données
   * `sqlite3` : pour SQLite.
   * `psycopg2` : pour PostGreSQL.
   * `pymysql` : pour MySQL.
   * `sqlalchemy` : une grande variété de base de données SQL.
   * `redis` : pour Redis (noSQL).
   * `pymongo` : pour MongoDB.
 * Les jeux
   * `pygame` : le plus populaire, permet des jeux simples.
   * `pyopengl` : utilise l'API d'OpenGL et se concentre sur les objets 3D.


### Conda

Conda est un `interpreter` Python qui cible les développeurs du secteur de l'Intelligence Artificiel. 
Il vient avec son propre environnement appelé `Conda env`, et à de nombreuses librairies installées par défaut. 
Il possède une gestion des fichiers hors normes qui isole les projets les uns des autres, 
et réduit radicalement les erreurs de version d'outils entre plusieurs projets.
Conda amène un certain nombre d'outils, 
mais en plus supporte plusieurs langages de programmation telle que _R_, _C++_, et bien plus encore.


## 1.4. Langage interprété vs. compilé vs. Byte-code

### Langage Interprété

Un langage de programmation interprété est un langage qui ne subit pas de transformation entre le code source et la sortie. Ainsi, il est dépendant de l'`interpreter`, qui va, comme son nom l'indique, interpréter le code et l'exécuté.

Pour imager, prenons un message à faire passer à quelqu'un.

_Imagine un ouvrier qui construit une maison sans plan complet. 
Il reçoit les instructions au fur et à mesure, comme quelqu'un lui dictant chaque étape sur place. 
Il pose une brique, puis attend la prochaine instruction. 
C'est ainsi qu'un langage interprété fonctionne : chaque ligne de code est exécutée immédiatement après avoir été lue,
sans plan global préétabli._

L'avantage des langages de programmation interprété se résume généralement sur le confort d'utilisation. Ceux-ci ont tendance à être plus simple à apprendre et à manier, mais sont plus lent à execute ou à `debugger` car le programme est exécuté au fur et à mesure, sans savoir l'instruction suivante. Il ce peut donc que votre programme ait une erreur après plusieurs minutes de lancement, car une instruction n'avait pas été atteinte jusqu'alors.
A noté que ces langages ont un accès très limité sur l'infrastructure de l'ordinateur, puisqu'une majeure partie est gérée par l'interpreter. Cela aussi fait d'eux des langages lents et peu performants à cause du passage à travers l'interpreter. 

> &#8505;&#65039; &nbsp; _Javascript_, _PHP_, et _Ruby_ sont tous les trois des langages de programmation interprétée.

### Langage compilé

Les langages compilés passent à travers un processus en plusieurs étapes,
qui va décortiquer le code et le transformer en binaire, puis en executable.
Cette étape est nécessaire seulement après les modifications du fichier source.
Les fichiers compilés sont directement compréhensible pour la machine, 
cela permet donc de directement communiquer avec elle, sans passer à travers un programme quelconque.
Les langages compilés sont ainsi bien plus rapide comparé aux autres languages, mais ont la spécificité de demander plus d'effort du développeur à cause de la gestion de la RAM et des types de variables. 

Pour imager ce concept, illustrons par cette analogie :

_Ici, un architecte prépare d'abord tous les plans de la maison. 
Il dessine chaque détail sur une feuille. 
Ensuite, une fois que tout est prêt, les ouvriers suivent ces plans pour construire la maison en une seule fois. 
Dans un langage compilé, le code est d'abord traduit entièrement en langage machine (les plans complets), 
puis exécuté par l'ordinateur._

> &#8505;&#65039; &nbsp; Beaucoup de langages de programmation sont compilé, on peut y retrouver notamment _C_, _Rust_ et _GoLang_.

### Langage byte-code

Le byte-code représente une étape intermédiaire d'un langage compilé : 
le code source est analysé et transcrit en _byte-code_, 
qui ne peut pas être éxecuté ou compris directement par l'ordinateur.
Un programme sous le nom de Virtual Machine, viendra interpréter ces fichiers.
On peut considérer ce système comme un entre-deux de ceux présenter précédemment. 


_L'architecte crée un plan général dans une sorte de croquis standardisé,
mais ce croquis doit être interprété différemment en fonction des outils et des matériaux disponibles. 
Avant de commencer la construction, les ouvriers utilisent un manuel spécialisé pour comprendre et adapter ce plan intermédiaire à leurs outils spécifiques. 
C'est ainsi que fonctionne le bytecode : le code est traduit en une forme intermédiaire, 
puis un interprète (machine virtuelle) le traduit pour l'ordinateur spécifique._

> &#8505;&#65039; &nbsp; Peu de langages de programmation utilisent cette technique, et les plus populaires sont _Java_ et _C# (à prononcer "C Sharp")_.


### Comparaison

|                       |                    Interprété                    |             Compilé             |          Byte-Code           |
|:---------------------:|:------------------------------------------------:|:-------------------------------:|:----------------------------:|
|   __Vitesse / 10__    |                        1                         |               10                |              7               |
|  __Cross platform*__  | Oui, mais a besoin d'un OS et de l'interpreter.  | Dépend seulement du processeur. | Besoin de la Virtual Machine |
|  __Simplicité / 10__  |                        1                         |               ~8                |              ~8              |
|   __Taille / 10**__   |                        3                         |                1                |              8               |
| __Low Level / 10***__ |                        2                         |               10                |              9               |

\* le _cross platform_ désigne la capacité d'un programme d'être compatible sur différente machine (téléphone, ordinateur Windows, Mac, etc.).

\** désigne la taille des fichiers produits. (plus petit est meilleur)

\*** fait référence à la distance d'un programme à l'ordinateur : plus un programme est _low level_, plus il aura de contrôle sur la machine.

## 1.5. Types statiques vs. Types dynamiques

Ces deux mots désignent un style de programmation, 
qui peut être employé seulement avec les langages qui supportent la définition des types en temps réel.
Le concept consiste à préciser le type de chaque variable, afin d'éviter les erreurs relaté à la mauvaise assignation de type, etc.
Par exemple : `variable1 = 123`, reviendrait à `variable1 : nombre = 123`.

> &#8505;&#65039; &nbsp; Les langages tels que _Python_, _TypeScript_, _JavaScript_ et _PHP_ supporte les 2 styles.

### Types statiques

Les types statiques, sont des types déterminés avant même l'éxecution du programme. Ceci permet à éviter les erreurs de type, et de mieux manipulé celle-ci.
En Python, pour déclarer un type, nous devons lui assigner un nom ainsi que sa valeur.
```python
# <variable> : <type> = <valeur>
variable: str = "salut"
```
Ici par exemple, nous assignons à la variable `variable` le type `string`, 
soit une chaine de caractères, une phrase, représenté en python par le mot `str`.
En revanche, cela peut causer des problèmes si l'on veut assigner cette variable à un type `NULL`,
ou `None` en Python, c'est-à-dire RIEN. Pour y remédié, on spécifie que le type peut aussi être `None`, comme cela :
```python
variable: str or None = "salut"
variable = None # ça marche 
```

### Types dynamiques

Les types dynamiques consistent seulement à ne pas préciser le type de la variable, 
et peut mener à des erreurs si l'utilisateur ne fait pas attention.

```python
variable = "salut"
variable = 123
variable = [1, 2, 3]
```

Ce code ci-dessus marchera sans problème.


### Conclusion sur les types

Il est préférable de coder avec des types statiques, pour éviter tous conflits,
et améliorer la compréhension du programme en son ensemble.

## 1.6. L'algorithmie et les mathématiques dans la programmation

La programmation, historiquement, ainsi que tout ce qui concerne l'informatique, viens des mathématiques.
Seulement, les ordinateurs ne calculs pas comme nous : nous utilisons des ensembles de chiffres, 
compris dans la base de 10, et utilisons notre cerveau, un outil puissant, mais complexe.
L'ordinateur, lui, utilise du million d'interrupteurs ON & OFF, représenté en binaire 1 et 0, qui, 
lorsqu'ils sont assemblé, peuvent former des chiffres extrêmement longs et précis.

La compréhension du fonctionnement d'un ordinateur est importante pour les développeurs, 
bien que quelques langages soient épargnés ; Python en fait partit.

Les maths, dans leur globalité, est nécessaire, car, 
grace au développement de la logique, résolution de problème, et algorithmie, 
une grande partie des bases sont acquises, et permettent un apprentissage rapide et fluide.
Prenons les boucles en exemple :
```
de 1 à 7, faire ...
```
qui équivaut à :
```python
for i in range(1, 7):
    ...
```
peut être représenté par :

$$
\sum_{i=1}^7 (...) = (...)
$$

Les mathématiques avancées sont requis pour les développeurs avancés, et ne concernent pas l'audience de ce livre, mais il est tout de même important a noté que la logique est surement la compétence __la plus importante__ en programmation.

## 1.7. Les conventions

Les conventions sont une grosse partie des langages de programmation. Elles définissent des règles à suivre, pour homogénéiser le code des différents développeurs. On peut rapporter ce principe a celui des Sciences, qui définit les notations, formules et unitées international, tel que $km.h^{-1}$, ou encore $\sqrt(a^{2} + b^{2})$. 

Il existe plusieurs types de notations :
 * _UpperCamelCase_ : consiste à mettre en majuscule la première lettre de chaque mot, sans les séparer par un espace. (`BonjourLesAmis`)
 * _lowerCamelCase_ : consiste à mettre en majuscule la première lettre de chaque mot, excepté le tout premier, sans les séparer par un espace. (`bonjourLesAmis`)
 * _snake\_case_ : consiste en remplacé les espaces par un tiret du bas `_`. (`bonjour_les_amis`)
 * _flatcase_ : consiste a écrire tout en minuscule sans espace. (`bonjourlesamis`)

Python utilise le _snake\_case_, et donc, chaque variable, fonction, ou classe, sauf exceptions, doivent se plier à ces conventions
Les espaces étant interdit dans ~99% des langages, dans la nomination, il faut pouvoir distinguer les mots entre eux.
Exemple en, Python :
```python
phrase_de_bonjour = "salut"
def dire_bonjour(): ...
class Mot_Bonjour: ...
```

Aucun mot définit par l'utilisateur tel que la nomination des variables, classes, et fonctions, ont interdiction de commencé par un chiffre, de contenir des espaces ou caractère spéciaux tel que les accents, les symboles monétaires, etc.

---

# 2. Les outils

## Les éditeurs de texte

Les éditeurs de texte sont présents sur quasiment n'importe quel ordinateur, et peuvent être très simpliste (NotePad sur windows), ou avancé, adapté pour la programmation avec des fonctionnalités supplémentaires.


## Les IDEs

## Les debuggers

## IDE vs. éditeur de texte