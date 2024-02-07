# Crie um script calcule a fórmula de fórmula de Bhaskara.
import math

def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

a = input('Informe o valor de "a":')
while is_numeric(a) == False:
    print ('Informação invalida!! Informe um número valido.')
    a = input('Informe o valor de "a":')

b = input('Informe o valor do "b":')
while is_numeric(b) == False:
    print ('Informação invalida!! Informe um número valido.')
    b = input('Informe o valor de "b":')

c = input('Informe o valor de "c":')
while is_numeric(c) == False:
    print ('Informação invalida!! Informe um número valido.')
    c = input('Informe o valor de "c":')

delta = (float(b)**2 - 4 * float(a) * float(c))

if delta < 0:
    print ('Essa equação não possui um valor real. :(')
else:
    raiz1 = (- float(b) + math.sqrt(float(delta))) / (2 * float(a))
    raiz2 = (- float(b) - math.sqrt(float(delta))) / (2 * float(a))
    print ('A equação possui duas raizes real: {:.2f} é {:.2f}' .format(raiz1, raiz2))