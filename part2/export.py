import csv
import reports

filename = 'game_stat.txt'
year = input("What year do you want me to look for? ")
title = input("What title are we looking for? ")
 
myData = [[reports.get_most_played(filename)], [reports.sum_sold(filename)],[reports.get_selling_avg(filename)],[reports.count_longest_title(filename)],[reports.get_date_avg(filename)],[reports.get_game(filename, title)],[reports.count_grouped_by_genre(filename)],[reports.get_date_ordered(filename)]]
myFile = open('export_report.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
# Export functions
