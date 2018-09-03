

def not_num(content):
    if content == "0":
        return 0
    if content == "1":
        return 0
    if content == "2":
        return 0
    if content == "3":
        return 0
    if content == "4":
        return 0
    if content == "5":
        return 0
    if content == "6":
        return 0
    if content == "7":
        return 0
    if content == "8":
        return 0
    if content == "9":
        return 0
    if content == "-":
        return 0
    return 1

def read_file_spice(filename):
    file = open(filename,'r')
    lines = file.readlines()

    index = 0
    master_data = []

    data = dict()

    data["f"] = []
    data["abs"] = []
    data["pha"] = []
    #print(lines)

    for i in range(1,len(lines)):
        pnt = 0
        c1 = ""
        c2 = ""
        c3 = ""
        if lines[i].find("Step Information") == -1:
            while lines[i][pnt] != '\t':
                c1 += lines[i][pnt]
                pnt += 1

            while not_num(lines[i][pnt]):
                pnt += 1

            while lines[i][pnt] != 'd':
                c2 += lines[i][pnt]
                pnt += 1
            pnt += 1
            while not_num(lines[i][pnt]):
                pnt += 1
            while lines[i][pnt] != '°':
                c3 += lines[i][pnt]
                pnt += 1


            c1 = float(c1)
            c2 = float(c2)
            c3 = float(c3)

            data["f"].append(c1)
            data["abs"].append(c2)
            data["pha"].append(c3)

        else:
            master_data.append(data)
            index+=1
    return master_data
#data = read_file_spice("input/EJ_1_simulaciones.txt")
#print(data["abs"])
