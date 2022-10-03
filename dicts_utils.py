# Jin Yang 260724904

# takes as input a str; returns a dictionary mapping characters to integers; the keys in the dictionary are
# are the characters from the input string, the values represent the # of occurences of those characters in the
# input string
def count_occurrences(word):
    """ (str) -> dict
    Returns a dictionary mapping characters to integers. The keys in the dictionary are the characters
    from the input string, the values represent the number of occurrences of those characters in the input string.
    
    >>> d = count_occurrences('banana'):
    >>> d == {'b':1, 'a':3, 'n':2}
    True
    >>> d = count_occurrences('hello')
    >>> d == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    True
    >>> d = count_occurrences('coronavirus')
    >>> d == {'c': 1, 'o': 2, 'r': 2, 'n': 1, 'a': 1, 'v': 1, 'i': 1, 'u': 1, 's': 1}
    True
    """
    count = {}
    
    for e in word:
        if e in count:
            count[e] += 1
        if e not in count:
            count[e] = 1
    
    return count

# takes as input a dictionary where all the values are non-negative integers; Returns a list containing
# the keys in the dictionary; Each key should appear in the list as many times as the value associated to such key
# function does not modify the input dictionary

def flatten_dict(flat_dict):
    """ (dict) -> list
    Returns a list containing the keys in the dictionary. Each key appears in the list as many times as the
    value associated to such key. Doesn't modify the input dictionary. Input dictionary values are all non-negative
    integers.
    
    >>> d = {'a':2, 'f':1, 'k':5}
    >>> flatten_dict(d)
    ['a', 'a', 'f', 'k', 'k', 'k', 'k', 'k']
    
    >>> d = {'c':5, 'h':3, 'j': 1, 'y':0}
    >>> flatten_dict(d)
    ['c', 'c', 'c', 'c', 'c', 'h', 'h', 'h', 'j']
    
    >>> d = {'a':0}
    >>> flatten(d)
    []
    """
    flat_list = []
    
    for key in flat_dict:
        flat = key * flat_dict[key]
        flat_list += flat
        
    return flat_list

# takes as input a string and a dictionary mapping characters to integers representing the # of points each
# character is worth; if a given character isn't a key in the input dictionary, assume such character is 0 points;
# Returns the score of a word (the input string) computed by summing together the value of each character
# in the word.
def get_word_score(word, score_dict):
    """ (str, dict) -> int
    Returns the score of a word (the input string) computed by summing together the value of each character in the
    word, which corresponds to the value of the character key in the input dictionary. If a given character isn't
    a key in the input dictionary, assume it's 0 points.
    
    >>> v = {'a':5, 't':3, 'n':-2}
    >>> get_word_score('cat', v)
    8
    >>> get_word_score('banter', v)
    6
    >>> get_word_score('sled', v)
    0
    """
    num_score = 0
    for i in range(len(word)):
        for key in score_dict:
            if word[i] in key:
                num_score += score_dict[key]
            
    return num_score

# takes as input 2 dictionaries, where all values are non-negative integers; Returns True if the 1st dictionary
# can be considered to be a subset of the 2nd one; Consider a dictionary d to be a subset of another dictionary b
# if all the keys in d are keys in b, and the value associated to each key d is smaller/or equal to the value
# associated to the same key  in b; Does not modify the input dictionaries
def is_subset(dict_1, dict_2):
    """ (dict, dict) -> bool
    Returns true if dictionary dict_1 can be considered a subset of dictionary dict_2. Consider a dict_1 to be
    a subset of dict_2 if all the keys in dict_1 are keys in dict_2.
    
    >>> a = {'a':2, 'c':1}
    >>> b = {'a':2, 'b':1, 'c':2}
    >>> c = {'a':3, 'b':3, 'c':1}
    >>> d = {'a':2, 'b':1, 'd':1}
    >>> is_subset(b, a)
    False
    >>> is_subset(a, b)
    True
    >>> is_subset(b, c)
    False
    >>> is_subset(d, b)
    False
    """
    for key1 in dict_1:
        if key1 not in dict_2:
            return False
        
    for key_1 in dict_1:
        if dict_1[key_1] > dict_2[key_1]:
            return False
        continue
    
    return True

# takes as input 2 dictionaries d1 and d2, where all the values are non-negative integers;
# if d2 is a subset of d1, updates d1 by replacing the values associated to the common keys with
# the difference between original value in d1 and d2; Otherwise, d1 remains as is; Returns True
# if d2 was subset of d1, False otherwise; Function should not modify d2
def subtract_dicts(d1, d2):
    """ (dict, dict) -> bool
    If d2 is a subset of d1, update d1 by replacing the values associated to the common keys with the
    difference between the original value in d1 and d2. Otherwise, d1 remains as is. Returns
    true if d2 was a subset of d1, false otherwise. Function does not modify d2.
    
    >>> a = {'a':2, 'c':1}
    >>> b = {'a':2, 'b':1, 'c':2}
    >>> c = {'a':5, 'b':3, 'c':5}
    >>> subtract_dicts(b, a)
    True
    >>> b == {'b':1, 'c':1}
    True
    
    >>> subtract_dicts(a, b)
    False
    >>> a == {'a':2, 'c':1}
    True
    
    >>> subtract_dicts(c, b)
    True
    >>> c == {'a': 3, 'b': 2, 'c': 3}
    True
    """
    if is_subset(d2, d1) == True:
        for key2 in d2:
            if d1[key2] > d2[key2]:
                d1[key2] = d1[key2] - d2[key2]
            else:
                del d1[key2]
        return True
    
    else:
        return False
    
