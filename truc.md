# Python #

---

## Sommaire ##

1. ### [Introduction et concepts](#1-introduction-et-concepts)
  * [1.1. Fonctionnement d'un ordinateur](#11-fonctionnement-dun-ordinateur)
    * [1.1.1. Les composants](#les-composants)
    * [1.1.2. Mémoire RAM](#mémoire-ram)
    * [1.1.3. CPU](#processeur)
      * 1.1.3.1. Threads 
      * 1.1.3.2. Cache
    * 1.1.4. GPU
      * 1.1.4.1. Mémoire
      * 1.1.4.2. Traitement des données
  * 1.2. Python et ses applications
  * 1.3. Python et son environnement
  * 1.4. Langage interprété vs. compilé vs. Byte-code
  * 1.5. Programmation "Static" vs. "Dynamic"
  * 1.6. L'algorithmie et les mathématiques dans la programmation
  * 1.7. Les conventions

2. ### Les outils
  * 2.1. IDE vs Editeur de texte
  * 2.2. Les IDEs
  * 2.3. Les Editeurs de texte
  * 2.4. Les débuggeurs
  * 2.5. Environnement Python
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

#### Les composants

Un ordinateur est une machine complexe, qui, a l'aide de calculs, nous aident au quotidien. Que ce soit au travaille, a l'école, à la bibliothèque, ou que vous vouliez acheter un article en ligne, ou même regarder une vidéo, vous utiliserez un ordinnateur.

Pour commencer, parlons des composants :
- CPU : _Central Processing Unit_, c'est l'élément principal qui va nous permettre de faire ces calculs. Elle est composée d'une `horloge` qui est définie en _Hz_, et qui définie le nombre d'actions réalisé/réalisable par seconde. Il est aussi composé de `coeurs`, qui vont être cadencé et ordonné par l'`horloge`, qui effectueront leurs tâches associées. Les `threads` peuvent être représenté comme une boite, qui sera dépendante d'un `coeur`, qui effectuera le travaille envoyé par l'`horloge` a son coeur associé.


- GPU : _Graphics Processing Unit_, celle-ci n'est pas obligatoire, mais généralement nécessaire pour les ordinateurs de travail ou autre. Elle permet de faire de nombreux calculs en temps réel simultanément. Elle fonctionne en couche appelée `layer`, empilé les une sur les autres, commandé par de complexe calculs de vecteur et de matrices.


- RAM : _Random Access Memory_, un élément très important dans la programmation, car c'est généralement a l'utilisateur de décider de comment l'utilisé, en revanche, cela est moins importante en Python. Elle est stock les données de manière temporaire, par exemple, les valeurs d'une variable dans un programme. Elle est différente du stockage physique (disque dur, etc.), parce qu'elle permet d'accéder très rapidement à une valeur, mais a pour inconvénient d'être réinitialisé lorsqu'elle n'est plus alimenté.


- Carte Mère : _MotherBoard_, c'est le composant qui relie tous ceux précédents entre eux. Elle n'a pas tant de fonctionnalité en elle-même, mais peut tout de même être couplé a une carte wifi par exemple, qui captera les réseaux wifis, et d'autre encore.



#### Mémoire RAM

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

#### Processeur

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

Les threads sont souvent utilisés dans des applications ou projets a charge lourde, qui ont un besoin critique de performance ou de parallélisme dans les taches effectuées (simultanées).
En programmation, on affecte souvent des fonctions complexe ou longue au threads, afin de ne pas ralentir le programme entier.
Par exemple, en Python :

```python

```



## 1.2. 