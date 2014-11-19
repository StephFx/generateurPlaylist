from Initialisations.connexion import mes_morceaux
from Initialisations.connexion import connexion
from Initialisations.argument import argumentsParser
import sqlalchemy
import random
import logging
from Initialisations.loggingConf import logging
'''
Created on 15 oct. 2014
@author: fx
'''

'''Liste des arguments du programme'''
Attributs=[('g', "genre"),('ar', "artiste"),('sg', "sousgenre"),('alb', "album"),('t', "titre")]

def rechercheBase(Attributs, valeurRechercher, arg):

    '''Initialisation d'un compteur pour parcourir la liste des arguments'''
    i=0
    trouve = False
    '''Recherche dans la liste des arguments'''
    while (i<len(Attributs) and trouve == False):

        if Attributs[i][0] == arg:
            nameColumn=Attributs[i][1]

            '''On essais de se connecter a la base et de recupere des donnees'''
            try :
                playList=list(connexion.execute(sqlalchemy.select([mes_morceaux]).where(getattr(mes_morceaux.c, nameColumn) == valeurRechercher)))
                trouve = True
            except Exception:
                logging.error("Le programme n'a pas pu acceder à la base de donnees")

        i+=1
    return playList

'''Fonction qui permet de recherche dans la base de données si la valeur voulu d'un argumetn existe '''
def verificationChoisi(selection, arg):

    '''On recherche dans la base'''
    select = rechercheBase(Attributs, selection, arg)

    '''Si le resultat n'est pas vide'''
    if select != []:
        '''On retourne true car il existe'''
        return True
    else :
        '''On retourne false car il n'existe pas'''
        return False

'''Module qui permet de recuperer une liste de morceaux selon les arguments de la commande'''
def recuperationDonnees(argumentsParser, existe):

    '''Permet de choisir dans la liste de morceaux ceux qui va correspondre à la durée demande'''
    def filtrerListe(listeFinale, listeAFiltrer, quantiteEscomptee):

        '''Si la quantite demander est superieur a 0'''
        if quantiteEscomptee > 0:
            '''On range le dernier morceaux de la playlist dans la liste final et on la supprime de l'ensemble'''
            morceauChoisi = listeAFiltrer[0]

            '''On remelange la liste a filtrer'''
            random.shuffle(listeAFiltrer)

            '''On l'ajout a la playlist final'''
            listeFinale.append(morceauChoisi)

            '''On decrément la quantite du morceaux ajoute au total de la quantiter voulue'''
            quantiteEscomptee -= morceauChoisi.duree
            '''On rappel la fonction avec une diminution des parametres'''
            filtrerListe(listeFinale, listeAFiltrer, quantiteEscomptee)
        else:
            return listeFinale

    '''On creer une liste de liste'''
    collectionListesFiltrees = list()

    '''Initialisation d'un compteur'''
    i=0

    while (i<len(Attributs)):

        '''On regarde s'il est rentree dans la commande'''
        if getattr(argumentsParser, Attributs[i][0]):
            '''On parcourt l'ensemble d'un attribut'''
            for unArgument in getattr(argumentsParser, Attributs[i][0]):
                playList = rechercheBase(Attributs, unArgument[0], Attributs[i][0])
                '''On applique la fonction de selection morceaux'''
                final=filtrerListe(collectionListesFiltrees, playList, unArgument[1] * argumentsParser.duree_playlist / 100 * 60)

                if (final is not None):
                    '''on passe en parametre la quantite à garder à l'interieur de la sous playlist'''
                    collectionListesFiltrees.append(final)
        i+=1

    '''S'il n'y a pas d'arguments optionnels'''
    if existe == False:
        try:
            '''on recupere l'ensemble des morceau de la base de donnees'''
            playList = list(connexion.execute(sqlalchemy.select([mes_morceaux])))
            '''On applique la fonction de selection morceaux'''
            final=filtrerListe(collectionListesFiltrees, playList, argumentsParser.duree_playlist * 60)
        except Exception:
            logging.error("Le programme n'a pas pu recuperer une liste de morceaux")

        if (final is not None):
            '''on passe en parametre la quantite à garder à l'interieur de la sous playlist'''
            collectionListesFiltrees.append(final)

    return collectionListesFiltrees