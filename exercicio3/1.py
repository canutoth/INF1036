# LCG

nsamples = 10000
a = 39373
c = 0
m = 2147483647
x = 12345

# a) lcg de 2 moedas nao viciadas
total = 0

for _ in range(nsamples):
    x = (a * x + c) % m
    u1 = x/m

    x = (a * x + c) % m
    u2 = x/m

    if (u1 < 0.5 and u2 >= 0.5) or (u1 >= 0.5 and u2 < 0.5):
        total += 1

print(f"total de cara e coroa: {total}")

# b) 1 moeda nao viciada (lcg) e 1d8 nao viciado (random)

import random

random.seed(123)

a = 39373
c = 0
m = 2147483647
x = 12345
coroa5 = 0

for _ in range(nsamples):
    x = (a * x + c) % m
    u = x/m

    dice = random.randint(1,8)

    if u >= 0.5 and dice == 5:
        coroa5 += 1

print(f"total de lancamentos coroa + face 5: {coroa5}")

# c) 1 moeda nao viciada (lcg) e 1d8 viciado (lm)

a = 39373
c = 0
m = 2147483647
x = 12345
coroa8 = 0
lm = 0
ncoins = 10

for _ in range(nsamples):

    lm = 0

    x = (a * x + c) % m
    u = x/m

    for i in range(ncoins):
        coin = random.randint(0, 1)
        lm += coin * 2**i

    lm /= (2**ncoins - 1)

    if lm >= (6/7) and u >= 0.5:
        coroa8 += 1

print(f"total de lancamentos coroa + face 8 viciada: {coroa8}")

# d) moeda viciada (random) e dado honesto (lm)

suc = 0

for _ in range(nsamples):

    coin = random.choices([0, 1], weights=[0.45, 0.55], k=1)[0]

    lm = 0

    for i in range(ncoins):
        coinlm = random.randint(0, 1)
        lm += coinlm * 2**i

    lm /= (2**ncoins - 1)

    if 0 <= lm < (1/8):
        if coin == 0:
            suc += 1
            
    elif (3/8) <= lm < (4/8):
        if coin == 0:
            suc += 1
            
    elif (6/8) <= lm < (7/8):
        if coin == 1:
            suc += 1

print(f"chance de cara1 ou cara4 ou coroa7: {suc/nsamples*100:.2f}%")