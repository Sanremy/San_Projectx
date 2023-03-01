indice = 13
soma = 0
k = 0

while k < indice:
    k = k + 1
    soma = soma + k
print(soma)

num = int(input("Digite um número inteiro: "))

fib1 = 0
fib2 = 1
fib3 = 1

while fib3 < num:
    fib1 = fib2
    fib2 = fib3
    fib3 = fib1 + fib2

if fib3 == num:
    print(num, "pertence à sequência de Fibonacci")
else:
    print(num, "não pertence à sequência de Fibonacci")
