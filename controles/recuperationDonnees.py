
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
        '''Si l'argument est semblable a ce qu'il y a dans le tableau Attribut'''
        if Attributs[i][0] == arg:
            '''On stock dans une variable la seconde valeur de notre liste'''
            nameColumn=Attributs[i][1]
            '''On effectue notre requete de select avec la colonne recupéré dans notre tableau (nameColumn'''
            playList=list(connexion.execute(sqlalchemy.select([mes_morceaux]).where(getattr(mes_morceaux.c, nameColumn) == valeurRechercher)))
            '''Quand on a trouvé un argument on initialise trouve a True'''
            trouve = True
        '''On incremente de 1 le compteur pour savoir quand on arréte de boucler'''
        i+=1
    return playList

def verificationChoisi(selection, arg):

    select = rechercheBase(Attributs, selection, arg)
    if select != []:
        return True
    else :
        return False

'''Module qui permet de recuperer une liste de morceaux selon les arguments de la commande'''
def recuperationDonnees(argumentsParser,existe):        

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
                final=filtrerListe(collectionListesFiltrees, playList, unArgument[1] * argumentsParser.duree_playlist /100 * 60)
                if (final is not None):
                    '''on passe en parametre la quantite à garder à l'interieur de la sous playlist'''
                    collectionListesFiltrees.append(final)
        i+=1
    
    '''S'il n'y a pas d'arguments optionnels'''
    if existe == False:
        '''on recupere l'ensemble des morceau de la base de donnees'''
        playList = list(connexion.execute(sqlalchemy.select([mes_morceaux])))
        '''On applique la fonction de selection morceaux'''
        final=filtrerListe(collectionListesFiltrees, playList, argumentsParser.duree_playlist * 60)
        if (final is not None):
                    '''on passe en parametre la quantite à garder à l'interieur de la sous playlist'''
                    collectionListesFiltrees.append(final)
                                          
    return collectionListesFiltrees
