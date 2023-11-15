board = [[0, 0, 0, 1],
         [0, 1, 0, 0],
         [1, 0, 1, 0],
         [1, 0, 0, 0]]

caselle = [
    [0b0000, 0b0001, 0b0010, 0b0011],
    [0b0100, 0b0101, 0b0110, 0b0111],
    [0b1000, 0b1001, 0b1010, 0b1011],
    [0b1100, 0b1101, 0b1110, 0b1111]
]

heads = 1
tails = 0

key = 0b0010

def player1(board, caselle, key):
    caselleConTesta = []
    risulatoXOR = 0 

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == heads:
                caselleConTesta.append(caselle[i][j])
                risulatoXOR ^= caselle[i][j]

    print("[+] Le caselle con testa sono:", caselleConTesta)
    print("[+] Il risultato dello XOR tra le caselle con testa è:", format(risulatoXOR, '04b'))  

    xor_minus_key = risulatoXOR ^ key
    print("[+] Il giocatore 1 deve girare la moneta a casella:", format(xor_minus_key, '04b'))

    
    newBoard = [row[:] for row in board]

    
    row = (xor_minus_key) // 4
    col = (xor_minus_key) % 4
    newBoard[row][col] = 1 if newBoard[row][col] == tails else tails  # Corrected line
#Cambia lo stato della casella

    return newBoard, risulatoXOR  

def player2(newBoard):
    caselleConTesta = []
    risulatoXOR = 0  

    for i in range(len(newBoard)):
        for j in range(len(newBoard[i])):
            if newBoard[i][j] == heads:
                caselleConTesta.append(caselle[i][j])
                risulatoXOR ^= caselle[i][j]  # Use XOR result of newBoard

    return caselleConTesta, risulatoXOR

while True:
    n = int(input("Scrivi 0 se vuoi conoscere le soluzioni per questa casistica: "))
    if n == 0:
        new_board, risultatoPlayer2 = player1(board, caselle, key)  # Call player1 to update the board
        risultatoPlayer2 = player2(new_board)  # Call player2 on the updated board
        print("[+] LA CHIAVE SI TROVA NELLA CASELLA:", format(risultatoPlayer2[1], '04b'))
        break
    else:
        break
