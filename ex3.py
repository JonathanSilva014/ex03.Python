"""
Faça um programa que peça ao usuário para digitar um numero inteiro,
informe SE este número é par ou ímpar.
Caso o usuário não digite um número inteiro, 
informe que não é um número inteiro
"""
    
numero = input("Digite um número inteiro: ")

try:
    numero = int(numero)
    
    if numero % 2 == 0:
        print("Esse número que você digitou é par")
    else: 
        print("Esse Número que você digitou é impar")
        
except:
    print("Infelizmente isso não é um numero Inteiro")