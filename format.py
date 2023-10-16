import aps
from random import randint
from numpy import std, round, mean
from tabulate import tabulate
from math import sqrt

# import matplotlib.pyplot as plt
# import scipy.stats as stats


pjRules = []
djRules = []

fluxoMedFifo = []
fluxoMedSpt = []
fluxoMedEdd = []
fluxoMedCrr = []
fluxoMedStr1 = []

atrasoMaxFifo = []
atrasoMaxSpt = []
atrasoMaxEdd = []
atrasoMaxCrr = []
atrasoMaxStr1 = []

earlinessFifo = []
earlinessSpt = []
earlinessEdd = []
earlinessCrr = []
earlinessStr1 = []

tardinessFifo = []
tardinessSpt = []
tardinessEdd = []
tardinessCrr = []
tardinessStr1 = []

tarefasFifo = []
tarefasSpt = []
tarefasEdd = []
tarefasCrr = []
tarefasStr1 = []

pjJohnsonMethod = []
makespanJohnson = []
fluxoMedJohnson = []
makespanFifoJohnson = []
fluxoMedFifoJohnson = []
makespanNehJohnson = []
fluxoMedNehJohnson = []

pjNehMethod = []
makespanNeh = []
fluxoMedNeh = []
makespanFifoNeh = []
fluxoMedFifoNeh = []

n = 1000
z = 1.96

pjSimulation = []
djSimulation = []
pjSimulationJohnson = []
pjSimulationFifoJohnson = []
pjSimulationNehJohnson = []

pjSimulationNeh = []
pjSimulationFifoNeh = []

lowerIndex = 0
lowerIndexJohnson = 0
lowerIndexNeh = 0

