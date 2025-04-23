''' Can be using to recognize the other files on the same(script what we ran) or specific directory/location...
# Script Location  # how to fined the files location

- os.path.dirname(os.path.abspath(__file__)) : Get the directory where the Python script is located.
- __file__ : Represents the relative path of the currently executing script. Use it with os.path functions to get the script's location.
- os.listdir(os.path.dirname(os.path.abspath(__file__))) : to make the list of the other iteams on the same directory. '''


from os import *    # or import os

   # find script location
fname = "1. _OS_library_in_py_.py"  # or use __file__ for use the script lopcation whare we ran
slocation = path.dirname(path.abspath(__file__))  # find script location
print(slocation)

   # make a list of the other files/folders on the same directory
iteamlist = listdir(slocation)
print(iteamlist)


 # Just for knowing
# give the main terminal path - just for knowing
jknow = path.dirname(path.abspath(fname))
print()
print(jknow)
