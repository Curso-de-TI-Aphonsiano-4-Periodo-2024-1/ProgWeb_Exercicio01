# Crie um script calcule a fórmula de fórmula de Bhaskara.

import math

def bhaskara(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return None, None
    elif delta == 0:
        raiz = - b / (2 * a)
        return raiz, None
    else:
        raiz1 = (- b + (delta ** 0.5)) / (2 * a)
        raiz2 = (- b - (delta ** 0.5)) / (2 * a)
        return raiz1, raiz2

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

raiz1, raiz2 = bhaskara(a, b, c)

if raiz1 is None:
    print("A equação não possui raízes reais.")
elif raiz2 is None:
    print(f"A única raiz real da equação é: {raiz1}")
else:
    print(f"As raízes reais da equação são: {raiz1} e {raiz2}")