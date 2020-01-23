X1 = int(input("Digite o número da cordenada X1: "))
Y1 = int(input("Digite o número da cordenada Y1: "))
X2 = int(input("Digite o número da cordenada X2: "))
Y2 = int(input("Digite o número da cordenada Y2: "))
import math
d = math.sqrt((X1 - X2)**2 + (Y1 - Y2)**2)
if d >= 10:
    print("longe")
else:
    print("perto")
