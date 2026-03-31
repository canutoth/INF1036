import random
import matplotlib.pyplot as plt

random.seed(123)

nsamples = 10000
total_pfa = 0
hsemanas = 40
total_semanas = 0
total_custo = 0
menor_280 = 0
menor_60s = 0
l_pfa = []
l_tempo = []
l_custo = []

for _ in range(nsamples):

    ee = sum(random.choices([3, 4, 6], weights=[3/10,5/10,2/10], k=25))

    ses = sum(random.choices([4, 5, 7], weights=[25/100,60/100,15/100], k=20))

    ces = sum(random.choices([3, 4, 6], weights=[4/10,4/10,2/10], k=15))

    alis = sum(random.choices([7, 10, 15], weights=[2/10,5/10,3/10], k=12))

    aies = sum(random.choices([5, 7, 10], weights=[35/100, 45/100, 20/100], k=8))

    pfna = ee + ses + ces + alis + aies
    fa = random.choices([1.05, 1.15, 1.25], weights=[2/10, 6/10, 2/10], k=1)[0]
    pfa = fa*pfna
    total_pfa += pfa

    prod = random.choices([4, 5, 6], weights=[2/10, 6/10, 2/10], k=1)[0]
    horas = pfa*prod
    semanas = horas/hsemanas

    if semanas < 60:
        menor_60s += 1

    total_semanas += semanas

    custo = random.choices([80, 100, 120], weights=[2/10, 6/10, 2/10], k=1)[0]
    custo *= horas

    if custo < 280000:
        menor_280 += 1

    total_custo += custo

    # para os histogramas:

    l_pfa.append(pfa)
    l_custo.append(custo)
    l_tempo.append(semanas)

print(f"a) valor medio esperado dos PFAs: {total_pfa/nsamples:.2f}")
print(f"b) tempo medio em semanas: {total_semanas/nsamples:.2f}")
print(f"c) custo medio do sistema: R${total_custo/nsamples:.2f}")
print(f"d) chance de custo menor que 280k: {menor_280/nsamples:.2f}")
print(f"e) chance de tempo menor que 60 semanas: {menor_60s/nsamples:.2f}")

# histogramas

plt.figure(figsize=(18,5))

plt.subplot(1,3,1)
plt.hist(l_pfa, color='skyblue', edgecolor='black', bins=50)
plt.subplot(1,3,2)
plt.hist(l_custo, color='skyblue', edgecolor='black', bins=50)
plt.subplot(1,3,3)
plt.hist(l_tempo, color='skyblue', edgecolor='black', bins=50)

plt.show()