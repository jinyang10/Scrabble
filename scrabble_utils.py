# Jin Yang 260724904
import dicts_utils as utilsd
import board_utils as utilsb
import random
# takes as input a dictionary representing the rack of a player; Displays one line containing
# the letter that're on the rack using upper case.
def display_rack(r):
    """ (dict) -> NoneType
    Displays one line containing the letter(s) that are in the dictionary using upper case.
    >>> display_rack({'a':2, 'f':1, 'g':2, 'o':1, 'z':1})
    A A F G G O Z
    >>> display_rack({'h': 1, 'e': 1, 'l': 2, 'o': 1})
    H E L L O
    >>> display_rack({'h': 1})
    H
    """
    r_list = utilsd.flatten_dict(r)
    
    r_str = ''
    for w in r_list:
        r_str += w + ' '
    print(r_str.upper())
    
# takes as input a dictionary representing the rack of a player, and a string; Returns True if all
# characters in the input string are available on the rack, and if so, removes those letters from
# the rack; Otherwise, return False and doesn't modify the rack.
def has_letters(rack, word):
    """ (dict, str) -> bool
    Returns true if all characters in the input string are available in the dictionary rack, and if
    so, removes those letters from the rack. Otherwise, returns false and doesn't modify the rack.
    
    >>> r = {'a':2, 'c':1, 't':1, 'i':2, 'r':1}
    >>> has_letters(r, 'cat')
    True
    >>> r == {'a':1, 'i':2, 'r':1}
    True
    
    >>> r == {'a':2, 'f':1, 'g':2, 'o':1, 'z':1}
    >>> has_letters(r, 'goof'
    False
    >>> r == {'a':2, 'f':1, 'g':2, 'o':1, 'z':1}
    True
    
    >>> has_letters(r, 'fog')
    True
    >>> r == {'a': 2, 'g': 1, 'z': 1}
    True 
    """
    d_occur = utilsd.count_occurrences(word)
    if utilsd.subtract_dicts(rack, d_occur) == True:
        return True
    else:
        return False
    
def get_num_rack(rack):
    """ (dict) -> int
    Returns the number of characters in the dictionary (which maps single str characters to an int
    representing its count)
    >>> b = {'a':1, 'e':2, 'h':1, 'l':2, 'n':1, 'p':2, 's':3, 't':2, 'z':1}
    >>> get_num_rack(b)
    15
    
    >>> b = {'a':2, 'f':1, 'g':2, 'o':1, 'z':1}
    >>> get_num_rack(b)
    7
    
    >>> b = {'a': 2, 'g': 1, 'z': 1}
    >>> get_num_rack(b)
    4
    """
    num = 0
    for key in rack:
        num += rack[key]
    
    return num

# takes as input 2 dictionaries (one representing player's rack, the other the pool of letters,
# respectively), and a positive integer n; function draws letters at random from the pool and adds them
# to the rack until there are either n letters on the rack or no more letters in the pool; Doesn't return
# anything, May modify both input dictionaries
def refill_rack(rack, pool, n):
    """(dict, dict, int) -> None
    
    >>> random.seed(5)
    
    >>> r1 = {'a':2, 'k':1}
    >>> b = {'a':1, 'e':2, 'h':1, 'l':2, 'n':1, 'p':2, 's':3, 't':2, 'z':1}
    >>> refill_rack(r1, b, 7)
    >>> r1
    {'a': 2, 'k': 1, 's': 1, 'l': 1, 't': 1, 'n': 1}
    
    >>> refill_rack(r1, b, 16)
    >>> r1
    {'a': 3, 'k': 1, 's': 3, 'l': 2, 't': 2, 'n': 1, 'z': 1, 'e': 2, 'h': 1}
    
    >>> r1 = {'a': 2, 'g': 1, 'z': 1}
    >>> b = {'a':2, 'f':1, 'g':2, 'o':1, 'z':1}
    >>> refill_rack(r1, b, 4)
    {'a': 2, 'g': 1, 'z': 1}
    
    """
    # get list of characters in pool
    #p_list = utilsd.flatten_dict(pool)
    
    # choose random character from pool
    #rand_char = random.choice(p_list)
    
    # modify p_list to not pick rand_char again
    #p_list.remove(rand_char)
    
    # get total number of rand_char that's in the rack
    #rand_char_in_rack = utilsd.get_word_score(rand_char, rack)
    
    # get total number of letters in rack and pool
    num_pool = get_num_rack(pool)
    num_rack = get_num_rack(rack)
    
    count = n - num_rack
    while count > 0 and num_pool != 0:
        p_list = utilsd.flatten_dict(pool)
        rand_char = random.choice(p_list)
        p_list.remove(rand_char)
        rand_char_in_rack = utilsd.get_word_score(rand_char, rack)
        
        if rand_char_in_rack == 0:
            rack[rand_char] = 1
        else:
            rack[rand_char] += 1
        
        pool[rand_char] -= 1
        if pool[rand_char] == 0:
            pool.pop(rand_char)
            
        count -= 1
        num_pool -= 1
        num_rack += 1
       
