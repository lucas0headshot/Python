#Determinar o posto mais logne possível que um carro consegue alcançar com uma quantidade de combustivel

def ultima_parada(combustivel,consumo,postos_de_gasolina): #Litros | L/Km | Postos(Km)
    i = 0
    postos_possiveis = []
    
    for i in range(len(postos_de_gasolina)):
      if (postos_de_gasolina[i] <= consumo * combustivel):
        postos_possiveis.append(postos_de_gasolina[i])
        
    if (len(postos_possiveis) > 0):
      return(max(postos_possiveis))
    else:
      return (-1)

ultima_parada(2, 8, [20, 30, 40])