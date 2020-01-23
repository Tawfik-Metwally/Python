n = int(input("Digite um número inteiro: "))
divisor = 1
divisores = 1
while True:
if n % divisor == 0:
    divisor += 1
    if divisores > 1:
        print ("não primo")
else:
    print ("primo")