# takes as input a list of str; Returns a dictionary that maps integers representing the number of
# characters in a word to a dictionary of words with the specified length; the latter maps a single
# letter to a list of words beginning with such letter
def create_scrabble_dict(list_chars):
    """(list) -> dict of dict
    Returns a dictionary that maps integers representing the # of characters in a word, to a dictionary
    of words with the specified length. The latter maps a single letter to a list of words beginning with
    such letter.
    
    >>> w = ['aa', 'qi', 'za', 'cat', 'can', 'cow', 'dog', 'dad', 'hippo', 'umami', 'uncle']
    >>> d = create_scrabble_dict(w)
    >>> d == {2 : {'a': ['aa'], 'q': ['qi'], 'z': ['za']}, 3 : {'c': ['cat', 'can', 'cow'],\
    'd': ['dog', 'dad']}, 5 : {'h': ['hippo'], 'u': ['umami', 'uncle']}}
    True
    
    >>> w = ['qi', 'za', 'cat', 'can', 'cow', 'dog', 'dad', 'hippo', 'umami', 'uncle', 'slower', 'faster']   
    >>> d = create_scrabble_dict(w)
    >>> d == {2: {'q': ['qi'], 'z': ['za']}, 3: {'c': ['cat', 'can', 'cow'], 'd': ['dog', 'dad']},\
    5: {'h': ['hippo'], 'u': ['umami', 'uncle']}, 6: {'s': ['slower'], 'f': ['faster']}}
    True
    
    >>> w = ['i', 'a', 'qi', 'za', 'can', 'cow', 'dog', 'dad', 'umami', 'uncle', 'slower', 'faster']   
    >>> d = create_scrabble_dict(w)
    >>> d == {1: {'i': ['i'], 'a': ['a']}, 2: {'q': ['qi'], 'z': ['za']}, 3: {'c': ['can', 'cow'],\
    'd': ['dog', 'dad']}, 5: {'u': ['umami', 'uncle']}, 6: {'s': ['slower'], 'f': ['faster']}}
    True
    """
    l_dict = {}
   
    for i in range(len(list_chars)):
        new_dict = {list_chars[i][0] : [list_chars[i]]}
        
        if len(list_chars[i]) not in l_dict:
            l_dict[len(list_chars[i])] = new_dict
            
        else:
            if list_chars[i][0] not in l_dict[len(list_chars[i])]:
                l_dict[len(list_chars[i])][list_chars[i][0]] = [list_chars[i]]
            else:
                l_dict[len(list_chars[i])][list_chars[i][0]].append(list_chars[i])
                    
    return l_dict

# takes as input a string and a dictionary; the dictionary has the same format as the one returned in
# create_scrabble_dict; Returns True if input string appears in the dictionary, False otherwise
def is_valid_word(chars, w_dict):
    """ (str, dict) -> bool
    Returns true if input string appears in the input dictionary, false otherwise.
    
    >>> w = ['i', 'a', 'qi', 'za', 'can', 'cow', 'dog', 'dad', 'umami', 'uncle', 'slower', 'faster']
    >>> d = create_scrabble_dict(w)
    >>> is_valid_word('hippo', d)
    False
    
    >>> is_valid_word('umami', d)
    True
    
    >>> is_valid_word('i', d)
    True
    """
    for num in w_dict:
        for c in w_dict[num]:
            if chars in w_dict[num][c]: 
                return True
            else:
                continue
        
    return False

def is_valid_word_list(word_list, w_dict):
    """ (list, dict) -> bool
    Similar to  is_valid_word, except takes as input a list of strings instead of just a string.
    If there's a string in the list which doesn't appear in the dictionary, returns false.
    
    Otherwise, returns true.
    
    >>> w = ['i', 'a', 'qi', 'za', 'can', 'cow', 'dog', 'dad', 'umami', 'uncle', 'slower', 'faster']
    >>> d = create_scrabble_dict(w)
    >>> is_valid_word_list(['hippo'], d)
    False
    
    >>> is_valid_word_list(['umami', 'hippo'], d)
    False
    
    >>> is_valid_word_list(['umami'], d)
    True
    
    >>> is_valid_word_list(['i'], d)
    True
    """
    
    for word in word_list:
        if is_valid_word(word, w_dict) == False:
            return False
        else:
            continue
        
    return True                
