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

#les joueurs sont définis par le paramètre suivant :
# - 'ia' pour l'ordinateur
# - 'utilisateur' pour le vrai joueur


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


def ajoute_coord(x, y, bateau, joueur):
	if joueur=='ia':
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

	elif joueur=='utilisateur':
		if bateau =="Porte-avion":
			UTILI_PORTE_AVION.append((x,y))
		elif bateau == "Croiseur":
			UTILI_CROISEUR.append((x,y))
		elif bateau == "Contre-torpilleur":
			UTILI_CONTRE_TORPILLEUR.append((x,y))
		elif bateau == "Sous-marin":
			UTILI_SOUS_MARIN.append((x,y))
		elif bateau == "Torpilleur":
			UTILI_TORPILLEUR.append((x,y))


def placer_bateaux(i,j,bateau,sens,grille,joueur):
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
				ajoute_coord(i, j1, bateau, joueur)
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
				ajoute_coord(i1, j, bateau, joueur)
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
		placer_bateaux(positionx,positiony,bateau,direction,grille,"ia")
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


##############################################################################################


UTILI_PORTE_AVION = []
UTILI_TIR_PORTE_AVION = []
UTILI_CROISEUR = []
UTILI_TIR_CROISEUR = []
UTILI_CONTRE_TORPILLEUR = []
UTILI_TIR_CONTRE_TORPILLEUR = []
UTILI_SOUS_MARIN = []
UTILI_TIR_SOUS_MARIN = []
UTILI_TORPILLEUR = []
UTILI_TIR_TORPILLEUR = []

SENS = ['H','V']


def placer_bateau_utilisateur(bateaux:list):
	
	for bateau in NAVIRES :
		longueur=NAVIRES[bateau]
		print("\nVous allez placer le bateau :", bateau)
		print("Sa longueur est de", longueur, "cases.\n")
		afficher_grille_bateau(bateaux)
		ok = 0
		while ok != 1:
			pos_depart_x=str(input("\nEntrer ici la lettre souhaitée :"))
			pos_depart_x=pos_depart_x.upper()
			while pos_depart_x not in LETTRES:
				print("/!\ Erreur de lettre, resaisie ta lettre ! /!\ ")
				pos_depart_x=str(input("Entrer ici la lettre souhaitée :"))
				pos_depart_x=pos_depart_x.upper()
			pos_depart_x=int(LIGNES[pos_depart_x])

			cond=0
			while cond!=1:	
				pos_depart_y = input("Entrer ici la colonne souhaitée :")
				while not pos_depart_y.isdigit():
					print("/!\ Erreur de colonne, resaisie ta colonne ! /!\ ")
					pos_depart_y = input("Entrer ici la colonne souhaitée :")
				pos_depart_y=int(pos_depart_y)
				if pos_depart_y in range(1,11):
					pos_depart_y=pos_depart_y-1
					cond=1
				else:
					print("/!\ Erreur de colonne, resaisie ta colonne ! /!\ ")

			sens=str(input("Entrer ici le sens souhaité (Horizontal ou Vertical) H/V :"))
			sens=sens.upper()
			while sens not in SENS:
				print("/!\ Erreur de sens, resaisie te sens ! /!\ ")
				sens=str(input("Entrer ici le sens souhaité (Horizontal ou Vertical) H/V :"))
				sens=sens.upper()
			if sens=='H':
				sens=1
			elif sens=="V":
				sens=2

			ok = bateau_possible(pos_depart_x,pos_depart_y,longueur,sens,bateaux)
			if ok==0:
				print("Erreur dans le placement, recommence ton placement !")
		placer_bateaux(pos_depart_x,pos_depart_y,bateau,sens,bateaux,'utilisateur')
	return bateaux


def afficher_grille_bateau(bateaux:list):
	numcolonne=1
	print("  ", end="")
	while numcolonne<=10:
		print(numcolonne, end=" ")
		numcolonne+=1
	print()
	lettre=0
	while lettre<=9:
		for ligne in bateaux:
			print(LETTRES[lettre], end=" ")
			for element in ligne:
				if element==0:
					print(".", end=" ")
				elif element==2:
					print(".", end=" ")
				elif element==1:
					print("O", end=" ")
				elif element=='tir':
					print("X", end=" ")
			print()
			lettre+=1


def prochain_coup_ia(tirs:list)->tuple:
	ligne=random.randint(0,9)
	colonne=random.randint(0,9)
	if tir_valide(tirs, ligne, colonne):
		return (ligne, colonne)
	else:
		return prochain_coup_ia(tirs)

def resultat_tir_ia(bateaux:list, ligne:int, colonne:int)->int:
	if (bateaux[ligne][colonne]==0) or (bateaux[ligne][colonne]==2):
		return 0
	if bateaux[ligne][colonne]==1:
		if ((ligne, colonne) in UTILI_PORTE_AVION):
			UTILI_PORTE_AVION.remove((ligne, colonne))
			UTILI_TIR_PORTE_AVION.append((ligne, colonne))
			if len(UTILI_PORTE_AVION)!=0:
				return 1
			elif len(UTILI_PORTE_AVION)==0:
				return 2

		elif ((ligne, colonne) in UTILI_CROISEUR):
			UTILI_CROISEUR.remove((ligne, colonne))
			UTILI_TIR_CROISEUR.append((ligne, colonne))
			if len(UTILI_CROISEUR)!=0:
				return 1
			elif len(UTILI_CROISEUR)==0:
				return 2

		elif ((ligne, colonne) in UTILI_CONTRE_TORPILLEUR):
			UTILI_CONTRE_TORPILLEUR.remove((ligne, colonne))
			UTILI_TIR_CONTRE_TORPILLEUR.append((ligne, colonne))
			if len(UTILI_CONTRE_TORPILLEUR)!=0:
				return 1
			elif len(UTILI_CONTRE_TORPILLEUR)==0:
				return 2

		elif ((ligne, colonne) in UTILI_SOUS_MARIN):
			UTILI_SOUS_MARIN.remove((ligne, colonne))
			UTILI_TIR_SOUS_MARIN.append((ligne, colonne))
			if len(UTILI_SOUS_MARIN)!=0:
				return 1
			elif len(UTILI_SOUS_MARIN)==0:
				return 2

		elif ((ligne, colonne) in UTILI_TORPILLEUR):
			UTILI_TORPILLEUR.remove((ligne, colonne))
			UTILI_TIR_TORPILLEUR.append((ligne, colonne))
			if len(UTILI_TORPILLEUR)!=0:
				return 1
			elif len(UTILI_TORPILLEUR)==0:
				return 2


