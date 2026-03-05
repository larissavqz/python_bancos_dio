# Desafio: Número que mais cresce
# Leia uma lista de números inteiros e descubra:
# 👉 Qual número teve o maior aumento de frequência ao longo da leitura.
# 📌 Regra:
# Você deve percorrer a lista na ordem original.
# Cada vez que um número aparecer, sua contagem aumenta.
# Você deve imprimir o número que primeiro atingir a maior contagem já vista até aquele momento.
# 🔎 Exemplo
# Entrada
# 1 2 1 3 2 1 2 2
# 🧠 Passo a passo da ideia:
# 1 → aparece 1 vez (maior até agora)
# 2 → aparece 1 vez (empata, mas 1 continua na frente)
# 1 → aparece 2 vezes (novo maior)
# 3 → aparece 1 vez
# 2 → aparece 2 vezes (empata com 1, mas 1 chegou primeiro)
# 1 → aparece 3 vezes (novo maior)
# 2 → aparece 3 vezes (empata, mas 1 chegou primeiro)
# 2 → aparece 4 vezes (novo maior)
# ✅ Saída
# 2
# Porque foi o primeiro número a atingir a maior contagem final (4).
# 🔥 O desafio aqui é:
# Você não pode simplesmente:
# contar tudo
# depois pegar o maior
# Você precisa atualizar a resposta durante a leitura.

def numero_que_mais_cresce(numeros):
    contagem = {}
    maior_frequencia = 0
    numero_mais_crescente = None

    for numero in numeros:
        if numero not in contagem:
            contagem[numero] = 0
        contagem[numero] += 1

        if contagem[numero] > maior_frequencia:
            maior_frequencia = contagem[numero]
            numero_mais_crescente = numero

    return numero_mais_crescente

def numero_que_mais_aparece_primeiro(numeros):
    contagem = {}
    maior_frequencia = 0
    numero_mais_frequente = None

    for numero in numeros:
        if numero not in contagem:
            contagem[numero] = 0
        contagem[numero] += 1

    for numero in numeros:
        if contagem[numero] > maior_frequencia:
            maior_frequencia = contagem[numero]
            numero_mais_frequente = numero

    return numero_mais_frequente

def numero_que_mais_aparece_ultimo(numeros):
    contagem = {}
    maior_frequencia = 0
    numero_mais_frequente = None

    for numero in numeros:
        if numero in contagem:
            contagem[numero] += 1
        else:
            contagem[numero] = 1

    for numero in numeros:
        if contagem[numero] >= maior_frequencia:
            maior_frequencia = contagem[numero]
            numero_mais_frequente = numero
    
    return maior_frequencia, numero_mais_frequente

# Exemplo de uso
entrada = input().split()
resultado = numero_que_mais_cresce(entrada)
print(resultado)  # Saída: 2    

resultado = numero_que_mais_aparece_primeiro(entrada)
print(resultado)  # Saída: 1

resultado = numero_que_mais_aparece_ultimo(entrada)
print(f"Maior frequencia: {resultado[0]} Número mais frequente que aparece por último: {resultado[1]}")