# Crie um script que receba 4 valores e retorne a média dos valores.
# media = (valor1 + valor2 + valor3 + valor4)/4
def calcular_media(nota1, nota2, nota3, nota4):
    soma_das_notas =nota1 + nota2 + nota3 + nota4
    qtd_de_notas = 4
    media_das_notas = soma_das_notas / qtd_de_notas
    return media_das_notas

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = calcular_media(nota1, nota2, nota3, nota4)
print("A média das notas é: ", media)