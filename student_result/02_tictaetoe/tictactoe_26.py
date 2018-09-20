map = [[' ']*4 for i in range(4)] # ���� �÷��̿� �� ����
User = ' '
Com = ' '
play = 1
full = 0
WhoseTurn = 0


def Reset(): # ���� ���� �� �缳��
    global User
    global Com
    global play
    global full
    global WhoseTurn
    print("\n\n\nSTART NEW TIATACTOE GAME") #���� ���� �˸�
    map = [[' ']*4 for i in range(4)]# �� �ʱ�ȭ
    User = 'X'
    Com = 'O' # ����� ��Ŀ ����. �⺻���� �÷��̾ X ��Ŀ
    full = 0 # ���� ��ô�� ����. ���� �� �������� �¸����� ����
    WhoseTurn = 1 # ���� ������ �Ǻ�. �⺻���� �÷��̾� ����. 2�� ���� �������� �Ǻ���

def isOK(x, y): # ���Ƶ� �Ǵ��� Ȯ��
    if x<0 or x>2 or y<0 or y>2: # ���� �ڸ����� �̻��ϸ� 0 ��ȯ
        return 0
    elif map[x][y] !=' ': # �̹� ä���� �ڸ��� 0 ��ȯ
        return 0
    else: # ���������� 1 ��ȯ
        return 1

#���� ����Լ�
def mapper(x, y, v): # ��ġ����, ���� �� ����
    global map
    map[x][y] = v
    global full
    full = full + 1 # ä���� ĭ�� �� ���� - ���� ����� �ľ�
        
    # ��ȭ�� �� ���
    print("[%c|%c|%c]" %(map[0][0], map[0][1], map[0][2]))
    print("[%c|%c|%c]" %(map[1][0], map[1][1], map[1][2]))
    print("[%c|%c|%c]" %(map[2][0], map[2][1], map[2][2]))


def SelectMarker(): # ��Ŀ ���� �Լ�
    global User
    global Com
    global WhoseTurn
    print("Please Select Your Mark. First Attack is X. (X or O)")
    while 1:
        Select = input().upper()  # �÷��̾��� ��Ŀ ����
        if (Select != 'X') and (Select != 'O'):  # �߸��� �Է� ����
            print("Please Select Again. ex) 'X' 'O' 'x' 'o'")
        else:
            if Select == 'X': #������� �Է¿� ���� ���� ��ȯ�մϴ�.
                User = 'X'
                WhoseTurn = 1 # X�� �����̹Ƿ� �÷��̾� �������� ����
                Com = 'O'
            else:
                User = 'O'
                WhoseTurn = 0 # O�� �İ��̹Ƿ� �÷��̾� �İ����� ����
                Com = 'X'
        return



# �÷��̾� ���ʿ� ����Ǵ� �Լ�
def user_turn():
    print("Your Turn")
    while 1:
        print("Where do you input? ex) '1 3' '2 2'")
        position = (input().split()) # ���������� ���� ������ �Է¹���
        x = int(position[0])-1 # �������� ���������� �ٲ�
        y = int(position[1])-1

        # �߸��� �Է� ����
        if isOK(x,y) == 0:
            print("Please Write Again. ex) '1 3' '2 2'")
        else:
            mapper(x, y, User) # ��ġ���� ��Ŀ�� ����Լ��� ����
            return # ���� �ѱ��

