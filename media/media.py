# Crie um script que receba 4 valores e retorne a média dos valores.
# media = (valor1 + valor2 + valor3 + valor4)/4


valor_primeiro = int(input("Informe 1:"))

valor_segundo = int(input("Informe 2:"))

valor_terceiro = int(input("Informe 3:"))

valor_quarto = int(input("Informe 4:"))

soma_dos_valores = valor_primeiro + valor_segundo + valor_terceiro + valor_quarto

print(soma_dos_valores)

media = soma_dos_valores / 4

print("Resultado:"+str(media))
