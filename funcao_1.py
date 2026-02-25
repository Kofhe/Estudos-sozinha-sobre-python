#função é entrada, corpo da função e saída
#def é palavra chave que define uma função

# def saudacao():
#     print('ola')
# saudacao()

#funcao com parametro
# def saudacao(nome):
#     print(f'olá {nome}')
# saudacao('Andreia')
# sobrenome = 'Dias'
# saudacao (sobrenome)


#essa funcao vai percorrer a lista usando for para filtrar os pares
# def lista_pares(lista:list): 
#     for numero in lista:
#         if numero%2==0:
#             print(numero)
# lista_numerica = [1,2,3,4,5,6,7,8,9,10]
# lista_pares(lista_numerica)

# Crie uma função chamada media 
# que receberá três números como argumentos.
#  Esta função deve calcular a média aritmética desses três números. Para fazer isso, 
# some os três números
#  e, em seguida, divida o resultado por três. 
# Por fim, a função deve retornar o valor da média aritmética calculada.

def media(n1, n2, n3):
    soma = n1 + n2 + n3
    divisao_com_soma = soma / 3
    return divisao_com_soma

print(media(7, 8, 9))
