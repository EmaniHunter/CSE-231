##############################################################################
#   Computer Project 10
#       Alogrithm
#           focus: classes, dictionaries, lists, gameplay
#           defined functions
#               implements a board game called Reversi (Othello) 
#                   using classes
#               implement board pieces of two colors to represent
#                   real two player gameplay on a board
#               places each piece in a specific position
#               if position is invalid, or not valid for the specific color
#                   error checking is made
#               determines who wins the game by counting how many pieces of
#                   one color are on the board, 
#                   if there is more pieces of one color the opponent that
#                   withholds that color wins
##############################################################################

import reversi 
import string
LETTERS = string.ascii_lowercase
#^everything in lowercase alphabet
"""
Implements a classical board game called Reversi in Python using classes.
"""

def indexify(position):
    """
    The indexify function converts letter-number
    positions to row-column indices. Runs through the 
    alphabetical keys and numerical values in a dictionary
    indexes at the given position parameter. It then
    creates a tuple containing the row and column numbers
    and returns that tuple.
    """
    #dictionary created with keys as letters and values as numbers
    alpha = {"a":0, "b":1,"c":2,"d":3,"e":4,"f":5, "g":6,"h":7, "i":8, "j":9, \
             "k":10,"l":11, "m":12, "n":13, "o":14, "p":15, "q":16,"r":17, \
             "s":18, "t":19, "u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
    
    row = alpha[position[0]] #row indexed at position zero 
    col = int(position[1:])-1 #column indexed and sliced [1:], subtracted by
                                #1 to get the value number less than that
                                #number in the dictionary
    
    indexed = (row,col) #new tuple created with row and column indices
    return indexed


def deindexify(row, col):
    """
    Creates a letter-number position from row- column values
    used as two parameters within deindexify function. Runs
    through each number within the range of 1to 26 and adds
    each number to a new list. Indexes the row alphabetic
    value and indexes the column numeric value from
    the new list. Concatenates the letter(row) and number(col)
    returns that concatenated letter-number position.
    """
    new_list = [] #creates new list
    for i in range(1,27): #loops through the range of 1-27 to go to 1-26
        new_list.append(i) #adds each item in that range to the new list
        
    rowval = LETTERS[row] #indexes the row values using the row parameter
                            #and indexes from the LETTERS variable
    colval = new_list[col] #indexes the column values from the new list
    deindexed = str(rowval) + str(colval) #concatenates the row and column
                                            #values
    
    return deindexed #returns that letter-number position that was concatenated

def initialize(board):
    """
    Initializes two black and two white pieces
    in the middle of the board. Black pieces placed
    diagonally right and white pieces placed diagonally left.
    Takes the length of the boards and uses floor division
    to get a whole number (instead of a floating point number).
    (This accounts for odd sized boards and even sized boards).
    
    """
    length = board.length // 2 - 1 #uses floor division to get length as a 
                                    #whole number, accounts for odd sized board
                                    #lengths
    #This makes the white pieces placed diagonally left and the blackpieces
    #placed diagonally right:
    board.place(length,length, reversi.Piece('white'))
    board.place(length + 1, length + 1, reversi.Piece('white'))
    board.place(length + 1, length, reversi.Piece('black'))
    board.place(length, length + 1, reversi.Piece('black'))
        
def count_pieces(board):
    """
    This function counts the total number of 
    black and white pieces that are currently on the
    board. Loops through the row, col of the board length,
    creates a count of black and white pieces, if the piece
    is white- count by 1- if the piece is black - count by 1. 
    The counts are returned as a tuple.
    """
    black, white = 0, 0 #initialize black and white counts to zero
    length = board.length
    
    #loops through the range of the length size:
    for i in range(length): 
        for j in range(length):
            p = board.get(i,j)
            if p != None: #if the get position is not equal to NONE
                if p.is_white(): #accounts for the piece being white
                    white +=1 #increments counts by 1

                if p.is_black(): #accounts for the piece being black
                    black += 1 #increments counts by 1
                    
    colorpieces_tup = (black, white) #creates a new tuple with the black and
                                    #white 
    return colorpieces_tup


def get_all_streaks(board, row, col, piece_arg):
    """
    This function finds all capturing streaks if a piece
    is placed on the row, column position. The function returns
    a dictionary of all capturing streaks in 8 directions. An empty
    dictionary is initialized in the beginning of the function, 
    the values of each key being 'None'. Values are later
    turned into lists, lists are sorted and then added to 
    the streaks dictionary.
    """
    streaks = {'e': None, 'w': None, 'n': None, 's': None, \
               'ne': None, 'nw': None, 'se': None, 'sw': None}
    
    color = piece_arg.color()
    other_color = 'white' if color == 'black' else 'black'
    # north
    L = []
    c = col
    for r in range(row-1,-1,-1):
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
    else:
        L = [] # streak not terminated with color piece
    streaks['n'] = sorted(L)

#    # east
    L = []
    c = col
    r = row
    for c in range(col+1,board.length):
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
    else:
        L = [] # streak not terminated with color piece
    streaks['e'] = sorted(L)
 
#    # south
    L = []
    c = col
    r = row
    for r in range(row+1,board.length):
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
    else:
        L = [] # streak not terminated with color piece
    streaks['s'] = sorted(L)

#    # west
    L = []
    c = col
    r = row
    for c in range(col-1,-1,-1):
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
    else:
        L = [] # streak not terminated with color piece
    streaks['w'] = sorted(L)

#    # northeast
    L = []
    c = col
    r = row
    c = col+1
    for r in range(row-1,-1,-1):
        if c == board.length:
            L = []  # terminated without finding color
            break
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
        c += 1
    else:
        L = [] # streak not terminated with color piece
    streaks['ne'] = sorted(L)
        
#    # southeast
    L = []
    c = col
    r = row
    c = col+1
    for r in range(row+1,board.length):
        if c == board.length:
            L = []  # terminated without finding color
            break
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
        c += 1
    else:
        L = [] # streak not terminated with color piece
    streaks['se'] = sorted(L)
                
#    # southwest
    L = []
    c = col
    r = row
    c = col - 1
    for r in range(row+1,board.length):
        if c == -1:
            L = []  # terminated without finding color
            break
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
        c = c - 1
    else:
        L = [] # streak not terminated with color piece
    streaks['sw'] = sorted(L)
    
#    # northwest
    L = []
    c = col
    r = row
    c = col - 1
    for r in range(row-1,-1,-1):
        if c == -1:
            L = []  # terminated without finding color
            break
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
        c = c - 1
    else:
        L = [] # streak not terminated with color piece
    streaks['nw'] = sorted(L)

            
    return streaks

def get_all_capturing_cells(board, piece):
    """
    This function takes two parameters, the board and 
    piece. Returns a list of all capturing streak found from all
    empty positions on the board in a dictionary. The key of
    the dictionary is the (row and column) in a tuple as the
    position and the vaoues being the list of the capturing streaks.
    (Overall, the values are extended to the list and sorts the list
     sets the dictionaries keys equal to the list (making the lists 
     the values)).
    """

    D = {}
    for col in range(board.length): #loops through the ranges of the length of
                                        #the board
        for row in range(board.length):
            if board.is_free(col, row): #calls is_free function from reversi.py
                #calls get_all_streaks function
                d = get_all_streaks(board, col,row, piece)
                my_list = []
                for k, v in d.items(): #loops through the get_all_streaks
                                        #function 
                    if len(v) > 0: #accounts if the length of the values (list)
                                    #is greater than zero
                        new_tup = (col, row) #creates new tuple with column
                                            #and row values
                        my_list.extend(v) #extends the list of values to the 
                                            #new list
                        my_list.sort() #sorts the new list
                        D[new_tup] = my_list #sets dictionary keys equal to 
                                            #the new list containing the values
     
    return D

def get_hint(board, piece):
    """
    This function takes two parameters, board and piece.
    It calls the get_all_capturing_cells function and gets 
    the streaks for each empty position on the board. Then sorts
    the list of positions in descending order , following the
    the length of the streaks and returns it.
    """
    new_list = []
    new_list2 = []
    new_dict = get_all_capturing_cells(board, piece) #calls get_all_capturing
                                                    #function
    for k,v in new_dict.items(): #loops through keys, values in the get_all
                                #capturing cells function
        length = len(v) #establishes the length of the values
        new_list.append((length, k)) #adds the length of the values and the key
                                    #in the function to the first new list
    new_list.sort(reverse = True) #sorts the first new list in descending order
    
    for number, values in new_list: #loops through the items in the first list
        new_list2.append(deindexify(values[0], values[1])) #adds the values 
                                                #indexed, with deindexify func
                                                #called, to the second new list
    
    return new_list2 #returns the second and final list
    
def place_and_flip(board, row, col, piece):
    """
    Calls the get_all_streaks function to get all the capturing
    streaks from the position row, column. Places the piece
    to that specific position and flips all the pieces that are 
    along the streak positions found in the called function.
    Raises ValueError if problems can be found on the board
    and outside of the board.
    
    """
    try:
        #goes to show if the row, column position is already occupied
        if board.get(row,col): 
            raise ValueError(\
 "Can't place {:s} at '{:s}', already occupied. Type 'hint' to get suggestions."\
 .format(str(piece),deindexify(row,col)))
       #calls get_all_streaks function
        streak_list = get_all_streaks(board, row, col, piece)
        newlist = []
        
        #loops through all key, value pairs returned in the get_all_streaks
        #function
        for key, value in streak_list.items():
            if  value: #if there is a value
                newlist.extend(value) #extend the value (s) to the newlist
        if newlist: #if the newlist is empty
            board.place(row,col,piece) #place a piece at position
            for position in newlist: #loops through the positions in the newlist
                board.get(position[0], position[1]).flip() #gets the piece
                                                        #at position, flips the
                                                        #one piece
        else:
            #goes to show if the row, column position does not yield any capture
            #if the newlist is not empty
            raise ValueError(\
 "Can't place {:s} at '{:s}', it's not a capture. Type 'hint' to get suggestions."\
 .format(str(piece),deindexify(row,col)))
            
    #throws an indexerror if the position is outside of the board or not at a
    #correct position on the board
    except IndexError:
        raise ValueError(\
 "Can't place {:s} at '{:s}', invalid position. Type 'hint' to get suggestions."\
 .format(str(piece),deindexify(row,col)))
        
def is_game_finished(board):
    """
    This function calls the get_all_capturing_cells
    function, takes the length of the dictionary returned
    in that function. If the length is empty, the function
    returns true- meaning the game is finished. If the 
    length is not empty, the function returns false- meaning
    the game is not finished.
    """
    #calling the get_all_capturing_cells function, accounting for the 
    #length of the dictionary that is returned in the function
    x = len(get_all_capturing_cells(board, reversi.Piece('white')))
    y = len(get_all_capturing_cells(board, reversi.Piece('black')))

    if x == 0 and y == 0: #if the length of the dictionary contains nothing,
                            #the game is finished, returns true that it is
        return True
    else:   #else if the length of the dictionary contains something
            #the game is not finished, returns false that it is not
        return False
            
def get_winner(board):
    """
    The function gets the current winner.It counts the
    number of black and white pieces and decides which player
    is the winner. Returns the opponents color that
    is the winner. In order to count the pieces- the
    count_pieces function is called.
    """
    x = count_pieces(board)
    if x[0] > x[1]: #if the amount of black pieces is more than the amount of
                    #white pieces, the winner black
        return 'black'
    if x[0] < x[1]: #if the amount of black pieces is less than the amount of
                    #white pieces, the winner is white
        return 'white'
    if x[0] == x[1]:    #if the amount of black and white pieces equal each 
                        #other, it is a tie/draw
        return 'draw'
    
def choose_color():
    """
    This function asks for a color inside a loop
    until a valid color name is entered. If wrong color
    is entered and not 'black' or 'white'- error message is
    printed. When the correct color name is entered
    the color values are stored in a tuple and returned.
    """
    color_input = input("Pick a color: ") #asks for input
    #loops to see if color input is not black or white, prints error statement
    while color_input != 'black' and color_input != 'white': 
        print("Wrong color, type only 'black' or 'white', try again.")
        color_input = input("Pick a color: ")
    if color_input == 'black': #if color input is black, opponents color is 
                                #white
        my_color = 'black'
        opponent_color = 'white'
    if color_input == 'white': #if color input is white, opponents color is 
                                #black
        my_color = 'white'
        opponent_color = 'black'
    
    color_tup = (my_color, opponent_color) #returns the user's color and the
                                            #opponents color as a tuple
    print("You are '{:s}' and your opponent is '{:s}'.".format(color_tup[0], \
          color_tup[1])) #formats tuple
    return color_tup
        
def game_play_human():
    """
    This is the main mechanism of the human vs. human game play.
    """
    
    banner = """
     _____                         _ 
    |  __ \                       (_)
    | |__) |_____   _____ _ __ ___ _ 
    |  _  // _ \ \ / / _ \ '__/ __| |
    | | \ \  __/\ V /  __/ |  \__ \ |
    |_|  \_\___| \_/ \___|_|  |___/_|
    
    Developed by The Students Inc.
    CSE231 Spring Semester 2018
    Michigan State University
    East Lansing, MI 48824, USA.
    """

    prompt = "[{:s}'s turn] :> "
    print(banner)
   
    # Choose the color here
    (my_color, opponent_color) = choose_color()
    
    # Take a board of size 8x8
    # Prompt for board size
    size = input("Input a board size: ")
    board = reversi.Board(int(size))
    initialize(board)
    
    # Decide on whose turn, use a variable called 'turn'.
    turn = my_color if my_color == 'white' else opponent_color
    
    # loop until the game is finished
    while not is_game_finished(board):
        try:
            # Count the pieces and assign into piece_count
            piece_count = count_pieces(board)
            
            print("Current board:")
            board.display(piece_count)    
            
            # Get a piece according to turn
            piece = reversi.Piece(turn)

            # Get the command from user using input
            command = input(prompt.format(turn)).lower()
            
            # Now decide on different commands
            if command == 'exit':
                break
            elif command == 'hint':
                print("\tHint: " + ", ".join(get_hint(board, piece)))
            elif command == 'pass':
                hint = get_hint(board, piece)
                if len(hint) == 0:
                    turn = my_color if turn == opponent_color \
                                        else opponent_color
                    print("\tHanded over to \'{:s}\'.".format(turn))
                else:
                    print("\tCan't hand over to opponent, you have moves," + \
                          " type \'hint\'.")
            else:
                    (row, col) = indexify(command)
                    place_and_flip(board, row, col, piece)
                    print("\t{:s} played {:s}.".format(turn, command))
                    turn = my_color if turn == opponent_color \
                                        else opponent_color
        except Exception as err:
            print("Error:", err)
    
    # The loop is over.
    piece_count = count_pieces(board)
    print("Current board:")
    board.display(piece_count)    
    winner = get_winner(board)
    if winner != 'draw':
        diff = abs(piece_count[0] - piece_count[1])
        print("\'{:s}\' wins by {:d}! yay!!".format(winner, diff))
    else:
        print("This game ends in a draw.")
    # --- end of game play ---

def figure_1(board):
    """
    You can use this function to test your program
    """
    board.place(0,0,reversi.Piece('black'))
    board.place(0,3,reversi.Piece('black'))
    board.place(0,4,reversi.Piece('white'))
    board.place(0,5,reversi.Piece('white'))
    board.place(0,6,reversi.Piece('white'))
    board.place(1,1,reversi.Piece('white'))
    board.place(1,3,reversi.Piece('white'))
    board.place(1,5,reversi.Piece('white'))
    board.place(1,6,reversi.Piece('white'))
    board.place(1,7,reversi.Piece('white'))
    board.place(2,2,reversi.Piece('white'))
    board.place(2,3,reversi.Piece('black'))
    board.place(2,4,reversi.Piece('white'))
    board.place(2,5,reversi.Piece('white'))
    board.place(2,7,reversi.Piece('white'))
    board.place(3,0,reversi.Piece('black'))
    board.place(3,1,reversi.Piece('white'))
    board.place(3,2,reversi.Piece('white'))
    board.place(3,4,reversi.Piece('white'))
    board.place(3,5,reversi.Piece('white'))
    board.place(3,6,reversi.Piece('black'))
    board.place(3,7,reversi.Piece('black'))
    board.place(4,0,reversi.Piece('white'))
    board.place(4,2,reversi.Piece('white'))
    board.place(4,4,reversi.Piece('white'))
    board.place(5,0,reversi.Piece('black'))
    board.place(5,2,reversi.Piece('black'))
    board.place(5,3,reversi.Piece('white'))
    board.place(5,5,reversi.Piece('black'))
    board.place(6,0,reversi.Piece('black'))
    board.place(6,1,reversi.Piece('black'))
    board.place(6,3,reversi.Piece('white'))
    board.place(6,6,reversi.Piece('white'))
    board.place(7,1,reversi.Piece('black'))
    board.place(7,2,reversi.Piece('white'))
    board.place(7,3,reversi.Piece('black'))
    board.place(7,7,reversi.Piece('black'))
    
if __name__ == "__main__":
    game_play_human()
