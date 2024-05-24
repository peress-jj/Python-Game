import random

print(" ______________________________________________________________________")
print("|                          Jogo da advinhação                          |")
print(" ______________________________________________________________________")

print("\nEscolha sua dificuldade: (insira apenas números)")
dificuldade = int(input("\n1-Muito fácil\n2-Fácil\n3-Médio\n4-Difícil\n5-Muito difícil\n\n"))
if dificuldade == 1: #Muito fácil
  numero_secreto = random.randint(1, 10)
  print("\nVocê escolheu a dificuldade Muito fácil, escolha um número de 1 a 10")
elif dificuldade == 2: #Fácil
  numero_secreto = random.randint(1, 15)
  print("\nVocê escolheu a dificuldade fácil ,escolha um número de 1 a 15")
elif dificuldade == 3: #Médio
  numero_secreto = random.randint(1, 20)
  print("\nVocê escolheu a dificuldade média, escolha um número de 1 a 20")
elif dificuldade == 4: #Difícil
  numero_secreto = random.randint(1, 25)
  print("\nVocê escolheu a dificuldade difícil, escolha um número de 1 a 25")
elif dificuldade == 5: #Muito difícil
  numero_secreto = random.randint(1, 30)
  print("\nVocê escolheu a dificuldade muito difícil escolha um número de 1 a 30")
else:
   print("\nVocê não escolheu nenhuma dificuldade, portanto irá jogar na dificuldade média.")
   numero_secreto = random.randint(1, 20)
   
escolha_tentativas = int(input("Quantas tentativas você deseja???\n\n"))
tentativas_maximas = escolha_tentativas
tentativas = 1

while tentativas <= tentativas_maximas:
  print("Você está na tentativa", tentativas, "de", tentativas_maximas)
  numero_usuario = int(input("\nDigite o número secreto:"))
  
  if numero_secreto == numero_usuario:
    print("\nBOA!!! Você acertou!")
    break
  elif tentativas >= tentativas_maximas:
    print("Você excedeu suas tentativas.")
  elif numero_secreto > numero_usuario:
    print("\nUm pouco mais")
  elif numero_secreto < numero_usuario:
    print("\nUm pouco menos")
  else:
    print("\nBOA!!! Você acertou!")

  
  # Tentativas = tentativas + 1
  tentativas += 1

if tentativas > tentativas_maximas:
  print("voce perdeu!!!")
else:
  print("\nVocê ganhou!")
  
