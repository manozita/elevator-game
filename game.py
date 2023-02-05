import random
import time
  
andares = [-2 -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
elevador1 = random.choice(andares)
elevador2 = random.choice(andares)
x=1

lista_p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_a = []
while x <= 30:
  lista_a.append(x)
  x+=1
lista_s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
perdeu = 0
morreu_1 = 0
morreu = 0
continuar = 0
el1_quebrado = 0
el2_quebrado = 0
money = 10

print ("Bem-vindo ao jogo do elevador.")

nome = input("Seu nome: ")
  
time.sleep(0.5)

while continuar != 'N':

  print('Seu dinheiro:', money, 'reais.')

  time.sleep(1)

  if el1_quebrado == 1:
    if money >= 50:
      print('Você tem dinheiro o suficiente para consertar o elevador quebrado!')
      consertar = input('Deseja consertá-lo? ')
  
      while consertar != 'S' and consertar != 'N':
        print('Responda com S ou N.')
        consertar = input('Deseja consertá-lo? ')

      if consertar == 'S':

        print('Você deu 50 reais para o zelador, que consertou o elevador 1.')
        money = money - 50
        el1_quebrado = 0

        time.sleep(3)
        
        print('Você agora tem', money, 'reais de lucro.')

  elif el2_quebrado == 1:
    if money >= 50:
      print('Você tem dinheiro o suficiente para consertar o elevador quebrado!')
      consertar = input('Deseja consertá-lo? ')
  
      while consertar != 'S' and consertar != 'N':
        print('Responda com S ou N.')
        consertar = input('Deseja consertá-lo? ')

      if consertar == 'S':

        print('Você deu 50 reais para o zelador, que consertou o elevador 2.')
        money = money - 50
        el2_quebrado = 0

        time.sleep(3)
        
        print('Você agora tem', money, 'reais de lucro.')

  print(nome + (", você está em um prédio de 20 andares."))

  time.sleep(1)
  
  p1 = int(input("Em qual andar você está? "))
  
  while p1 > 20 or p1 < -2:
  
    print("Lembrando: você está em um prédio de 20 andares!")
  
    time.sleep(0.5)
  
    p1 = int(input(nome + ", em qual andar você está? "))
  
  p2 = int(input("Para qual andar você quer ir? "))

  while p2 > 20 or p2 < -2 or p1 == p2:

    if p2 > 20 or p2 < -2:
      print("Lembrando: você está em um prédio de 20 andares!")

      time.sleep(0.5)
      
    elif p1 == p2:
      print("Sua mãe, frustrada com seu comportamento infantil, te deu umas palmadas, e retirou da sua conta 5 reais.")

      money = money - 5

    p2 = int(input("Para qual andar você quer ir? "))
  
  dif1 = int(abs(p1 - elevador1))
  dif2 = int(abs(p1 - elevador2))
  
  time.sleep(0.5)
  
  print('Calculando...')
  
  time.sleep(1.5)

  porcentagem = random.choice(lista_p)

  anao = random.choice(lista_a)

  nota = random.choice(lista_s)

  if anao == 22:

    if el1_quebrado == 1:

      print('O elevador 1 está quebrado, devido a recentes acidentes.')
  
      time.sleep(1)
      
      if elevador2 < 0:
        print("O elevador 2 está no subsolo", abs(elevador2))
      elif elevador2 > 0:
        print("O elevador 2 está no andar", elevador2)
      elif elevador2 == 0:
        print("O elevador 2 está no térreo.")
  
      print("ATENÇÃO: você encontrou um ANÃO DOURADO no hall de entrada. Vocês entraram no elevador 2.")
  
      pergunta_anao = input("O anão tem dificuldades em alcançar o PRIMEIRO andar. Deseja ajudá-lo? ")
    
      while pergunta_anao != 'S' and pergunta_anao != 'N':
          
        print('Responda com S ou N.')
    
        pergunta_anao = input("O anão tem dificuldades em alcançar o PRIMEIRO andar. Deseja ajudá-lo? ")
  
      if pergunta_anao == "S":
  
        print('O anão se estende para te dar um aperto de mão, mas não consegue.')
  
      else:
      
        print('O anão morde sua canela por não ter ajudado.')
  
      time.sleep(2)
    
      if porcentagem == 7:
          
        print('Após entrarem no elevador 2, ele caiu.')
    
        time.sleep(2)
          
        print('Você morreu, junto com o ANÃO DOURADO.')

        perdeu = 1
  
        el2_quebrado = 1
  
      else:
  
        if pergunta_anao == "S":
  
          if p2 == 1:
            print('Após entrarem no elevador 2, antes de descerem no andar 1, o anão, agradecido pela ajuda, lhe dá uma nota de 50 reais. Você desce no andar, muito contente.')
  
          elif p2 < 0:
            print('Após entrarem no elevador 2, o anão, antes de descer no andar 1, agradecido pela ajuda, lhe dá uma nota de 50 reais. Você desce no subsolo', abs(p2), 'muito contente.')
          elif p2 > 1:
            print('Após entrarem no elevador 2, o anão, antes de descer no andar 1, agradecido pela ajuda, lhe dá uma nota de 50 reais. Você desce, muito contente, no andar', p2)

          elif p2 == 0:
            print('Após entrarem no elevador 2, o anão, antes de descer no andar 1, agradecido pela ajuda, lhe dá uma nota de 50 reais. Você desce no térreo, muito contente.')
  
          money = money + 50
  
        else:
  
          if p2 == 1:
            print('Por mais que você não tenha ajudado o anão, ele desceu junto com você no andar 1, te deu um soco no saco e roubou 5 reais.')
            money = money - 5
          elif p2 < 0:
            print("Após entrarem no elevador 2, você desceu no subsolo", int(abs(p2)), "e deixou o anão dourado sozinho e enfurecido.")
          elif p2 > 1:
            print("Após entrarem no elevador 2, você desceu no andar", p2, "e deixou o anão dourado sozinho e enfurecido.")
          elif p2 == 0:
            print("Após entrarem no elevador 2, você desceu no térreo e deixou o anão dourado sozinho e enfurecido.")
          
        elevador2 = p2

    elif el2_quebrado == 1:
  
      if elevador1 < 0:
        print("O elevador 1 está no subsolo", abs(elevador1))
      elif elevador1 > 0:
        print("O elevador 1 está no andar", elevador1)
      elif elevador1 == 0:
        print("O elevador 1 está no térreo.")
  
      time.sleep(1)
  
      print('O elevador 2 está quebrado, devido a recentes acidentes.')
  
      print("ATENÇÃO: você encontrou um ANÃO DOURADO no hall de entrada. Vocês entraram no elevador 1.")
  
      pergunta_anao = input("O anão tem dificuldades em alcançar o PRIMEIRO andar. Deseja ajudá-lo? ")
    
      while pergunta_anao != 'S' and pergunta_anao != 'N':
          
        print('Responda com S ou N.')
    
        pergunta_anao = input("O anão tem dificuldades em alcançar o PRIMEIRO andar. Deseja ajudá-lo? ")
  
      if pergunta_anao == "S":
  
        print('O anão se estende para te dar um aperto de mão, mas não consegue.')
  
      else:
      
        print('O anão morde sua canela por não ter ajudado.')
  
      time.sleep(2)
    
      if porcentagem == 7:
          
        print('Após entrarem no elevador 1, ele caiu.')
    
        time.sleep(2)
          
        print('Você morreu, junto com o ANÃO DOURADO.')

        perdeu = 1
        
        el2_quebrado = 1
  
      else:
  
        if pergunta_anao == "S":
  
          if p2 == 1:
            print('Após entrarem no elevador 1, antes de descerem no andar 1, o anão, agradecido pela ajuda, lhe dá uma nota de 50 reais. Você desce no andar, muito contente.')
  
          elif p2 < 0:

            print('Após entrarem no elevador 1, o anão, antes de descer no andar 1, agradecido pela ajuda, lhe dá uma nota de 50 reais. Você desce no subsolo', abs(p2), 'muito contente.')
            
          elif p2 > 1:
            print('Após entrarem no elevador 1, o anão, antes de descer no andar 1, agradecido pela ajuda, lhe dá uma nota de 50 reais. Você desce no andar', p2, 'muito contente.')
          elif p2 == 0:
            print('Após entrarem no elevador 1, o anão, antes de descer no andar 1, agradecido pela ajuda, lhe dá uma nota de 50 reais. Você desce no térreo, muito contente.')
  
          money = money + 50
  
        else:
  
          if p2 == 1:
            print('Por mais que você não tenha ajudado o anão, ele desceu junto com você no andar 1, te deu um soco no saco e roubou 5 reais.')
            money = money - 5
          elif p2 < 0:
            print("Após entrarem no elevador 1, você desceu no subsolo", int(abs(p2)), "e deixou o anão dourado sozinho e enfurecido.")
          elif p2 > 1:
            print("Após entrarem no elevador 1, você desceu no andar", p2, "e deixou o anão dourado sozinho e enfurecido.")
          elif p2 == 0:
            print("Após entrarem no elevador 1, você desceu no térreo e deixou o anão dourado sozinho e enfurecido.")
          
        elevador1 = p2

    else:
      
      if elevador1 < 0:
        print("O elevador 1 está no subsolo", abs(elevador1))
      elif elevador1 > 0:
        print("O elevador 1 está no andar", elevador1)
      elif elevador1 == 0:
        print("O elevador 1 está no térreo.")
      
      time.sleep(1)
      
      if elevador2 < 0:
        print("O elevador 2 está no subsolo", abs(elevador2))
      elif elevador2 > 0:
        print("O elevador 2 está no andar", elevador2)
      elif elevador2 == 0:
        print("O elevador 2 está no térreo.")

      time.sleep(1)

      if dif1 > dif2:
        print("ATENÇÃO: você encontrou um ANÃO DOURADO no hall de entrada. Vocês entraram no elevador 2.")

      else:
        print("ATENÇÃO: você encontrou um ANÃO DOURADO no hall de entrada. Vocês entraram no elevador 1.")
  
      pergunta_anao = input("O anão tem dificuldades em alcançar o PRIMEIRO andar. Deseja ajudá-lo? ")
    
      while pergunta_anao != 'S' and pergunta_anao != 'N':
          
        print('Responda com S ou N.')
    
        pergunta_anao = input("O anão tem dificuldades em alcançar o PRIMEIRO andar. Deseja ajudá-lo? ")
  
      if pergunta_anao == "S":
  
        print('O anão se estende para te dar um aperto de mão, mas não consegue.')
  
      else:
      
        print('O anão morde sua canela por não ter ajudado.')
  
      time.sleep(2)
    
      if porcentagem == 7:
        if dif1 > dif2:

          print('Após entrarem no elevador 2, ele caiu.')
    
          time.sleep(2)
          
          print('Você morreu, junto com o ANÃO DOURADO.')

          morreu_1 += 1
          morreu = 1
          
          el2_quebrado = 1
    
        else:
          
          print('Após entrarem no elevador 1, ele caiu.')
    
          time.sleep(2)
          
          print('Você morreu, junto com o ANÃO DOURADO.')

          morreu_1 += 1
          morreu = 1
  
          el1_quebrado = 1
    
      else:
        if dif1 > dif2:

          if pergunta_anao == "S":
  
            if p2 == 1:
              print('Após entrarem no elevador 2, antes de descerem no andar 1, o anão, agradecido pela ajuda, lhe dá uma nota de 50 reais. Você desce no andar, muito contente.')
    
            elif p2 < 0:
              print('Após entrarem no elevador 2, o anão, antes de descer no andar 1, agradecido pela ajuda, lhe dá uma nota de 50 reais. Você desce no subsolo', abs(p2), 'muito contente.')
            elif p2 > 1:
              print('Após entrarem no elevador 2, o anão, antes de descer no andar 1, agradecido pela ajuda, lhe dá uma nota de 50 reais. Você desce, muito contente, no andar', p2)
            elif p2 == 0:
              print('Após entrarem no elevador 2, o anão, antes de descer no andar 1, agradecido pela ajuda, lhe dá uma nota de 50 reais. Você desce no térreo, muito contente.')
    
            money = money + 50
    
          else:
    
            if p2 == 1:
              print('Por mais que você não tenha ajudado o anão, ele desceu junto com você no andar 1, te deu um soco no saco e roubou 5 reais.')
              money = money - 5
            elif p2 < 0:
              print("Após entrarem no elevador 2, você desceu no subsolo", int(abs(p2)), "e deixou o anão dourado sozinho e enfurecido.")
            elif p2 > 1:
              print("Após entrarem no elevador 2, você desceu no andar", p2, "e deixou o anão dourado sozinho e enfurecido.")
            elif p2 == 0:
              print("Após entrarem no elevador 2, você desceu no térreo e deixou o anão dourado sozinho e enfurecido.")
            
          elevador2 = p2
        
        else:
          if pergunta_anao == "S":
  
            if p2 == 1:
              print('Após entrarem no elevador 1, antes de descerem no andar 1, o anão, agradecido pela ajuda, lhe dá uma nota de 50 reais. Você desce no andar, muito contente.')
    
            elif p2 < 0:
              print('Após entrarem no elevador 1, o anão, antes de descer no andar 1, agradecido pela ajuda, lhe dá uma nota de 50 reais. Você desce no subsolo', abs(p2), 'muito contente.')
            elif p2 > 1:
              print('Após entrarem no elevador 1, o anão, antes de descer no andar 1, agradecido pela ajuda, lhe dá uma nota de 50 reais. Você desce, muito contente, no andar', p2)
            elif p2 == 0:
              print('Após entrarem no elevador 1, o anão, antes de descer no andar 1, agradecido pela ajuda, lhe dá uma nota de 50 reais. Você desce no térreo, muito contente.')
    
            money = money + 50
    
          else:
    
            if p2 == 1:
              print('Por mais que você não tenha ajudado o anão, ele desceu junto com você no andar 1, te deu um soco no saco e roubou 5 reais.')
              money = money - 5
            elif p2 < 0:
              print("Após entrarem no elevador 1, você desceu no subsolo", int(abs(p2)), "e deixou o anão dourado sozinho e enfurecido.")
            elif p2 > 1:
              print("Após entrarem no elevador 1, você desceu no andar", p2, "e deixou o anão dourado sozinho e enfurecido.")
            elif p2 == 0:
              print("Após entrarem no elevador 1, você desceu no térreo e deixou o anão dourado sozinho e enfurecido.")
            
          elevador1 = p2

  else:

    if el1_quebrado == 1:
  
      print('O elevador 1 está quebrado, devido a recentes acidentes.')
  
      time.sleep(1)
      
      if elevador2 < 0:
        print("O elevador 2 está no subsolo", abs(elevador2))
      elif elevador2 > 0:
        print("O elevador 2 está no andar", elevador2)
      elif elevador2 == 0:
        print("O elevador 2 está no térreo.")
    
      if porcentagem == 7:
    
        time.sleep(1)
          
        print('O elevador 2 te buscou e caiu.')
    
        time.sleep(2)
          
        print('Você morreu.')
  
        el2_quebrado = 1

        perdeu = 1
  
      else:
        time.sleep(1)
        
        if p2 < 0:
          print("O elevador 2 te buscou e te levou até o subsolo", abs(p2))
        elif p2 > 0:
          print("O elevador 2 te buscou e te levou até o andar", p2)
        elif p2 == 0:
          print("O elevador 2 te buscou e te levou até o térreo.")

        if nota == 10:
          print("No caminho, você encontrou uma nota de 10 reais no chão. Que sonho!")
          money = money + 10
        
        elevador2 = p2
  
    elif el2_quebrado == 1:
  
      if elevador1 < 0:
        print("O elevador 1 está no subsolo", abs(elevador1))
      elif elevador1 > 0:
        print("O elevador 1 está no andar", elevador1)
      elif elevador1 == 0:
        print("O elevador 1 está no térreo.")
  
      time.sleep(1)
  
      print('O elevador 2 está quebrado, devido a recentes acidentes.')
  
      time.sleep(1)
    
      if porcentagem == 7:
    
        time.sleep(1)
          
        print('O elevador 1 te buscou e caiu.')
    
        time.sleep(2)
          
        print('Você morreu.')
  
        el1_quebrado = 1

        perdeu = 1
  
      else:
        time.sleep(1)
        
        if p2 < 0:
          print("O elevador 1 te buscou e te levou até o subsolo", abs(p2))
        elif p2 > 0:
          print("O elevador 1 te buscou e te levou até o andar", p2)
        elif p2 == 0:
          print("O elevador 1 te buscou e te levou até o térreo.")

        if nota == 10:
          print("No caminho, você encontrou uma nota de 10 reais no chão. Que sonho!")
          money = money + 10
        
        elevador1 = p2
      
    else:
      
      if elevador1 < 0:
        print("O elevador 1 está no subsolo", abs(elevador1))
      elif elevador1 > 0:
        print("O elevador 1 está no andar", elevador1)
      elif elevador1 == 0:
        print("O elevador 1 está no térreo.")
      
      time.sleep(1)
      
      if elevador2 < 0:
        print("O elevador 2 está no subsolo", abs(elevador2))
      elif elevador2 > 0:
        print("O elevador 2 está no andar", elevador2)
      elif elevador2 == 0:
        print("O elevador 2 está no térreo.")
    
      if porcentagem == 7:
        if dif1 > dif2:
    
          time.sleep(1)
          
          print('O elevador 2 te buscou e caiu.')
    
          time.sleep(2)
          
          print('Você morreu.')

          morreu_1 += 1
          morreu = 1
  
          el2_quebrado = 1
    
        else:
    
          time.sleep(1)
          
          print('O elevador 1 te buscou e caiu.')
    
          time.sleep(2)
          
          print('Você morreu.')
  
          el1_quebrado = 1

          morreu_1 += 1
          morreu = 1
    
      else:
        if dif1 > dif2:
            
          time.sleep(1)
        
          if p2 < 0:
            print("O elevador 2 te buscou e te levou até o subsolo", abs(p2))
          elif p2 > 0:
            print("O elevador 2 te buscou e te levou até o andar", p2)
          elif p2 == 0:
            print("O elevador 2 te buscou e te levou até o térreo.")

          if nota == 10:
            print("No caminho, você encontrou uma nota de 10 reais no chão. Que sonho!")
            money = money + 10
        
          elevador2 = p2
        
        else:
          time.sleep(1)
        
          if p2 < 0:
            print("O elevador 1 te buscou e te levou até o subsolo", abs(p2))
          elif p2 > 0:
            print("O elevador 1 te buscou e te levou até o andar", p2)
          elif p2 == 0:
            print("O elevador 1 te buscou e te levou até o térreo.")

          if nota == 10:
            print("No caminho, você encontrou uma nota de 10 reais no chão. Que sonho!")
            money = money + 10
        
          elevador1 = p2

  if money < 0:
    time.sleep(1)
    print('Você ficou com a conta negativa e foi expulso pelo síndico do prédio.')
    continuar = 'N'
  elif perdeu == 1:
    time.sleep(1)
    print('Você quebrou os dois elevadores e foi expulso pelo síndico do prédio.')
    continuar = 'N'
  elif morreu_1 == 1:
    time.sleep(3)
    morreu_1 += 1
    morreu = 0
    nome1 = nome
    nome = input('Escolha um nome para seu sucessor: ')
    print(nome + ', seu antecessor,', nome1 + ', lhe deixou todas as suas heranças!')
    print('Mas, também o prejuízo de um elevador quebrado.')
    print('O custo para conserto é de 50 reais.')
    time.sleep(2)
    print('Consiga dinheiro o suficiente para consertá-lo, antes de quebrar o outro, para não perder o jooj!')
    print('Obs: se ficar com a conta negativa, você também perde.')
    time.sleep(2)

    continuar = input('Deseja continuar? ')
  
    while continuar != 'S' and continuar != 'N':
      print ("Responda com S ou N.")
      continuar = input('Deseja continuar? ')

  elif morreu == 1:
    time.sleep(3)
    morreu_1 += 1
    morreu = 0
    nome1 = nome
    nome = input('Escolha um nome para seu sucessor: ')
    print(nome + ', seu antecessor,', nome1 + ', lhe deixou todas as suas heranças!')

    time.sleep(2)
    
    continuar = input('Deseja continuar? ')
  
    while continuar != 'S' and continuar != 'N':
      print ("Responda com S ou N.")
      continuar = input('Deseja continuar? ')

  else:
    continuar = input('Deseja continuar? ')
  
    while continuar != 'S' and continuar != 'N':
      print ("Responda com S ou N.")
      continuar = input('Deseja continuar? ')

  print('')
  print('')
  print('')

time.sleep(2)
print ('Fim de jogo.')