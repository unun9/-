board = list(range(1, 10))

wins = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def qwe():
    print("-------------")
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], '|', board[2 + i * 3], "|")
    print("-------------")

global value
def take_input(fg='X'):

    while True:
       value = input("Куда поставить - " + fg+' ?')
       if not (value in '123456789'):
            print("Ошибичный ввод.Повтарите.")
            continue

       value = int(value)
       if str(board[value - 1]) in "xo":
            print("Эта клетка занята ")
            continue
       board[value - 1] = fg
       break

def bot():
    numbers=[]
    for i in board:
        if board[str(i)]=='X':
            print(i)
            numbers.append(str(i))
def win():
    for er in wins:
        if (board[er[0] - 1]) == (board[er[1] - 1]) == (board[er[2] - 1]):
            return board[er[1] - 1]
    else:
        return False


def main():
    co = 0
    while True:
        qwe()
        if co>4:
            None







main()