#Lambda são funções anonimas e pequenas

# def menos_tres(x):
#     return x - 3
# print(menos_tres(10))

# é a mesma coisa que

# f = lambda x: x - 3
# # x = 10
# # 10 - 3
# print(f(10)) #os () é para executar a função e 10 argumento

### #atividade multiplicar cada número por 2
# numeros = [1, 2, 3, 4, 5]

# #map() serve para aplicar a mesma função em cada item de uma coleção sem precisar usar um for

# resultado = list(map(lambda x: x * 2,numeros))
# print(resultado) #resultado é só o nome da lista final que você quer guardar

# lambda parametro: expressão

# parametro → nome que você escolhe para cada elemento (pode ser x, n, num…)

# expressão → o que você quer que a função retorne automaticamente
# lambda x: x * 2         # multiplica por 2
# lambda n: n + 5         # soma 5
# lambda s: s.upper()     # deixa maiúsculo (para strings)

###Primeiro é subtraído de 3 e depois multiplicado por 2

# numeros = [5, 10, 15, 20]

# resultado = list(map(lambda x : (x - 3) *2, numeros))
# print(resultado)

##Crie uma lista nova usando lambda + map, onde cada nome fique em maiúsculas.

# nomes = ["ana", "bruno", "carla"]

# maiusculas = list(map(lambda x:x.upper(), nomes)) #upper é uma função do objeto string, então usamos parênteses () para chamar
# print(maiusculas)

##filter
# lista = [1, 2, 3, 4, 5, 6]
# pares = list(filter(lambda x: x % 2 == 0, lista))
# print(pares)

# Crie uma função chamada maior_numero que receberá três números como argumentos. Esta função deve comparar os três números e identificar qual deles é o maior. Para isso, utilize uma estrutura de controle que verifique qual número é maior que os outros dois. A função deve então retornar o maior número encontrado.

def maior_numero(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n1 and n2>n3:
        return n2
    else:
        return n3
print(maior_numero(10, 20, 15))
