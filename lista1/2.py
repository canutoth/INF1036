import random

random.seed(123)

total_rolls = 0
nsamples = 10000

for i in range(nsamples):
    l_results = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    while len(l_results) > 0:
        total_rolls += 1
        dices = random.choices(["1", "2", "3", "4", "5", "6"], weights=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], k=2)
        result = int(dices[0]) + int(dices[1])
        if int(result) in l_results:
            i = l_results.index(result)
            l_results.pop(i)

media = total_rolls/nsamples
print(f"aproximadamente {media:.2f} pares de dados foram jogados ate obter todas as somas")