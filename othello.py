"""
A Python module for the Othello game.
"""

# Used for copying a variable.
from copy import deepcopy

def newGame(player1,player2):
    """
        Initiliases a new game dictionary and then returns it, whos fields are set to initial values, and fields 
        "player1", "player2" are set according to the arguments given.
        
        @param 'player1': Non-empty string representing player 1's name or "C" for an ai player.
        @param 'player2': Non-empty string representing player 2's name or "C" for an ai player.
        @return: - Type: Dictionary
                 - Content: A dictionary containing the fields: "player1", "player2", "who" and "board",
                            where "player1", "player2" are set from arguments, and "who", "board" are 
                            preset intial values.
        @throws: - ValueError: If either argument for the player names is empty.
    """
    try:   
        # Check if arguments are empty.
        if len(str(player1)) == 0: raise ValueError(1)
        if len(str(player2)) == 0: raise ValueError(2)
        
        # Initlise the dictionary.
        game = {
                 "player1" : player1,
                 "player2" : player2,
                 "who" : 1,
                 "board" :  [
                             [0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0],
                             [0,0,0,2,1,0,0,0],
                             [0,0,0,1,2,0,0,0],
                             [0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0]
                             ]
                }
        # Return the initilisation.
        return game
    except ValueError as e:
        print("Player " + str(e.args[0]) + " name, should be non-empty.")

def alphaRange(start, stop, step = 1):
    """
        Basic generator function to cycle through the alphabet from and to a character.
        
        @param 'start': Begininning alphabetical character of sequence.
        @param 'stop': Last alphabetical character of sequence.
        @param 'step': How many characters to shift through each pass.
        @yield: - Type: String 
                - Content: String of the current character.
    """
    
    char = start    
    while True:
        yield char
        if char >= chr(ord(stop)-step): break
        char = chr(ord(char)+step)

def printBoard(board):
    """
        Prints a correctly formated "board" argument to console.
        
        @param 'board': A list of lists represting the Othello board in (row, column).
        @return: - Type: void
                 - Content: N/A
        @throws: - TypeError: If the argument is of wrong type (e.g: if the argument is a 
                                                                incorrectly formatted dictionary, or wrong type).
    """
    try:
        # Check argument is of correct type.
        if not isinstance(board, list): raise TypeError(type(board))
        for i in board:
            if not isinstance(i, list): raise TypeError(type(i))
        
        # Initlise some variables.
        horiSpace = 3
        maxHori = len(board[0])
        maxVert = len(board)+3
        printString = ""
        
        # Print the Table
        for j in range(maxVert):
            # First Line.
            if j == 0:
                printString += ("{:^"+str(horiSpace)+"}").format("") + "|"
                for i in alphaRange("a", chr(maxHori+97)):
                    printString += ("{:^"+str(horiSpace)+"}").format(i) + "|"
            # Second Line.
            elif j == 1: 
                printString += ("{:^"+str(horiSpace)+"}").format("") + "+"
                for i in range(maxHori):
                    printString += ("{:-^"+str(horiSpace)+"}").format("") + "+"
            # 3rd - 9th Line.
            elif j in range(2, 10):
                printString += ("{:^"+str(horiSpace)+"}").format(j-1) + "|"
                for i in range(maxHori):
                    if board[j-2][i] == 0:
                        printString += ("{:^"+str(horiSpace)+"}").format("") + "|"
                    elif board[j-2][i] == 1:
                        printString += ("{:^"+str(horiSpace)+"}").format("X") + "|"
                    elif board[j-2][i] == 2:
                        printString += ("{:^"+str(horiSpace)+"}").format("O") + "|"
            # Last Line.
            else:
                printString += ("{:^"+str(horiSpace)+"}").format("") + "+"
                for i in range(maxHori):
                    printString += ("{:-^"+str(horiSpace)+"}").format("") + "+"
            # Print the string that has been correctly formated, and then clear for next line. 
            print(printString)
            printString = ""
        
        # Return nothing as of now. @todo: Maybe return a bool for success?
        return
    except TypeError as e:
        print("Argument must be lists of a list, not: ", str(e.args[0]))

