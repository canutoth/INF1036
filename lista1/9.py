import random

random.seed(123)

nsamples = 10000

awins = 0
bwins = 0
over3matches = 0
b_b = 0
a_rarewin = 0


for _ in range(nsamples):
    win_a = 0
    win_b = 0
    matches = 0
    matching = []
    while win_a < 3 and win_b < 3:
        matches += 1
        winner = random.choices(["A", "B"], weights=[4/10, 6/10], k=1)[0]
        matching.append(winner)

        if winner == "A":
            win_a += 1
        else:
            win_b += 1

    if matches > 3:
        over3matches += 1
    
    if win_a == 3:
        awins += 1
    elif win_b == 3:
        bwins += 1
    
    if matching[0] == "B" and matching[1] == "B":
        b_b += 1
        if win_a == 3:
            a_rarewin += 1
    

print(f"chance de A ganhar: {awins/nsamples:.2f}")
print(f"chance de B ganhar: {bwins/nsamples:.2f}")

print(f"chance de mais de 3 partidas: {over3matches/nsamples:.2f}")

print(f"chance de B ganhar após 2 vitórias iniciais de A: {a_rarewin/b_b:.2f}")