# ��ǻ�� ���ʿ� ����Ǵ� �Լ�
def computer_turn():
    doX = -1 # ��ǻ�Ͱ� ���ƾ� �� ��
    doY = -1
    print("Computer Turn")

    # �ϼ� �������� ��üŽ��
    for i in range(0, 3):
        if (map[i][0] == map[i][1] == Com) and (isOK(i, 2)):
            doX = i
            doY = 2
            break
        elif (map[i][0] == map[i][2] == Com) and (isOK(i, 1)):
            doX = i
            doY = 1
            break
        elif (map[i][1] == map[i][2] == Com) and (isOK(i, 0)):
            doX = i
            doY = 0
            break
        elif (map[0][i] == map[1][i] == Com) and (isOK(2, i)):
            doX = 2
            doY = i
            break
        elif (map[0][i] == map[2][i] == Com) and (isOK(1, i)):
            doX = 1
            doY = i
            break
        elif (map[1][i] == map[2][i] == Com) and (isOK(0, i)):
            doX = 0
            doY = i
            break
    if (map[0][0] == map[1][1] == Com) and (isOK(2, 2)):
        doX = 2
        doY = 2
    elif (map[0][0] == map[2][2] == Com) and (isOK(1, 1)):
        doX = 1
        doY = 1
    elif (map[1][1] == map[2][2] == Com) and (isOK(0, 0)):
        doX = 0
        doY = 0
    elif (map[2][0] == map[1][1] == Com) and (isOK(0, 2)):
        doX = 0
        doY = 2
    elif (map[2][0] == map[0][2] == Com) and (isOK(1, 1)):
        doX = 1
        doY = 1
    elif (map[1][1] == map[0][2] == Com) and (isOK(2, 0)):
        doX = 2
        doY = 0
    if doX != -1:  # ���� ���� ������ ���� �ִٸ�
        mapper(doX, doY, Com) # ���� ��
        return # �� �ѱ�


    else:# ������ ���� ���ٸ�
        for i in range(0, 3):# ���� �� ã��
            if (map[i][0] == map[i][1] == User) and (isOK(i, 2)):
                doX = i
                doY = 2
                break
            elif (map[i][0] == map[i][2] == User) and (isOK(i, 1)):
                doX = i
                doY = 1
                break
            elif (map[i][1] == map[i][2] == User) and (isOK(i, 0)):
                doX = i
                doY = 0
                break
            elif (map[0][i] == map[1][i] == User) and (isOK(2, i)):
                doX = 2
                doY = i
                break
            elif (map[0][i] == map[2][i] == User) and (isOK(1, i)):
                doX = 1
                doY = i
                break
            elif (map[1][i] == map[2][i] == User) and (isOK(0, i)):
                doX = 0
                doY = i
                break
        if (map[0][0] == map[1][1] == User) and (isOK(2, 2)):
            doX = 2
            doY = 2
        elif (map[0][0] == map[2][2] == User) and (isOK(1, 1)):
            doX = 1
            doY = 1
        elif (map[1][1] == map[2][2] == User) and (isOK(0, 0)):
            doX = 0
            doY = 0
        elif (map[2][0] == map[1][1] == User) and (isOK(0, 2)):
            doX = 0
            doY = 2
        elif (map[2][0] == map[0][2] == User) and (isOK(1, 1)):
            doX = 1
            doY = 1
        elif (map[1][1] == map[0][2] == User) and (isOK(2, 0)):
            doX = 2
            doY = 0

        if (doX != -1): # ���� ���ƾ� �� ���� �ִٸ�
            mapper(doX, doY, Com) # ���� ��
            return # ���� �ѱ�


    # ���������� �˸°� ��,��,�߾� ������ ������ ��ġ�� Ž��
    while 1:
        if (isOK(0, 0)):
            doX = 0
            doY = 0
        elif (isOK(0, 2)):
            doX = 0
            doY = 2
        elif (isOK(2, 0)):
            doX = 2
            doY = 0
        elif (isOK(2, 2)):
            doX = 2
            doY = 2
        elif (isOK(1, 0)):
            doX = 1
            doY = 0
        elif (isOK(0, 1)):
            doX = 0
            doY = 1
        elif (isOK(2, 1)):
            doX = 2
            doY = 1
        elif (isOK(1, 2)):
            doX = 1
            doY = 2
        elif (isOK(1, 1)):
            doX = 1
            doY = 1
        mapper(doX, doY, Com) # ���� ��
        return # ���� �ѱ�

# �ٽ� �÷��� ���� ���� �Լ� - play ���� ���� ������ ������ �Լ���
def PlayAgain():
    while 1: # �߸��� �Է� ����
        print("Play Again? Y or N")
        r = input().upper()
        if r == 'Y':
            play = 1 # �÷��� ���� ����
            return
        elif r == 'N':
            play = 0 # �÷��� ���� ����
            return
        else:
            print("Please Input Again. ex) 'Y' 'y' 'N' 'n'")


def win(): # �¸��� ��Ŀ�� ��ȯ
    if (map[0][0] == map[0][1]) and (map[0][1] == map[0][2]):
        return map[0][0]
    elif (map[1][0] == map[1][1]) and (map[1][1] == map[1][2]):
        return map[1][0]
    elif (map[2][0] == map[2][1]) and (map[2][1] == map[2][2]):
        return map[2][0]
    elif (map[0][0] == map[1][0]) and (map[1][0] == map[2][0]):
        return map[0][0]
    elif (map[0][1] == map[1][1]) and (map[1][1] == map[2][1]):
        return map[0][1]
    elif (map[0][2] == map[1][2]) and (map[1][2] == map[2][2]):
        return map[0][2]
    elif (map[0][0] == map[1][1]) and (map[1][1] == map[2][2]):
        return map[0][0]
    elif (map[0][2] == map[1][1]) and (map[1][1] == map[2][0]):
        return map[0][2]

    elif full<9:
        return 'N'
    else:
        return 'D'

#���� ���� �Լ�
def Ender():
    if win() == User: # �÷��̾ �¸���
            print("You Win !!!")
    elif win() == Com: # ��ǻ�� �¸���
            print("You Lose ...")
    elif win() == 'D':
        print("DRAW")
    return


while play == 1: # �÷����ϴ� ����
    Reset() # ������ �����ϱ� ���� ����
    SelectMarker() # ��Ŀ ����
    while full<9: # ���� �� �������� ���� ����
        if WhoseTurn % 2 == 1:
            user_turn()
            WhoseTurn+=1
        else:
            computer_turn()
            WhoseTurn+=1
        if win() == 'X' or win() == 'O' or win() == 'D':
            break
    Ender() # ���� ������ ��� ���
    PlayAgain() # �ٽ� �ϰڳİ� �����