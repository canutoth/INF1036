import random

random.seed(123)

nsamples = 1000
numpastilhas = 4
size = 11
total_wins = 0
total_lost = 0

def mover(posicao, dimensao):
    direcoes = [(-1,0), (1,0), (0,-1), (0,1)]
    x, y = posicao
    while True:
        dx, dy = random.choice(direcoes)
        nx, ny = x + dx, y + dy
        if (1 <= nx) and (nx <= dimensao) and (1 <= ny) and (ny <= dimensao):
            return (nx, ny)

def alocapastilhas(qtd_pastilhas, dimensao):
    pastilhas = set()

    while len(pastilhas) < qtd_pastilhas:
        pos = (random.randint(1, dimensao), random.randint(1, dimensao))
        if (pos != (1,1)):
            pastilhas.add(pos)
    
    return list(pastilhas)

for _ in range(nsamples):
    pastilhas = alocapastilhas(numpastilhas, size)
    pacman = (1, 1)
    ghosts = [(1, size), (size, 1), (size, size)]
    pacdies = False
    past_coletadas = 0

    while not pacdies:
        pacman = mover(pacman, size)
        
        if pacman in pastilhas:
            pastilhas.remove(pacman)
            past_coletadas += 1
            
        if past_coletadas == numpastilhas:
            total_wins += 1
            break
            
        ghosts = [mover(g, size) for g in ghosts]
            
        if pacman in ghosts:
            pacdies = True


print(f"chance de vitoria estimada: {total_wins/nsamples:.4f}")