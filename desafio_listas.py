def numero_inteiro(lista):
    return list(map(int, lista))

def elementos_comuns(set1, set2):
    return list(set1.intersection(set2))

# Leitura das listas
lista1 = input().split()
lista2 = input().split()

# Verifica se todas os elementos das listas podem ser convertidos para inteiros
if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    lista1 = numero_inteiro(lista1)
    lista2 = numero_inteiro(lista2)
    comuns = elementos_comuns(set(lista1), set(lista2))
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")