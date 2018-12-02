# Bataille-Navale

Le célèbre jeu de la Bataille Navale.

## Description

Portage du célèbre jeu de la Bataille Navale, avec 2 modes de jeu :

* Possibilité de jouer seul : seul l'ordinateur place ses bateaux, et vous devez les détruire.
* Possibilité de jouer contre l'ordinateur : Vous placez vos bateaux, l'ordinateur aussi, et, à tour de rôle, vous tirez pour toucher les bateaux (l'ordinateur tire de manière random, sans aucune logique).

Projet réalisé en groupe de 2 personnes, codé en Python, sans interface graphique, et donc se lance sur un terminal.

## Utilisation

Ce jeu ne possédant pas d'interface graphique, il se lance et s'éxecute sur un terminal, il faut donc simplement lancer le fichier "Bataille_Navale_vX.X.py" pour jouer (avec X.X le numéro de version).

## Changelog

* 1.0
  * Finalisation de la première partie de la Bataille Navale (Mode de jeu simple : l'utilisateur est le seul à tirer sur les bateaux de l'ordinateur qu'il placera de manière aléatoire).

* 2.0
  * Finalisation de la deuxième partie de la Bataille Navale (2ème mode de jeu : l'utilisateur place ses bateaux, ainsi que l'ordinateur, et l'utilisateur ainsi que l'ordinateur tirent à tour de rôle. L'ordinateur tire de manière random uniquement, sans aucune logique).

* 3.0 (Version finale actuelle)
  * Améliorations/Optimisations du code
  * Utilisation au max des fonctions déjà écrites (suppression des copies prochain_coup_ia / resultat_tir_ia / tir_ia)
  * Affichage plus jolie et ajout d'un menu
  * Ajout de la doc des fonctions

## Amélioration

Le fait que l'ordinateur tire était une partie "Bonus" du projet. Actuellement, l'ordinateur tire de manière random, sans aucune logique : si il touche un bateau, il ne suivra aucune logique pour son prochain tir.
Il faudrait donc corriger ceci, et modifier le code pour que l'ordinateur tire son prochain tire de manière logique.