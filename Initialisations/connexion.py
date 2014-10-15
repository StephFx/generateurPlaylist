import sqlalchemy
from Initialisations import loginMdpBdd as logBDD

# Connexion à la BDD
connexion = sqlalchemy.create_engine('postgresql://'+logBDD.loginBdd+':'+logBDD.mdpBdd+'@172.16.99.2:5432/radio_libre')


metadata = sqlalchemy.MetaData()

# Redéfinition de la table morceux
mes_morceaux = sqlalchemy.Table('morceaux', metadata, sqlalchemy.Column('titre', sqlalchemy.String), sqlalchemy.Column('album', sqlalchemy.String), sqlalchemy.Column('artiste', sqlalchemy.String), sqlalchemy.Column('genre', sqlalchemy.String), sqlalchemy.Column('sousgenre', sqlalchemy.String), sqlalchemy.Column('duree', sqlalchemy.Integer), sqlalchemy.Column('format', sqlalchemy.String), sqlalchemy.Column('polyphonie', sqlalchemy.Integer), sqlalchemy.Column('chemin', sqlalchemy.String))

# Requête de selection en BDD
selection_morceaux = sqlalchemy.select([mes_morceaux.c.titre]).where(mes_morceaux.c.titre == 'Toxic')

# On stock le resultat de la requête dans une variable
resultat = connexion.execute(selection_morceaux)

# On affiche les résultats de la requête
for i in resultat:
    print(i)