import csv
import reports

filename = 'game_stat.txt'
year = input("What year do you want me to look for? ")
genre = input ("What genre do you want me to count? ")
title = input("What title are we looking for? ")
 
myData = [[reports.count_games(filename)], [reports.decide(filename, year)],[reports.count_by_genre(filename, genre)],[reports.get_line_number_by_title(filename, title)],[reports.get_latest(filename)],[reports.sort_abc(filename)],[reports.get_genres(filename)],[reports.when_was_top_sold_fps(filename)]]
          
 
myFile = open('export_report.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)

    