def strToIndex(s):
    """
        Converts a string coordinate into a tuple index coordinate for the "board" variable.
        
        @param 's': String of coordinate. E.g: "a1" or "3d"
        @return: - Type: Tuple
                 - Content: A tuple t, such that t[0] = row coordiate, t[1] = col coordinate.
        @throws: - TypeError: If the argument is of wrong type (e.g: not a string).
                 - ValueError: If the argument is not correctly formatted.
    """
    try:
        # Check parameter is a string.
        if not isinstance(s, str): raise TypeError(type(s))
        
        #Get rid of spaces in string.
        s = "".join(s.split(" "))
        
        #Initiliase some values.
        row = 0
        col = 0
        
        #Check size of string is exactly 2.
        if len(s) != 2: raise ValueError((s, 1))
        
        # Check first element of string.
        if s[0].isdigit():
            if int(s[0]) > 8: raise ValueError((s, 2))
            row = int(s[0])-1
        else:
            if not s[0].lower() in alphaRange("a", "i"): raise ValueError((s, 3))
            col = ord(s[0])-97
        # Check second element of string.
        if s[1].isdigit():
            if int(s[1]) > 8: raise ValueError((s, 2))
            row = int(s[1])-1
        else:
            if not s[1].lower() in alphaRange("a", "i"): raise ValueError((s, 3))
            col = ord(s[1])-97
            
        # Check both elements of the string, for 2 integers, or 2 characters.    
        if (s[0].isdigit() and s[1].isdigit()) or (s[0].isalpha() and s[1].isalpha()): raise ValueError((s, 4))
    
        return (row, col)
    except TypeError as e:
        print("Error: Argument must be a string, not: ", str(e.args[0]))
        return ""
    except ValueError as e:
        if e.args[0][1] == 1:
            print("Error: String '", e.args[0][0],"' must only have a size of 2.")
        elif e.args[0][1] == 2:
            print("Error: String '", e.args[0][0],"' cannot contain a number not in 1-8.")
        elif e.args[0][1] == 3:
            print("Error: String '", e.args[0][0],"' cannot contain a character not in a-h.")
        elif e.args[0][1] ==4:
            print("Error: String '", e.args[0][0],"' must be of the form Character-Number or Number-Character.")
        return ""

def isInt(n):
    """
        Returns true if n is a integer, otherwise returns false.
        
        @param 'n': Variable to be tested if it is a integer.
        @return: - Type: Boolean
                 - Content: True if argument is a integer.
                            False if argument is not a integer.
    """
    try:
        int(n)
        return True
    except ValueError:
        return False
    
def indexToStr(t):
    """
        Converts a tuple index to a 2 character string based on the position on the console board.
        
        @param 't': Tuple of (row, column).
        @return: - Type: String
                 - Content: 2 Character coordinate string of the front-end table.
    """
    try:
        if t[0] < 8 and t[1] < 8 and isInt(t[0]) and isInt(t[0]):
            return str(chr(t[1]+97)) + str(t[0]+1)
        else: raise ValueError
    except ValueError:
        print("Argument must have row and column index coordinate be an integer < 8.")

