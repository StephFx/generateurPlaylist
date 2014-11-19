#!/usr/bin/python3
import logging
import Initialisations.loggingConf
from Initialisations.argument import argumentsParser
import Initialisations.argument
from controles.recuperationDonnees import verificationChoisi


'''Liste des arguments du programme'''
Attributs=['g','ar','sg','alb','t','r']

'''
Created on 8 oct. 2014

@author: kitsune, Fx
'''

'''Fonction qui permet de verifier si l'utilisateur a bien saisie un entier pour une quantite voulue'''
def VerifInt (quantity):

        '''On essais de convertir le format de la saisie en entier'''
        try:
            '''Convertion de la saisie'''
            goodQte=int(quantity)
            logging.info("Un entier a bien ete saisie.")

            '''Si la quantite saisie est un entier naturel'''
            if goodQte >0:
                logging.info("L'entier saisie est bien positif.")
                '''On retourne la saisie convertie en entier'''
                return goodQte

                '''Sinon (inferieur ou egale a 0) on regarde s'il est egale a 0'''
            elif goodQte==0:
                '''Si c'est le cas on renvoie en erreur et le programme s'arrete'''
                logging.error("0 a ete saisie.")
                print('Veuillez saisir un nombre non nul.')
                exit(2)

                '''Dans le dernier cas (strictement inferieur a 0)'''
            else:
                    '''On convertie le negatif en positif'''
                    goodQte=abs(goodQte)
                    logging.info("L'entier saisie est negatif saisie a ete transformer en entier positif.")
                    return goodQte
                    '''On retroune maintenant un entier naturel'''
        except ValueError:
            '''Si le programme n'a pas reussi a convertir la saisie en entier (il s'agit donc de caracteres ou caracteres speciaux'''
            logging.error("Erreur de conversion,la saisie est une chaine.")
            print("Il y a une erreur, veuillez saisir un entier naturel.")
            exit(1)

