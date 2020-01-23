a = float(input("Digite o numero a: "))
b = float(input("Digite o numero b: "))
c = float(input("Digite o numero c: "))
delta = (b**2) - (4 * a * c)
import math
if delta < 0:
    print("esta equação não possui raízes reais")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    if raiz1 > raiz2:
        R1 = int(raiz1)
        R2 = int(raiz2)
    else:
        R1 = int(raiz2)
        R2 = int(raiz1)
    if delta == 0:
        print("a raiz desta equação é", raiz1)
    else:
        print("as raízes da equação são",R2,"e",R1)
