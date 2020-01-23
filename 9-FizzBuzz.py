numero = int(input("Digite um número inteiro: "))
N = (numero % 3) + (numero % 5)
if N == 0 :
    print("FizzBuzz")
else:
    print(numero)
