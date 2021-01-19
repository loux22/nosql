import pymongo
from pymongo import MongoClient

try :
    client = MongoClient('mongodb://localhost:27017/')
    client.server_info()
except :
    print("connexion error")

# supprimer la database
client.drop_database('metflix')
# client.drop_database('movies_artists')

# affiche toute les databases
dblist = client.list_database_names()
# si base de donnée existe pas on la créer
if not "metflix" in dblist:
  db = client["metflix"]

try : 
    # connexion a la base de données
    db = client.metflix
    
    # selection de la table movies
    movies = db.movies
except :
    print("database introuvable")

try :   
    movies.insert_one({"title": "Rocky", "year": 1976})
    movies.insert_one({"title": "Rocky", "year": 1976})
    movies.insert_one({"title": "Rocky", "year": 1976})
    movies.insert_one({"title": "Rocky", "year": 1976})
except :
    print("Insert failed")

users = db.users

try : 
    users.insert_one({"firstname": "Louis", "lastname": "Ardilly"})
except : 
    print("User insertion failed")

# insere plusieurs lignes
list = [{
        "title": "Rocky", 
        "year": 1976,
        "_id": "tt0075148"
    },
    {
        "title": "Jaws", 
        "year": 1975,
        "imdb": "tt0073195"
    },
    {
        "title": "Mad Max 2 : The road Warrior", 
        "year": 1981,
        "imdb": "tt0082694"
    },
    {
        "title": "Raiders of the Lost Ark", 
        "year": 1981,
        "imdb": "tt0082971"
    }
 ]
movies.insert_many(list)

# recuperation des données en filtrant
query = {'year': 1981}
items = movies.find(query)
for item in items :
    print(item)


query = {'title': "jaws"}
items = movies.find(query)
for item in items :
    print(item)

db = client.movies_artists

if not db.artist.find() : 
    db.artists.drop()

if not db.movies.find():
    db.movies.drop()

films = db.movies.find({},{"title" : 1}).limit(12).skip(9)
for film in films:
    print(film)

films_byTitleC = db.movies.find({},{"title" : 1}).sort("title", -1)
films_byTitleD = db.movies.find({},{"title" : 1}).sort("title", 1)

for film in films_byTitleC:
    print(film)

for film in films_byTitleD:
    print(film)


film2 = db.movies.find_one({"_id": "movie:2"},{"title" : 1, "genre": 1, "summary": 1 })
print(film2)

film1979 = db.movies.find({"year": 1979},{"title" : 1, "year": 1, "actors": 1 }).sort("title", -1)
for film in film1979:
    print(film)

filmScience = db.movies.find({"year": 1979, "genre" : "Science-fiction"},{"_id" : 0, "summary": 0})
for film in filmScience:
    print(film)


filmByDirector4 = db.movies.find({"director":{"_id" : "artist:4"}},{"genre" : 0, "summary": 0, "country": 0}).sort("year", 1)
for film in filmByDirector4:
    print(film)

filmByDirector4Maximus = db.movies.find({"director":{"_id" : "artist:4"}, {"actors":[{"role" : "Maximus"}]}},{"genre" : 0, "summary": 0, "country": 0}).sort("year", 1)
for film in filmByDirector4Maximus:
    print(film)




# try :
#     with open('json/artists.json') as json_data:
#         data_artists = json.load(json_data)

#     with open('json/movies.json') as json_data:
#         data_movies = json.load(json_data)
# except :
#     print("impossible d'ouvrir les fichiers json")

# try :
#     client = pymongo.MongoClient('mongodb://localhost:27017/')
# except :
#     print("connexion error")





# movies = db.movies
# artists = db.artists

# try:
#     db.artists.insert_many(data_artists)
#     db.movies.insert_many(data_movies)
# except:
#     print("Insert many error")


# try :
#     with open('json/artists_suite.json') as json_data:
#         data_artists = json.load(json_data)

#     with open('json/movies_suite.json') as json_data:
#         data_movies = json.load(json_data)
# except :
#     print("impossible d'ouvrir les fichiers json")

# try:
#     db.artists.insert_many(data_artists)
#     db.movies.insert_many(data_movies)
# except:
#     print("Insert many error")





