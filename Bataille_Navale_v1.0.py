#!/usr/bin/python3

import random
import os

NAVIRES = {'Porte-avion':5,'Croiseur':4,'Contre-torpilleur':3,'Sous-marin':3,'Torpilleur':2}

LIGNES = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}

LETTRES = ['A','B','C','D','E','F','G','H','I','J']

PORTE_AVION = []
TIR_PORTE_AVION = []
CROISEUR = []
TIR_CROISEUR = []
CONTRE_TORPILLEUR = []
TIR_CONTRE_TORPILLEUR = []
SOUS_MARIN = []
TIR_SOUS_MARIN = []
TORPILLEUR = []
TIR_TORPILLEUR = []

## RAPPEL :
#tirs est la grille affichée à l'utilisateur
#elle comporte des -1 au départ

#bateaux est la grille cachéee à l'utilisateur
#elle comporte :
# - des 0 si il n'y a rien
# - des 1 si il y a un bateau
# - des 2 si tout autour d'un bateau


def initialiser_grille(symbole):
	grille=[]
	for i in range(10):
		grille.append([])
		for j in range (10):
			grille[i].append(symbole)
	return grille


def bateau_possible(i,j,longueur,sens,grille):	
	if sens == 1:
		if j<=(10-longueur) and j+(longueur-1)<10:
			j1 = j
			cpt = 0
			possible = 1
			while cpt !=longueur and possible ==1:
				possible = 0
				if grille[i][j1] == 0:
					possible = 1
					j1+=1
					cpt+=1
			return possible
		else:
			return 0

	else:
		if i<=(10-longueur) and i+(longueur-1)<10:
			i1 = i
			cpt = 0
			possible = 1
			while cpt !=longueur and possible ==1:
				possible = 0
				if grille[i1][j] == 0:
					possible = 1
					i1+=1
					cpt+=1
			return possible
		else:
			return 0


def ajoute_coord(x, y, bateau):
	if bateau =="Porte-avion":
		PORTE_AVION.append((x,y))
	elif bateau == "Croiseur":
		CROISEUR.append((x,y))
	elif bateau == "Contre-torpilleur":
		CONTRE_TORPILLEUR.append((x,y))
	elif bateau == "Sous-marin":
		SOUS_MARIN.append((x,y))
	elif bateau == "Torpilleur":
		TORPILLEUR.append((x,y))


def placer_bateaux(i,j,bateau,sens,grille):
	longueur=NAVIRES[bateau]
	if sens == 1: #sens 1 = horizontalement
		if j<=(10-longueur) and j+(longueur-1)<10:
			i1 = i-1
			for cpt in range(3):
				j1 = j-1
				for cpt1 in range(longueur+2):
					if i1<10 and i1>=0 and j1<10 and j1>=0:
						grille[i1][j1]=2
					j1+=1
				i1+=1
			j1=j
			for cpt in range(longueur):
				grille[i][j1]=1
				ajoute_coord(i, j1, bateau)
				j1+=1
			return grille

	else: #sens 2 = verticalement
		if i<=(10-longueur) and i+(longueur-1)<10:
			j1 = j-1
			for cpt in range(3):
				i1 = i-1
				for cpt1 in range(longueur+2):
					if i1<10 and i1>=0 and j1<10 and j1>=0:
						grille[i1][j1]=2
					i1+=1
				j1+=1
			i1=i
			for cpt in range(longueur):
				grille[i1][j]=1
				ajoute_coord(i1, j, bateau)
				i1+=1
			return grille
		

def placer_bateaux_aleatoirement(grille:list)->list:
	for bateau in NAVIRES:
		longueur = NAVIRES[bateau]
		ok = 0
		while ok != 1:
			positionx = random.randint(0,9)# position x du bateau 
			positiony = random.randint(0,9)# position y du bateau 
			direction = random.randint(1,2) # direction : 1 = horizontal & 2 = vertical
			ok = bateau_possible(positionx,positiony,longueur,direction,grille)
		placer_bateaux(positionx,positiony,bateau,direction,grille)
	return grille


def tir_valide(tirs:list, ligne:int, colonne:int)->bool:
	if (0<=ligne<=9) and (0<=colonne<=9) and (tirs[ligne][colonne]==-1):
		return True
	else:
		return False


def prochain_coup(tirs:list)->tuple:
	print("Saisissez la position du prochain tir :")
	ligne=str(input("Lettre :"))
	ligne=ligne.upper() #Répare l'erreur si l'utilisateur rentre un a au lieu de A
	while ligne not in LETTRES:
		print("/!\ Erreur de lettre, resaisie ta lettre ! /!\ ")
		ligne=str(input("Lettre :"))
		ligne=ligne.upper()
	ligne_numerique=int(LIGNES[ligne])

	cond=0
	while cond!=1:	
		colonne = input("Colonne :")
		while not colonne.isdigit():
			print("/!\ Erreur de colonne, resaisie ta colonne ! /!\ ")
			colonne=input("Colonne :")
		colonne=int(colonne)
		if colonne in range(1,11):
			colonne=colonne-1 #car colonne 5 en vrai = colonne 4 en python
			cond=1
		else:
			print("/!\ Erreur de colonne, resaisie ta colonne ! /!\ ")

	if tir_valide(tirs, ligne_numerique, colonne):
		return (ligne_numerique, colonne)
	else:
		print("/!\ Erreur tir, déjà fait ou incorrect, recommence le tir ! /!\ ")
		return prochain_coup(tirs)


