from Initialisations.connexion import mes_morceaux
from Initialisations.connexion import connexion
from controles.verificationsArguments import Attributs
from Initialisations.argument import argumentsParser
import sqlalchemy 
import random

'''
Created on 15 oct. 2014

@author: fx
'''

def recuperationDonnees(argumentsParser):
    for recherche in Attributs:
        if getattr(argumentsParser, recherche):
            for unArgument in getattr(argumentsParser, recherche):
                if (recherche == 'titre'):
                    selectionMorceaux = sqlalchemy.select([mes_morceaux]).where(mes_morceaux.c.titre == unArgument[0])
                if (recherche == 'artiste'):
                   selectionMorceaux = sqlalchemy.select([mes_morceaux]).where(mes_morceaux.c.artiste == unArgument[0])
                if(recherche == 'duree'):
                    selectionMorceaux = sqlalchemy.select([mes_morceaux]).where(mes_morceaux.c.duree == unArgument[0])
                if(recherche == 'chemin'):
                    selectionMorceaux = sqlalchemy.select([mes_morceaux]).where(mes_morceaux.c.chemin == unArgument[0]) 
                    
                resultat = connexion.execute(selectionMorceaux)
                playList = list(resultat)
                random.shuffle(playList)