import random

random.seed(123)
nsamples = 10000
n_notm = 6000
n_m = 4000
deffect_notm = 0
deffect_m = 0
total_c1_notm = 0
total_c3_notm = 0
total_c1_m = 0
total_c3_m = 0

for _ in range(n_notm):
    c1 = random.choices([True, False], weights=[4/100, 96/100], k=1)[0]
    c2 = random.choices([True, False], weights=[4/100, 96/100], k=1)[0]
    c3 = random.choices([True, False], weights=[6/100, 94/100], k=1)[0]
    c4 = random.choices([True, False], weights=[6/100, 94/100], k=1)[0]

    if c1 or c2 or c3 or c4:
        deffect_notm += 1

    if c1:
        total_c1_notm += 1
    
    if c3:
        total_c3_notm += 1

for _ in range(n_m):
    c1 = random.choices([True, False], weights=[4/100, 96/100], k=1)[0]
    c2 = random.choices([True, False], weights=[4/100, 96/100], k=1)[0]
    c3 = random.choices([True, False], weights=[3/100, 97/100], k=1)[0]
    c4 = random.choices([True, False], weights=[3/100, 97/100], k=1)[0]

    if c1 or c2 or c3 or c4:
        deffect_m += 1

    if c1:
        total_c1_m += 1
    
    if c3:
        total_c3_m += 1

print(f"chance de defeito num geral: {(deffect_notm+deffect_m)/nsamples:.5f}")
print(f"chance de defeito sem preventiva: {deffect_notm/n_notm:.5f}")
print(f"chance de defeito com preventiva: {deffect_m/n_m:.5f}")

print(f"defeito c1: {total_c1_m / (total_c1_m + total_c1_notm):.5f}")
print(f"defeito c3: {total_c3_m / (total_c3_m + total_c3_notm):.5f}")