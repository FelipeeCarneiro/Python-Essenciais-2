def achar_proximo_vazio(peça):
    # encontrar a proxima linha, col no jogo que não esteja preenchida --> rep com -1
    # retornar tuple linha, col (ou (None, None) se não tiver preenchido)

    # lembrar que usa-se 0-8 pros índices
    for l in range(9):
        for c in range(9):                  # range(9) é 0, 1, 2, .. 8
            if peça[l][c] == -1:
                return l, c
    return None, None                       # se sem espaços vazios (-1)

def é_valido(peça, chute, linha, col):
    # imaginar que o chute na linha/col do puzzle é um chute válido
    # retornar True se sim, False caso contrário

    #Começando com a linha:
    linha_valores = peça[linha]
    if chute in linha_valores:
        return False

    # agora com colunas
    # col_valores = []
    # for i in range(9):
    #     col_valores.append(peça[i][col])
    col_valores = [peça[i][col] for i in range(9)]
    if chute in col_valores:
        return False

    # e então o quadrado
    # esse é o macete, mas precisa começao com quadrado 3x3
    # e interagir sobre os 3 valores da linha/coluna
    linha_inicio    = (linha // 3) * 3     # 1 // 3 = 0,   5 // 3 = 1, ...
    col_inicio      = (col   // 3) * 3

    for l in range(linha_inicio, linha_inicio + 3):
        for c in range(col_inicio, col_inicio + 3):
            if peça[l][c] == chute:
                return False

    # o grande fim é: se chegar até aqui, deixa passar
    return True

def solucionar_sudoku(peça):
    # resolver sudoku com backtraking (rastreamento por regresão)!
    # nosso quebra-cabeça é uma lista de lista, onde cada lista é uma linha do sudoku.
    # retornar se existe uma solulção
    # alterar o jogo pra solução (se ela existir)

    # passo 1: escolher em algum lugar no jogo pra dar um chute
    linha, col = achar_proximo_vazio(peça)

    # passo 1.1: se não sobrar nada, então termina porque só é permitido inputs válidos
    if linha is None:
        return True

    # passo 2: se tiver lugar pra por um número, então damos um chute entre 1 e 9
    for chute in range(1, 10):              # range(1, 10) é 1, 2, 3, .. 9
        # passo 3: checar se é um chute válido
        if é_valido(peça, chute, linha, col):
            # passo 3.1: se é valido, então coloque o chute no jogo!
            peça[linha][col] = chute
            # agora recurse (reconsidere) usando o jogo!
            # passo 4: reconsiderar chamar a função
            if solucionar_sudoku(peça):
                return True
        # passo 5: e se não validar OU se o chute não resolver o jogo, então precisa
        # rastrear por regresão e tentar o novo número
        peça[linha][col] = -1 # dar um resetar no chute

    # passo 6: se nenhuma dos números chutados funcionarem, então esse jogo é não pode ser resolvido!
    return False

if __name__ == '__main__':
    tabuleiro_exemplo_1 = [
        [2,9,5,7,4,3,8,6,1],
        [4,3,1,8,6,5,9,2,7],
        [8,7,6,1,9,2,5,4,3],
        [3,8,7,4,5,9,2,1,6],
        [6,1,2,3,8,7,4,9,5],
        [5,4,9,2,1,6,7,3,8],
        [7,6,3,5,2,4,1,8,9],
        [9,2,8,6,7,1,3,5,4],
        [1,5,4,9,3,8,6,7,2]
    ]
    tabuleiro_exemplo_2 = [
        [1,9,5,7,4,3,8,6,2],
        [4,3,1,8,6,5,9,2,7],
        [8,7,6,1,9,2,5,4,3],
        [3,8,7,4,5,9,2,1,6],
        [6,1,2,3,8,7,4,9,5],
        [5,4,9,2,1,6,7,3,8],
        [7,6,3,5,2,4,1,8,9],
        [9,2,8,6,7,1,3,5,4],
        [2,5,4,9,3,8,6,7,1],
    ]
print(solucionar_sudoku(tabuleiro_exemplo_1))
print(tabuleiro_exemplo_1)
print(solucionar_sudoku(tabuleiro_exemplo_2))
print(tabuleiro_exemplo_2)

# ESSA BOSTA DE CÓDIGO NÃO FUNCIONA!!!!!