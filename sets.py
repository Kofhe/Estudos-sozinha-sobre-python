#set conjunto de elementos unicos e não ordenados (me lembra ul de html)
#Exemplo
# set1 = {'Infinity', 'School','BH'}
# set1 = {letra for letra in 'Infinity' if letra not in 'ae'}
# #if letra in infinity irá percorrer cada letra
# #if letra not in 'ae', remove a e
# print(set1)

# #Para adicionar no set se usa add().Exemplo:
# convidados = {'João', 'Maria', 'Eduarda'}
# convidados.add('Marcela')
# print(convidados)

# #ou o update, intersection
# convidados = {'João', 'Maria', 'Eduarda'}
# bicos = {'José','Carlos','Larisa'}
# convidados.update(bicos)
# print(convidados)

#precisa percorrer o set para visualizar
# convidados = {'João', 'Maria', 'Eduarda'}
# for i in convidados:
#     print(i)

#remover itens de um set
# convidados = {'João', 'Maria', 'Eduarda'}
# print(convidados.remove('Maria'))
# print(convidados)

#union()
# set1 = {1, 2, 3}
# set2 = {'z', 'x', 'a'}
# print(set1.union(set2))
# #ou
# print(set1 | set2)

