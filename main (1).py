n = str(input('Informe seu nome ')).strip()
sem_branco = len(n) - n.count(' ')

print(f'Seu nome tem ao todo {sem_branco} letras')
first = n.split()

print(f'Seu nome tem {len(first[0])} letras')
letra = str(input('Qual letra quer ve quantas vezes aparece '))

print(f'A letra {letra.upper()} aparece {n.count(letra)} vezes')
print(f'Seu nome em maiusculo fica assim: {n.upper()}')
print(f'Seu nome em minuscula fica assim: {n.lower()}')