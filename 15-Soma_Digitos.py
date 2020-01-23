n = int(input("Digite um número inteiro: "))
p = n
x = 0
while not(p == 0):
        n = p
        n = n % 10
        p = p // 10
        x = x + n
print(x)
