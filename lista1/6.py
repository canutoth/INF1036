import random

random.seed(123)

nsamples = 10000
area = 0
count = 0

for _ in range(nsamples):
    x = random.random()
    y = random.random()
    no_a = False
    no_c = False

    if (x*x + y*y) <= 1:
        no_a = True
    
    if (((x-1)*(x-1))+((y-1)*(y-1))) <= 1:
        no_c = True
    
    if no_a and no_c:
        count += 1

print(f"media da area: {count/nsamples:.2f}")

print(f"total de adubo para {count/nsamples:.2f}km^2 de area em 12 meses = {count/nsamples*200*12:.2f}")