# Jin Yang 260724904

# take as input two ints representing # of rows and columns respectively
# returns a 2D list of strings, where all elements of sublists are
# strings containing only the space character (we indicate an empty square on the board with a space character)
# raise ValueError if inputs are not both positive ints
def create_board(row, col):
    """ (int, int) -> list of list of str
    Returns 2D list of strings, where all elements of sublists are
    str containing only space characer. Raise ValueError if inputs aren't positive ints
    
    >>> create_board(2,3)
    [[' ',' ',' '], [' ',' ',' ']]
    >>> create_board(-1, 3)
    Traceback (most recent call last):
    ValueError: Inputs must be positive
    >>> create_board(3, 0)
    Traceback (most recent call last):
    ValueError: Inputs must be positive
    """
    main_list = []
    
    if row > 0 and col > 0:
        for r in range(row):
            main_list += [[' ']*col]
                  
        return main_list
    else:
        raise ValueError("Inputs must be positive")

# takes a 2D list of str as input (representing a board); assume a retangular list
# (all sublists same size), both dimensions positive, and all elements of sublists are str
# with exactly 1 character; displays the board, one row per line;  numbers indicating column # at the top,
# numbers indicating row # on the left; for each row, elements of corresponding sublist displayed in correct order

def display_board(board):
    """ (list of list of str) -> NoneType
    Displays the board, one row per line. Numbers indicating column # at the top, numbers indicating row # on the
    left. For each row, elements of corresponding sublist displayed in correct order. Assume a retangular list,
    both dimensions being positive, and all elements of sublists are string with exactly 1 character.
    
    >>> b = create_board(4,3)
    >>> display_board(b)
    0   1   2   
  +-----------+
0 |   |   |   |
  +-----------+
1 |   |   |   |
  +-----------+
2 |   |   |   |
  +-----------+
3 |   |   |   |
  +-----------+
  >>> display_board([[' ',' ',' ',' ',' '], [' ',' ','c','a','t']])
    0   1   2   3   4   
  +-------------------+
0 |   |   |   |   |   |
  +-------------------+
1 |   |   | c | a | t |
  +-------------------+
  >>> display_board([[' ',' ','d','o','g'], [' ',' ','c','a','t']])
    0   1   2   3   4   
  +-------------------+
0 |   |   | d | o | g |
  +-------------------+
1 |   |   | c | a | t |
  +-------------------+ 
    """
    space = ' '*3
    
    print((' ' * 4),end = '')
    for i in range(len(board[0])):
        print(str(i) + (space), end = '')    
    print()

    for r in range(len(board)):
        print('  ' + '+' + (('-' * 4) * (len(board[0]) - 1)) + ('-' * 3) + '+')
        print(str(r) + ' ', end = '')
        
        for c in range(len(board[r])):
            if board[r][c] in [' ']:
                print('|' + space, end = '')
            else:
                print('|' + ' ' + board[r][c] + ' ', end = '')
                
        print('|')
        
    print('  ' + '+' + (('-' * 4) * (len(board[0]) - 1)) + ('-'*3) + '+')

# takes as input 2D list of str representing board, and an int representing number of a column
# returns list of str containing all elements from the board on the specified column
def get_vertical_axis(board, col_num):
    """ (list of list of str, int) -> list of str
    Returns list of str containing all elements from the board on the specified col_num column.
    
    >>> b = [['c','a','t',' '], [' ','a','r','t'], [' ',' ','a',' '], [' ',' ','i',' '], [' ',' ','n',' ']]
    >>> get_vertical_axis(b, 0)
    ['c', ' ', ' ', ' ', ' ']
    
    >>> b = [['c','a','t',' '], [' ','a','r','t'], [' ',' ','a',' '], [' ',' ','i',' '], [' ',' ','n',' ']]
    >>> get_vertical_axis(b, 2)
    ['t', 'r', 'a', 'i', 'n']
    
    >>> b = [['c','a','t',' '], [' ','a','r','t'], [' ',' ','a',' ']]
    >>> get_vertical_axis(b, 1)
    ['a', 'a', ' ']
    """
    col_list = []
    for i in range(len(board)):
        col_list.append(board[i][col_num])
    
    return col_list

# takes as input list of str, and an int i; returns the str built by concatenating the sequence of consecutive strings
# from the list that aren't the space characters; sequence must include the string in position i
# returns the empty string if in position i, there's a space character
def find_word(word_list, i):
    """ (list of str, int) -> str
    Returns the string built by concatenating the sequence of consecutive strings from word_list that aren't the space
    characters. Sequence includes the string in position i. Returns the empty string if in position i, there's a space
    character.
    
    >>> find_word([' ', 'c', 'a', 't', ' ', 'a', 'p', 'p', 'l', 'e'], 7)
    'apple'
    >>> find_word(['c', ' ',' '], 0)
    'c'
    >>> find_word(['c', ' ',' '], 1)
    ''
    >>> find_word([' ', 'c', 'a', 't', ' ', 'a', 'p', 'p', 'l', 'e'], 3)
    'cat'
    """
    word_str = ''
    
    if word_list[i] == ' ':
        return ''
    
    index = i
    while (word_list[index] != ' ' and index >= 0):
        index -= 1
    
    #loop from index+1 until the next space   
    for c in range(index + 1, len(word_list)):
        if word_list[c] == ' ':
            break
        else:
            word_str += word_list[c]
    
    return word_str 

# takes as input list of str representing row/column of the board, and an int i;
# returns # of empty squares on the row/column starting from position i
def available_space(row_col, i):
    """ (list of str) -> int
    Returns the number of empty squares on the row/column of the board, starting from position i.
    
    >>> r = ['a',' ',' ','b',' ',' ','c',' ',' ']
    >>> available_space(r, 2)
    5
    >>> r = ['h','e',' ','l',' ',' ',' ','l','o']
    >>> available_space(r, 3)
    3
    >>> r = ['h','e',' ','l',' ',' ',' ','l','o']
    >>> available_space(r, 2)
    4
    """
    new_rowcol = row_col[i:]
    return new_rowcol.count(' ')
 
# takes as input list of str representing a row/col on the board, a str 'letters', and an int i;
# returns True if the square in position i is empty + if there's enough space on the board to fit
# all the characters in 'letters' starting from position i; False otherwise;
# Note: each square on board can only contain one letter; function should NOT modify input list
def fit_on_board(board, letters, i):
    """ (list of str, str, int) -> bool
    Returns True if the square in position i is empty and there's enough space on board to fit all the
    characters in letters starting from position i; returns False otherwise. Each square on the board
    fits only one letter at most. Function doesn't modify the input list.
    
    >>> a = ['a', ' ', ' ', 'b', ' ']
    >>> fit_on_board(a, 'cat', 1)
    True
    >>> a = ['b', ' ',' ', ' ', 'd', 'e']
    >>> fit_on_board(a, 'here', 0)
    False
    >>> a = ['b', ' ',' ', ' ', 'd', 'e']
    >>> fit_on_board(a, 'here', 1)
    False
    """
    if board[i] != ' ':
        return False 
    avail_space = available_space(board, i)
    
    if avail_space >= len(letters):
        return True
    return False




