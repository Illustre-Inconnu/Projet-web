import flask
import sqlite3

app = flask.Flask(__name__, template_folder='views')

# Route pour la page principale
@app.route('/', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'POST':
        # Gestion de la soumission du formulaire
        nom = flask.request.values.get('nom')
        prenom = flask.request.values.get('prenom')
        date_naissance = flask.request.values.get('date_naissance')
        genre = flask.request.values.get('genre')
        departement = flask.request.values.get('departement')
        sport = flask.request.values.get('sport')

        # Connexion à la base de données SQLite
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        # Récupération des identifiants de sport et de département en utilisant les noms fournis
        cursor.execute("SELECT id_sport FROM Sports WHERE nom_sport = ?", (sport,))
        id_sport = cursor.fetchone()[0]
        cursor.execute("SELECT id_departement FROM Departement WHERE nom_departement = ?", (departement,))
        id_departement = cursor.fetchone()[0]

        # Insertion des données de l'utilisateur dans la base de données
        cursor.execute('''INSERT INTO Utilisateurs (nom_utilisateur, prenom_utilisateur, date_naissance, genre, id_departement, id_sport)
        VALUES (?, ?, ?, ?, ?, ?)''', (nom, prenom, date_naissance, genre, id_departement, id_sport))

        connection.commit()
        connection.close()

        return flask.redirect('/')
    else:
        # Récupération des sports et des départements depuis la base de données pour afficher dans le formulaire
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("SELECT nom_sport FROM Sports")
        sports = cursor.fetchall()
        cursor.execute("SELECT nom_departement FROM Departement")
        departements = cursor.fetchall()
        connection.close()

        liste_sports = [sport[0] for sport in sports]
        liste_departements = [departement[0] for departement in departements]

        return flask.render_template('index.html', sports=liste_sports, departements=liste_departements)

# Route pour la page de matching
@app.route('/matching', methods=['GET', 'POST'])
def matching():
    if flask.request.method == 'POST':
        # Gestion de la soumission du formulaire de matching
        departement = flask.request.values.get('departement')
        sport = flask.request.values.get('sport')

        # Connexion à la base de données SQLite
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        # Requête de base pour récupérer les utilisateurs
        requete_de_base = '''SELECT nom_utilisateur, prenom_utilisateur, nom_sport, nom_departement
                            FROM Utilisateurs
                            JOIN Sports ON Utilisateurs.id_sport = Sports.id_sport
                            JOIN Departement ON Utilisateurs.id_departement = Departement.id_departement
        '''
        parametres_methode_execute = []

        # Filtrage par département si spécifié par l'utilisateur
        if departement != 'aucun':
            requete_de_base += 'WHERE Departement.nom_departement = ?'
            parametres_methode_execute.append(departement)

        # Filtrage par sport si spécifié par l'utilisateur
        if sport != 'aucun':
            if 'WHERE' in requete_de_base:
                requete_de_base += ' AND Sports.nom_sport = ?'
            else:
                requete_de_base += ' WHERE Sports.nom_sport = ?'
            parametres_methode_execute.append(sport)

        # Exécution de la requête avec les filtres
        cursor.execute(requete_de_base, tuple(parametres_methode_execute))
        liste_utilisteur_match = cursor.fetchall()

        connection.close()

        return flask.render_template("resultat.html", liste_utilisteur_match=liste_utilisteur_match)
    else:
        # Récupération des sports et des départements depuis la base de données pour afficher dans le formulaire
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("SELECT nom_sport FROM Sports")
        sports = cursor.fetchall()
        cursor.execute("SELECT nom_departement FROM Departement")
        departements = cursor.fetchall()
        connection.close()

        liste_sports = [sport[0] for sport in sports]
        liste_departements = [departement[0] for departement in departements]

        return flask.render_template('matching.html', sports=liste_sports, departements=liste_departements)