def loadGame():
    """
        Attempts to load the game from the "game.txt" file.
        If it succeeds, then returns a game dictionary of the current game.
        Note that the "game.txt" file must be in the same folder as the python file.
        
        @return: - Type: Dictionary
                 - Content: A dictionary containing the fields: "player1", "player2", "who" and "board",
                            where "player1", "player2", "who", "board" are set from the file "game.txt".
        @throws: - FileNotFoundError: If the file "game.txt" cannot be found in the same folder as the python file.
                 - ValueError: If the content of the "game.txt" file is in an incorrect format.
    """
    try:
        # Open file
        with open("game.txt", mode = "rt", encoding = "utf8") as f:
            # Pull first 2 lines under the assumption they are the names.
            player1 = "".join((f.readline()).split("\n"))
            player2 = "".join((f.readline()).split("\n"))
            
            # Test if there are indeed the names.
            if (isInt(player1) or isInt(player2)) and ((len(player1) == 1) or (len(player2) == 1)): raise ValueError
            
            # Create new game with the new player names.
            game = newGame(player1, player2)
            
            # Test for third line being "who".
            line = f.readline()
            if not(isInt(line) and int(line) in [1, 2]): raise ValueError 
            
            # Update dictionary with the "who" value.
            game["who"] = int(line)
            
            # Test and set the remaining lines to the dict.
            for indx, line in enumerate(f):
                line = "".join(line.split(","))
                line = "".join(line.split("\n"))
                if len(line) != 8: raise ValueError
                game["board"][indx] = [int(x) for x in line]
        
        return game
    
    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError:
        print("Error: Content format is not correct.")

def getLine(board,who,pos,dir):
    """
        Returns a list of all positions of the opponents pieces in a line, from a position, in a direction,
        untill your piece comes up.
        
        @param board: A list of lists represting the Othello board in (row, column).
        @param who: The current players value, i.e 1 or 2.
        @return: - Type: List of tuples.
                 - Content: List containing tuples which correspond to the index positions for a "board".
                            e.g: [(1,2), (1, 3)]
    """
    #Initlise parameters.
    cnt = 0
    posList = list() 
    
    # Keep looping till the end point of the line has been reached.
    while True:
        # Increase the counter.
        cnt += 1
        # Test to see if the position and direction list go out of the boards bounds, if so then return an empty list.
        if ( (pos[0]+(cnt*dir[0]) > 7) or 
             (pos[1]+(cnt*dir[1]) > 7) or 
             (pos[0]+(cnt*dir[0]) < 0) or 
             (pos[1]+(cnt*dir[1]) < 0) ):
            return []
        # Test to see if the next piece is an opponent piece, if so add to the posList.
        elif board[pos[0]+(cnt*dir[0])][pos[1]+(cnt*dir[1])] == [x for x in [1,2] if x != who][0]:
            posList.append((pos[0]+(cnt*dir[0]), pos[1]+(cnt*dir[1])))
        # Test to see if the next piece is your own piece, if so then a line has been formed, so return the posList.
        elif board[pos[0]+(cnt*dir[0])][pos[1]+(cnt*dir[1])] == [x for x in [1,2] if x == who][0]:
            return posList
        # If nothing is valid then just return an empty list.
        else:
            return []


def dir2DVect():
    """
        Simple yield function which yields the 8 possible tuple unit directions.
        
        @yield: - Type: tuple
                - Content: Unit direction corresponding to the possible directions for a othello board.
    """
    allDir = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
    for i in allDir:        
        yield i

def getValidMoves(board,who):
    """
        Returns a list of all valid moves the player "who" can make for a board "board".
        
        @param board: A list of lists represting the Othello board in (row, column).
        @param who: The current players value, i.e 1 or 2.
        @return: - Type: List of tuples
                 - Content: A list of tuple positions correspond to the (row, column) of the board which are valid moves to make.
    """
    
    # Empty list to add valid positions.
    validMoves = list()
    
    # Iterate through the rows
    for row, line in enumerate(board):
        # Iterate through the columns
        for col, num in enumerate(line):
            # Check if current position has no pieces on it.
            if num == 0:
                # Iterate through all possible direction vectors. @todo Maybe change for readability.
                for dir in dir2DVect():
                    # Check for a valid line in each direction for the current position.
                    if getLine(board, who, (row, col), dir) != []:
                        # Add to valid list if true.
                        validMoves.append((row, col))
                        # Once a line has been detected and added to list, dont need to cary on checking for other dirctions.
                        break
            else:
                # Go to next position.
                pass
    
    # Return the list of valid moves.
    return validMoves

