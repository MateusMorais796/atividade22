# Crie um programa que receba vários números do usuário e some-os até que o número 0 seja digitado, momento em que o programa deve exibir o valor total.
soma = 0

n = float(input("Digite o número"))

while n > 1:
    soma += n
    n = float(input("Digite o número"))
    if n == 0:
        print(f'o valor total é', soma)


