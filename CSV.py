import sqlite_utils
import csv

#Create a SQL database
db = sqlite_utils.Database("spotify.db")

#Read data from the spotify csv file
with open('spotify-data.csv', 'r', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    data = [row for row in csvreader]

#Insert the data into the db table
db['spotify_data'].insert_all(data)
