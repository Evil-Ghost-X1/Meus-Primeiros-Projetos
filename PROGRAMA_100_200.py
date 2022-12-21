print("PROGRAMA QUE MOSTRA QUANTOS NÚMEROS FORAM DIGITADOS ENTRE 100 E 200")
print("                                                                   ")
print("Digite 0 a qualquer momento para interromper a execução")
print("                                                                   ")

N = 1
tot=0
while N != 0:
    N = int(input("Digite um número inteiro: "))
    if (N > 100) and (N <200):
        tot = tot + 1
print("Foram digitados " + str(tot) + " numero(s) entre 100 e 200")




