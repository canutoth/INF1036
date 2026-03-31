import random

random.seed(123)

nsamples = 10000
all_dif = 0 # a) nao tenha letras em comum
same_three = 0 # b) tenha as mesmas 3 letras, mas em posicoes diferentes
start_vowel = 0 # c) comece por vogal

letters = ["A", "B", "C", "D", "E", "F"]
vowels = {"A", "E"}

for _ in range(nsamples):
    sam = random.choices(letters, k=3)
    cat = random.choices(letters, k=3)

    if sam[0] in vowels and cat[0] in vowels:
        start_vowel += 1
    if not set(sam) & set(cat):
        all_dif += 1
    if sorted(sam) == sorted(cat) and sam != cat:
        same_three += 1

print(f"probabilidade A) {all_dif/nsamples:.2f}")
print(f"probabilidade B) {same_three/nsamples:.2f}")
print(f"probabilidade C) {start_vowel/nsamples:.2f}")