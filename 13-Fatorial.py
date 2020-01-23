n = int(input("Digite o valor de n: "))
p = n
if n == 0:
     p = 1
else:
    while n != 1:
        n -= 1
        p = p * n
print(p)
