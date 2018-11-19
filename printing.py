import reports

filename = input ("Please give the name of the file: ")

print("Number of games in the file:") 
print(reports.count_games(filename))
year = input("What year do you want me to look for? ")
print("Is there any game from this year? ")
print(reports.decide(filename, year))
genre = input ("What genre do you want me to count? ")
print("Total games of this genre: ")
print(reports.count_by_genre(filename, genre))
title = input("What title are we looking for? ")
print("This title is in the line: ")
print (reports.get_line_number_by_title(filename, title))
print("The latest game is: ")
print(reports.get_latest(filename))
print("Alphabetical list of games:")
print(reports.sort_abc(filename))
print("Alphabetical list of genres:")
print(reports.get_genres(filename))
print("The top sold First-person shooting game was released in:")
print(reports.when_was_top_sold_fps(filename))



