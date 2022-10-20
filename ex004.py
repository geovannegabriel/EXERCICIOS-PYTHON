#DISSECANDO UMA VARIAVEL

pergunta = input('Digite algo: ')

print("O tipo primitivo é: ", type(pergunta))

print("Só tem espaços? ", pergunta.isspace())

print("É um numero? ", pergunta.isnumeric())

print(("É alfabetico? ", pergunta.isalpha()))

print("É alfanumerico? ", pergunta.isalnum())

print("Está em maiusculo? ", pergunta.isupper())

print("está minuscula? ", pergunta.islower())

print("Esta capitalizada? ", pergunta.istitle())




