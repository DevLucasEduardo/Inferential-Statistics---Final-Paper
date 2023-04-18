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
'''
def contagem(a:list, b:list, nome:str):
    menor = 0
    conta = 0
    contb = 0


    for cont in range(0, n):
        menor = a[cont]
        if b[cont] < menor:
            menor = b[cont]

        if menor == a[cont]:
            conta += 1
        elif menor == b[cont]:
            contb += 1


    print(nome, conta, contb)


contagem(fluxoMedFifo, fluxoMedSpt, 'Fluxo Médio SPT/FIFO: ')
contagem(atrasoMaxFifo, atrasoMaxSpt, 'Atraso Máximo SPT/FIFO: ')
contagem(earlinessFifo, earlinessSpt, 'Earliness SPT/FIFO: ')
contagem(tardinessFifo, tardinessSpt, 'Tardiness SPT/FIFO: ')
contagem(tarefasFifo, tarefasSpt, 'Tarefas em atraso SPT/FIFO: ')

contagem(fluxoMedFifo, fluxoMedEdd, 'Fluxo Médio EDD/FIFO: ')
contagem(atrasoMaxFifo, atrasoMaxEdd, 'Atraso Máximo EDD/FIFO: ')
contagem(earlinessFifo, earlinessEdd, 'Earliness EDD/FIFO: ')
contagem(tardinessFifo, tardinessEdd, 'Tardiness EDD/FIFO: ')
contagem(tarefasFifo, tarefasEdd, 'Tarefas em atraso EDD/FIFO: ')

contagem(fluxoMedFifo, fluxoMedCrr, 'Fluxo Médio CRR/FIFO: ')
contagem(atrasoMaxFifo, atrasoMaxCrr, 'Atraso Máximo CRR/FIFO: ')
contagem(earlinessFifo, earlinessCrr, 'Earliness CRR/FIFO: ')
contagem(tardinessFifo, tardinessCrr, 'Tardiness CRR/FIFO: ')
contagem(tarefasFifo, tarefasCrr, 'Tarefas em atraso CRR/FIFO: ')

contagem(fluxoMedFifo, fluxoMedStr1, 'Fluxo Médio STR/FIFO: ')
contagem(atrasoMaxFifo, atrasoMaxStr1, 'Atraso Máximo STR/FIFO: ')
contagem(earlinessFifo, earlinessStr1, 'Earliness STR/FIFO: ')
contagem(tardinessFifo, tardinessStr1, 'Tardiness STR/FIFO: ')
contagem(tarefasFifo, tarefasStr1, 'Tarefas em atraso STR/FIFO: ')





def contagem1(a:list, b:list):
    menor = 0
    conta = 0
    contb = 0


    for cont in range(0, n):
        menor = a[cont]
        if b[cont] < menor:
            menor = b[cont]
        if menor == a[cont]:
            conta += 1
        elif menor == b[cont]:
            contb += 1

    print(conta, contb)


########
def dispersion(y):
    x = arange(1, n + 1)
    plt.rcParams.update({'font.size': 20})
    plt.scatter(x, y)
    plt.show()

#################

medFluxoMedFifo = mean(fluxoMedFifo)
medFluxoMedSpt = mean(fluxoMedSpt)
medFluxoMedEdd = mean(fluxoMedEdd)
medFluxoMedCrr = mean(fluxoMedCrr)
medFluxoMedStr1 = mean(fluxoMedStr1)

medAtrasoMaxFifo = mean(atrasoMaxFifo)
medAtrasoMaxSpt = mean(atrasoMaxSpt)
medAtrasoMaxEdd = mean(atrasoMaxEdd)
medAtrasoMaxCrr = mean(atrasoMaxCrr)
medAtrasoMaxStr1 = mean(atrasoMaxStr1)

medLatenessFifo = mean(latenessFifo)
medLatenessSpt = mean(latenessSpt)
medLatenessEdd = mean(latenessEdd)
medLatenessCrr = mean(latenessCrr)
medLatenessStr1 = mean(latenessStr1)

medTardinessFifo = mean(tardinessFifo)
medTardinessSpt = mean(tardinessSpt)
medTardinessEdd = mean(tardinessEdd)
medTardinessCrr = mean(tardinessCrr)
medTardinessStr1 = mean(tardinessStr1)

medTarefasFifo = mean(tarefasFifo)
medTarefasSpt = mean(tarefasSpt)
medTarefasEdd = mean(tarefasEdd)
medTarefasCrr = mean(tarefasCrr)
medTarefasStr1 = mean(tarefasStr1)

medMakespanJohnson = mean(makespanJohnson)
medMakespanFifoJohnson = mean(makespanFifoJohnson)
medFluxoMedJohnson = mean(fluxoMedJohnson)
medFluxoMedFifoJohnson = mean(fluxoMedFifoJohnson)

medMakespanNeh = mean(makespanNeh)
medMakespanFifoNeh = mean(makespanFifoNeh)
medFluxoMedNeh = mean(fluxoMedNeh)
medFluxoMedFifoNeh = mean(fluxoMedFifoNeh)

newFluxoMedFifo = []
newAtrasoMaxFifo = []
newLatenessFifo = []
newTardinessFifo = []
newTarefasFifo = []
newFluxoMedSpt = []
newAtrasoMaxSpt = []
newLatenessSpt = []
newTardinessSpt = []
newTarefasSpt = []
newFluxoMedEdd = []
newAtrasoMaxEdd = []
newLatenessEdd = []
newTardinessEdd = []
newTarefasEdd = []
newFluxoMedCrr = []
newAtrasoMaxCrr = []
newLatenessCrr = []
newTardinessCrr = []
newTarefasCrr = []
newFluxoMedStr1 = []
newAtrasoMaxStr1 = []
newLatenessStr1 = []
newTardinessStr1 = []
newTarefasStr1 = []
newMakespanJohnson = []
newMakespanFifoJohnson = []
newFluxoMedJohnson = []
newFluxoMedFifoJohnson = []
newMakespanNeh = []
newMakespanFifoNeh = []
newFluxoMedNeh = []
newFluxoMedFifoNeh = []

for c in range(0, n):
    newFluxoMedFifo.append(abs(fluxoMedFifo[c] - medFluxoMedFifo))
    newAtrasoMaxFifo.append(abs(atrasoMaxFifo[c] - medAtrasoMaxFifo))
    newLatenessFifo.append(abs(latenessFifo[c] - medLatenessFifo))
    newTardinessFifo.append(abs(tardinessFifo[c] - medTardinessFifo))
    newTarefasFifo.append(abs(tarefasFifo[c] - medTarefasFifo))
    newFluxoMedSpt.append(abs(fluxoMedSpt[c] - medFluxoMedSpt))
    newAtrasoMaxSpt.append(abs(atrasoMaxSpt[c] - medAtrasoMaxSpt))
    newLatenessSpt.append(abs(latenessSpt[c] - medLatenessSpt))
    newTardinessSpt.append(abs(tardinessSpt[c] - medTardinessSpt))
    newTarefasSpt.append(abs(tarefasSpt[c] - medTarefasSpt))
    newFluxoMedEdd.append(abs(fluxoMedEdd[c] - medFluxoMedEdd))
    newAtrasoMaxEdd.append(abs(atrasoMaxEdd[c] - medAtrasoMaxEdd))
    newLatenessEdd.append(abs(latenessEdd[c] - medLatenessEdd))
    newTardinessEdd.append(abs(tardinessEdd[c] - medTardinessEdd))
    newTarefasEdd.append(abs(tarefasEdd[c] - medTarefasEdd))
    newFluxoMedCrr.append(abs(fluxoMedCrr[c] - medFluxoMedCrr))
    newAtrasoMaxCrr.append(abs(atrasoMaxCrr[c] - medAtrasoMaxCrr))
    newLatenessCrr.append(abs(latenessCrr[c] - medLatenessCrr))
    newTardinessCrr.append(abs(tardinessCrr[c] - medTardinessCrr))
    newTarefasCrr.append(abs(tarefasCrr[c] - medTarefasCrr))
    newFluxoMedStr1.append(abs(fluxoMedStr1[c] - medFluxoMedStr1))
    newAtrasoMaxStr1.append(abs(atrasoMaxStr1[c] - medAtrasoMaxStr1))
    newLatenessStr1.append(abs(latenessStr1[c] - medLatenessStr1))
    newTardinessStr1.append(abs(tardinessStr1[c] - medTardinessStr1))
    newTarefasStr1.append(abs(tarefasStr1[c] - medTarefasStr1))
    newMakespanJohnson.append(abs(makespanJohnson[c] - medMakespanJohnson))
    newMakespanFifoJohnson.append(abs(makespanFifoJohnson[c] - medMakespanFifoJohnson))
    newFluxoMedJohnson.append(abs(fluxoMedJohnson[c] - medFluxoMedJohnson))
    newFluxoMedFifoJohnson.append(abs(fluxoMedFifoJohnson[c] - medFluxoMedFifoJohnson))
    newMakespanNeh.append(abs(makespanNeh[c] - medMakespanNeh))
    newMakespanFifoNeh.append(abs(makespanFifoNeh[c] - medMakespanFifoNeh))
    newFluxoMedNeh.append(abs(fluxoMedNeh[c] - medFluxoMedNeh))
    newFluxoMedFifoNeh.append(abs(fluxoMedFifoNeh[c] - medFluxoMedFifoNeh))
    pass

a1 = 2
a2 = 3
a3 = 2
for c in range(0, n):

    if newFluxoMedFifo[c] <= a1 and newAtrasoMaxFifo[c] <= a1 and newLatenessFifo[c] <= a1 and newTardinessFifo[c] <= a1 and newTarefasFifo[c] <= a1 and \
            newFluxoMedSpt[c] <= a1 and newAtrasoMaxSpt[c] <= a1 and newLatenessSpt[c] <= a1 and newTardinessSpt[c] <= a1 and newTarefasSpt[c] <= a1 and \
            newFluxoMedEdd[c] <= a1 and newAtrasoMaxEdd[c] <= a1 and newLatenessEdd[c] <= a1 and newTardinessEdd[c] <= a1 and newTarefasEdd[c] <= a1 and \
            newFluxoMedCrr[c] <= a1 and newAtrasoMaxCrr[c] <= a1 and newLatenessCrr[c] <= a1 and newTardinessCrr[c] <= a1 and newTarefasCrr[c] <= a1 and \
            newFluxoMedStr1[c] <= a1 and newAtrasoMaxStr1[c] <= a1 and newLatenessStr1[c] <= a1 and newTardinessStr1[c] <= a1 and newTarefasStr1[c] <= a1 and\
            newMakespanJohnson[c] <= a1 and newMakespanFifoJohnson[c] <= a1 and newFluxoMedJohnson[c] <= a1 and newFluxoMedFifoJohnson[c] <= a1:
        lowerIndex = c
    if newMakespanJohnson[c] <= a2 and newMakespanFifoJohnson[c] <= a2 and newFluxoMedJohnson[c] <= a2 and newFluxoMedFifoJohnson[c] <= a2:
        lowerIndexJohnson = c
    if newMakespanNeh[c] <= a3 and newMakespanFifoNeh[c] <= a3 and newFluxoMedNeh[c] <= a3 and newFluxoMedFifoNeh[c] <= a3:
        lowerIndexNeh = c

if lowerIndex > 0:
    print(f'\n')
    print(f'Índice escolhido: {lowerIndex}')


    print("FIFO")
    aps.message_single_machine(aps.fifo(pjSimulation[lowerIndex], djSimulation[lowerIndex])[0],
                               aps.fifo(pjSimulation[lowerIndex], djSimulation[lowerIndex])[1],
                               aps.fifo(pjSimulation[lowerIndex], djSimulation[lowerIndex])[2])
    print(f'pj: {pjSimulation[lowerIndex]} dj: {djSimulation[lowerIndex]}')
    print("\nSPT")
    aps.message_single_machine(aps.spt(pjSimulation[lowerIndex], djSimulation[lowerIndex])[0],
                               aps.spt(pjSimulation[lowerIndex], djSimulation[lowerIndex])[1],
                               aps.spt(pjSimulation[lowerIndex], djSimulation[lowerIndex])[2])
    print(f'pj: {pjSimulation[lowerIndex]} dj: {djSimulation[lowerIndex]}')
    print("\nEDD")
    aps.message_single_machine(aps.edd(pjSimulation[lowerIndex], djSimulation[lowerIndex])[0],
                               aps.edd(pjSimulation[lowerIndex], djSimulation[lowerIndex])[1],
                               aps.edd(pjSimulation[lowerIndex], djSimulation[lowerIndex])[2])
    print(f'pj: {pjSimulation[lowerIndex]} dj: {djSimulation[lowerIndex]}')
    print("\nCRR")
    aps.message_single_machine(aps.crr(pjSimulation[lowerIndex], djSimulation[lowerIndex])[0],
                               aps.crr(pjSimulation[lowerIndex], djSimulation[lowerIndex])[1],
                               aps.crr(pjSimulation[lowerIndex], djSimulation[lowerIndex])[2])
    print(f'pj: {pjSimulation[lowerIndex]} dj: {djSimulation[lowerIndex]}')
    print("\nSTR")
    aps.message_single_machine(aps.str1(pjSimulation[lowerIndex], djSimulation[lowerIndex])[0],
                               aps.str1(pjSimulation[lowerIndex], djSimulation[lowerIndex])[1],
                               aps.str1(pjSimulation[lowerIndex], djSimulation[lowerIndex])[2])
    print(f'pj: {pjSimulation[lowerIndex]} dj: {djSimulation[lowerIndex]}')


if lowerIndexJohnson > 0:
    print("\nJohnson\n")
    aps.message_parallel_machine(aps.johnson(pjSimulationFifoJohnson[lowerIndexJohnson])[0],
                                 aps.johnson(pjSimulationFifoJohnson[lowerIndexJohnson])[1])
    print(f'\nFifo Johnson\n')
    aps.message_parallel_machine(['J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'J10'],
                                 pjSimulationFifoJohnson[lowerIndexJohnson])
    print(f'\npj Johnson: {pjSimulationJohnson[lowerIndexJohnson]}')
    print(f'pj Johnson FIFO: {pjSimulationFifoJohnson[lowerIndexJohnson]}')

if lowerIndexNeh > 0:
    print("\nNeh\n")
    aps.message_parallel_machine(aps.neh(pjSimulationFifoNeh[lowerIndexNeh])[0],
                                 aps.neh(pjSimulationFifoNeh[lowerIndexNeh])[1])
    print(f'\nFifo Neh\n')
    aps.message_parallel_machine(['J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'J10'],
                                 pjSimulationFifoNeh[lowerIndexNeh])
    print(f'\npj Neh: {pjSimulationNeh[lowerIndexNeh]}')
    print(f'pj Neh FIFO: {pjSimulationFifoNeh[lowerIndexNeh]}')

'''

