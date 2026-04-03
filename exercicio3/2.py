import random

random.seed(123)

nsamples = 10000
area_total = 100*100
ruim = 0
media = 0
boa = 0
excelente = 0

for _ in range(nsamples):

    ax, ay = random.uniform(0,100), random.uniform(0,100)
    bx, by = random.uniform(0,100), random.uniform(0,100)
    cx, cy = random.uniform(0,100), random.uniform(0,100)

    area = abs((ax*(by-cy) + bx*(cy-ay) + cx*(ay-by)))/2

    if area < 0.05*area_total:
        ruim += 1
    elif area < 0.1*area_total:
        media += 1
    elif area < 0.2*area_total:
        boa += 1
    else:
        excelente += 1

print("chance de cada qualidade de cobertura:")
print(f"ruim: {ruim/nsamples*100:.2f}%")
print(f"media: {media/nsamples*100:.2f}%")
print(f"boa: {boa/nsamples*100:.2f}%")
print(f"excelente: {excelente/nsamples*100:.2f}%")