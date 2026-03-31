import random
import matplotlib.pyplot as plt

random.seed(123)

nsamples = 1000000

freq_e1 = 0
freq_e2 = 0
freq_e3 = 0
e = 2 # estado inicial

for _ in range(nsamples):

    # qual o proximo estado?
    if e == 1: # to no estado 1
        freq_e1 += 1
        e = random.choices([1, 2, 3], weights=[0.6, 0.3, 0.1], k=1)[0]
    elif e == 2: # to no estado 2
        freq_e2 += 1
        e = random.choices([1, 2, 3], weights=[0.2, 0.5, 0.3], k=1)[0]
    else:
        freq_e3 += 1
        e = random.choices([1, 2, 3], weights=[0.1, 0.3, 0.6], k=1)[0]

print("frequencia relativa de: ")
print(f"e1: {freq_e1/nsamples*100:.2f}%")
print(f"e2: {freq_e2/nsamples*100:.2f}%")
print(f"e3: {freq_e3/nsamples*100:.2f}%")

pct = [
    (freq_e1 / nsamples) * 100, 
    (freq_e2 / nsamples) * 100, 
    (freq_e3 / nsamples) * 100
]

estados = ["e1", "e2", "e3"]

plt.bar(estados, pct, color='skyblue', edgecolor='black')
plt.title(f"frequencia relativa por estado pra {nsamples} passos")
plt.xlabel("estados")
plt.ylabel("porcentagem")

plt.show()