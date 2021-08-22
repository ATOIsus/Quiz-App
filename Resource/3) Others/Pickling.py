

import pickle

ques = (['Which of the following is the use of id() function in python? ', ' Id returns the identity of the object ',
        ' Every object doesn’t have a unique id ', ' All of the mentioned ', ' None of the mentioned'],
       ['All keywords in Python are in ', ' None of the mentioned ', ' lower case ', ' Capitalized ', ' UPPER CASE'],
       ['Which one of the following has the highest precedence in the expression? ', ' Parentheses ',
        ' Multiplication ', ' Exponential ', ' Addition'],
       ['What is the return type of function id? ', ' int ', ' bool ', ' dict ', ' float'],
       ['Which of the following data types is not supported in python ? ', ' Slice ', ' Numbers ', ' String ',
        ' List'],
       ['Which Of The Following Keywords Mark The Beginning Of The Class Definition? ', ' class ', ' return ', ' def ',
        ' All of the above'],
       ['Select the reserved keyword in python: ', ' All of the above ', ' raise ', ' import ', ' else'],
       ['The format function when applied on a string returns : ', ' str ', ' bool ', ' int ', ' list'],
       ['Which statement is correct....? ', ' List is mutable & Tuple is immutable ',
        ' List is immutable & Tuple is mutable ', ' Both are Mutable. ', ' Both are Immutable'],
       ['What is the maximum possible length of an identifier? ', ' 31 Characters ', ' 63 characters ',
        ' 79 characters ', ' 32 characters'],
       ["Which one of the following is not a python's predefined data type? ", ' Class ', ' Dictionary ', ' Tuple ',
        ' List'], ['What will be the output of 7^10 in python? ', ' 13 ', ' 15 ', ' 2 ', ' None of these'],
       ['19 % 2 in python ', ' None of these  ', ' 17 ', ' 21 ', ' 2'],
       ['Which of the following has more precedence? ', ' ()  ', ' + ', ' / ', ' –'],
       ['Which is the special symbol used in python to add comments ? ', ' "#"  ', '  "//"  ', '  "/*...*/"  ',
        '  "$" '],
       ['Which options are correct to create an empty set in python? ', ' set()  ', '  ()  ', '  []  ', '  {}'],
       ['How to create a frame in python? ', ' Frame = frame()  ', ' Frame = frame.new() ', ' Frame = new.window()   ',
        ' Frame = window.new()'],
       ['Tkinter tool in python provides the ', ' GUI ', ' OS Commands  ', ' Database  ', ' All of the above'],
       ['Numpy in the python provides the ', ' Array ', ' Lambda function  ', ' Type casting  ', ' Function'],
       ['Is list mutable ? ', ' Yes ', ' No '])

file = open('Lab.txt', 'ab')


pickle.dump(ques, file)
file.close()

