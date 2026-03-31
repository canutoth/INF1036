import random

random.seed(123)

nsamples = 1000
awins = 0
bwins = 0
cwins = 0
fighters = ["A", "B", "C"]

for _ in range(nsamples):
    rest = random.choices(fighters, weights=[4/10, 3/10, 3/10], k=1)[0]

    if rest == "A":
        winner = random.choices(["B", "C"], weights=[65/100, 35/100], k=1)[0]
        if winner == "B":
            winner = random.choices(["A", "B"], weights=[60/100, 40/100], k=1)[0]
        else:
            winner = random.choices(["A", "C"], weights=[45/100, 55/100], k=1)[0]
    
    elif rest == "B":
        winner = random.choices(["A", "C"], weights=[45/100, 55/100], k=1)[0]
        if winner == "A":
            winner = random.choices(["A", "B"], weights=[60/100, 40/100], k=1)[0]
        else:
            winner = random.choices(["B", "C"], weights=[65/100, 35/100], k=1)[0]
    
    else:
        winner = random.choices(["A", "B"], weights=[60/100, 40/100], k=1)[0]
        if winner == "A":
            winner = random.choices(["A", "C"], weights=[45/100, 55/100], k=1)[0]
        else:
            winner = random.choices(["B", "C"], weights=[65/100, 35/100], k=1)[0]
    
    if winner == "A":
        awins += 1
    elif winner == "B":
        bwins += 1
    else:
        cwins += 1

print(f"chance do A ganhar: {awins/nsamples:.2f}")
print(f"chance do B ganhar: {bwins/nsamples:.2f}")
print(f"chance do C ganhar: {cwins/nsamples:.2f}")