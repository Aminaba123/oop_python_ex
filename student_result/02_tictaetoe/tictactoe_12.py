import random

def showBoard(board): #�۾��� �������� ���
    print('=' * 80)
    print("""
      %c |  %c  | %c
    --- | --- | ---
      %c |  %c  | %c
    --- | --- | ---
      %c |  %c  | %c
    """ % (board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8], board[9]))
    print('=' * 80)

def inputPlayerLetter(): #����ڰ� O,X�� ���ϴ� ���� ����
    letter = ''
    while True:
        print('Choose X or O')
        letter = input().upper()
        if (letter == 'X' or letter == 'O'):
            break
        print('Only X or O!')

    if letter == 'X':
        return['X','O']
    else:
        return ['O','X']

def whoGoFirst(): #������ �������� ����
    if random.randint(0,1) == 0:
        return 'com'
    else:
        return 'player'

def playAgain(): #�ٽ� ���� ����� �Լ�
    print('You want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move): #�����ǿ� move��ġ�� ���� ���´�
    print(move, type(move))
    board[move] = letter

def copyBoard(board): #ȭ�鿡 �������� �� �۾��� �� ���� ����
    otherBoard = []

    for i in board:
        otherBoard.append(i)

    return otherBoard

def isWinner(b, l): #b���忡�� l ���� �̰���� Ȯ��
    return ((b[7] == l and b[8] == l and b[9] == l)or
    (b[4] == l and b[5] == l and b[6] == l)or
    (b[1] == l and b[2] == l and b[3] == l) or
    (b[7] == l and b[4] == l and b[1] == l) or
    (b[8] == l and b[5] == l and b[2] == l) or
    (b[9] == l and b[6] == l and b[3] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def isSpaceEmpty(board, move): #���� ���� ������ ����ִ��� Ȯ��
    return board[move]==' '

def isBoardFull(board): #�������� ��á���� Ȯ��
    for i in range(1, 10):
        if isSpaceEmpty(board, i):
            return False
    return True

def getPlayerMove(board): #����ڰ� ���°��� �Է¹޾� ��ȯ
    move=''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceEmpty(board, int(move)): #���ϴ� ���� ����־����
        print('Where do you want to put? input a number in 1~9')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, moveList): #�̵������� ����Ʈ���� ��ġ�� �������� ����
    possibleMoves = []
    for i in moveList:
        if isSpaceEmpty(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) !=0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter): #�����ǰ� ��ǻ���� ���� �Ѱ��ְ� ��ǻ�Ͱ� ���� ��ġ�� ��ȯ
    if computerLetter == 'X':
        playerLetter ='O'
    else:
        playerLetter = 'X'

    #ƽ���� AI�� �˰���
    #1. ���� ���� �̱�� �ִٸ� ����ġ�� ����
    for i in range(1, 10):
        copy = copyBoard(board)
        if isSpaceEmpty(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                print(i)
                return i

    #2. ����ڰ� �̱�� �ִ��� Ȯ���ϰ� �����
    for i in range(1,10):
        copy = copyBoard(board)
        if isSpaceEmpty(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                print(i)
                return i

    #3. 1,3,7,9 �ڳ��� �ϳ��� ���� ������
    move = chooseRandomMoveFromList(board, [1,3,7,9])
    if move != None :
        return move

    #4. ����� ����ִٸ� ������
    if isSpaceEmpty(board, 5):
        return 5

    #5. �� ���� �ϳ��� ������
    move = chooseRandomMoveFromList(board,[2,4,6,8])
    if move != None :
        return move
#���� ����
print('Tic Tac Toe!')

while True: #�ݺ����� ����
    gameBoard = [' ']*10 #������ �ʱ�ȭ
    playerLetter, computerLetter = inputPlayerLetter() #����ڿ� ��ǻ�� ������
    turn = whoGoFirst() #����
    print('The ' + turn + ' will go first.')
    isPlaying = True

    while isPlaying:
        if turn =='player':
            #����� ����
            showBoard(gameBoard)
            move = getPlayerMove(gameBoard)
            makeMove(gameBoard,playerLetter,move)

            if isWinner(gameBoard, playerLetter):
                showBoard(gameBoard)
                print('You win the game!!!!!')
                isPlaying = False
            else:
                if isBoardFull(gameBoard):
                    print(gameBoard)
                    showBoard(gameBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'com'

        else:
            #��ǻ�� ����
            move = getComputerMove(gameBoard,computerLetter)
            makeMove(gameBoard, computerLetter, move)

            if isWinner(gameBoard,computerLetter):
                showBoard(gameBoard)
                print('You lose...')
                isPlaying = False
            else:
                if isBoardFull(gameBoard):
                    print(gameBoard)
                    showBoard(gameBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break