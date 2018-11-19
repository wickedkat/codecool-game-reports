import reports

filename = input ("Please give the name of the file: ")

print("The most played game is:") 
print(reports.get_most_played(filename))
print("Total games sold: ")
print(reports.sum_sold(filename))
print("Average sales: ")
print(reports.get_selling_avg(filename))
print("The longest title has xx characters: ")
print (reports.count_longest_title(filename))
print("The average release date is : ")
print(reports.get_date_avg(filename))
title = input("Which game you want to know more about?:")
print(reports.get_game(filename, title))
print("Number of games in genre:")
print(reports.count_grouped_by_genre(filename))
print("Date ordered game list:")
print(reports.get_date_ordered(filename))





