# github repositorios
 # testando o git
# Definindo uma lista de números
numeros = [10, 20, 30, 50, 50]

# Calculando a soma dos números
soma = sum(numeros)

# Calculando a média dos números
media = soma / len(numeros)

# Imprimindo os resultados 
print("Números:", numeros)
print("Soma:", soma)
print("Média:", media)
print(len(numeros))

#custo por anuncio
anuncio = 1200
#valor das compras
compras = 100
#em quantos dias
dias = 30

#vlor faturado
faturado = compras * dias

#lucro total
lucro = faturado - anuncio

print("faturado", faturado)
print("lucro", lucro)

contrato = 120.3
tempo = 12
resultado = contrato - tempo

#email de testes
email = "richardlorran@gmail.com"


#tamanho do texto em numeros
print(email.find(""))
 
#pegar um caractere
print(email[:10])


#troca um pedaço do texto
novo_texto = email.replace("gmail.com", "gag")

print(novo_texto)

nome = "richard lorran"
#deixar letras especificas maiusculas
#apenas a primeira letra
print(nome.capitalize())
#deixa a primeira letra de cada palavra maiuscula
print(nome.title())


#input faz o usuario respondere alguma coisa
email = input("Escreva seu email: ")
nome = input("Escreva seu nome: ")

print(nome, email)

print(f"{nome}, verifique seu email: {email} que enviamos")