
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
Attributs=['g','ar','sg','alb','t','r']

def verificationChoisi(selection, arg):

    if (arg == 'g'):
        select=list(connexion.execute(sqlalchemy.select([mes_morceaux]).where(mes_morceaux.c.genre == selection)))

    if (arg == 'ar'):
        select=list(connexion.execute(sqlalchemy.select([mes_morceaux]).where(mes_morceaux.c.artiste == selection)))

    if (arg=='sg'):
        select=list(connexion.execute(sqlalchemy.select([mes_morceaux]).where(mes_morceaux.c.sousgenre == selection)))

    if (arg=='alb'):
        select=list(connexion.execute(sqlalchemy.select([mes_morceaux]).where(mes_morceaux.c.album == selection)))

    if (arg =='t'):
        select=list(connexion.execute(sqlalchemy.select([mes_morceaux]).where(mes_morceaux.c.titre == selection)))

    if select != []:
        return True
    else :
        return False


'''Module qui permet de recuperer une liste de morceaux selon les arguments de la commande'''
def recuperationDonnees(argumentsParser):

    '''Permet de choisir dans la liste de morceaux ceux qui va correspondre à la durée demande'''
    def filtrerListe(listeFinale, listeAFiltrer, quantiteEscomptee):

        '''Si la quantite demander est superieur a 0'''
        if quantiteEscomptee > 0:
            '''On trie l'ensemble aleatoire'''
            random.shuffle(listeAFiltrer)
            '''On range le dernier morceaux de la playlist dans la liste final et on la supprime de l'ensemble'''
            morceauChoisi = listeAFiltrer.pop()

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

    '''On va parcourir l'ensemble des Attributs possible'''
    for recherche in Attributs:
        '''On regarde s'il est rentree dans la commande'''
        if getattr(argumentsParser, recherche):
            '''On parcourt l'ensemble d'un attribut'''
            for unArgument in getattr(argumentsParser, recherche):
                '''Si l'argument est le genre'''
                if (recherche == 'g'):
                    ''' On crée la liste avec les resultats de la requete'''
                    playList = list(connexion.execute(sqlalchemy.select([mes_morceaux]).where(mes_morceaux.c.genre == unArgument[0])))

                if (recherche == 'ar'):
                     playList = list(connexion.execute(sqlalchemy.select([mes_morceaux]).where(mes_morceaux.c.artiste == unArgument[0])))

                '''On applique la fonction de selection morceaux'''
                final=filtrerListe(collectionListesFiltrees, playList, unArgument[1] * argumentsParser.duree_playlist / 100 * 60)

                if (final is not None):
                    '''on passe en parametre la quantite à garder à l'interieur de la sous playlist'''
                    collectionListesFiltrees.append(final)

    return collectionListesFiltrees
