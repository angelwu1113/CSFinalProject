import random
import time

def inarow_Neast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading east and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start > H - 1:
        return False            # Out-of-bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False            # O.o.b. column
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start][c_start+i] != ch: # A mismatch!
            return False
    return True                 # All offsets succeeded, so we return True

def inarow_Nsouth(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading south and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start] != ch: # A mismatch!
            return False
    return True                 # All offsets succeeded, so we return True

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading northeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start - (N-1) < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start-i][c_start+i] != ch: # A mismatch!
            return False
    return True                 # All offsets succeeded, so we return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading southeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False            # Out-of-bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False            # O.o.b. column
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start+i] != ch: # A mismatch!
            return False
    return True                 # All offsets succeeded, so we return True

class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """



    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # The string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-' + "\n"   # Bottom of the board

        # Add code here to put the numbers underneath
        for col in range (0, self.width):
            s += ' ' + str(col)

        return s       # The board is complete; return it
    
    def gravity_storeData(self):
        '''
        We create a new list that only stores the non-empty list row by row
        '''
        new_row = [[] for row in range(self.height)]
        for row in range(self.height):
            for col in range(self.width):
                if self.data[row][col] != ' ':
                    new_row[row].append(self.data[row][col])
        # print(new_row)

        #[[' ']*width for row in range(height)]
        return new_row
    '''
    def gravity_backleft(self):
        
        shifting all the piece to the left
        
        
        list = self.gravity_storeData() #storing the data
        self.clear() #clear the board
        result = list[::-1]
        # result = [row[::-1] for row in list[::-1]] #reverse the list
        col = 0
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.addMove(col, result[i][j])
                col = col + 1
                if j + 1 == len(result[i]):
                    col = 0
        print(self)
    '''
    
    def gravity_backToRight(self):
        list = self.gravity_storeData()
        new_board= [[' ']*self.width for row in range(self.height)]
        for i in range(len(list)):
            pieces = list[i]
            a = len(pieces)
            start_col = self.width - a
            for j in range(a):
                new_board[i][start_col + j] = pieces[j]
        self.data = new_board
        return self
    
    def gravity_backToLeft(self):
        list = self.gravity_storeData()
        new_board= [[' ']*self.width for row in range(self.height)]
        for i in range(len(list)):
            pieces = list[i]
            a = len(pieces)
            for j in range(a):
                new_board[i][0+j] = pieces[j]
        self.data = new_board
        return self

    def addMove(self, col, ox):
        '''
        the first, col, represents the index of the column to which the checker will be added. The second argument, ox, will be a 1-character string representing the checker to add to the board. That is, ox should either be 'X' or 'O' (again, capital O, not zero).
        '''
        for row in range (self.height):
            if self.data[self.height - row - 1][col] == ' ':
                self.data[self.height - row - 1][col] = ox
                break

    def clear(self):
        '''
        should clear the board that calls it.
        '''
        for row in range (self.height):
            for col in range(self.width):
                self.data[row][col] = ' '
    
    def setBoard(self, moveString):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.setBoard('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.setBoard('000000') to
           see them alternate in the left column.

           moveString must be a string of one-digit integers.
        """
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'

    def allowsMove(self, c):
        '''
        This method should return True if the calling object (of type Board) does allow a move into column c. It returns False if column c is not a legal column number for the calling object. It also returns False if column c is full. Thus, this method should check to be sure that c is within the range from 0 to the last column and make sure that there is still room left in the column!
        '''
        if c < 0 or c > self.width -1:
            return False
        elif self.data[0][c] != ' ':
            return False
        else:
            return True

    def isFull(self):
        '''
        This method should return True if the calling object (of type Board) is completely full of checkers. It should return False otherwise. Notice that you can leverage allowsMove to make this method very concise! Unless you're supernaturally patient, you'll want to test this on small boards:
        '''
        for c in range(self.width):
            if self.allowsMove(c) == True:
                return False
        return True
    
    def delMove(self, c):
        '''
        This method should do the opposite of addMove. It should remove the top checker from the column c. If the column is empty, then delMove should do nothing. This function may not seem useful now, but it will become very useful when you try to implement your own Connect Four player... .
        '''
        for row in range (self.height):
            if self.data[row][c] != ' ':
                self.data[row][c] = ' '
                break
    
    def winsFor(self, ox):
        '''
        This method's argument ox is a 1-character checker: either 'X' or 'O'. It should return True if there are four checkers of type ox in a row on the board. It should return False otherwise. Important Note: you need to check whether the player has won horizontally, vertically, or diagonally (and there are two different directions for a diagonal win).
        '''
        H = self.height
        W = self.width
        D = self.data

        # Check to see if ox wins, starting from any checker:
        for row in range(H):
            for col in range(W):
                if inarow_Neast(ox, row, col, D, 4) == True:
                    return True
                # you need three more, very similar, such checks
                # for the three other directions!
                if inarow_Nsouth(ox, row, col, D, 4) == True:
                    return True 
                if inarow_Nsoutheast(ox, row, col, D, 4) == True:
                    return True 
                if inarow_Nnortheast(ox, row, col, D, 4) == True:
                    return True 

        # but, if it looks at EACH row and col and never finds a win...
        return False     # only gets here if it never returned True, above
    
    def hostGame(self):
        '''
        This method brings everything together into the familiar game. It should host a game of Connect Four, using the methods listed above to do so. In particular, it should alternate turns between 'X' (who will always go first) and 'O' (who will always go second). It should ask the user (with the input function) to select a column number for each move
        '''
        currentplayer = 'X'
        print("Welcome to Connect Four!")
        while True:
            print(self)
            user_column = int(input(currentplayer + "'s choice:"))
 
            while self.allowsMove(user_column) == False:

                # intentionally not valid, the first time...
                user_string = input("Choose a column: ")
                try:
                    user_column = int(user_string)
                except ValueError:       # in case an integer wasn't typed...
                    user_column = -1
            self.addMove(user_column, currentplayer)
            print("player's move:")
            print(self)


            if self.winsFor(currentplayer) == True:
                print(self)
                print("Congratulations! You", currentplayer, "wins! Awesome!!! Thanks for playing.")
                break
            
            self.addMove(self.aiMove('O'), 'O')
            print("ai's move:")
            print(self)

            if self.winsFor('O') == True:
                print(self)
                print("Uh oh. O wins. You lost. Thanks for playing.")
                break

            if self.isFull() == True:
                print(self)
                print("The game draws! Thanks for playing. :D")
                break

            gravity = random.choice(range(0, 100))
            if gravity % 2 == 0:
                self.gravity_backToLeft()
                print("Gravity is going to the left!")
            else:
                self.gravity_backToRight()
                print("Gravity is going to the right!")

    
    def colsToWin(self, ox):
        '''
        colsToWin method should return the list of columns where ox can move in the next turn in order to win and finish the game. The columns should be in numeric order (if there are more than one). Also, colsToWin should not look ahead more than one turn. 
        '''
        win = []
        for i in range(self.width):
            if self.allowsMove(i):
                self.addMove(i, ox)
                if self.winsFor(ox):
                    win.append(i)
                self.delMove(i)
        return win

    def aiMove(self, ox):
        winningMoves = self.colsToWin(ox)
        if winningMoves != []:
            return winningMoves[0]
        '''
        elif winningMoves == []:
            return random.choice(range(0, 7))
        '''
        
        if ox == "X":
            opponent = "O"
        else:
            opponent = "X"
        opponent_winningMoves = self.colsToWin(opponent)
        if opponent_winningMoves != []:
            return opponent_winningMoves[0]
        while True:
            i = random.choice(range(0, 7))
            print ("AI's move:", i)
            if self.allowsMove(i) == True:
                return i
            
        '''
        for i in range(self.width):

            if self.allowsMove(i) == True:
                return i
        '''
    
    def aivsaiMove(self, ox):
        winningMoves = self.colsToWin(ox)
        if winningMoves != []:
            return winningMoves[0]
        '''
        elif winningMoves == []:
            return random.choice(range(0, 7))
        '''
        
        if ox == "X":
            opponent = "O"
        else:
            opponent = "X"
        opponent_winningMoves = self.colsToWin(opponent)

        if opponent_winningMoves != []:
            return opponent_winningMoves[0]
        '''
        midrow = self.height // 2
        for i in range(midrow+1):
            if self.allowsMove(midrow+i) == True:
                return midrow+i
            elif self.allowsMove(midrow-i) == True:
                return midrow-i
        '''
        midrow = self.height // 2 + random.choice(range(-2, 3))

        if self.allowsMove(midrow) == True:
            return midrow

            
        while True:
            i = random.choice(range(0, 7))
            if self.allowsMove(i) == True:
                return i
            
    def aihostGame(self):
        '''
        This method brings everything together into the familiar game. It should host a game of Connect Four, using the methods listed above to do so. In particular, it should alternate turns between 'X' (who will always go first) and 'O' (who will always go second). It should ask the user (with the input function) to select a column number for each move
        '''
        turn = 0
        print("Welcome to Connect Four!")
        print(self)
        while True:
            print("turns:", turn)

            a = self.aivsaiMove('X')
            self.addMove(a, 'X')
            print("aiX's move:", a)
            print(self)
            time.sleep(1)

            if self.winsFor('X') == True:
                print(self)
                print("X wins! Thanks for playing.")
                break
            
            b = self.aivsaiMove('O')
            self.addMove(b, 'O')
            print("aiO's move:", b)
            print(self)
            time.sleep(1)

            if self.winsFor('O') == True:
                print(self)
                print("O wins! Thanks for playing.")
                break

            if self.isFull() == True:
                print(self)
                print("The game draws! Thanks for playing. :D")
                break

            gravity = random.choice(range(0, 100))
            if gravity % 2 == 0:
                self.gravity_backToLeft()
                print("Gravity is going to the left!")
            else:
                self.gravity_backToRight()
                print("Gravity is going to the right!")

            print(self)
            time.sleep(1)
            
            print("Loop paused. Press Enter to continue...")
            input()

            turn += 1

    
b = Board(7, 6)