'''Fonction qui permet la verification de tout les quantites de chaque arguments saisies'''
def Veriff (Attributs):

    '''On initialise le pourcentage total de la playlist'''
    pourcentage=0
    compteurArg=0

    '''On initialise une variable intialiser a false mais qui passe a true si on trouve au moin un argument optionnel dans la ligne de commande '''
    trouveArg=False

    ''''Boucle pour parcourir la liste des arguments saisies par l'utilisateur'''
    for arg in Attributs:
        '''On initialise un compteur de tuple par argument'''
        i=0

        '''On regarde si dans l'argumentParser on trouve un argument qui n'est pas vide (donc ecrit dans la ligne de commande'''
        if getattr(argumentsParser, arg) is not None:

            '''On a trouve au moin un argument dans la ligne de commande'''
            trouveArg=True

            '''Si le trouve on le range dans une variable de type liste de liste (liste de tuple d'argument)'''
            ListeArg=getattr(argumentsParser, arg)
            '''On enregistre dans le fichier logging l'information '''
            logging.info("L'option "+arg+" est bien present.")

            '''Tant qu'il y a plusieurs des tuples pour un argument trouve'''
            while i<len(ListeArg):
                '''On range dans une variable le premier tuple de l'argument'''
                Argument=ListeArg[i]

                '''On incremente lorsqu'on trouve un argument'''
                compteurArg+=1

                '''On recupere le pourcentage du tuple (ex:Pour g : (Rock, 34) on recupere 34'''
                ArgumentEntier=Argument[1]

                '''On controle la saisie qui represente le pourcentage du tuple'''
                try:
                    '''On va donner la saisie a une fonction pour la verifier'''
                    argVerif=VerifInt(ArgumentEntier)

                    '''On rentre la saisie dans une variable qui totalise les pourcentages saisies'''
                    pourcentage+=argVerif

                    '''On remplace la saisir de l'utilisateur par un entier'''
                    ListeArg[i][1]=argVerif

                    '''Incrementation du compteur de tuple'''
                    i=i+1

                except Exception:
                    logging.error("La fonction de verification d'un entier n'a pas fonctionner")

                '''On controle la valeur voulu pour un argument (Ex pour g : (Rock, 34) on recupere Rock)'''
                '''On regarde si la saisie est present dans la base de donne'''
                try:
                    '''On verifie que le choisie saisie existe dans la base de donnée grace a une fonction'''

                    trouveBase=verificationChoisi(Argument[0], arg)

                    '''On regarde si la valeur retourner'''
                    if (trouveBase == False):
                        '''Si c'est faux on affiche un message d'erreur a l'utilisateur'''
                        print("Votre demande "+ Argument[0]+ " pour l'argument "+arg+" n'a pas dans la base.")
                        exit(3)
                        '''On quitte le programme'''

                except Exception:
                    logging.error("La verification de la saisie dans la base de donnée n'a pas pu se faire.")

                    '''Si l'argument n'a pas ete trouve dans l'argumentParser'''
        else:
            logging.info("L'option "+arg+" n'est pas presente.")


    '''On regarde si on a trouver au moin un argument optionnel dans la ligne de commande pour continuer la verification'''
    if trouveArg==True:

        '''On donne le total des pourcentages a un fonction'''
        valeurPourcentage=round(pourcentages(pourcentage),2)

        '''On regarde si on doit faire une mise à l'echelle ou non'''
        if valeurPourcentage!=0:
            '''On regarde pour chaque argument possible'''
            for args in Attributs:

                '''On regarde si dans l'argumentParser on trouve un argument qui n'est pas vide (donc ecrit dans la ligne de commande'''
                if getattr(argumentsParser, args) is not None:
                    '''Et on le range dans une variable'''
                    ListeArg=getattr(argumentsParser, args)

                    '''On initialise un compteur d'argument par option'''
                    i=0
                    '''Tant qu'il y a plusieurs tuples dans un argument'''
                    while i<len(ListeArg):
                        '''On recupere le premier tuple'''
                        Argument=ListeArg[i]
                        '''On recupere l'entier du tuple'''
                        ArgumentEntier=Argument[1]

                        '''Si la valeur est differente de 0 on fais une mise à l'echelle'''
                        argPourcent=round(ArgumentEntier*round(valeurPourcentage,2))

                        '''On essais de convertire les saisies entiers (pourcentage) en minutes'''
                        try:

                            ''''Maintenant on convertie la saisie correcte est remis e l'echelle'''
                            tempsArg=conversionMinutes(int(argPourcent))

                            '''On remplace la saisir de l'utilisateur par un entier'''
                            ListeArg[i][1]=tempsArg

                        except Exception:
                            logging.error("Le remplacement de la valeur entier n'a pas pu se faire.")
                            exit(4)
                        '''On incremente le i'''
                        i=i+1

'''Fonction qui permet de calculer un taux de remise a l'echelle selon le pourcentage total qui lui est transmis'''
def pourcentages (pourcentage):

    '''On regarde si le pourcentage est different de 100 donc non correcte'''
    if pourcentage!=100:

        '''S'il est superieur a 100'''
        if pourcentage>100:
            logging.info("Le programme a mis les pourcentages proportionnel a leur nombre car le max a etait atteint.")

            '''On va mettre tout les pourcentages des arguments proportionnellement pour atteindre les 100'''
            proportion=100/pourcentage

            '''S'il est inferieur a 100'''
        else:
            '''On va mettre tout les pourcentges des arguments proportionnellement pour atteindre les 100.'''
            proportion=100/pourcentage

        return proportion
    else:
        proportion=0
        return proportion

'''Fonction qui permet de convertir un entier (pourcentage) en minutes'''
def conversionMinutes(ArgumentEntier):
    '''On convertie le pourcentage en minutes selon la duree de la playlist'''
    Conversion = int (argumentsParser.duree_playlist*ArgumentEntier/100)
    return Conversion