def makeMove(board,move,who):
    """
        Makes a Othello move on the board given, flipping any pieces if needed, and returns a copy of the new board.
        Note that it expects a correct move, and does not test against it.
        
        @param board: A list of lists represting the Othello board in (row, column).
        @param move: A tuple of the row and column, i.e (row, column) of the position to place a piece of player who.
        @param who: The current players value, i.e 1 or 2.
        @return: - Type: List of Lists
                 - Content: The "board", which has been updated with the move given, with all pieces flipped
                            if needed.
    """
    
    # Place a piece of type who on the position move.
    board[move[0]][move[1]] = who
    
    # Get a list of all the opponent piece that need to be changed to who's pieces.
    oppPieces = [getLine(board, who, move, dir) 
        for dir in dir2DVect()
        if getLine(board, who, move, dir) != []
        ]
    
    # Update the newBoard, with the flipped oponent pieces.
    for posLines in oppPieces:
        for pos in posLines:
            board[pos[0]][pos[1]] = who  
    
    return board

def scoreBoard(board):
    """
        Returns the difference in score of player 1 and player 2 from the board.
        @param board: A list of lists represting the Othello board in (row, column).
        @return: - Type: Integer
                 - Content: An integer of the difference in score(that is the number of pieces a player has on the board)
                            between the 2 players.
    """
    
    # Initilise the players score variables.
    play1Score = 0
    play2Score = 0
    
    # Iterate through each value of the board
    for rowLine in board:
        for num in rowLine:
            # Test if the value is players 1 piece, if so add 1 to there score.
            if num == 1:
                play1Score += 1
            # Test if the value is players 2 piece, if so add 1 to there score.
            elif num == 2:
                play2Score += 1
    
    # Return the difference in players 1 score to player 2 score.
    # A positive number means player 1 is winning, and a negative score means player 2 is winning.
    # If it equals 0, then they are drawing.
    return play1Score - play2Score

def suggestMove1(board,who):
    """
        Returns a tuple of a "ideal" position on the board for "who" to place there piece.
        @param board: A list of lists represting the Othello board in (row, column).
        @param who: The current players value, i.e 1 or 2.
        @return: - Type: Tuple
                 - Content: A (row, height) tuple position on the "board" based on the position
                            which would give the biggest score increase.
    """
    
    # Initlise some variables using functions already made.
    valMoves = getValidMoves(board, who)
    curScore = scoreBoard(board)
    bestMove = tuple()
    
    # Loop through all possible valid moves.
    for move in valMoves:
        # Create a copy of the board.
        board2 = deepcopy(board)
        # Make a move on the copied board.
        makeMove(board2, move, who)
        # Find the new score variable of the copied modified board.
        newScore = scoreBoard(board2)
        # Check the new score against the current score, judging based on "who" whether
        # the new Score is better than the current score.
        # i.e For player 2, a new lower score means a better move, whereas for player 1,
        #     a new higher score means a better move. (As more positive is better for player 1,
        #     but a less negative score is better for player 2).
        if who == 1 and newScore > curScore:
            # If so update the current score, and the bestMove.
            curScore = newScore
            bestMove = move
        elif who == 2 and newScore < curScore:
            # If so update the current score, and the bestMove.
            curScore = newScore
            bestMove = move
    
    # Return the best move.
    return bestMove

def isCorner(pos):
    """
        Test if the position given is a corner on the board.
    
        @return: - Type: Boolean
                 - Content: True if pos is a corner, False otherwise.
    """
    if pos in [(0,0), (0,8), (8,0), (8,8)]:
        return True
    else: return False
    
