import random

nsamples = 1000
random.seed(123)

total_subs = 0
total_cost = 0
total_failures = 0

for _ in range(nsamples):
    vida = 1.0
    subs = 0
    cost = 0
    failures = 0

    for _ in range(720):
        # verifica falha total
        if random.random() < 0.002:
            cost += 2000
            subs += 1
            failures += 1
            vida = 1.0
            continue

        # sorteia desgaste
        r = random.random()
        if r < 0.7:
            desgaste = 0.01
            custo = 400
        elif r < 0.9:
            desgaste = 0.03
            custo = 500
        else:
            desgaste = 0.07
            custo = 700

        vida -= desgaste

        # verifica se precisa substituir
        if vida <= 0:
            cost += custo
            subs += 1
            vida = 1.0

    total_subs += subs
    total_cost += cost
    total_failures += failures

# resultados
print("a) Média de substituições:", total_subs / nsamples)
print("b) Custo médio: R$", round(total_cost / nsamples, 2))
print("c) Média de falhas totais:", total_failures / nsamples)