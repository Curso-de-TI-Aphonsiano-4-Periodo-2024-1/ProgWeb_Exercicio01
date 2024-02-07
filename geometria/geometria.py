# Crie um script para calcular a área de formas geométricas
#  * Retângulo (area = base * altura)
#  * Triângulo (area = (base * altura)/2 )
#  * Círculo (area = ℼ * r²)
import math

print ('*' * 10, 'GEOMETRIA', '*' * 10)

# Verifica se o valor infomrado e um número ou não
def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
#---------------------------------------------------------------------------------#
# Calculo da área do retângulo
def AreaRetangulo():

    print ('*' * 10,'CALCULO DO RETÂNGULO', '*' * 10)

    baseRetangulo = input('Informe o valor da base:')
    while is_numeric(baseRetangulo) == False:
        print ('Valor informado invalido!!. Tente novamente.')
        baseRetangulo = input('Informe o valor da base:')

    alturaRetangulo = input('informe o valor da altura:')
    while is_numeric(alturaRetangulo) == False:
        print('Valor informado invalido!!. Tente novamente.')
        alturaRetangulo = input('Informe o valor da altura:')

    areaRetangulo = (float(baseRetangulo) * float(alturaRetangulo))

    print ('O valor da área do retângulo é: {}' .format(areaRetangulo))
#---------------------------------------------------------------------------------#
# calculo da área do triângulo
def AreaTriangulo():

    print ('*' * 10, 'CALCULO DO TRIÂNGULO', '*' * 10)

    baseTriangulo = input('Informe o valor da base:')
    while is_numeric(baseTriangulo) == False:
        print ('Valor informado invalido!!. Tente novamente.')
        baseTriangulo = input('Informe o valor da base:')

    alturaTriangulo = input('Informe o valor da área:')
    while is_numeric(alturaTriangulo) == False:
        print ('Valor informado invalido!!. Tente novamente.')
        alturaTriangulo = input('Informe o valor da área:')
    
    areaTriangulo = ((float(baseTriangulo) * float(alturaTriangulo)) / 2)

    print ('O valor da área do triângulo é: {}' .format(areaTriangulo))
#---------------------------------------------------------------------------------#
# calculo da área do círculo
def AreaCirculo():

    print('*' * 10, 'CALCULO DO CÍRCULO', '*' * 10)

    raioCirculo = input('Informe o valor do raio:')
    while is_numeric(raioCirculo) == False:
        print ('Valor informado invalido!!. Tente novamente.')
        raioCirculo = input('Informe o valor do raio:')

    pi_valor = math.pi

    areaCirculo = (pi_valor * (float(raioCirculo)**2))

    print ('O valor da área do círculo é: {:.2f}' .format(areaCirculo))
#---------------------------------------------------------------------------------#
    
alternativas = True

while alternativas:
    print ('-' * 50)
    print("""
          1. Calcular a área do retângulo.
          2. Calcular a área do triângulo.
          3. Calcular a área do círculo.
          4. Sair.
          """)
    print ('-' * 50)
    
    alternativas = input('Escolha a forma geométrica que deseja calcula:')
    
    if alternativas == '1':
        AreaRetangulo()
    if alternativas == '2':
        AreaTriangulo()
    if alternativas == '3':
        AreaCirculo()
    else:
        exit()