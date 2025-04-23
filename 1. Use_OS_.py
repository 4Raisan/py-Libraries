''' Can be using to recognize the other files on the same(script what we ran) or specific directory/location...
# Script Location  # how to fined the files location

- os.path.dirname(os.path.abspath(__file__)) : Get the directory where the Python script is located.
- __file__ : Represents the relative path of the currently executing script. Use it with os.path functions to get the script's location.
- os.listdir(os.path.dirname(os.path.abspath(__file__))) : to make the list of the other iteams on the same directory. '''