def isSide(pos):
    """
        Tests if the position given is a side or edge on the board.
        
        @return: - Type: Boolean
                 - Content: True if pos is a side, False otherwise.
    """
    if (pos in [(0, x) for x in range(8)] or
        pos in [(x, 0) for x in range(8)] or
        pos in [(8, x) for x in range(8)] or
        pos in [(x, 8) for x in range(8)]):
        return True
    else: return False

def suggestMove2(board, who):
    """
        Returns a tuple of a "ideal" position on the board for "who" to place there piece.
        This algorithm is based on the idea on the idea of giving each valid move a unique weight depending 
        on several factors.
        
        @param board: A list of lists represting the Othello board in (row, column).
        @param who: The current players value, i.e 1 or 2.
        @return: - Type: void
                 - Content: N/A
        @return: - Type: Tuple
                 - Content: A (row, height) tuple position on the "board".
    """
    #@todo Add weight to counter opponent moves.
    
    # Initlise some variables using functions already made.
    valMoves = getValidMoves(board, who)
    weight = [0 for x in valMoves]
    bestMove = tuple()
    
    # Some weight-constants to customise the algorithm
    cornerWeight = 10
    sideWeight = 2
    maxScoreWeight = 1
    oppCorWeight = -10
    oppSideWeight = -5
    
    # Find the position that given most score.
    maxScoreMove = suggestMove1(board, who)
    
    # Iterate through each move, finding the weighting of placing a piece there.
    for indx, move in enumerate(valMoves):
        # Corner and side weights
        if isCorner(move):
            weight[indx] += cornerWeight
        elif isSide(move):
            weight[indx] += sideWeight
        # Max Score weight
        if move == maxScoreMove:
            weight[indx] += maxScoreWeight
        # Take a copy of the board and place the piece there.
        cpBoard = deepcopy(board)
        makeMove(cpBoard, move, who)
        # Check if the opponent can now place a corner weight.
        for oppMove in getValidMoves(cpBoard, [x for x in [1,2] if x != who][0]):
            if isCorner(oppMove):
                weight[indx] += oppCorWeight
            if isSide(oppMove):
                weight[indx] += oppSideWeight
            
    # Attempt to find the max weight if there are valid moves.
    try:
        bestMove = valMoves[weight.index(max(weight))]
        print("Weight of move is:", max(weight))
        print("Weight list is:", weight)
    # If not ignore enforce the bestMove as an empty tuple.
    except ValueError:
        bestMove = tuple()
    # Then return the move.
    return bestMove

