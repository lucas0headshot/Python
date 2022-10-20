import os #Importando comandos externos
import time
import colorama
from colorama import Fore
from colorama import Style
from random import choice


vocabulario = ["algoritmo", "programar", "python", "programa", "software", "computador", "hardware", "carlos", "desafio"]
#Variáveis | Lista contendo as palavras que vamos usar \ Não pode olhar! xD
palavra = choice(vocabulario) #Escolhendo aleatoriamente uma palavra do vocabulário
erros = 0
alfabeto = list("abdcefghijklmnopqrstuvwxyz") #Lista contendo o alfabeto, para evitar que o usuário digite números, símbolos e etc
tentativas = []
letra = str


def forca(erros): #Função que "desenha" a forca
    print(Style.RESET_ALL +"  _______     ")
    print(" |/      |    ") #"Style.RESET_ALL" é usado para atribuir cores ao texto
    
    if (erros == 1): #Se a variável "erros" for igual a 1 ...
        print(Fore.WHITE +" |      "+ Style.RESET_ALL + Fore.RED +"(_)   "+ Style.RESET_ALL)
        print(" |            ")
        print(" |            ")
        print(" |            ")
    
    if (erros == 2):
        print(Fore.WHITE +" |      "+ Style.RESET_ALL + Fore.RED +"(_)   "+ Style.RESET_ALL)
        print(Fore.WHITE +" |      "+ Style.RESET_ALL + Fore.RED +"\     "+ Style.RESET_ALL)
        print(" |            ")
        print(" |            ")
    
    if (erros == 3):
        print(Fore.WHITE +" |      "+ Style.RESET_ALL + Fore.RED +"(_)   "+ Style.RESET_ALL)
        print(Fore.WHITE  +" |      "+ Style.RESET_ALL + Fore.RED +"\|    "+ Style.RESET_ALL)
        print(" |            ")
        print(" |            ")
    
    if (erros == 4):
        print(Fore.WHITE +" |      "+ Style.RESET_ALL + Fore.RED +"(_)   "+ Style.RESET_ALL)
        print(Fore.WHITE +" |      "+ Style.RESET_ALL + Fore.RED +"\|/   "+ Style.RESET_ALL)
        print(" |            ")
        print(" |            ")
    
    if (erros == 5):
        print(Fore.WHITE +" |      "+ Style.RESET_ALL + Fore.RED +"(_)   "+ Style.RESET_ALL)
        print(Fore.WHITE +" |      "+ Style.RESET_ALL + Fore.RED +"\|/   "+ Style.RESET_ALL)
        print(Fore.WHITE +" |       "+ Style.RESET_ALL + Fore.RED +"|    "+ Style.RESET_ALL)
        print(" |            ")
    
    if (erros == 6):
        print(Fore.WHITE +" |      "+ Style.RESET_ALL + Fore.RED +"(_)   "+ Style.RESET_ALL)
        print(Fore.WHITE +" |      "+ Style.RESET_ALL + Fore.RED +"\|/   "+ Style.RESET_ALL)
        print(Fore.WHITE +" |       "+ Style.RESET_ALL + Fore.RED +"|    "+ Style.RESET_ALL)
        print(Fore.WHITE +" |      "+ Style.RESET_ALL + Fore.RED +"/     "+ Style.RESET_ALL)
    
    if (erros == 7):
        print(Fore.WHITE +" |      "+ Style.RESET_ALL + Fore.RED +"(_)   "+ Style.RESET_ALL)
        print(Fore.WHITE +" |      "+ Style.RESET_ALL + Fore.RED +"\|/   "+ Style.RESET_ALL)
        print(Fore.WHITE +" |       "+ Style.RESET_ALL + Fore.RED +"|    "+ Style.RESET_ALL)
        print(Fore.WHITE +" |      "+ Style.RESET_ALL + Fore.RED +"/ \   "+ Style.RESET_ALL)
    
    print(" |            ")
    print("_|___         ")
    print()

def perder(palavra): #Fuynção para exibir mensagem caso o jogador perca
    os.system('clear') or None #Limpa a tela
    print(Fore.RED + "Vish, você foi enforcado!" + Style.RESET_ALL)
    time.sleep(1.5) #Timer de 1,5 segundos
    print("A palavra era: {}".format(palavra)) #Exibe a palavra em um formato padrão
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print('')
    print('Feito por:' + Fore.RED + ' Lucas0 headshot' + Style.RESET_ALL)
    print('Obrigado por tentar. Boa sorte na proxima! ;)')

def ganhar(): #Função para exibir mensagem caso o jogador ganhe
    os.system('clear') or None
    print(Fore.GREEN +"Parabéns, você ganhou!"+ Style.RESET_ALL)
    time.sleep(1.5)
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print('')
    print('Feito por:' + Fore.RED + ' Lucas0 headshot' + Style.RESET_ALL)
    print('Obrigado por jogar! ;)')

while True: #Estrutura de repetição que manterá o jogo em execução até que o jogador perca ou ganhe
    if set(palavra).issubset(set(tentativas)): #Verifica se o jogador acertou a palavra
      ganhar()
      break

    os.system('clear') or None 
    print('Bem-vindo(a) ao Jogo da Forca!')
    print('Feito por:' + Fore.RED + ' Lucas0 headshot' + Style.RESET_ALL)
    print('')
    print(Fore.BLUE +'Tentativas: ',tentativas)
    
    forca(erros) #Chama a função "forca", fazendo com que ela "comece" a "desenhar" a forca
    if (erros == 6): #Se "erros" for igual a 6, exibe uma mensagem avisando o jogador
      print(Fore.YELLOW +'Se errar novamente, voce sera enforcado!'+ Style.RESET_ALL)
      print('')

    for letra in palavra: #For que fará a tracejado indicando a palavra
        if letra in tentativas:
            print(letra, end = ' ')
        else:
            print('_', end = ' ')
    
    print('')
    print('')
    palpite = input('Digite o seu palpite! ') #Perguntando ao jogador o seu palpite
    if (palpite not in alfabeto or palpite == ''): #Se o palpite não estiver no alfabeto ou for nulo, exibe uma mensagem avisando
        print(Fore.YELLOW + 'O que? Isso nao e uma letra! *-*' + Style.RESET_ALL)
        time.sleep(1.2)
    elif (palpite in tentativas): #Se o palpite estiver na lista "tentativas", exibe uma mensagem avisando
        print('')
        print(Fore.YELLOW + 'Ham? Voce ja tentou esta letra. Tente outra! *-*' + Style.RESET_ALL)
        time.sleep(1.25)
        pass

    tentativas.append(palpite) #Adiciona o palpite a lista de tentativas
    if (palpite in palavra): #Se o palpite estiver na palavra, exibe uma mensagem ao jogador
        print('')
        print(Fore.GREEN + 'Parabens! Voce acertou ;)' + Style.RESET_ALL)
        time.sleep(1.15)
    else:
        print('')
        print(Fore.RED + 'F! Voce errou ;(' + Style.RESET_ALL)
        erros += 1
        time.sleep(1.15)
  
    if (erros == 7): #Se "erros" for igual a 7, chama a função "perder"
        perder(palavra)
        break