from openpyxl import *


def read_bode_data(filename):
    data = []

    content = load_workbook(filename)

    sheet = content.active

    abs = []
    i = 1
    while sheet["A"+str(i)] != "Gain":
        i += 1
    i += 1
    while sheet["A"+str(i)] != "":
        abs.append(sheet["A"+str(i)])

    return abs

