def contar_caracteres(string):
  #TODO: Inicialize um dicionário vazio 'contador' para armazenar as contagens de caracteres.:
  contador = {}

  for char in string:
    if char in contador:
      contador[char] += 1
    else:
      contador[char] = 1
    
  return contador

# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)