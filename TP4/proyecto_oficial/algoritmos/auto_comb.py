# coding=utf-8
import config
from utils.etapas import getSingText

# Buscar una combinacion buena para armar las etapas


def autoComb(etapas):
    if config.debug:
        print("Iniciando combinador automatico de etapas")

    # for etapa in etapas.polos:
    #     print("Etapa: ")
    #     print(getSingText(etapa))
    #
    # for etapa in etapas.ceros:
    #     print("Etapa: ")
    #     print(getSingText(etapa))

    ceros = []

    for cero in etapas.ceros:
        pass



