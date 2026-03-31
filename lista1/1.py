import random

nsamples = 10000
double_heads = 0
random.seed(123)


for i in range(nsamples):
    coin = random.choices(["heads", "tails"], weights=[1/2, 1/2], k=2)
    if "tails" not in coin:
        double_heads += 1
    
    
print("o numero de lancamentos com 2 caras foi:" + str(double_heads))
