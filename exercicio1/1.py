# a) usando LCG

x = 3
a = 39373
c = 0
m = 2147483647

nsamples = 10

for i in range(nsamples):
    x = (a * x + c) % m
    u = x / m
    strength = 10.0 + u * (20.0 - 10.0)
    
    x = (a * x + c) % m
    u = x / m
    speed = 5.0 + u * (15.0 - 5.0)
    
    x = (a * x + c) % m
    u = x / m
    brightness = 8.0 + u * (18.0 - 8.0)
    
    print(f"personagem {i+1:02d}: forca - {strength:.2f}; agilidade - {speed:.2f}; inteligencia - {brightness:.2f}")

print("\n\n")

# b) usando random

import random

random.seed(123)

for i in range(nsamples):
    strength = random.uniform(10,20)
    speed = random.uniform(5, 15)
    brightness = random.uniform(8,18)
    print(f"personagem {i+1:02d}: forca - {strength:.2f}; agilidade - {speed:.2f}; inteligencia - {brightness:.2f}")