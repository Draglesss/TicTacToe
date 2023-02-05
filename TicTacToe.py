import os
import time
def clearConsole() :
    command = 'clear'
    if os.name in ('nt', 'dos') :
        command = 'cls'
    os.system(command)
    
class board :
    def __init__(self) :
        self.board = ['', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    def print_board(self) :
        clearConsole()
        print('---------------')
        print(self.board[7], ' | ', self.board[8], ' | ', self.board[9])
        print('---------------')
        print(self.board[4], ' | ', self.board[5], ' | ', self.board[6])
        print('---------------')
        print(self.board[1], ' | ', self.board[2], ' | ', self.board[3])
        print('---------------')

    def isfull(self) :
        for i in range(1, 10) :
            if self.board[i] == 'X' or self.board[i] == 'O' :
                continue
            else :
                return False
        return True

    def check_win(self) :
        if self.board[1] == self.board[2] == self.board[3] :
            return True, self.board[1]
        elif self.board[4] == self.board[5] == self.board[6] :
            return True, self.board[4]
        elif self.board[7] == self.board[8] == self.board[9] :
            return True, self.board[7]
        elif self.board[1] == self.board[4] == self.board[7] :
            return True, self.board[1]
        elif self.board[2] == self.board[5] == self.board[8] :
            return True, self.board[2]
        elif self.board[3] == self.board[6] == self.board[9] :
            return True, self.board[3]
        elif self.board[1] == self.board[5] == self.board[9] :
            return True, self.board[1]
        elif self.board[3] == self.board[5] == self.board[7] :
            return True, self.board[3]
        else :
            return False, False

    def check_tie(self) :
        return self.isfull()
           
    def new_board(self) :
        self.board = ['', '1', '2', '3', '4', '5', '6', '7', '8', '9']
my_board = board()
my_board.print_board()

def run(board) :
    turn = 'X'
    while not board.isfull() :
        cancel = False
        try :
            inp = int(input('Enter the position: '))
        except ValueError :
            print('Invalid input')
            time.sleep(2)
            board.print_board()
            continue
        finally :
            pass
        if inp in range(1,10) :
            if board.board[inp].isdigit() == True :
                board.board[inp] = turn
                board.print_board()
            else :
                print('Position already taken')
                time.sleep(2)
                board.print_board()
                cancel = True
            if turn == 'X' and cancel == False :
                turn = 'O'
            elif turn == 'O' and cancel == False:
                turn = 'X'
        else :
            print('Invalid input')
            time.sleep(2)
            board.print_board()
        if board.check_win()[0] :
            print(board.check_win()[1], ' wins')
            break
    if board.check_tie() and board.check_win()[0] == False :
        print('Tie')
replay = True
run(my_board)
while replay :
    choice = input('Do you want to play again? (y/n) ')
    if choice == 'y' or choice == 'yes' :
        clearConsole()
        my_board.new_board()
        my_board.print_board()
        run(my_board)
    elif choice == 'n' or choice == 'no' :
        clearConsole()
        print('Thank you for playing !!')
        break
    else :
        print('Invalid input')
        time.sleep(2)
        clearConsole()
        my_board.print_board()
