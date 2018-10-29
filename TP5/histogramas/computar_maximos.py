
margin = 3


def computar_maximos_bp(data):
    # busco el maximo
    max_value = -1e5

    for i in range(len(data["mag"])):
        max_value = max(max_value , data["mag"][i])
    f1 = -1
    f2 = -1

    for i in range(len(data["mag"])):
        if f1 == -1 and data["mag"][i] > max_value - margin:
            f1 = data["f"][i]
        elif f2 == -1 and data["mag"][i] < max_value - margin:
            f2 = data["f"][i]

    return {"max":max_value,"f1":f1,"f2":f2}