def resultat_tir(bateaux:list, ligne:int, colonne:int)->int:
	if (bateaux[ligne][colonne]==0) or (bateaux[ligne][colonne]==2):
		return 0
	if bateaux[ligne][colonne]==1:
		if ((ligne, colonne) in PORTE_AVION):
			PORTE_AVION.remove((ligne, colonne))
			TIR_PORTE_AVION.append((ligne, colonne))
			if len(PORTE_AVION)!=0:
				return 1
			elif len(PORTE_AVION)==0:
				return 2

		elif ((ligne, colonne) in CROISEUR):
			CROISEUR.remove((ligne, colonne))
			TIR_CROISEUR.append((ligne, colonne))
			if len(CROISEUR)!=0:
				return 1
			elif len(CROISEUR)==0:
				return 2

		elif ((ligne, colonne) in CONTRE_TORPILLEUR):
			CONTRE_TORPILLEUR.remove((ligne, colonne))
			TIR_CONTRE_TORPILLEUR.append((ligne, colonne))
			if len(CONTRE_TORPILLEUR)!=0:
				return 1
			elif len(CONTRE_TORPILLEUR)==0:
				return 2

		elif ((ligne, colonne) in SOUS_MARIN):
			SOUS_MARIN.remove((ligne, colonne))
			TIR_SOUS_MARIN.append((ligne, colonne))
			if len(SOUS_MARIN)!=0:
				return 1
			elif len(SOUS_MARIN)==0:
				return 2

		elif ((ligne, colonne) in TORPILLEUR):
			TORPILLEUR.remove((ligne, colonne))
			TIR_TORPILLEUR.append((ligne, colonne))
			if len(TORPILLEUR)!=0:
				return 1
			elif len(TORPILLEUR)==0:
				return 2


def tirer(bateaux:list, tirs:list, ligne:int, colonne:int)->int:
	res=resultat_tir(bateaux, ligne, colonne)
	if res==0:
		print("Dans l'eau !\n")
		tirs[ligne][colonne]=0
		return 0

	elif res==1:
		print("Touché !\n")
		tirs[ligne][colonne]=1
		return 1

	elif res==2:
		print("Coulé !\n")
		if ((ligne, colonne)) in TIR_PORTE_AVION:
			for elt in TIR_PORTE_AVION:
				tirs[elt[0]][elt[1]]=2
			return 2

		elif ((ligne, colonne)) in TIR_CROISEUR:
			for elt in TIR_CROISEUR:
				tirs[elt[0]][elt[1]]=2
			return 2

		elif ((ligne, colonne)) in TIR_CONTRE_TORPILLEUR:
			for elt in TIR_CONTRE_TORPILLEUR:
				tirs[elt[0]][elt[1]]=2
			return 2

		elif ((ligne, colonne)) in TIR_SOUS_MARIN:
			for elt in TIR_SOUS_MARIN:
				tirs[elt[0]][elt[1]]=2
			return 2

		elif ((ligne, colonne)) in TIR_TORPILLEUR:
			for elt in TIR_TORPILLEUR:
				tirs[elt[0]][elt[1]]=2
			return 2


def partie_finie(tirs:list)->bool:
	#Cette partie va compter le nombre de 2 dans le tableau
	compteur=0
	for ligne in tirs:
		for valeur in ligne:
			if valeur==2:
				compteur +=1
	#Cette partie va compter la somme de la longueur de tous les bateaux
	total=0
	for valeur in NAVIRES.values():
		total += valeur
	if compteur==total:
		return True
	else:
		return False


def afficher_grille(tirs):
	numcolonne=1
	print("  ", end="")
	while numcolonne<=10:
		print(numcolonne, end=" ")
		numcolonne+=1
	print()
	lettre=0
	while lettre<=9:
		for ligne in tirs:
			print(LETTRES[lettre], end=" ")
			for element in ligne:
				if element==-1:
					print(".", end=" ")
				elif element==0:
					print("*", end=" ")
				elif element==1:
					print("+", end=" ")
				elif element==2:
					print("X", end=" ")
			print()
			lettre+=1


def jouer():
	os.system("clear")
	bateaux=initialiser_grille(0)
	bateaux=placer_bateaux_aleatoirement(bateaux)

	tirs=initialiser_grille(-1)

	print("#######################################################################")
	print("############# Bienvenue dans le jeu de la Bataille Navale #############")
	print("#######################################################################\n")
	print("Vous jouez contre l'ordinateur : il a placé ses bateaux aléatoirement.")
	print("Il dispose :")
	print(" - 1 Porte-avion (5 cases)\n - 1 Croiseur (4 cases)\n - 1 Contre-torpilleur (3 cases)\n - 1 Sous-marin (3 cases)\n - 1 Torpilleur (2 cases)\n")
	print("Règles :")
	print(" - Les bateaux peuvent être disposés horizontalement ou verticalement,\n   mais jamais en diagonale.")
	print(" - Deux bateux ne peuvent pas non plus se chevaucher, ni être collés \n   l'un à l'autre : au moins une case doit les séparer.")
	print("\n Prêt ? C'est parti, bonne chance ! \n")
	while not partie_finie(tirs):
		afficher_grille(tirs)
		#Réponses affichées pour le test, à retirer apres !
		#afficher_grille_bateau(bateaux)
		res=prochain_coup(tirs)
		tirer(bateaux, tirs, res[0], res[1])
	print("#######################################################################")
	print("###################### Bravo, vous avez gagné !!! #####################")
	print("#######################################################################\n")
	afficher_grille(tirs)


jouer()

