import sqlite3

# Établir une connexion à la base de données ou la créer si elle n'existe pas
connection = sqlite3.connect("database.db")

# Créer un objet curseur pour exécuter des commandes SQL
cursor = connection.cursor()

# Définir la table Utilisateurs
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Utilisateurs
    (
        id_utilisateur INTEGER PRIMARY KEY AUTOINCREMENT,
        id_sport INTEGER NOT NULL,
        id_departement INTEGER NOT NULL,
        nom_utilisateur VARCHAR(20) NOT NULL,
        prenom_utilisateur VARCHAR(20) NOT NULL,
        date_naissance DATE NOT NULL,
        genre VARCHAR(10) NOT NULL,
        FOREIGN KEY(id_sport) REFERENCES Sports(id_sport),
        FOREIGN KEY(id_departement) REFERENCES Departement(id_departement)
    )
''')
connection.commit()

# Définir la table Sports
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Sports
    (
        id_sport INTEGER PRIMARY KEY AUTOINCREMENT,
        nom_sport VARCHAR(20) NOT NULL
    )
''')
connection.commit()

# Définir la table Departement
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Departement
    (
        id_departement INTEGER PRIMARY KEY AUTOINCREMENT,
        nom_departement VARCHAR(20) NOT NULL,
        numero_departement VARCHAR(3) NOT NULL
    )
''')
connection.commit()

# Ajouter des utilisateurs avec plusieurs sports et départements
cursor.execute('''
    INSERT INTO Utilisateurs (id_sport, id_departement, nom_utilisateur, prenom_utilisateur, date_naissance, genre)
    VALUES
    (1, 1, 'Jean', 'Dupont', '1990-01-15', 'Homme'),
    (3, 5, 'Sophie', 'Martin', '1985-05-22', 'Femme'),
    (2, 10, 'Pierre', 'Lefevre', '1995-08-07', 'Homme'),
    (4, 15, 'Emma', 'Duchamps', '1988-11-30', 'Femme'),
    (5, 20, 'Lucas', 'Bertrand', '1992-03-12', 'Homme'),
    (6, 25, 'Marie', 'Girard', '1998-06-25', 'Femme'),
    (7, 30, 'Thomas', 'Lemoine', '1993-09-18', 'Homme'),
    (8, 35, 'Camille', 'Roux', '1980-12-05', 'Femme')
''')

# Valider les insertions dans la base de données
connection.commit()

# Insertion de sports de base dans la table Sports
cursor.execute('''
    INSERT INTO Sports (nom_sport)
    VALUES
    ('Football'), ('Rugby'), ('Escalade'), ('Musculation'), ('Natation'), ('Athlétisme'), ('Tennis'), ('Boxe')
''')

# Valider les insertions dans la base de données
connection.commit()

# Exécution de la requête pour insérer les départements avec les numéros
cursor.execute('''
    INSERT INTO Departement (nom_departement, numero_departement)
    VALUES
    ('Ain', '01'), ('Aisne', '02'), ('Allier', '03'), ('Alpes-de-Haute-Provence', '04'), ('Alpes-Maritimes', '06'), ('Ardèche', '07'), ('Ardennes', '08'), ('Ariège', '09'), ('Aube', '10'), ('Aude', '11'),
    ('Aveyron', '12'), ('Bouches-du-Rhône', '13'), ('Calvados', '14'), ('Cantal', '15'), ('Charente', '16'), ('Charente-Maritime', '17'), ('Cher', '18'), ('Corrèze', '19'), ('Corse du Sud', '2A'), ('Haute Corse', '2B')
''')

# Valider les insertions dans la base de données
connection.commit()

# Fermer la connexion à la base de données
connection.close()
