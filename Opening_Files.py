# file manipulation

'''with open('system_config.txt') as file_object:
        contents = file_object.read()
        print(contents)'''

#open file function hard code file name
def OpenFile():
    with open('system_config.txt') as file_object:
        contents = file_object.read()
        print(contents)

#open file function with argument
def openFile2(file):
    with open(file) as file_object:
        contents = file_object.read()
        print(contents)

openFile('system_config.txt')        

    

    
