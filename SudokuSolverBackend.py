
from SudokuSolverUI import SudokuSolver
from SudokuProblems import PROBLEMS
import copy

class SudokuSolverClass(SudokuSolver):
    def __init__(self):
            super().__init__()
            self.solveBoardButton.configure(command=self.onSolveClicked)
            for number in range(1, 51):
                button = getattr(self, f"libraryCardUploadButton{number:02d}") #js gets the buttons, again the buttons that I mentioned to LJ for clikcing to get problem
                button.configure(command=lambda n=number: self.GenerateBoard(n)) #generates the board to the screen
            
            self.resetBoardButton.configure(command=self.onResetClicked)
            self.clearBoardButton.configure(command=self.onClearClicked)
    def setStatus(self, title, detailed, type): #fixes the statust
                color = "#e6edf3" #defailt
                    
                if type == 1: #informative
                    color = "#288efa"
                elif type == 2: #success!
                    color = "#20d63e"
                elif type == 3: #ERROR
                    color = "#fa4e4e"
                self.statusLabel.configure(text=title, fg_color=color)
                self.statusDetailedLabel.configure(text=detailed)

    def onSolveClicked(self): #ts for my reference
        board = self.readBoard() #this gives us a full board to work with
        solution = copy.deepcopy(board) #solved copy, we use it to get answer for square
        check = self.Backtrack(solution) 
        if check == True:
            for row in range(9): 
                        for col in range(9):
                            if board[row][col] == 0: #ts js changes 0 to include answer
                                square = getattr(self, f"boardCellR{row}C{col}")
                                square.delete(0, "end")
                                square.insert(0, str(solution[row][col]))
                                square.configure(text_color="#3d9bff")
        else: #no solutoion
            self.setStatus("STATUS: The board cannot be solved.", "Please check your answer & try again.", 3)

    
        
    def readBoard(self): #this reads the board
            board = []
            for row in range(9): #in range 9, because theres 9 rows, so we start working with whats in the rows
                rowList = []
                for col in range(9): #in range 9, as theres 9 columns, so per row, whats in each column?
                    name = f"boardCellR{row}C{col}" #this calls the widget (with format of boardCellR(Row)C(Column)) box, allowing us to view whats in it
                    widget = getattr(self, name) #this allows us to get the value of said widget
                    value = widget.get() #same here, gets the value
                    if value.isdigit(): #if its a digit, it will append to our current list we're making
                        rowList.append(int(value)) 
                    else:
                        rowList.append(0) #if nothings in it, it defaults to zero
                board.append(rowList) #this just appends the current row

            """ Please note this is for UI backend purposes, pls ignore (dis for u LJ)
            Example of what it does, essentially gives us the board @ hand:
            
            [5, 0, 0, 0, 0, 0, 0, 0, 0]
            [0, 0, 5, 0, 0, 0, 0, 0, 3]
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
            [0, 0, 0, 0, 5, 0, 0, 3, 0]
            [4, 0, 0, 0, 0, 0, 0, 0, 0]
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
            [0, 0, 0, 0, 0, 0, 0, 2, 0]
            """
            return board



    def GenerateBoard(self, index): #generate UI of board based on the current puzzle when clicked on a puzzle button
        #Output to the UI board the current board (self.board)
        self.currentIndex = index
        self.board = copy.deepcopy(PROBLEMS[index - 1]) #this allows us to copy the current puzzle into the board, so we can work with it without changing the original puzzle

        for row in range(9):
            for col in range(9):
                name = f"boardCellR{row}C{col}" #this calls the widget (with format of boardCellR(Row)C(Column)) box, allowing us to view whats in it
                widget = getattr(self, name) #this allows us to get the value of said widget
                widget.delete(0, "end") #this clears the current value in the widget
                if self.board[row][col] != 0: #if the current square is not empty, it will insert the value into the widget
                    widget.insert(0, str(self.board[row][col]))

        #button to relate to the puzzle
        
        
        

    def LocationValidator(self, board, row, col, num):
        #note that board allows us to traverse, so think of editting via 2d array

        #check if valid in row
        for c in range(9): 
            if c == col:
                continue #skip if its our square

            if board[row][c] == num: #checks if a number is already in the row, if it is, it returns false
                return False
                  
        #check if valid in column
        for r in range(9):
            if r == row:
                continue #skip if its our square
            if board[r][col] == num: #checks if a number is already in the column, if it is, it returns false
                return False
                  
        #check if valid in 3x3 square
        currentRow = (row//3) * 3 #row // 3 gives row divided by 3 without remainder, then multiplies 3 gives starting row of the 3x3 square
        currentCol = (col//3) * 3 #column // 3 gives column divided by 3 without remainder, then multiplies 3 gives starting row of the 3x3 square
        for r in range(currentRow, currentRow+3): #add +3 to the current row and column to get the end of the 3x3 square
            for c in range(currentCol, currentCol+3): 
                if r == row and c == col:
                    continue #skip if its our square

                if board[r][c] == num: #checks if a number is already in the 3x3 square generated, if it is, it returns false
                    return False

        return True #otherwise, it returns true, meaning the number is valid in that location

    def CurrentSquare(self, board): 
        #this one changes the current square that is being worked on so returns row and col of empty square, or none if traversal is done
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0: #if square is empty, it returns the row and col of that square
                    return (row, col)
        return None #if none then traversal is done

        

    def Backtrack(self,board):
        #this easily just combines location validator and current square 
        
        square = self.CurrentSquare(board) #this gets the current square to work on, again returns the row AND column
        if square is None: #if none, then the board is solved
            return True
        row, col = square #otherwise, it gets the row and col of the current square

        for num in range(1, 10): #this loops through the numbers 1-9 to see if they are valid in the current square
            if self.LocationValidator(board, row, col, num): #if the number is valid in the current square
                board[row][col] = num #this is so the next call sees it, when the next cals locationValidator looks @ row/column/box the num is placed in
                if self.Backtrack(board): #redoes shit recursively so js solves the entire board
                    return True #if it can be solved, it returns true
                board[row][col] = 0 #essentially undoes it if its not valid so it tries next number, the most IMPORTANT part 

        return False #this returns false if it ccannot be solved
    
    """ are you catching my drift? - AZ
    
    CurrentSquare - finds next empty square so it can work on that
    LocattionValidator - checks if number is valid in that square in three parameters (row, column, 3x3)

    backtrack - connects everything together, recursively solves the board by checking if a number is valid in the current square, and if it is, it places it there and calls itself again to check the next square. If it cannot be solved, it backtracks and tries the next number.
    
    """

    

    
    
            
    def ProblemClicked(self):
        #this is the function that is called when a puzzle button is clicked, it will generate the board based on the puzzle number
        button = self.focus_get() #this gets the button that was clicked
        if button is not None: #if a button was clicked
            index = int(button.cget("text")) #this gets the text of the button, which is the puzzle number
            self.GenerateBoard(index) #this generates the board based on the puzzle number


    def onResetClicked(self): #if reset is clicked, then it js resets back to the problem set from earlier
        if self.currentIndex is not None:
            self.GenerateBoard(self.currentIndex)

    def onClearClicked(self): #clear js removes everything, basic shit
        for row in range(9):
            for col in range(9):
                square = getattr(self, f"boardCellR{row}C{col}")
                square.delete(0, "end")



    #ZIP BOMB!! THINK FAST CHUCKLENUTS

    """
    TODO pls work on this later
    - add customhandler (ts too hard)
    - create a new function to change the text of for example if theres a conflict or the backtrack algorithm didn't work
    - I think set status is good
    - include light and dark mode
    - crash bug (if you click on a puzzle and then click on another puzzle, it will crash the program, this is because the currentIndex is not updated when a new puzzle is generated, so when the reset button is clicked, it will try to generate the old puzzle again, which will cause an error because the old puzzle is not in the PROBLEMS list anymore)
    - zip bomb (for legal reasons thats a joke)
    """



