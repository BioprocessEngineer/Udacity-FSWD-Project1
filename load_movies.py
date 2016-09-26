import bioprocess_engineer
import media
import webbrowser
import csv

title = []
story_line = []
poster = []
trailer = []
year = []
director = []
rating = []

with open('favorite_movies.csv') as f:
    mov = csv.reader(f)
    for row in mov:
        title.append(row[0])
        story_line.append(row[1])
        poster.append(row[2])
        trailer.append(row[3])
        year.append(row[4])
        director.append(row[5])
        rating.append(row[6])

movie_1 = media.Movie(title[0], story_line[0], poster[0], trailer[0], year[0], director[0], rating[0])
movie_2 = media.Movie(title[1], story_line[1], poster[1], trailer[1], year[1], director[1], rating[1])
movie_3 = media.Movie(title[2], story_line[2], poster[2], trailer[2], year[2], director[2], rating[2])
movie_4 = media.Movie(title[3], story_line[3], poster[3], trailer[3], year[3], director[3], rating[3])
movie_5 = media.Movie(title[4], story_line[4], poster[4], trailer[4], year[4], director[4], rating[4])
movie_6 = media.Movie(title[5], story_line[5], poster[5], trailer[5], year[5], director[5], rating[5])

movies = [movie_1, movie_2, movie_3, movie_4, movie_5, movie_6]
bioprocess_engineer.open_movies_page(movies)