for qt_vezes in range(0, n):
    for x in range(0, 5):
        pjNehMethod.append([])
        if x < 2:
            pjJohnsonMethod.append([])
    for c in range(0, 10):
        pjRules.append(randint(1, 10))
        djRules.append(randint(10, 100))
        pjJohnsonMethod[0].append(randint(1, 3))
        pjJohnsonMethod[1].append(randint(1, 3))
        pjNehMethod[0].append(randint(1, 10))
        pjNehMethod[1].append(randint(1, 10))
        pjNehMethod[2].append(randint(1, 10))
        pjNehMethod[3].append(randint(1, 10))
        pjNehMethod[4].append(randint(1, 10))

    pj_fifo = pjRules[:]
    dj_fifo = djRules[:]
    pj_spt = pjRules[:]
    dj_spt = djRules[:]
    pj_edd = pjRules[:]
    dj_edd = djRules[:]
    pj_crr = pjRules[:]
    dj_crr = djRules[:]
    pj_str1 = pjRules[:]
    dj_str1 = djRules[:]
    pj_johnson = pjJohnsonMethod[:]
    pj_fifo_johnson = pjJohnsonMethod[:]
    pj_neh_johnson = pjJohnsonMethod[:]
    pj_neh = pjNehMethod[:]
    pj_fifo_neh = pjNehMethod[:]

    aps.fifo(pj_fifo, dj_fifo)
    aps.spt(pj_spt, dj_spt)
    aps.edd(pj_edd, dj_edd)
    aps.crr(pj_crr, dj_crr)
    aps.str1(pj_str1, dj_str1)
    pj_johnson = aps.johnson(pj_johnson)[1]
    pj_neh_johnson = aps.neh(pj_neh_johnson)[1]
    pj_neh = aps.neh(pj_neh)[1]
    pjSimulation.append(pj_fifo)
    djSimulation.append(dj_fifo)
    pjSimulationJohnson.append(pj_johnson)
    pjSimulationNehJohnson.append(pj_neh_johnson)
    pjSimulationFifoJohnson.append(pj_fifo_johnson)
    pjSimulationNeh.append(pj_neh)
    pjSimulationFifoNeh.append(pj_fifo_neh)

    fluxoMedFifo.append(aps.mean_flow_time_rules(pj_fifo))
    fluxoMedSpt.append(aps.mean_flow_time_rules(pj_spt))
    fluxoMedEdd.append(aps.mean_flow_time_rules(pj_edd))
    fluxoMedCrr.append(aps.mean_flow_time_rules(pj_crr))
    fluxoMedStr1.append(aps.mean_flow_time_rules(pj_str1))

    atrasoMaxFifo.append(aps.max_lateness(pj_fifo, dj_fifo))
    atrasoMaxSpt.append(aps.max_lateness(pj_spt, dj_spt))
    atrasoMaxEdd.append(aps.max_lateness(pj_edd, dj_edd))
    atrasoMaxCrr.append(aps.max_lateness(pj_crr, dj_crr))
    atrasoMaxStr1.append(aps.max_lateness(pj_str1, dj_str1))

    earlinessFifo.append(aps.average_earliness(pj_fifo, dj_fifo))
    earlinessSpt.append(aps.average_earliness(pj_spt, dj_spt))
    earlinessEdd.append(aps.average_earliness(pj_edd, dj_edd))
    earlinessCrr.append(aps.average_earliness(pj_crr, dj_crr))
    earlinessStr1.append(aps.average_earliness(pj_str1, dj_str1))

    tardinessFifo.append(aps.average_tardiness(pj_fifo, dj_fifo))
    tardinessSpt.append(aps.average_tardiness(pj_spt, dj_spt))
    tardinessEdd.append(aps.average_tardiness(pj_edd, dj_edd))
    tardinessCrr.append(aps.average_tardiness(pj_crr, dj_crr))
    tardinessStr1.append(aps.average_tardiness(pj_str1, dj_str1))

    tarefasFifo.append(aps.number_tardy_jobs(pj_fifo, dj_fifo))
    tarefasSpt.append(aps.number_tardy_jobs(pj_spt, dj_spt))
    tarefasEdd.append(aps.number_tardy_jobs(pj_edd, dj_edd))
    tarefasCrr.append(aps.number_tardy_jobs(pj_crr, dj_crr))
    tarefasStr1.append(aps.number_tardy_jobs(pj_str1, dj_str1))

    makespanJohnson.append(aps.makespan(pj_johnson))
    fluxoMedJohnson.append(aps.mean_flow_time_methods(pj_johnson))
    makespanFifoJohnson.append(aps.makespan(pj_fifo_johnson))
    fluxoMedFifoJohnson.append(aps.mean_flow_time_methods(pj_fifo_johnson))
    makespanNehJohnson.append(aps.makespan(pj_neh_johnson))
    fluxoMedNehJohnson.append(aps.mean_flow_time_methods(pj_neh_johnson))

    makespanNeh.append(aps.makespan(pj_neh))
    fluxoMedNeh.append(aps.mean_flow_time_methods(pj_neh))
    makespanFifoNeh.append(aps.makespan(pj_fifo_neh))
    fluxoMedFifoNeh.append(aps.mean_flow_time_methods(pj_fifo_neh))

    pjRules.clear()
    djRules.clear()
    pjJohnsonMethod.clear()
    pjNehMethod.clear()


def int_conf_media(result: list, n1: int, z1: float):
    return str(round(mean(result), 2)) + " ± " + str(round(std(result, ddof=1) * z1 / sqrt(n1), 2))


medFluxoMedFifo = int_conf_media(fluxoMedFifo, n, z)
medFluxoMedSpt = int_conf_media(fluxoMedSpt, n, z)
medFluxoMedEdd = int_conf_media(fluxoMedEdd, n, z)
medFluxoMedCrr = int_conf_media(fluxoMedCrr, n, z)
medFluxoMedStr1 = int_conf_media(fluxoMedStr1, n, z)

medAtrasoMaxFifo = int_conf_media(atrasoMaxFifo, n, z)
medAtrasoMaxSpt = int_conf_media(atrasoMaxSpt, n, z)
medAtrasoMaxEdd = int_conf_media(atrasoMaxEdd, n, z)
medAtrasoMaxCrr = int_conf_media(atrasoMaxCrr, n, z)
medAtrasoMaxStr1 = int_conf_media(atrasoMaxStr1, n, z)

