import random

def simular_evento(n, num_simulacoes=10000):
    if n < 3:
        print("Para n < 3, não é possível sentar as pessoas seguindo as regras.")
        return 0.0, 0.0

    def gerar_dia_valido():
        while True:
            homens = ["H" + str(i) for i in range(1, n + 1)]
            mulheres = ["M" + str(i) for i in range(1, n + 1)]
            
            random.shuffle(homens)
            random.shuffle(mulheres)
            
            comeca_homem = random.choice([True, False])
            
            cadeiras = []
            for i in range(n):
                if comeca_homem:
                    cadeiras.append(homens[i])
                    cadeiras.append(mulheres[i])
                else:
                    cadeiras.append(mulheres[i])
                    cadeiras.append(homens[i])
                    
            valido = True
            for i in range(2 * n):
                pessoa_atual = cadeiras[i]
                pessoa_seguinte = cadeiras[(i + 1) % (2 * n)]
                
                id_atual = pessoa_atual[1:]
                id_seguinte = pessoa_seguinte[1:]
                
                if id_atual == id_seguinte:
                    valido = False
                    break
                
            if valido:
                return cadeiras
    
    casos_condicao_1 = 0
    casos_condicao_2 = 0
    
    for _ in range(num_simulacoes):
        dia1 = gerar_dia_valido()
        dia2 = gerar_dia_valido()
        dia3 = gerar_dia_valido()
        
        if dia1 == dia2 and dia3 != dia1:
            casos_condicao_1 += 1
            
        if dia1 != dia2 and dia1 != dia3 and dia2 != dia3:
            casos_condicao_2 += 1
            
    prob_1 = casos_condicao_1 / num_simulacoes
    prob_2 = casos_condicao_2 / num_simulacoes
    
    return prob_1, prob_2

n_casais = 5
simulacoes = 10000

print(f"simulando {n_casais} casais ({simulacoes} eventos)...")
prob1, prob2 = simular_evento(n_casais, simulacoes)

print(f"chance de D1=D2 e D3!=D1: {prob1:.10f}")
print(f"chance de D1, D2 e D3 diferentes: {prob2:.10f}")