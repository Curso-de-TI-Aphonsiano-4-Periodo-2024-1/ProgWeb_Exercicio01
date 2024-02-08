# Crie um script que receba 4 valores e retorne a média dos valores.
# media = (valor1 + valor2 + valor3 + valor4)/4


valor_primeiro = int(input("informe o primeiro valor:"))
valor_segundo = int(input("informe o segundo valor:"))
valor_terceiro = int(input("informe o terceiro valor:"))
valor_quarto = int(input("informe o quarto valor:"))
soma_dos_valores = valor_primeiro + valor_segundo + valor_terceiro + valor_quarto 
media = soma_dos_valores / 4
print(soma_dos_valores)
print("Resultado:"+str(media))

