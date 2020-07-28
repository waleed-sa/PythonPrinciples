# file manipulation and exception handling: try, except, and else


# Win path: c:\Users\(username)\Desktop\python ch8\people.txt

class Filer():
    

    def OpenFile(self):
        with open('system_config.txt') as file_object:
            contents = file_object.read()
            print(contents)

    #open file function with argument
    def openFile2(self, file):
        try:
            with open(file) as file_object:
                contents = file_object.read()
                print(contents)
        except FileNotFoundError:
                print("\nERROR: We had trouble reading the file.")
        else:
                print("\nWe were able to access the file. Cool!")
    
myFiler = Filer()
myFiler.openFile2('/Users/Desktop/people.txt')
