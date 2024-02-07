# Crie um script que receba 4 valores e retorne a média dos valores.
# media = (valor1 + valor2 + valor3 + valor4)/4
print ('*' * 5, 'MEDIA', '*' * 5)

def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
   
valor1 = input('Informe o 1º valor:')
while is_numeric(valor1) == False:
    print('Infomração invalida. Por favor, inforem um numero!')
    valor1 = input('Informe o 1º valor')

valor2 = input('Informe o 2º valor:')
while is_numeric(valor2) == False:
    print('Informação invalida. Por favor, informe um número!')
    valor2 = input('Informe o 2º valor:')

valor3 = input('Informe o 3º valor:')
while is_numeric(valor3) == False:
    print('Informação invalida. Por favor, informe um número.')
    valor3 = input('Informe o 3º valor:')

valor4 = input('Informe o 4º valor:')
while is_numeric(valor4) == False:
    print('Informação invalida. Por favor, informe um número.')
    valor4 = input('Informe o 4º valor:')

media = ((float(valor1) + float(valor2) + float(valor3) + float(valor4)) / 4)

print ('A média dos 4 valores informados foi:{:.1f}' .format(media))