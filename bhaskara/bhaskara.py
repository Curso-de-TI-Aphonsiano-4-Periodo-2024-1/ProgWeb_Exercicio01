# Crie um script calcule a fórmula de fórmula de Bhaskara.


def bhaskara(a,b,c):
  delta = (b**2) - (4*a*c)

  raiz1 = (((-1)*b) + (delta**0.5))/(2*a)
  raiz2 = (((-1)*b) - (delta**0.5))/(2*a)

  if delta == 0:
    print('\n')
    print("Como Delta = 0, temos um único valor de raíz: ",raiz1)

  elif delta > 0:
    print('\n')
    print("Como Delta > 0, temos dois valores distintos de raízes: ",raiz1,"e",raiz2)

  else:
    print()
    print("Como Delta < 0, não temos raízes reais!")


a = float(input("Informe o valor do coeficiente a: "))
b = float(input("Informe o valor do coeficiente b: "))
c = float(input("Informe o valor do coeficiente c: "))
bhaskara(a,b,c)