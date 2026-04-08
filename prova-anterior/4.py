import random

random.seed(123)

nsamples = 10000
dentro = 0

for i in range(nsamples):
    x = random.random()
    y = random.random()

    if x**2 + y**2 > 1 and x >= 0.5:
        dentro += 1
    
area = dentro/nsamples
volume = area*6

custo = volume * 250.00

print(f"gasto: R${custo:.2f}")