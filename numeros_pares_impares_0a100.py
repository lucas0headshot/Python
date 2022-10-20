#Lucas Teixeira Ronchi 
#Vaga de estágio - Desenvolvedor
#Imprimir todos os números pares e ímpares entre 0(zero) e 100(cem)

Numero = int(0) #Variável

print ('Números pares entre 0(zero) e 100(cem) -')
for Numero in range(0,101,2): #Estrutura de repetição, utilizando a função range com três argumentos (num inicial, num final, intervalo entre os números)
  print(Numero)
  
print('')

print ('Números ímpares entre 0(zero) e 100(cem) -')
for Numero in range(1,101,2):
  print(Numero)