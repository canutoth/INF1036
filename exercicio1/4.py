import random

random.seed(123)

dias = 100
voos = 2000
p = 190
capacidade = 180
total_sobra = 0
total_voluntarios = 0
total_forcados = 0
custo_total = 0
overbooking = 0
fila = 0

for voo in range(voos):
    presente = 0

    for _ in range(p):
        chance = random.uniform(0.90,0.95)
        if random.random() < chance:
            presente += 1
    
    embarque = fila + presente

    if embarque > capacidade:
        overbooking += 1
        sobra = embarque - capacidade
    
        voluntarios = int(sobra * 0.25)
        total_voluntarios += voluntarios

        forcado = sobra - voluntarios
        total_forcados += forcado
        
        gasto = voluntarios*1000 + forcado*2500
        custo_total += gasto
        fila = sobra
    else:
        fila = 0


print(f"taxa media de overbooking: {(overbooking/voos)*100:.2f}%")
print(f"custo total de compensacoes: R${custo_total:.2f}")
print(f"custo medio diario de compensacoes: R${custo_total/dias:.2f}")
print(f"passageiros voluntarios: {total_voluntarios}")
print(f"passageiros forcados: {total_forcados}")