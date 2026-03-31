import random

random.seed(123)

nsamples = 10000

print("a) 6*4 possibilidades de ataque = 24")
print("b) 1 possibilidade entre 24 combinações, 1/24")

fis4 = 0

for _ in range(nsamples):
    coin = random.choices(["heads", "tails"], weights=[2/3, 1/3], k=1)[0]
    dice = random.randint(1,6)

    if coin == "heads" and dice == 4:
        fis4 += 1

print(f"c) chance de {fis4/nsamples}")
