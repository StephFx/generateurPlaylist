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
        

    
    collectionListesFiltrees = dict(list(list()))
    for recherche in Attributs:
        if getattr(argumentsParser, recherche):
            for unArgument in getattr(argumentsParser, recherche):
                if (recherche == 'g'):
                    # On crée la liste avec les resultats de la requete
                    playList = list(connexion.execute(sqlalchemy.select([mes_morceaux]).where(mes_morceaux.c.genre == unArgument[0])))
                    filtrerListe(collectionListesFiltrees[recherche],
                                 playList,
                                 unArgument[1] * argumentsParser.duree_playlist / 100 * 60)
                    # on passe en parametre la quantite à garder à l'interieur de la sous playlist
                    collectionListesFiltrees[recherche].append(playList)
                
                '''
    
    for recherche in Attributs:
        if getattr(argumentsParser, recherche) is not None:
            print('reussi')
            rechercheArgument = getattr(argumentsParser, recherche)
            for unArgument in rechercheArgument:
                print(unArgument)
                try:
                    selectionMorceaux = sqlalchemy.select([mes_morceaux]).where(mes_morceaux.c.titre == unArgument[0])
                    try: 
                        selectionMorceaux = sqlalchemy.select([mes_morceaux]).where(mes_morceaux.c.artiste == unArgument[0])
                        try:
                            selectionMorceaux = sqlalchemy.select([mes_morceaux]).where(mes_morceaux.c.duree == unArgument[0])
                            try:
                                selectionMorceaux = sqlalchemy.select([mes_morceaux]).where(mes_morceaux.c.chemin == unArgument[0])
                            except Exception:
                                logging.info('Pas de chemin trouvé')
                        except Exception:
                            logging.info('Pas de durée trouvé')
                    except Exception:
                        logging.info('Pas d\'artiste trouvé')
                except Exception:
                    logging.info('Pas de titre trouvé')
                    
                resultat = connexion.execute(selectionMorceaux)
                
            # On crée la liste avec les resultats de la requete
                playList = list(resultat)
                
                # On les tri aléatoirement
                random.shuffle(playList)
                
                for i in playList:
                    print(i)'''
            
            
            
        else:
            print('Erreur')
                        
