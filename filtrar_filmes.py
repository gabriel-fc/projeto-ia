# useful columns: budget, genres, original language, original title, release date
# all columns: ['adult', 'belongs_to_collection', 'budget', 'genres', 'homepage', 'id',
#       'imdb_id', 'original_language', 'original_title', 'overview',
#       'popularity', 'poster_path', 'production_companies',
#      'production_countries', 'release_date', 'revenue', 'runtime',
#       'spoken_languages', 'status', 'tagline', 'title', 'video',
#       'vote_average', 'vote_count'],

import csv
import json
import ast
"""
-> script para gerar arquivo json a partir do csv
fieldnames = ("adult","belongs_to_collection","budget","genres","homepage","id","imdb_id","original_language","original_title","overview","popularity","poster_path","production_companies","production_countries","release_date","revenue","runtime","spoken_languages","status","tagline","title,video","vote_average","vote_count")


csvfile = open('dataset.csv', 'r')
jsonfile = open('file.json', 'w')

reader = csv.DictReader( csvfile, fieldnames)
jsonfile.write("{\n    dataset:[\n");
for row in reader:
    jsonfile.write('        ')
    json.dump(row, jsonfile)
    jsonfile.write(',\n')
    
jsonfile.write("    ]\n}");
jsonfile.close()

----> converte as strings de belongs_to_collection e genres para objetos
jsonfile = open('file.json', 'r')
obj = json.load(jsonfile)

for movie in obj["dataset"]:
    if movie["belongs_to_collection"] == "":
        movie["belongs_to_collection"] = "{}"
    
    movie["genres"] = ast.literal_eval(movie["genres"])
    movie["belongs_to_collection"] = ast.literal_eval(movie["belongs_to_collection"])

jsonfile.close()
"""


#----> gera a base de conhecimentos a partir do json do csv


def getGenres(genres):
    output = []
    for genre in genres:
        if genre['name'] == "Drama" or  genre['name'] == "Horror" or genre['name'] == "Animation" or genre['name'] == "Comedy" or genre['name'] == "Romance":
            output.append(genre)
    return output

def addMovie(movies, new_movie):
    index = 0
    for index in range(len(movies)):
        if movies[index]["vote_count"] <= new_movie['vote_count']:
            break
    
    movies.insert(index, new_movie)
    if len(movies) > 10:
        movies = movies[:10]
    return movies




file = open("file.json", 'r')
obj = json.load(file)
file.close()

file = open("base de conhecimento.json", "w")


final = {"drama":{"newer": {"pt": {"low budget":[], "high budget":[]}, "en":{"low budget":[], "high budget":[]}}, "older": {"pt": {"low budget":[], "high budget":[]}, "en":{"low budget":[], "high budget":[]}}}, 
"animation":{"newer": {"pt": {"low budget":[], "high budget":[]}, "en":{"low budget":[], "high budget":[]}}, "older": {"pt": {"low budget":[], "high budget":[]}, "en":{"low budget":[], "high budget":[]}}}, 
"horror":{"newer": {"pt": {"low budget":[], "high budget":[]}, "en":{"low budget":[], "high budget":[]}}, "older": {"pt": {"low budget":[], "high budget":[]}, "en":{"low budget":[], "high budget":[]}}}, 
"romance":{"newer": {"pt": {"low budget":[], "high budget":[]}, "en":{"low budget":[], "high budget":[]}}, "older": {"pt": {"low budget":[], "high budget":[]}, "en":{"low budget":[], "high budget":[]}}}, 
"comedy":{"newer": {"pt": {"low budget":[], "high budget":[]}, "en":{"low budget":[], "high budget":[]}}, "older": {"pt": {"low budget":[], "high budget":[]}, "en":{"low budget":[], "high budget":[]}}}}



for x in obj["dataset"]:
    realese = ''
    lang = ''
    budget = ''

    if x['release_date'] != None and x['release_date'][:4].isnumeric():
        if int(x['release_date'][:4]) < 2000:
            realese = 'older'
        else: realese = 'newer'    

    if x['budget'] != None and x['budget'].isnumeric():
        if float(x['budget']) < 50000.00:
            budget = "low budget"
        else:   budget = "high budget" 
    
    if x['original_language'] == 'en':
        lang = "en"
    elif  x['original_language'] == 'pt':
        lang = 'pt'  

    if lang != '' and realese != '' and budget != '':      
        list = getGenres(x['genres'])
        for genre in list:
            movies = final[(genre['name']).lower()][realese][lang][budget]
            final[(genre['name']).lower()][realese][lang][budget] = addMovie(movies, x)
            print('add!')
        



file.write(json.dumps(final, indent=4))
file.close()

























     




