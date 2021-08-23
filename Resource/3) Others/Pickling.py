

import pickle

ques = (['Is Python case sensitive when dealing with identifiers? ', ' Yes ', ' No ', ' Machine dependent ', ' None of the mentioned'],
        ['What is the maximum possible length of an identifier? ', ' none of the mentioned ', ' 63 characters ', ' 79 characters ', ' 31 characters '],
        ['Which of the following is an invalid variable? ', ' 1st_string ', ' my_string_1 ', ' foo ', ' _'],
        ['Why are local variable names beginning with an underscore discouraged? ', ' They are used to indicate a private variables of a class ', ' They confuse the interpreter ', ' They are used to indicate global variables ', ' They slow down execution'],
        ['Which of the following is invalid? ', ' None of the mentioned ', ' __a = 1 ', ' __str__ = 1 ', ' _a = 1'],
        ['Which of the following is not a keyword? ', ' eval ', ' assert ', ' nonlocal ', ' pass'],
        ['All keywords in Python are in _________ ', ' None of the mentioned ', ' UPPER CASE ', ' Capitalized ', ' Lower case '],
        ['Which of the following is true for variable names in Python? ', ' Unlimited length ', ' All private members must have leading and trailing underscores ', ' Underscore and ampersand are the only two special characters allowed ', ' None of the mentioned'],
        ['Which of the following is an invalid statement? ', ' a b c = 1000 2000 3000 ', ' abc = 1', '000', '000 ', ' a', 'b', 'c = 1000', ' 2000', ' 3000 ', ' a_b_c = 1', '000', '000'], ['Which of the following cannot be a variable? ', ' in ', ' __init__ ', ' it ', ' on'], ['What is the output of print 0.1 + 0.2 == 0.3? ', ' False ', ' True ', ' Machine dependent ', ' Error'],
        ['Which of the following is not a complex number? ', ' k = 2 + 3l ', ' k = complex(2', ' 3) ', ' k = 2 + 3j ', ' k = 2 + 3J'], ['What is the type of inf? ', ' Float ', ' Integer ', ' Boolean ', ' Complex'], ['What does ~4 evaluate to? ', ' -5 ', ' -4 ', ' -3 ', ' +3'], ['What does ~~~~~~5 evaluate to? ', ' +5 ', ' -11 ', ' +11 ', ' -5'], ['Which of the following is incorrect? ', ' x = 03964 ', ' x = 0x4f5 ', ' x = 19023 ', ' x = 0b101'], ['What is the result of cmp(3', ' 1)? ', ' 1 ', ' 0 ', ' True ', ' False'], ['What is the result of round(0.5) – round(-0.5)? ', ' 2.0 ', ' 1.0 ', ' 0.0 ', ' None of the mentioned'], ['Which of these about a set is not true? ', ' Immutable data type ', ' Allows duplicate values ', ' Data type with unordered values ', ' Mutable data type'],
        ['Which of the following statements is used to create an empty set? ', ' set() ', ' { } ', ' [ ] ', ' ( )'])

file = open('Programming.txt', 'ab')


pickle.dump(ques, file)
file.close()

