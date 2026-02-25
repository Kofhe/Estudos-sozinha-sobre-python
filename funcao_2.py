#funcao é para realizar tarefa especificas

# def soma(a,b):
#     return a + b
# resultado = soma(5, 3)
# print(resultado)

#calcular o quadrado de um numero
# def quadrado(numero):
#     resultado = numero ** 2
#     return resultado
# resultado = quadrado(5)
# print(resultado)

#args(argumentos posicionais arbitrários)
#permite que você passe vários argumentos posicionais para uma função, sem definir quantos serão.

# def exemplo(*args):
#     print(args)
# exemplo(1,2,3) #transforma em tupla

# def somar(*args):
#     total = 0
#     for numero in args:
#         total += numero
#     return total
# print(somar(1,2,3))

# def apresentar(*args):
#     print(f" ola meu nome e {args[0]},tenho {args[1]} idade, moro no {args[2]}")

# apresentar("Ana", 25, "Brasil")

#Kwargs - chave e valor(dicionario)

def mostrar (**kwargs):
    print(kwargs)
mostrar(nome = 'ana', idade = 25, pais = 'brasil')
