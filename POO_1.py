# class Carro: #molde de carro

#     # Aqui é o método construtor.
#     '''
#         Nele, a gente vai instaciar o próprio objeto dessa clase e irá pegar as caracteristicas (atributos) do carro.

#         - O que é o 'self'?
#             r. O self é o próprio objeto que será construído depois.

#         __init__ significa inicializar.
#     '''
#     def __init__(self, marca, modelo, ano, possui_4_rodas):
#         self.marca = marca #self representa o objeto que está sendo criado
#         self.modelo = modelo #guarda o modelo dentro do objeto
#         self.ano = ano 
#         self.possui_4_rodas = possui_4_rodas

#     '''
#         def (função) dentro de uma classe é um método (ação)

#         O 'self' dentro do método, serve para você pegar os atributos do método construtor.
#     '''
  
#     def ligar(self): #está criando um método
#      return f' O {self.marca} {self.modelo} está ligado' #pq usar o return: devolver o valor para quem chamou a função
        
# # Agora vamos fabricar um carro

# carro1 = Carro('Fiat', 'Palio', 2009, True)

# print(carro1.ligar())
# print(carro1.modelo)
# print(carro1) #objeto


class ContaBancaria: #molde de conta
    def __init__(self, saldo_inicial): #init é para iniciar e self representa o que irá cria
        self.saldo_inicial = saldo_inicial
    
    def depositar(self, novo_valor):
        if novo_valor > 0:
            self.saldo_inicial += novo_valor
            print(f'R${novo_valor} depositado com sucesso.')
            print(f'Novo saldo: R${self.saldo_inicial}')
        else:
            print('Erro! O valor não pode ser negativo.')
    
    # Método (Ação)
    def sacar(self, valor):
        if valor < self.saldo_inicial:
            self.saldo_inicial = self.saldo_inicial - valor
            print(f'R${valor} sacado com sucesso')
            print(f'Novo saldo: R${self.saldo_inicial}')
        else:
            print('Erro! Saldo insuficiente.')

andreia = ContaBancaria(50) #quanto tenho em conta
andreia.depositar(1500) #sou rica
andreia.sacar(1500) #tristeza
andreia.sacar(1500) #não vai permitir
