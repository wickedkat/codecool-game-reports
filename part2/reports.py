def get_most_played(filename):
    file = open(filename)
    list_of_lists = [word.split('\t') for word in file.readlines()]
    all_sells = []
    for i in range (0,len(list_of_lists)):
        all_sells.append(float(list_of_lists[i][1]))
    max_sell = int(sorted(all_sells)[-1])
    count = 0
    while count <= max_sell:
        for line in list_of_lists:
            if str(max_sell) in line:
                return line[0]
        max_sell -= 0.01
        count += 1

def sum_sold(filename):
    file = open(filename)
    list_of_lists = [word.split('\t') for word in file.readlines()]
    sum_sold = 0.0
    i= 0
    while i  in range (0,len(list_of_lists)):
        sum_sold += float(list_of_lists[i][1])
        i+=1
    return sum_sold

def get_selling_avg(filename):
    file = open(filename)
    list_of_lists = [word.split('\t') for word in file.readlines()]
    sum_sold = 0.0
    i= 0
    while i  in range (0,len(list_of_lists)):
        sum_sold += float(list_of_lists[i][1])
        i+=1
    return sum_sold/ len(list_of_lists)

def count_longest_title(filename):
    file = open(filename)
    list_of_lists = [word.split('\t') for word in file.readlines()]
    list_names = []
    for line in list_of_lists:
        for i in range(len(list_of_lists)):
            list_names.append(list_of_lists[i][0])
            list_names.sort(key = len)
        return len(list_names[-1])

def get_date_avg(filename):
    file = open(filename)
    list_of_lists = [word.split('\t') for word in file.readlines()]
    list_year = []
    num_years = 0
    sum_year = 0.0
    for line in list_of_lists:
        for i in range (len(list_of_lists)):
            if list_of_lists[i][2] not in list_year:
                list_year.append(list_of_lists[i][2])
                sum_year += float(list_of_lists[i][2])
                num_years+=1
            i+=1
    return int(sum_year/ num_years)+ (sum_year % num_years > 0)

def get_game(filename, title):
    file = open(filename)
    list_of_lists = [word.split('\t') for word in file.readlines()]
    for line in list_of_lists:
        if line [0] == title:
            line[1] = float(line[1])
            line[2] = int(line[2])
            line[4] = line[4][:-1]
            return line

def count_grouped_by_genre(filename):
    file = open(filename)
    list_of_lists = [word.split('\t') for word in file.readlines()]
    list_genres = []
    dict_genres = {}
    for i in range(0,len(list_of_lists)):
        list_genres.append(list_of_lists[i][3])
    for item in list_genres:
        if item in dict_genres:
            dict_genres[item] +=1
        else: 
            dict_genres[item] = 1            
    return dict_genres

def get_date_ordered(filename):
    file = open(filename)
    sorted_games_list = []
    list_of_lists = [word.split('\t') for word in file.readlines()]
    for y in list_of_lists:
        y[2] = int(y[2])
    list_of_lists.sort( key=lambda x: (-x[2],x[0]), reverse=False)
    for i in range (len(list_of_lists)):
        sorted_games_list.append(list_of_lists[i][0])
    return sorted_games_list


print(get_date_ordered('game_stat.txt'))

