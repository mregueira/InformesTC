# coding=utf-8
import config
from utils.etapas import getSingText, getEtapa, getDualZero, getSingleZero
import random

# Buscar una combinacion buena para armar las etapas


def autoComb(etapas, min_freq, max_freq, total_gain):
    if config.debug:
        print("Iniciando combinador automatico de etapas")

    answer = []

    polos = etapas.polos
    ceros = etapas.ceros
    if len(polos) == 0: # Mal!
        return None

    var = polos[0].var

    tipos = {
        "conjugados, eje jw": [],
        "conjugados": [],
        "origen": [],
        "real": []
    }

    for cero in ceros:
        tipos[cero.getType()].append(cero)

    prioridades = [
        "conjugados, eje jw",
        "conjugados",
        "origen",
        "real"
    ]

    # Recombinamos ceros en el origen como ceros dobles siempre que se pueda
    # Esta es una decision arbitraria, no tendría, en principio, por que ser lo mejor

    duales, singles = convertDual(len(tipos["origen"]))
    codes = getCodes(tipos["origen"])

    tipos["origen"] = []
    i = 0
    while duales > 0:
        tipos["origen"].append(getDualZero(var, codes[i],codes[i+1]))
        duales -= 1
        i += 2

    while singles > 0:
        tipos["origen"].append(getSingleZero(var, codes[i]))
        singles -= 1

    # Los ceros conjugados vamos a tener que ordenarlos de Q mayor a Q menor
    # Va a ser mejor siempre primero recolocar los ceros de Q alto
    tipos["conjugados"] = sorted(tipos["conjugados"], key=lambda x: x.q, reverse=True)

    # Ordenamos los complejos en jw y reales por f0, es arbitrario
    tipos["conjugados, eje jw"] = sorted(tipos["conjugados, eje jw"], key=lambda x: x.f0)
    tipos["real"] = sorted(tipos["real"], key=lambda x: x.f0)

    used = [0] * len(polos)

    # vamos a matchear el cero con el mejor polo que haya disponible, utilizando un algoritmo cuadrático heuristico
    for tipo in prioridades:
        for cero in tipos[tipo]:
            mejor_etapa = None
            mejor_polo = None
            index_best = None
            best = 1e10

            for pi in range(len(polos)):
                if used[pi]:
                    continue

                polo = polos[pi]
                #conseguimos el rango dinamico de jutar dicho polo con dicho cero
                etapa = getEtapa(polo, cero, min_freq, max_freq)

                beneficio = etapa.maxGain - etapa.minGain

                if beneficio < best:
                    best = beneficio
                    mejor_etapa = etapa
                    mejor_polo = polo
                    index_best = pi

            used[index_best] = 1

            answer.append(mejor_etapa)

    for polo in polos:
        answer.append(getEtapa(polo, None, min_freq, max_freq))

    for ans in answer:
        ans.computarMinMaxGain(min_freq, max_freq)
    # agregamos index

    # Ya tenemos armados los pares. Ahora determinaremos el orden y calcularemos la constante de cada etapa

    #ordenamos de mayor a menor
    answer = sorted(answer, key=lambda x: x.maxGain-x.minGain, reverse=True)
    #answer = random.shuffle(answer)

    othersGain = 0
    for i in range(len(answer)-1, 0, -1):
        kmax = answer[i].maxGain
        kmin = answer[i].minGain

        answer[i].gain = (- kmin - kmax) / 2
        othersGain += answer[i].gain

    answer[0].gain = total_gain - othersGain

    i = 0
    for ans in answer:
        ans.index = i
        i += 1

    return answer

# combinar pares de polos o ceros en el origen

def convertDual(cantidad):
    return int(cantidad / 2), cantidad % 2

def getCodes(ceros):
    ans = []
    for cero in ceros:
        ans.append(cero.index)
    return ans
