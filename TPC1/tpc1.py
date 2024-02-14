FILE_PATH = "emd.csv"
TOKEN = ","

#############################

def parse_fields(fields):

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
    
    return line_data

def parse_dataset(file_path, token):
    data = []
    column_names = []
    with open(file_path, 'r') as file:
        for i,line in enumerate(file):
            # Split the line into fields using comma as delimiter
            fields = line.strip().split(token)

            #To store the values for each dict key
            if (i == 0):
                column_names = fields
            else:
                line_data = parse_fields(fields)
                data.append(line_data)

    return data

def list_modalidades(emd):

    modalidade = set()

    for line in emd:
        modalidade.add(line["modalidade"])

    modalidade_list = list(modalidade)
    modalidade_list.sort()

    return modalidade_list

def perc_ap(emd):

    total = len(emd)

    approved = 0
    not_approved = 0
    for line in emd:
        if line["resultado"]:
            approved += 1
        else: 
            not_approved += 1

    return (approved/total, not_approved/total)

def divisions_dist(emd, i=5):

    division = [0] * (100 // i)

    for line in emd:
        index = line["idade"] // i
        division[index] += 1

    return (division,i)

def print_modalidades(modalidades):

    print("")
    print("Lista de todas as modalidades (Ordem Alfabética):")
    for m in modalidades:
        print(" - " + m)

def print_percentagens_approved(tuplo, total):

    print("")
    print("Número total de atletas: " + str(total))
    print("Percentagem de atletas aprovados: " + str(tuplo[0]) + " (" + str(int(tuplo[0] * total)) + ") ")
    print("Percentagem de atletas não aprovados: " + str(tuplo[1]) + " (" + str(int(tuplo[1] * total)) + ") ")

def print_divisions(div, total):
    
    division = div[0]
    interv = div[1]

    print("")
    print("Distribuição de idades (Intervalos de " + str(interv) +"):")
    for i,v in enumerate(division):
        if v != 0:
            min_age = i * interv
            max_age = ((i+1) * interv) - 1

            percent = v / total * 100

            print(str(min_age) + " - " + str(max_age) + ": " + str(percent) +"% (" + str(v) +")")


def main():
    emd = parse_dataset(FILE_PATH, TOKEN)

    modalidades = list_modalidades(emd)
    ap_n = perc_ap(emd)
    division = divisions_dist(emd)

    print_modalidades(modalidades)
    print_percentagens_approved(ap_n, len(emd))
    print_divisions(division, len(emd))


if __name__ == '__main__':
    main()
