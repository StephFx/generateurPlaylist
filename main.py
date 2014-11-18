#!/usr/bin/python3
from controles.verificationsArguments import Veriff
from controles.recuperationDonnees import recuperationDonnees
from Initialisations.argument import argumentsParser
import controles.playlistFormat
from controles.playlistFormat import writeM3U, writeXSPF
import random

'''On execute la requete qui va lancer le controle des saisies (argument et entier) de l'utilisateur'''
Veriff()

'''On recupere la playlist des morceaux trier selon les arguments demander par l'utilisateur'''
playlist=recuperationDonnees(argumentsParser)
random.shuffle(playlist)

if (argumentsParser.type_playlist =='m3u'):
    writeM3U(argumentsParser, playlist)
    print('La playlist a bien ete genere')

if(argumentsParser.type_playlist=='xspf'):
    writeXSPF(argumentsParser, playlist)
    print('La playlist a bien ete genere')

if(argumentsParser.type_playlist=='pls'):
    writeXSPF(argumentsParser, playlist)
    print('La playlist a bien ete genere')