medEarlinessFifo = int_conf_media(earlinessFifo, n, z)
medEarlinessSpt = int_conf_media(earlinessSpt, n, z)
medEarlinessEdd = int_conf_media(earlinessEdd, n, z)
medEarlinessCrr = int_conf_media(earlinessCrr, n, z)
medEarlinessStr1 = int_conf_media(earlinessStr1, n, z)

medTardinessFifo = int_conf_media(tardinessFifo, n, z)
medTardinessSpt = int_conf_media(tardinessSpt, n, z)
medTardinessEdd = int_conf_media(tardinessEdd, n, z)
medTardinessCrr = int_conf_media(tardinessCrr, n, z)
medTardinessStr1 = int_conf_media(tardinessStr1, n, z)

medTarefasFifo = int_conf_media(tarefasFifo, n, z)
medTarefasSpt = int_conf_media(tarefasSpt, n, z)
medTarefasEdd = int_conf_media(tarefasEdd, n, z)
medTarefasCrr = int_conf_media(tarefasCrr, n, z)
medTarefasStr1 = int_conf_media(tarefasStr1, n, z)

medMakespanJohnson = int_conf_media(makespanJohnson, n, z)
medFluxoMedJohnson = int_conf_media(fluxoMedJohnson, n, z)
medMakespanFifoJohnson = int_conf_media(makespanFifoJohnson, n, z)
medFluxoMedFifoJohnson = int_conf_media(fluxoMedFifoJohnson, n, z)
medMakespanNehJohnson = int_conf_media(makespanNehJohnson, n, z)
medFluxoMedNehJohnson = int_conf_media(fluxoMedNehJohnson, n, z)

medMakespanNeh = int_conf_media(makespanNeh, n, z)
medFluxoMedNeh = int_conf_media(fluxoMedNeh, n, z)
medMakespanFifoNeh = int_conf_media(makespanFifoNeh, n, z)
medFluxoMedFifoNeh = int_conf_media(fluxoMedFifoNeh, n, z)

dataRules = [["FIFO ", medFluxoMedFifo, medAtrasoMaxFifo,
              medEarlinessFifo, medTardinessFifo, medTarefasFifo],
             ["SPT", medFluxoMedSpt, medAtrasoMaxSpt,
              medEarlinessSpt, medTardinessSpt, medTarefasSpt],
             ["EDD", medFluxoMedEdd, medAtrasoMaxEdd,
              medEarlinessEdd, medTardinessEdd, medTarefasEdd],
             ["CRR", medFluxoMedCrr, medAtrasoMaxCrr,
              medEarlinessCrr, medTardinessCrr, medTarefasCrr],
             ["STR", medFluxoMedStr1, medAtrasoMaxStr1,
              medEarlinessStr1, medTardinessStr1, medTarefasStr1]]

dataJohnsonMethod = [["JOHNSON ", medMakespanJohnson, medFluxoMedJohnson],
                     ["NEH", medMakespanNehJohnson, medFluxoMedNehJohnson],
                     ["FIFO", medMakespanFifoJohnson, medFluxoMedFifoJohnson]]

dataNehMethod = [["NEH ", medMakespanNeh, medFluxoMedNeh],
                 ["FIFO", medMakespanFifoNeh, medFluxoMedFifoNeh]]

print(tabulate(dataRules, headers=["Média/Regra", "Fluxo Médio",
                                   "Atraso Máximo", "Earliness",
                                   "Tardiness", "Tarefas em atraso"]))
print(f'\n')
print(tabulate(dataJohnsonMethod, headers=["Média/Médodo", "Makespan",
                                           "Fluxo Médio"]))
print(f'\n')
print(tabulate(dataNehMethod, headers=["Média/Médodo", "Makespan",
                                       "Fluxo Médio"]))

######


