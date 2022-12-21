

print("-------------------------------------------------------------")
print ("PPROGRAMA QUE MULTIPLICA OS NÚMEROS ÍPARES E SOMA OS PARES")
print("-------------------------------------------------------------")
n= 1
par = 0
impar = 1
print("Digite qualquer numero negativo para sair da repetição")
print("                                                       ")
while n >= 0:
    n = int(input("Digite um número inteiro e Positivo: "))
    if (n%2 == 0) and n>=0:
        par=par + n
    elif (n%2 == 1) and (n>=0):
        impar = impar * n
print("A Soma dos números pares é " + str(par))
print("A Multiplicação dos números impares é " + str(impar))






