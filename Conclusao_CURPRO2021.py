#Trabalho Final | Gustavo, Lucas e Vinicius


import time
import os #Importando bibliotecas com comandos externos


opcao = int(0) #Variáveis
paciente = []


def cadastrar(): #Funcao para realizar cadastro
      os.system('clear') or None
      print('----- CADASTRO -----')
      print('')
      paciente.append(input('Digite o nome: '))
      os.system('clear') or None
      print('----- CADASTRO -----')
      print('')
      print('Cadastro concluido!')
      time.sleep(2)

def atender(): #Função para realizar o atendimento
    if not paciente: #Caso a lista de pacientes esteja vazia
        os.system('clear') or None
        print('----- ATENDIMENTO -----')
        print('')
        print('A lista de pacientes esta vazia!')
        time.sleep(2)
    else:
        os.system('clear') or None
        print('----- ATENDINENTO -----')
        print('')
        paciente.pop(0)
        print('Atendimento concluido!')
        time.sleep(2)

def remover():
  if not paciente:
      os.system('clear') or None
      print('----- REMOVER -----')
      print('')
      print('A lista esta vazia!')
      time.sleep(2)
  else:
      os.system('clear') or None
      print('----- REMOVER -----')
      print('')
      paciente.pop(int(input('Digite o numero, do paciente: '))) #Remove paciente na posição desejada
      os.system('clear') or None
      print('----- REMOVER -----')
      print('')
      print('Paciente removido!')
      time.sleep(1)

def listar(): #Função para realizar a listagem
  if not paciente:
    os.system('clear') or None
    print('----- LISTAGEM -----')
    print('')
    print('A lista esta vazia!')
    time.sleep(2)
  else:
    for i in paciente:
      os.system('clear') or None
      print('----- LISTAGEM -----')
      print('')
      print('Paciente: ',i)
      time.sleep(2)

      
while (opcao != 5): #Repita se opcão não é 5
    os.system('clear') or None #Limpa tela
    print("---------- MENU ----------") #Menu
    print("|                        |")
    print("|   1 - Atendimento      |")
    print("|   2 - Cadastro         |")
    print("|   3 - Remover usuario  |")
    print("|   4 - Listagem         |")
    print("|   5 - Sair             |")
    print("|                        |")
    print("")
    time.sleep(0.5) #Timer de meio segundo
    opcao = int(input(' Digite a sua opcao: ')) 

    if (opcao == 1):
        atender()

    elif (opcao == 2):    
        cadastrar()

    elif (opcao == 3):
        remover()

    elif (opcao == 4):
        listar()

    elif (opcao > 5): 
        os.system('clear') or None
        print(' Opcao invalida! ')
        time.sleep(1.25)

    if (opcao == 5):
        break