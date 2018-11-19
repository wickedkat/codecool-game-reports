def count_games(filename):
    with open(filename) as file:
        num_lines = len(file.readlines())
    return num_lines

def decide(filename, year):
    if str(year) in open(filename).read():
        return True
    else:
        return False
    
def count_by_genre(filename, genre):
    total = 0
    with open(filename) as file:
        for line in file:
            found = line.find(genre)
            if found !=-1 and found !=0:
                total+=1
    return total

def get_latest(filename):
    file = open(filename)
    list_of_lists = [word.split('\t') for word in file.readlines()]
    year = 2019
    count = 0
    while count < year:
        for x in list_of_lists:
            if str(year) in x:
                return x[0]
        year -= 1
        count += 1
                

def get_line_number_by_title(filename, title):
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            if title in line:
                return lines.index(line) +1

def sort_abc(filename):
    file = open(filename)
    list_of_lists = [word.split('\t') for word in file.readlines()]
    list_of_titles=[]
    sorted_list = []
    for i in range (0,len(list_of_lists)):
        list_of_titles.append(list_of_lists[i][0])
    while list_of_titles:
        smallest = min(list_of_titles)
        sorted_list.append(min(list_of_titles))
        list_of_titles.pop(list_of_titles.index(smallest))
    return sorted_list

def get_genres(filename):
    file = open(filename)
    list_of_lists = [word.split('\t') for word in file.readlines()]
    list_of_genres=[]
    sorted_genres_list = []
    for i in range (len(list_of_lists)):
        list_of_genres.append(list_of_lists[i][3])
    for genre in list_of_genres:
        if genre not in sorted_genres_list:
            sorted_genres_list.append(genre)

    return sorted(sorted_genres_list)

def when_was_top_sold_fps(filename):
    file = open(filename)
    list_of_lists = [word.split('\t') for word in file.readlines()]
    fps_lines = []
    fps_sells = []
    for line in list_of_lists:
        if line [3] == "First-person shooter":
            fps_lines.append(line)
            fps_sells.append(float(line[1]))
    if fps_lines = []:
        raise ValueError
    sorted_values = sorted(fps_sells)
    max_value = sorted_values[-1]
    sells = max_value
    count = 0
    while count <= sells:
        for line in fps_lines:
            if str(max_value) in line:
                return int(line[2])
        sells -= 1
        count += 1
    
