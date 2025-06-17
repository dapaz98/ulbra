import numpy as np
import random as rd

size_cromossomo = 30
pc = 0.95
pm = 0.1
num_geracoes_populacao = 100
size_populacao = 50

p = np.zeros((size_populacao, size_cromossomo))
for i in range(size_populacao):
    for j in range(size_cromossomo):
        a = rd.uniform(0, 1)
        p[i][j] = 1 if a >= 0.5 else 0

ind = np.zeros(size_cromossomo)
individuo = np.zeros(size_populacao)
aptidao = np.zeros(size_populacao)
n_geracao = np.zeros((size_populacao, size_cromossomo))
geracao = 0

mel = -np.inf 

while geracao <= num_geracoes_populacao:
    n_individuos = 0
    while n_individuos < (size_populacao - 1):
        for i in range(size_populacao):
            ind[:] = p[i, :]
            conv = 0
            for j in range(size_cromossomo):
                conv += ind[j] * (2 ** (size_cromossomo - (j + 1)))
            individuo[i] = (512 / (2**size_cromossomo - 1)) * conv

        total_aptidao = 0
        for i in range(size_populacao):
            aptidao[i] = abs(individuo[i] * np.sin(individuo[i] ** 2)) + 5
            total_aptidao += aptidao[i]

        # Probabilidade de seleção
        pic = (1 / total_aptidao) * aptidao
        pi_total = np.zeros(size_populacao)
        pi_total[0] = pic[0]
        for i in range(1, size_populacao):
            pi_total[i] = pic[i] + pi_total[i - 1]

        # Seleção dos pais
        roleta_1 = rd.uniform(0, 1)
        i = 0
        while roleta_1 > pi_total[i]:
            i += 1
        pai_1 = i

        roleta_2 = rd.uniform(0, 1)
        i = 0
        while roleta_2 > pi_total[i]:
            i += 1
        pai_2 = i

        while pai_2 == pai_1:
            roleta_2 = rd.uniform(0, 1)
            i = 0
            while roleta_2 > pi_total[i]:
                i += 1
            pai_2 = i

        if pc > rd.uniform(0, 1):
            c = int(rd.randint(1, size_cromossomo - 2))  # ponto de corte
            gene11 = p[pai_1][0:c]
            gene12 = p[pai_1][c:size_cromossomo]

            gene21 = p[pai_2][0:c]
            gene22 = p[pai_2][c:size_cromossomo]

            filho_1 = np.concatenate((gene11, gene22))
            filho_2 = np.concatenate((gene21, gene12))

            n_geracao[n_individuos, :] = filho_1
            n_individuos += 1

            n_geracao[n_individuos, :] = filho_2
            n_individuos += 1

            # Mutação
            if pm > rd.uniform(0, 1):
                d = rd.randint(0, size_cromossomo - 1)
                n_geracao[n_individuos - 2][d] = 1 - n_geracao[n_individuos - 2][d]
                n_geracao[n_individuos - 1][d] = 1 - n_geracao[n_individuos - 1][d]

    # Atualiza melhor indivíduo
    index = aptidao.argmax()
    elemento = individuo[index]
    if geracao == 0:
        mel = elemento
    elif elemento > mel:
        mel = elemento

    p = n_geracao.copy()
    geracao += 1

print("Melhor valor encontrado:", mel)
