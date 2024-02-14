number_of_players = 0
able_players = 0

#multiset to store modalidades
modalidades = set()

#division numbers
divisions_dist = [0] * 20

def parse_fields(fields):

    global number_of_players
    global able_players
    global divisions_dist

    #_id,index,dataEMD,nome/primeiro,nome/último,idade,género,morada,modalidade,clube,email,federado,resultado
    line_data = {
        "_id" : fields[0],
        "index": int(fields[1]),
        "dataEMD": fields[2],
        "nome/primeiro": fields[3],
        "nome/útlimo": fields[4],
        "idade": int(fields[5]),
        "género": fields[6],
        "morada": fields[7],
        "modalidade": fields[8],
        "clube": fields[9],
        "email": fields[10],
        "federado": fields[11] == "true",
        "resultado": fields[12] == "true"
    }

    number_of_players += 1
    modalidades.add(fields[8])

    if(line_data["federado"]):
        able_players += 1

    index = line_data["idade"] // 5
    divisions_dist[index] += 1
    
    return line_data

def parse_csv(file_path):
    data = []
    column_names = []
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into fields using comma as delimiter
            fields = line.strip().split(',')

            #To store the values for each dict key
            if (fields[0] == "_id"):
                column_names = fields
            else:
                line_data = parse_fields(fields)
                data.append(line_data)

    return data

def print_modalidades():
    modalidades_list = list(modalidades)
    modalidades_list.sort()

    for str in modalidades_list:
        print("- " + str)

def print_able_players():
    global number_of_players
    global able_players

    print("Total number of players: " + str(number_of_players))
    print("Percentage of Approved Players: " + str(able_players / number_of_players * 100) + "%")
    print("Percentage of Not Approved Players: " + str((number_of_players - able_players) / number_of_players * 100) + "%")

def print_division_dist():
    global divisions_dist
    global number_of_players

    for i,v in enumerate(divisions_dist):
        if v != 0:
            print(str(i*5) + " - " + str(i*5 + 4) + ": " + str(v/number_of_players * 100) +"% (" + str(v) + ")" )



csv_data = parse_csv('emd.csv')
print(" ")
print_modalidades()
print(" ")
print_able_players()
print(" ")
print_division_dist()


