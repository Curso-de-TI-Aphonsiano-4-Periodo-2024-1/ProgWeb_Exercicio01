# Crie um script para calcular a área de formas geométricas
#  * Retângulo (area = base * altura)
#  * Triângulo (area = (base * altura)/2 )
#  * Círculo (area = ℼ * r²)
import math

def area_retangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_circulo(raio):
    return math.pi * (raio ** 2)

def calculadora_geometrica():
    print("Bem-vindo(a) à calculadora de figuras geométricas!")
    print("Qual figura você gostaria de calcular a área?")
    print("1. Retângulo")
    print("2. Triângulo")
    print("3. Círculo")
    escolha = input("Digite o número correspondente à figura: ")

    
    if escolha == "1":
        base = float(input("Digite o tamanho da base do retângulo: "))
        altura = float(input("Digite o tamanho da altura do retângulo: "))
        print(f"A área do retângulo é {area_retangulo(base, altura)}")
    elif escolha == "2":
        base = float(input("Digite o tamanho da base do triângulo: "))
        altura = float(input("Digite o tamanho da altura do triângulo: "))
        print(f"A área do triângulo é {area_triangulo(base, altura)}")
    elif escolha == "3":
        raio = float(input("Digite o tamanho do raio do círculo: "))
        print(f"A área do círculo é {area_circulo(raio)}")
    else:
        print("Opção inválida")

calculadora_geometrica()