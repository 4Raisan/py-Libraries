# using string.printable

# from string import *
'''
string module contains; all printable ASCII characters...

.printable : all printabels
---------------------------------------------------------
.digits : '0123456789'  
---------------------------------------------------------
.ascii_letters   
.ascii_lowercase : 'abcdefghijklmnopqrstuvwxyz' 
.ascii_lowercase : 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  
---------------------------------------------------------
.punctuation : '!"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~'`  
---------------------------------------------------------
.whitespace : ' \t\n\r\x0b\x0c' (space, tab, newline, carriage return, vertical tab, form feed)  
                                (carriage return - couser comes to the begining of the line and overwrite)
'''


import string

print(string.printable)
print('---')

print((string.digits)+(string.digits))
print('---')

print('1 2\t3\n4\r5\x0b6\x0c7')
