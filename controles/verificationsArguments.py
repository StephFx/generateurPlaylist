#!/usr/bin/python3
import logging
import Initialisations.loggingConf
from Initialisations.argument import argumentsParser
import Initialisations.argument

'''
Created on 8 oct. 2014

@author: kitsune, Fx
'''

'''Fonction qui permet de verifier si l'utilisateur a bien saisie un entier pour une quantite voulue'''
def VerifInt (quantity):

        try:
            goodQte=int(quantity)
            logging.info("Un entier a bien ete saisie.")

            if goodQte >=0 and goodQte<=100:
                logging.info("L'entier saisie est bien positif et inferieur a 100.")
                return goodQte
            elif (goodQte<0 and goodQte>=-100):
                    '''On convertie le negatif en positif'''
                    goodQte=abs(goodQte)
                    logging.info("L'entier saisie est negatif saisie a ete transformer en entier positif.")
                    return goodQte
            else:
                    logging.error("L'entier saisie est inferieur a -100 ou superieur a 100.")
                    exit(2)
        except ValueError:
            logging.error("Erreur de conversion,la saisie est une chaine.")
            print("Il y a une erreur, veuillez saisir un entier naturel.")
            exit(1)

            '''Fonction qui permet la verification de tout les quantites de chaque arguments saisies'''
def Veriff ():

    '''Liste des arguments du programme'''
    Attributs=['g','ar','sg','alb','t','r']

    ''''Boucle pour parcourir la liste des arguments saisies par l'utilisateur'''
    for arg in Attributs:

        '''On initialise un compteur d'argument par option'''
        i=0
        '''On initialise le pourcentage total de la playlist'''
        pourcentage=0
        if getattr(argumentsParser, arg) is not None:
            ListeArg=getattr(argumentsParser, arg)
            logging.info("L'option "+arg+" est bien present.")

            '''Tant qu'il y a plusieurs argument de la meme option'''
            while i<len(ListeArg):
                Argument=ListeArg[i]
                '''On recupere le pourcentage d'un argument (ex: genre)'''
                ArgumentEntier=Argument[1]

                conversionMinutes(ArgumentEntier)
                '''On incremente le curseur'''
                i=i+1

                try:
                    '''On va donner l'entier saisie a une fonction pour la verifier'''
                    argVerif=VerifInt(ArgumentEntier)
                except Exception:
                    logging.error("La fonction de verification d'un entier n'a pas fonctionner")

                try:
                    '''On rentre la saisie dans une variable qui totalise les pourcentages saisies'''
                    pourcentage+=argVerif

                    '''On verifie le le total des pourcentages saisies par l'utilisateur.'''
                    if pourcentage>100:
                        print("Votre demande est superieur a 100%, veuillez saisir un valeur dont le total ne depasse pas ce seuil!")
                        logging.info("Le programme c'est arrete car le max de pourcentage a ete atteint.")
                        exit(3)

                except Exception:
                    logging.error("Le compte des pourcentages c'est mal effectue.")

                try:
                    '''On remplace la saisir de l'utilisateur par un entier'''
                    setattr(argumentsParser,arg,argVerif)
                except Exception:
                    logging.error("Le remplacement de la valeur entier n'a pas pu se faire.")
                    exit(4)
        else:
            logging.info("L'option "+arg+" n'est pas presente.")
            
            
def conversionMinutes(ArgumentEntier):
    '''On convertie le pourcentage en minutes selon la duree de la playlist'''
    Conversion = int (argumentsParser.duree_playlist*ArgumentEntier/100)
    return Conversion