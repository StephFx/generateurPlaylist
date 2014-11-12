from Initialisations.connexion import mes_morceaux
from Initialisations.connexion import connexion
from controles.verificationsArguments import Attributs
from Initialisations.argument import argumentsParser
import sqlalchemy 
import random
import logging

'''
Created on 15 oct. 2014

@author: fx
'''
def recuperationDonnees(argumentsParser):
    def filtrerListe(listeFinale, listeAFiltrer, quantiteEscomptee):
        if quantiteEscomptee > 0:
            random.shuffle(listeAFiltrer)
            morceauChoisi = listeAFiltrer.pop()
            listeFinale.append(morceauChoisi)
            quantiteEscomptee -= morceauChoisi.duree
            filtrerListe(listeFinale, listeAFiltrer, quantiteEscomptee)
        else: 
            return listeFinale
        

    
    collectionListesFiltrees = list(list())
    for recherche in Attributs:
        if getattr(argumentsParser, recherche):
            for unArgument in getattr(argumentsParser, recherche):
                if (recherche == 'g'):
                    # On crée la liste avec les resultats de la requete
                    playList = list(connexion.execute(sqlalchemy.select([mes_morceaux]).where(mes_morceaux.c.genre == unArgument[0])))
                
                if (recherche == 'ar'):
                    # On crée la liste avec les resultats de la requete
                    playList = list(connexion.execute(sqlalchemy.select([mes_morceaux]).where(mes_morceaux.c.artiste == unArgument[0])))
                    
                if (recherche == 'alb'):
                    # On crée la liste avec les resultats de la requete
                    playList = list(connexion.execute(sqlalchemy.select([mes_morceaux]).where(mes_morceaux.c.album == unArgument[0])))
                    
                if (recherche == 't'):
                    # On crée la liste avec les resultats de la requete
                    playList = list(connexion.execute(sqlalchemy.select([mes_morceaux]).where(mes_morceaux.c.titre == unArgument[0])))
                    
                if (recherche == 'sg'):
                    # On crée la liste avec les resultats de la requete
                    playList = list(connexion.execute(sqlalchemy.select([mes_morceaux]).where(mes_morceaux.c.sousgenre == unArgument[0])))
                                     
                final = filtrerListe(collectionListesFiltrees,
                            playList,
                            unArgument[1] * argumentsParser.duree_playlist / 100 * 60)
                # on passe en parametre la quantite à garder à l'interieur de la sous playlist
                collectionListesFiltrees.append(final)    
                
    
    print(collectionListesFiltrees)     
                        
