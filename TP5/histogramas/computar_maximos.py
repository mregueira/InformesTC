
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

    return {"max":max_value, "f1": f1, "f2": f2}


def computar_notch(data):
    min_value = 1e5
    notch_f = -1
    for i in range(len(data["mag"])):
        if data["mag"][i] < min_value:
            notch_f = data["f"][i]
        min_value = min(min_value, data["mag"][i])

    f1 = -1
    f2 = -1
    for i in range(len(data["mag"])):
        if f1 == -1 and data["mag"][i] < -margin:
            f1 = data["f"][i]
        elif f2 == -1 and data["mag"][i] > -margin:
            f2 = data["f"][i]
    return {"notch_f": notch_f, "f1": f1, "f2": f2, "min": min_value}






def conseguir_fp(data, cuttoff):
    for i in range(len(data["abs"])):
        if data["abs"][i] < cuttoff:
            return (data["f"][i] + data["f"][i-1]) / 2
    return -1