# takes as input a list of strings, a dictionary mapping letters to integers representing
# the number of points each letter's worth, and a dictionary representing valid words
# (same format as the one returned by dicts_utils.create_scrabble_dict);
# Returns the score obtained by summing together the score of each word from the input list
# if any of the words in the list isn't valid, TOTAL score should be 0
def compute_score(list_words, dict_points, dict_valid):
    """(list, dict, dict) -> int
    Returns the score obtained by summing together the score of each word from the input list (score
    is obtained from the values of the dictionary dict_points). If any of the words in the list
    isn't valid (decided by dict_valid), total score should be 0. 
    >>> v = {'a':1, 'p':3, 'h':2}
    >>> w = ['aa', 'qi', 'za', 'cat', 'can', 'cow', 'dog', 'dad', 'hippo', 'umami', 'uncle']
    >>> d = utilsd.create_scrabble_dict(w)
    
    >>> compute_score(['hippo', 'aa'], v, d)
    10
    
    >>> v = {'c':3, 'f':1, 'j':6, 'd':2}
    >>> w = ['aa', 'qi', 'za', 'cat', 'can', 'cow', 'dog', 'dad', 'hippo', 'umami', 'uncle']
    >>> d = utilsd.create_scrabble_dict(w)
    
    >>> compute_score(['cow', 'hello'])
    0
    
    >>> compute_score(['dog', 'uncle', 'can'])
    8
    
    >>> compute_score(['here', 'now', 'rat'])
    0
    """
    is_valid = utilsd.is_valid_word_list(list_words, dict_valid)
    
    score = 0
    if is_valid == True:
        for word in list_words:
            for char in word:
                if char in dict_points:
                    score += dict_points[char]
    
    else:
        return 0
    
    return score

# takes as input a two-dimensional list representing the board, a string representing
# the letters the player wants to add to the board, 2 integers representing the row and col
# number (respectively) of the starting square, and a string indicating the direction to
# take when placing the letters on the board (either 'down' or 'right');
# 1) adds the letters received as input to the board given a starting position, and a direction;
# 2) returns a list of words created by adding those letters to the board;
# the list will contain the main word as well as any hook word generated; order of the elements
# doesn't matter; Note: input list should be modified, unless the direction provided is not equal
# to neither 'down' nor 'right';
# in such case, returns an empty list; ASSUME the starting square is empty and the provided letters
# will fit the board
def place_tiles(board, letters, row, col, direction):
    """ (list of list, str, int, int, str) -> list
    Adds the letters received as input to the board given a starting position at row/col number, and a
    direction ('down' or 'right'). Returns a list of words created by adding those letters to the board.
    The list will contain the main word, as well as any hook word generated; order of the elements doesn't
    matter. The input list is modified unless the direction provided isn't 'down' nor 'right'; in such a case,
    returns an empty list. Assume the starting square is empty and the provided letters will fit the board. 

    >>> b = [['c','a','t',' '], [' ',' ',' ',' '], [' ',' ',' ',' '], [' ',' ',' ',' '], [' ',' ',' ',' ']]
    >>> place_tiles(b, 'rain', 1, 2, 'down')
    ['train']
    
    >>> words = place_tiles(b, 'mt', 2, 1, 'right')
    >>> words
    ['mat']
    
    >>> words2 = place_tiles(b, 'sa', 0, 3, 'down')
    >>> words2.sort()
    >>> words2
    ['cats', 'ra', 'sat']
    
    """
    # deep copy of the original (input) board
    copy_ori_board = []
    for ele in board:
        ori_board = []
        for n in ele:
            ori_board.append(n)
        copy_ori_board.append(ori_board)
        
    board_speci = []
    if direction not in ['down', 'right']:
        return board_speci
    
    row_speci = row
    if direction == 'down':
        while row_speci < len(board):
            board_speci += board[row_speci][col]
            
            row_speci += 1 
        
        row_speci = row
        if utilsb.fit_on_board(board_speci, letters, 0) == True:
            for char in range(len(letters)):
                if board[row_speci][col] == ' ':
                    board[row_speci][col] = letters[char]
                    row_speci += 1
                    
                else:
                    board[row_sepcial + 1][col] = letters[char]
                
                    row_speci += 1            
                   
               
    col_speci = col        
    if direction == 'right':
        while col_speci < len(board[0]):
            board_speci += board[row][col_speci]
            col_speci += 1
        
        col_speci = col
        if utilsb.fit_on_board(board_speci, letters, 0) == True:
            for char in range(len(letters)):
                if board[row][col_speci] == ' ':
                    board[row][col_speci] = letters[char]
                    col_speci += 1
               
                else:
                    board[row][col_speci + 1] = letters[char]
                    col_speci += 1
    
    # get a list of str from column col
    ori_col_word = utilsb.get_vertical_axis(copy_ori_board, col)
    new_col_word = utilsb.get_vertical_axis(board, col)
    
    # compare words in the list of list of str in each row and col, add word to an empty str
    # if word isn't in the original board (before adding letters), and add the str to a new list;
    # return the list 
    new_board_list = []
    new_str = ''
    
    if new_col_word != ori_col_word:
        for c in range(len(ori_col_word)):
            if utilsb.find_word(new_col_word, c) != utilsb.find_word(ori_col_word, c):
                if utilsb.find_word(new_col_word, c) not in new_str:
                    if len(utilsb.find_word(new_col_word, c)) > 1:
                        
                        new_str += utilsb.find_word(new_col_word, c)
                        new_board_list.append(new_str)
           
    for w in range(len(board)):
            
        if board[w] == copy_ori_board[w]: 
            continue
        else:
            for el in range(len(board[w])):
                if len(utilsb.find_word(board[w], el)) > 1:
                    if utilsb.find_word(board[w], el) != utilsb.find_word(copy_ori_board[w], el):
                        if utilsb.find_word(board[w], el) not in new_board_list:
                            
                            new_board_list.append(utilsb.find_word(board[w], el))
                        
    return new_board_list

