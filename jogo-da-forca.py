from time import sleep
import random

linha = "-" * 100
titulo = "Gerenciador de Senhas"

print(linha)
print(titulo.center(75))
print(linha)

tamanho = int(input("Quantos elementos terá sua senha? [1/71]: "))
print(linha)

geren_letras = "abcdefghijklmnopqrstuvwxyz"
geren_letras_grandes = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
geren_number = "0123456789"
geren_simbolos = "!@#$%&*()"

gerenciamento = geren_letras + geren_letras_grandes + geren_number + geren_simbolos

senha = "".join(random.sample(gerenciamento, tamanho))

print(f"O tamanho da senha será de {tamanho} elementos")
print(linha)
sleep(1.5)
print(f"Sua senha é -> {senha}")
print(linha)
input()
