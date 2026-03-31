import random

random.seed(123)
tot5 = 0
nsamples = 10000
others = 0

for _ in range(nsamples):
    dice = random.randint(1,10)

    if dice == 5:
        tot5 += 1
    
print("total de faces 5: ", tot5)

prob_b = 0

for _ in range(nsamples):
    dice = random.randint(1,9) #exclui a face 2, agora 2 = 10 e nao e mais um range de 1 a 10
    coin = random.choices(["heads", "tails"], weights=[55/100, 45/100], k=1)[0]

    if (coin == "heads" and dice == 6) or (coin == "tails" and dice == 9) or dice == 8:
        prob_b += 1

print(f"probabilidade de um dos 3 eventos acontecerem: {prob_b/nsamples:.2f}")
