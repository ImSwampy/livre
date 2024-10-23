# Python #

---

## Sommaire ##

1. ### [Introduction et concepts](#1-introduction-et-concepts)
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
  * 1.3. Python et son environnement
    * 1.3.1. Package Manager
    * 1.3.2. Librairies de base
    * 1.3.3. Conda
  * 1.4. Langage interprété vs. compilé vs. Byte-code
  * 1.5. Programmation "Static" vs. "Dynamic"
  * 1.6. L'algorithmie et les mathématiques dans la programmation
  * 1.7. Les conventions

2. ### Les outils
  * 2.1. IDE vs Editeur de texte
  * 2.2. Les IDEs
  * 2.3. Les Editeurs de texte
  * 2.4. Les debuggers
  * 2.5. Environnement Python
    * 2.5.1. Pipenv
    * 2.5.2. Virtualenv
    * 2.5.3. Conda env
  * 2.6. Le Package Manager

3. ### Les bases
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

4. ### Python dans son ensemble
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

5. ### Python avancé : plongé dans le threading, l'asynchrone et le web
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

```
┌ 1  2  7  8 ┐
| 3  8  9  0 |
| 5  7  3  2 |
└ 9  0  3  0 ┘
```

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

Le package manager est un terme anglais, qui désigne un outil permettant entre autre l'installation de bibliothèque ou encore de mettre en place un environnement local au projet.
Le package manager officiel de Python s'appelle `pip`.
L'installation de `packets` (des bibliothèques) nécessite une connexion internet, et ont plusieurs répertoire d'installation par défaut.
Il est possible de créer un environnement local dans notre projet, ce qui permettra à nos libraries d'être utilisable seulement par ce projet.
Ces packets (ou _packages_) sont fait en Python, et permettent au développeur d'utiliser des fonctions ou classe déjà existante.

Plusieurs moyens existent afin d'utiliser `pip`, voici une liste complète :
```shell
pip ...
pip3 ...
python -m pip ...
python -m pip3 ...
```

Véerifiez bien que Python et (si possible) `pip` soit dans les variables systeme, ou `%PATH%`

### SAluut