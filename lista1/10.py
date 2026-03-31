import random

random.seed(123)

nsamples = 1000
reps = 100
p = 150
s = 70
i = 240
j = 0

while p > 0 and s > 0 and i > 0 and j < nsamples:
    winner = random.choices(["P", "S", "I"], weights=[3/10, 4/10, 3/10], k=1)[0]

    if winner == "P":
        s -= 1
        i -= 1
        p += 2
    elif winner == "S":
        s += 2
        i -= 1
        p -= 1
    else:
        s -= 1
        i += 2
        p -= 1

    j += 1

print("sobrou ", s, " para simone")
print("sobrou ", p, " para pedro")
print("sobrou ", i, " para ivo")

media_s = 0
media_p = 0
media_i = 0
tot_fails = 0

for _ in range(reps):
    p = 150
    s = 70
    i = 240
    j = 0

    while p > 0 and s > 0 and i > 0 and j < nsamples:
        winner = random.choices(["P", "S", "I"], weights=[3/10, 4/10, 3/10], k=1)[0]

        if winner == "P":
            s -= 1
            i -= 1
            p += 2
        elif winner == "S":
            s += 2
            i -= 1
            p -= 1
        else:
            s -= 1
            i += 2
            p -= 1

        j += 1
    
    media_s += s
    media_p += p
    media_i += i
    if p == 0 or s == 0 or i == 0:
        tot_fails += 1

print(f"quantia final media da simone: R${media_s/reps:.2f}")
print(f"quantia final media do pedro: R${media_p/reps:.2f}")
print(f"quantia final media do ivo: R${media_i/reps:.2f}")
print("total de rodadas em que alguem faliu: ", tot_fails)