def tirer_ia(bateaux:list, tirs:list, ligne:int, colonne:int)->int:
	res=resultat_tir_ia(bateaux, ligne, colonne)
	if res==0:
		print("L'ordinateur à fait : Dans l'eau !\n")
		tirs[ligne][colonne]=0
		return 0

	elif res==1:
		print("L'ordinateur à fait : Touché !\n")
		tirs[ligne][colonne]=1
		return 1

	elif res==2:
		print("L'ordinateur à fait : Coulé !\n")
		if ((ligne, colonne)) in UTILI_TIR_PORTE_AVION:
			for elt in UTILI_TIR_PORTE_AVION:
				tirs[elt[0]][elt[1]]=2
			return 2

		elif ((ligne, colonne)) in UTILI_TIR_CROISEUR:
			for elt in UTILI_TIR_CROISEUR:
				tirs[elt[0]][elt[1]]=2
			return 2

		elif ((ligne, colonne)) in UTILI_TIR_CONTRE_TORPILLEUR:
			for elt in UTILI_TIR_CONTRE_TORPILLEUR:
				tirs[elt[0]][elt[1]]=2
			return 2

		elif ((ligne, colonne)) in UTILI_TIR_SOUS_MARIN:
			for elt in UTILI_TIR_SOUS_MARIN:
				tirs[elt[0]][elt[1]]=2
			return 2

		elif ((ligne, colonne)) in UTILI_TIR_TORPILLEUR:
			for elt in UTILI_TIR_TORPILLEUR:
				tirs[elt[0]][elt[1]]=2
			return 2


def jouer_ia():
	os.system("clear")
	bateaux_utilisateur=initialiser_grille(0)
	tirs_utilisateur=initialiser_grille(-1)

	bateaux_ia=initialiser_grille(0)
	bateaux_ia=placer_bateaux_aleatoirement(bateaux_ia)
	tirs_ia=initialiser_grille(-1)

	print("#######################################################################")
	print("############# Bienvenue dans le jeu de la Bataille Navale #############")
	print("#######################################################################\n")
	print("Vous jouez contre l'ordinateur : il a placé ses bateaux aléatoirement.")
	print("Vous disposez tous les deux :")
	print(" - 1 Porte-avion (5 cases)\n - 1 Croiseur (4 cases)\n - 1 Contre-torpilleur (3 cases)\n - 1 Sous-marin (3 cases)\n - 1 Torpilleur (2 cases)\n")
	print("Règles :")
	print(" - Les bateaux peuvent être disposés horizontalement ou verticalement,\n   mais jamais en diagonale.")
	print(" - Deux bateux ne peuvent pas non plus se chevaucher, ni être collés \n   l'un à l'autre : au moins une case doit les séparer.")
	print("\n Prêt ? C'est parti, bonne chance ! \n")

	print("Pour placer tes bateaux, saisie la case de départ,\nensuite son sens, il se placera automatiquement :\n - Vers la droite à partir de la case de départ si tu choisis horizontalement\n - Vers le bas à partir de la case de départ si tu choisis verticalement.\n")
	input("Appuie sur <Entrée> pour commencer à placer tes bateaux...")
	os.system("clear")

	placer_bateau_utilisateur(bateaux_utilisateur)
	print()

	input("Ta grille est prête, appuie sur <Entrée> pour commencer à jouer...")
	while not partie_finie(tirs_utilisateur) and not partie_finie(tirs_ia):
		os.system('clear')
		print("Ton placement (O) et les tirs de l'ordinateur (X) :\n")
		afficher_grille_bateau(bateaux_utilisateur)
		print("\nTa grille de tirs :\n")
		afficher_grille(tirs_utilisateur)
		print("\nA toi de jouer !\n")
		res=prochain_coup(tirs_utilisateur)
		tirer(bateaux_ia, tirs_utilisateur, res[0], res[1])

		res_ordi=prochain_coup_ia(tirs_ia)
		print("L'ordinateur à tiré en",LETTRES[res_ordi[0]], res_ordi[1]+1)
		tirer_ia(bateaux_utilisateur, tirs_ia, res_ordi[0], res_ordi[1])
		bateaux_utilisateur[res_ordi[0]][res_ordi[1]]='tir'
		#Réponses affichées pour le test, à retirer apres !
		#afficher_grille_bateau(bateaux_ia)

		if partie_finie(tirs_utilisateur):
			print("\n#######################################################################")
			print("###################### Bravo, vous avez gagné !!! #####################")
			print("#######################################################################\n")
		elif partie_finie(tirs_ia):
			print("\n#######################################################################")
			print("################### L'ordinateur à gagné, dommage ... #################")
			print("#######################################################################\n")
		else:
			input("Appuie sur <Entrée> pour continuer..")



jouer_ia()
#jouer()

