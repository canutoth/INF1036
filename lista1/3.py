import random

random.seed(123)

nsamples = 10000
count_a = 0
count_b = 0

for i in range(nsamples):
    coins = random.choices(["heads", "tails"], weights=[2/5, 3/5], k=3)
    if (coins[0] == "heads" and coins[1] == "tails") or (coins[0] == "tails" and coins[1] == "heads"):
        count_a += 1
    if (coins[1] == "tails" and coins[2] == "tails"):
        count_b += 1

pa = count_a/nsamples
pb = count_b/nsamples

print("P(A) = ", pa)
print("P(B) = ", pb)