# takes as input a list representing the board, a dictionary representing  the player's rack,
# a string representing the letters the player wants to place, two integers representing the row and column
# number (respectively) of the starting square on the board, and a string representing the direction (either
# 'down' or 'right'; if direction isn't 'down' or 'right', return an empty string (terminate right away).
# Othwerise, checks if this is a valid move:
# Is there enough space on the board to place those letters? Does the player actually have those letters on the
# rack? If so, then the letters are placed on the board, and a list of words created by performing the move
# is returned; Otherwise, if letters don't fit on the board, function raises an IndexError
# If they fit but player doesn't have those letters on their rack, function raises a ValueError;
# if an Error is raised, neither the board nor rack is modified; Otherwise, letters are removed from the rack
# and placed on the board.
def make_a_move(board, rack, letters, row, col, direction):
    """ (list, dict, str, int, int, str) -> list
    If the string indictating direction isn't 'down' or 'right', returns an empty string. If there's enough
    space on the board to place the letters, and player actually has those letters on the rack, then
    letters are placed on the board and a list of words created by performing the move is returned.
    Otherwise, if letters if letters don't fit on the board, function raises an IndexError. If they fit but
    player doesn't have those letters on their rack, function raises a ValueError; if an Error is raised,
    neither the board nor rack is modified; Otherwise, letters are removed from the rack and placed on the board.
    
    >>> b = [['c','a','t',' '], [' ',' ',' ',' '], [' ',' ',' ',' '], [' ',' ',' ',' '], [' ',' ',' ',' ']]
    >>> r = {'a':3, 't':2, 'c':1, 'r':1, 'i':1, 'n':1}
    
    >>> make_a_move(b, r, 'rain', 1, 2, 'down')
    ['train']
    >>> r == {'a':2, 't':2, 'c':1}
    True
    
    >>> words = make_a_move(b, r, 'mt', 2, 1, 'right')
    Traceback (most recent call last):
    You do not have those letters on your rack!
    >>> r == {'a':2, 't':2, 'c':1}
    True
    
    >>> make_a_move(b, r, 'cat', 3, 1, 'down')
    Traceback (most recent call last):
    IndexError: There is not enough space to place the specified letters on the board.
    >>> r == {'a':2, 't':2, 'c':1}
    True
    
    >>> make_a_move(b, r, 'cat', 2, 1, 'down')
    ['cat', 'ca', 'ai', 'tn']
    >>> r == {'a':1, 't':1}
    True
    """
    board_speci = []
    
    dict_letters_occur = utilsd.count_occurrences(letters)
    
    if direction not in ['down', 'right']:
        return board_speci
    
    row_speci = row
    if direction == 'down':
        while row_speci < len(board):
            board_speci += board[row_speci][col]
            
            row_speci += 1 
        
        if utilsb.fit_on_board(board_speci, letters, 0) == True:
            if utilsd.subtract_dicts(rack, dict_letters_occur) == True:
                made_move = place_tiles(board, letters, row, col, direction)
                return made_move
            else:
                raise ValueError('You do not have those letters on your rack!')
        else:
            raise IndexError('There is not enough space to place the specified letters on the board.')
    
    col_speci = col        
    if direction == 'right':
        while col_speci < len(board[0]):
            board_speci += board[row][col_speci]
            col_speci += 1
            
        if utilsb.fit_on_board(board_speci, letters, 0) == True:
            if utilsd.subtract_dicts(rack, dict_letters_occur) == True:
                made_move = place_tiles(board, letters, row, col, direction)
                return made_move 
            else:
                raise ValueError('You do not have those letters on your rack!')
        else:
            raise IndexError('There is not enough space to place the specified letters on the board.')
        
