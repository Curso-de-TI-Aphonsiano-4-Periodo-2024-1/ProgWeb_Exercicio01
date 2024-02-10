# Crie um script que receba 4 valores e retorne a média dos valores.
# media = (valor1 + valor2 + valor3 + valor4)/4
print('*' * 5, 'Media', '*' *5)

def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

valor1 = float(input("Digite o primeiro valor: "))
while is_numeric(valor1) == False:
   print('Informação Invalida! Por favor, informe um numero')
   valor1 = input('Informe o 1º valor')
   
valor2 = float(input("Digite o segundo valor: "))
while is_numeric(valor2) == False:
   print('Informação Invalida! Por favor, informe um numero')
   valor2 = input('Informe o 2º valor')
   
valor3 = float(input("Digite o terceiro valor: "))
while is_numeric(valor3) == False:
   print('Informação Invalida! Por favor, informe um numero')
   valor3 = input('Informe o 3º valor')
   
valor4 = float(input("Digite o quarto valor: "))
while is_numeric(valor4) == False:
   print('Informação Invalida! Por favor, informe um numero')
   valor4 = input('Informe o 4º valor')
   
media = ((float(valor1) + float(valor2) + float(valor3) + float(valor4)) / 4)
print("A média dos 4 valores informados são:", media)