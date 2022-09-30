X = 0
Y = 0
Z = 0
N = 0
stop = False
while stop == False :
    print("Candidato X => 889")
    print("Candidato Y => 847")
    print("Candidato Z => 515")
    print("Nulo/Branco => 0")
    try:
     voto = int(input("Qual seu voto"))
     
     def eleicao(voto) :
      if voto ==889: resu = 1
      elif voto ==847: resu = 2
      elif voto ==515: resu = 3 
      else : resu = 0 
      return resu
      
     apu = eleicao(voto) 
     if apu == 1:
      X = X + 1
     if apu == 2:
      Y = Y + 1
     if apu == 3:
      Z = Z + 1
     if apu == 0:
      N = N + 1
      
      stop1 = False
      while stop1 == False :
        confirma = str (input("deseja encerrar a votação? S/N"))
       if (confirma == "S"): stop = True
           stop1 = True
       if (confirma == "N"):
           stop = False
           stop1 = True
      else : print ("responda denovo por favor")
          
    except :
        print("nao compreendi")
print ("voce encerrou a votaçao")
if(X>Y) and (X>Z) : print("O eleito é o X")
if(X<Y) and (Y>Z) : print("O eleito é o Y")
if(X<Z) and (Y<Z) : print("O eleito é o Z")
else : print("empate")
print ("o candidato X teve:",X)  
print ("o candidato Y teve:",Y)  
print ("o candidato Z teve:",Z)  
print ("Teve ", N," votos em branco")  