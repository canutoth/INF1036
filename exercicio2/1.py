import random
import matplotlib.pyplot as plt

random.seed(123)

nsamples = 10000

pfna = 3500
hsemana = 40
total_pfa = 0
total_semanas = 0
total_custo = 0
menor1_5 = 0
menor_450s = 0
l_pfa = []
l_semanas = []
l_custo = []

for _ in range(nsamples):
    lcharacteristics = []

    c = random.choices([2, 3, 4], weights=[2/10, 6/10, 2/10], k=1)[0]
    lcharacteristics.append(c)

    c = random.choices([3, 4, 5], weights=[1/10, 7/10, 2/10], k=1)[0]
    lcharacteristics.append(c)

    c = random.choices([1, 2, 3], weights=[1/10, 7/10, 2/10], k=1)[0]
    lcharacteristics.append(c)

    c = random.choices([2, 3, 4, 5], weights=[1/10, 6/10, 2/10, 1/10], k=1)[0]
    lcharacteristics.append(c)

    for i in range(10):
        c = random.choices([1, 2, 3], weights=[2/10, 6/10, 2/10], k=1)[0]
        lcharacteristics.append(c)
    
    fa = 0.65 + 0.01 * sum(lcharacteristics)
    pfa = pfna * fa
    total_pfa += pfa

    prod = random.choices([4, 5, 6], weights=[2/10, 7/10, 1/10], k=1)[0]
    horas = pfa * prod
    semanas = horas / hsemana

    if semanas < 450:
        menor_450s += 1

    total_semanas += semanas

    custo = random.choices([80, 100, 120], weights=[2/10, 6/10, 2/10], k=1)[0]
    custo *= horas

    if custo < 1500000:
        menor1_5 += 1

    total_custo += custo

    # para o histograma
    l_pfa.append(pfa)
    l_custo.append(custo)
    l_semanas.append(semanas)

print(f"a) valor medio esperado de PF ajustado: {total_pfa/nsamples:.2f}")
print(f"b) tempo medio em semanas: {total_semanas/nsamples:.2f}")
print(f"c) custo medio do sistema: R${total_custo/nsamples:.2f}")
print(f"d) chance de custo menor que 1.5M: {menor1_5/nsamples*100:.2f}%")
print(f"e) chance de menos de 450 semanas: {menor_450s/nsamples*100:.2f}%")

# histogramas:

plt.figure(figsize=(15,4))

plt.subplot(1,3,1)
plt.hist(l_custo, bins=20, color='skyblue', edgecolor='black')
plt.title('distribuicao de custos')
plt.xlabel('custo')
plt.ylabel('frequencia')

plt.subplot(1,3,2)
plt.hist(l_semanas, bins=20, color='skyblue', edgecolor='black')
plt.title('distribuicao de semanas')
plt.xlabel('numero de semanas')

plt.subplot(1,3,3)
plt.hist(l_pfa, bins=20, color='skyblue', edgecolor='black')
plt.title('distribuicao de PFs ajustados')
plt.xlabel('num de PFs')
plt.show()