# ------------------- Main function --------------------
def play():
    """
        Plays the game Orthello in the command console.
        
        @return: - Type: void
                 - Content: N/A
    """
    # Print welcoming messages.
    print("*"*55)
    print("***"+" "*8+"WELCOME TO JOSH'S OTHELLO GAME!"+" "*8+"***")
    print("*"*55,"\n")
    print("Enter the players' names, or type 'C' or 'A' or 'L'.\n")

    # Initilise player 1's name.
    player1Name = ""
    # Keep looping until a non-empty string is given as a name for player 1.
    while player1Name == "":
        player1Name = input("Please input Player 1's name: ")
    # Capitilise the first letter of player 1's name.
    player1Name = player1Name[0].upper() + player1Name[1:]  
    
    # Check if player 1 name is L, if so load the game.txt file.
    if player1Name == "L":
        # Load function.
        game = loadGame()
    # Otherwise continue on for a new game.
    else:
        # Initilise player 2's name.
        player2Name = ""
        # Keep looping until a non-empty string is given as a name for player 2.
        while player2Name == "":
            player2Name = input("Please input Player 2's name: ")
        # Capitilise the first letter of player 2's name.
        player2Name = player2Name[0].upper() + player2Name[1:]  
        
        # Create a new game.
        game = newGame(player1Name, player2Name)
    
    # Initlise some variables.
    player1Comp = bool(False)
    player2Comp = bool(False)
    
    # Check if either playre is a computer.
    if game["player1"] == "C" or game["player1"] == "A":
        player1Comp = True
    if game["player2"] == "C" or game["player2"] == "A":
        player2Comp = True
        
    while True:
        # Print to console current board.
        printBoard(game["board"])
        #Check which persons turn it is.
        if game["who"] == 1:
            # Check if player is a computer or human.
            if player1Comp:
                print("Comp 1 is thinking...")
                # Get valid moves with current board.
                validMoves = getValidMoves(game["board"], game["who"])
                # Check which computer algorithm to use to determine move.
                if game["player1"] == "C":
                    bestMove = suggestMove1(game["board"], game["who"])
                elif game["player1"] == "A":
                    bestMove = suggestMove2(game["board"], game["who"])
                # Check for an empty tuple move bestMove, as player may not have any valid moves.
                if bestMove != tuple():
                    # Make the suggested move on the current board.
                    makeMove(game["board"], bestMove, game["who"])
                    print("Comp 1 chose to go", indexToStr(bestMove))
                else: print("Comp 1 skipping go, no valid moves.")
            else:
                # Get valid moves with current board.
                validMoves = getValidMoves(game["board"], game["who"])
                # Convert valid moves into a string for outputting to player.
                strValidMoves = [indexToStr(x) for x in validMoves]
                # Loop until a valid move is given.
                while True:   
                    print("Valid moves are: ", strValidMoves)
                    # Get a input from player.
                    move = input("Please enter a valid move: ")
                    # Check for validity of move.
                    if move != "" and ((move in strValidMoves) or (move in [x[::-1] for x in strValidMoves])):
                        # Convert string to a tuple move.
                        move = strToIndex(move)
                        break
                    else:
                        print("You inputted: ", move)
                        print("Not valid move, try again.")
                # Make the move.
                makeMove(game["board"], move, game["who"])
        elif game["who"] == 2:
            if player2Comp:
                print("Comp 2 is thinking...")
                # Get valid moves with current board.
                validMoves = getValidMoves(game["board"], game["who"])
                # Check which computer algorithm to use to determine move.
                if game["player2"] == "C":
                    bestMove = suggestMove1(game["board"], game["who"])
                elif game["player2"] == "A":
                    bestMove = suggestMove2(game["board"], game["who"])
                # Check for an empty tuple move bestMove, as player may not have any valid moves.
                if bestMove != tuple():
                    # Make the suggested move on the current board.
                    makeMove(game["board"], bestMove, game["who"])
                    print("Comp 2 chose to go", indexToStr(bestMove))
                else: print("Comp 2 skipping go, no valid moves.")
            else:
                # Get valid moves with current board.
                validMoves = getValidMoves(game["board"], game["who"])
                # Convert valid moves into a string for outputting to player.
                strValidMoves = [indexToStr(x) for x in validMoves]
                # Loop until a valid move is given.
                while True:   
                    print("Valid moves are: ", strValidMoves)
                    # Get a input from player.
                    move = input("Please enter a valid move: ")
                    # Check for validity of move.
                    if move != "" and ((move in strValidMoves) or (move in [x[::-1] for x in strValidMoves])):
                        # Convert string to a tuple move.
                        move = strToIndex(move)
                        break
                    else:
                        print("You inputted: ", move)
                        print("Not valid move, try again.")
                # Make the move.
                makeMove(game["board"], move, game["who"])
        
        # Altenate between the current player who variable.
        game["who"] = [x for x in [1,2] if x != game["who"]][0] 
        
        # Check if both players have no valid moves, if so then game has ended.
        if (getValidMoves(game["board"], 1) == []) and (getValidMoves(game["board"], 2) == []):
            # Print final board.
            printBoard(game["board"])
            score = scoreBoard(game["board"])
            print("The end score is:", score)
            if score > 0:
                print("Player 1 has won.")
            elif score < 0:
                print("Player 2 has won.")
            elif score == 0:
                print("Draw")
            return
    
# the following allows your module to be run as a program
if __name__ == '__main__' or __name__ == 'builtins':
    play()