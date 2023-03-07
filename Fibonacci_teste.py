indice = 13
soma = 0
k = 0

while k < indice:
    k += 1
    soma = soma + k
print(soma)

num = int(input("Digite um número inteiro: "))

fibo1 = 0
fibo2 = 1
fib03 = 1

while fibo3 < num:
    fibo1 = fibo2
    fibo2 = fibo3
    fibo3 = fibo1 + fibo2

if fibo3 == num:
    print("O número " + str(num) + "pertence à sequência de Fibonacci")
else:
    print("O número " + str(num) + "não pertence à sequência de Fibonacci")
