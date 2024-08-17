import random
from datetime import datetime

cartoes = ['R$50,00','R$250,00','R$120,00']

nome_de_usuario = str(input('Qual será o seu nome de usuario? '))
idade = datetime.strptime(input('Digite a sua data de nascimento seguindo o exemplo (dd/mm/aaaa): '),'%d/%m/%Y')
data_de_cadastro = datetime.now().day
print(f'Sejá bem vindo {nome_de_usuario}, seu registo foi concluido no dia {data_de_cadastro}')
print(f'Houve um sortei e você ganhou um cartão de compras no valor {random.choice(cartoes)}')
