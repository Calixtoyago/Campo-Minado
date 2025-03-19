import random

def criarCampoMinado(bombas, linhas, colunas):
    if bombas >= linhas * colunas:
        print("Quantidade de bombas invalida para linhas e colunas selecionadas")
        return 0

    campo = []
    for _ in range(linhas):
        campo.append([0]*colunas)

    bombas_marcadas = 0
    while bombas_marcadas != bombas:
        linha_random = random.randint(0, linhas-1)
        coluna_random = random.randint(0, colunas-1)

        if campo[linha_random][coluna_random] == 0:
            campo[linha_random][coluna_random] = 9
            bombas_marcadas += 1

    i = 0
    j = 0
    for i in range(linhas):
        for j in range(colunas):
            if campo[i][j] >= 9:
                try:
                    if i == 0 and j == 0:
                        campo[i][j+1] += 1
                        campo[i+1][j] += 1
                        campo[i+1][j+1] += 1
                    elif i == linhas - 1 and j == 0:
                        campo[i-1][j] += 1
                        campo[i-1][j+1] += 1
                        campo[i][j+1] += 1
                    elif i == 0 and j == colunas - 1:
                        campo[i][j-1] += 1
                        campo[i+1][j-1] += 1
                        campo[i+1][j] += 1
                    elif i == linhas - 1 and j == colunas -1:
                        campo[i-1][j-1] += 1
                        campo[i-1][j] += 1
                        campo[i][j-1] += 1
                    elif i == 0:
                        campo[i][j-1] += 1
                        campo[i][j+1] += 1
                        campo[i+1][j-1] += 1
                        campo[i+1][j] += 1
                        campo[i+1][j+1] += 1
                    elif i == linhas - 1:
                        campo[i-1][j-1] += 1
                        campo[i-1][j] += 1
                        campo[i-1][j+1] += 1
                        campo[i][j-1] += 1
                        campo[i][j+1] += 1
                    elif j == 0:
                        campo[i-1][j] += 1
                        campo[i-1][j+1] += 1
                        campo[i][j+1] += 1
                        campo[i+1][j] += 1
                        campo[i+1][j+1] += 1
                    elif j == colunas - 1:
                        campo[i-1][j-1] += 1
                        campo[i-1][j] += 1
                        campo[i][j-1] += 1
                        campo[i+1][j-1] += 1
                        campo[i+1][j] += 1
                    else:
                        campo[i-1][j-1] += 1
                        campo[i-1][j] += 1
                        campo[i-1][j+1] += 1
                        campo[i][j-1] += 1
                        campo[i][j+1] += 1
                        campo[i+1][j-1] += 1
                        campo[i+1][j] += 1
                        campo[i+1][j+1] += 1
                except IndexError:
                    ...
                except TypeError:
                    ...
            j += 1
        i += 1

    for i in range(linhas):
        for j in range(colunas):
            if campo[i][j] >= 9:
                campo[i][j] = "B"

    return campo

def prepararCampo(campo):
    campo_temporario = []

    for linha in campo:
        campo_temporario.append(linha.copy())

    for i in range(len(campo_temporario)):
        for j in range(len(campo_temporario[i])):
            campo_temporario[i][j] = "+"
    
    return campo_temporario

def mostrarJogo(campo, campo_temporario):
    print('   ', end=' ')
    for i in range(len(campo[0])):
        print(i, end=' ')
    print("\n  ", end= ' ')
    print("-"*18)

    posicao_linha = 0
    for linha in campo_temporario:
        print(posicao_linha, end= ' ')
        print("|", end = ' ')
        posicao_linha += 1
        for elemento in linha:
            print(elemento, end=" ")
        print()

def jogar(campo, campo_temporario):
    while True:
        try:
            mostrarJogo(campo, campo_temporario)

            print()
            x = int(input("x: "))
            y = int(input("y: ")) 
            print()

            if campo_temporario[x][y] != "+":
                print("Posicao ja escolhida")
            elif campo[x][y] == 0:
                mostrarZeros(campo, campo_temporario, x, y)
            else:
                campo_temporario[x][y] = campo[x][y]

            if campo_temporario[x][y] == "B":
                print("Voce perdeu")
                mostrarJogo(campo, campo_temporario)
                break
        except IndexError:
            pass


def mostrarZeros(campo, campo_temporario, x, y):

    if x < 0 or y < 0 or x >= len(campo) or y >= len(campo[0]):
        return
    
    if campo_temporario[x][y] != "+":
        return 
    
    campo_temporario[x][y] = campo[x][y]

    if campo[x][y] == 0:

            mostrarZeros(campo, campo_temporario, x-1, y-1) 
            mostrarZeros(campo, campo_temporario, x-1, y) 
            mostrarZeros(campo, campo_temporario, x-1, y+1) 
            mostrarZeros(campo, campo_temporario, x, y-1) 
            mostrarZeros(campo, campo_temporario, x, y+1) 
            mostrarZeros(campo, campo_temporario, x+1, y-1) 
            mostrarZeros(campo, campo_temporario, x+1, y) 
            mostrarZeros(campo, campo_temporario, x+1, y+1)     
