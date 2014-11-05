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

            if goodQte >0:
                logging.info("L'entier saisie est bien positif.")
                return goodQte
            elif goodQte==0:
                logging.error("0 a ete saisie.")
                print('Veuillez saisir un nombre non nul.')
                exit(2)
            else:
                    '''On convertie le negatif en positif'''
                    goodQte=abs(goodQte)
                    logging.info("L'entier saisie est negatif saisie a ete transformer en entier positif.")
                    return goodQte
        except ValueError:
            logging.error("Erreur de conversion,la saisie est une chaine.")
            print("Il y a une erreur, veuillez saisir un entier naturel.")
            exit(1)

            '''Fonction qui permet la verification de tout les quantites de chaque arguments saisies'''
def Veriff ():

    '''Liste des arguments du programme'''
    Attributs=['g','ar','sg','alb','t','r']

    '''On initialise le pourcentage total de la playlist'''
    pourcentage=0
    compteurArg=0

    ''''Boucle pour parcourir la liste des arguments saisies par l'utilisateur'''
    for arg in Attributs:
        '''On initialise un compteur d'argument par option'''
        i=0

        if getattr(argumentsParser, arg) is not None:
            ListeArg=getattr(argumentsParser, arg)
            logging.info("L'option "+arg+" est bien present.")

            '''Tant qu'il y a plusieurs argument de la meme option'''
            while i<len(ListeArg):
                Argument=ListeArg[i]

                '''On incremente lorsqu'on trouve un argument'''
                compteurArg+=1

                '''On recupere le pourcentage d'un argument (ex: genre)'''
                ArgumentEntier=Argument[1]

                try:
                    '''On va donner l'entier saisie a une fonction pour la verifier'''
                    argVerif=VerifInt(ArgumentEntier)

                    '''On rentre la saisie dans une variable qui totalise les pourcentages saisies'''
                    pourcentage+=argVerif

                    '''On remplace la saisir de l'utilisateur par un entier'''
                    ListeArg[i][1]=argVerif

                    '''Incrementation'''
                    i=i+1

                except Exception:
                    logging.error("La fonction de verification d'un entier n'a pas fonctionner")

        else:
            logging.info("L'option "+arg+" n'est pas presente.")

    '''On donne le total des pourcentages a un fonction'''
    valeurPourcentage=round(pourcentages(pourcentage),2)

    '''On regarde si on doit faire une mise à l'echelle ou non'''
    if valeurPourcentage!=0:
        for args in Attributs:

            if getattr(argumentsParser, args) is not None:
                ListeArg=getattr(argumentsParser, args)

                '''On initialise un compteur d'argument par option'''
                i=0
                '''Tant qu'il y a plusieurs argument de la meme option'''
                while i<len(ListeArg):
                    Argument=ListeArg[i]
                    ArgumentEntier=Argument[1]

                    '''Si la valeur est differente de 0 on fais une mise à l'echelle'''
                    argPourcent=round(ArgumentEntier*round(valeurPourcentage,2))

                    try:

                        ''''Maintenant on convertie la saisie correcte est remis e l'echelle'''
                        tempsArg=conversionMinutes(int(argPourcent))

                        '''On remplace la saisir de l'utilisateur par un entier'''
                        ListeArg[i][1]=tempsArg

                        print(ListeArg[i][1])

                    except Exception:
                        logging.error("Le remplacement de la valeur entier n'a pas pu se faire.")
                        exit(4)
                    '''On incremente le i'''
                    i=i+1

def pourcentages (pourcentage):

    '''On parcoure tout les arguments saisie si le pourcentage est different de 100'''
    if pourcentage!=100:

        if pourcentage>100:
            logging.info("Le programme a mis les pourcentages proportionnel a leur nombre car le max a etait atteint.")

            '''On va mettre tout les pourcentages des arguments proportionnellement pour atteindre les 100'''
            proportion=100/pourcentage

        else:
            '''On va mettre tout les pourcentges des arguments proportionnellement pour atteindre les 100.'''
            proportion=100/pourcentage

        return proportion
    else:
        proportion=0
        return proportion

def conversionMinutes(ArgumentEntier):
    '''On convertie le pourcentage en minutes selon la duree de la playlist'''
    Conversion = int (argumentsParser.duree_playlist*ArgumentEntier/100)
    return Conversion