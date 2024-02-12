# Crie um script para calcular a área de formas geométricas
#  * Retângulo (area = base * altura)
#  * Triângulo (area = (base * altura)/2 )
#  * Círculo (area = ℼ * r²)
import math
#Retângulo

def areaRetanguo():

    baseR = float(input('Informe o valor da base do retângulo: '))
    alturaR = float(input('Informe o valor da altura do retângulo: '))

    areaR = round((baseR * alturaR),2)

    print('A área do Retângulo é: ', areaR)


#Triângulo

def areaTriangulo():

    baseT = float(input('Informe a base do triângulo: '))
    alturaT = float(input('Informe a altura do triangulo: '))

    areaT = round(((baseT * alturaT)/2),2)

    print('A área do Triângulo é: ', areaT)


#Círculo

def areaCirculo():

    raio = float(input('Informe o raio do círculo: '))

    areaC = round((math.pi * raio**2),2)

    print('A area do Círculo é: ', areaC)


alternativas = True

while alternativas:
    print('\n')
    print('Calcule a área de uma forma geométrica')
    print("""
    1.Calcular área do Retângulo
    2.Calcular área do Triângulo
    3.Calcular área do Círculo
    4.Sair
    """)

    alternativas= input('Gostaria de calcular a área de qual forma?: ')
    if alternativas == "1":
        print('\n')
        areaRetanguo()

    elif alternativas == "2":
        print('\n')
        areaTriangulo()

    elif alternativas == "3":
        print('\n')
        areaCirculo()

    elif alternativas == "4":
        print("\n Bye!")
        alternativas = None

    else:
        print("\n Tente novamente!")