class MyDoctor:
    '''-> MyDoctor class docstring ... tell programmers about your class.'''

    
    def sayHi(self):
        print("Hi!")
        
    def sayBye(self):
        '''sayBye() docstring ...'''
        print("Bye!")
    
    def askDocQuestion(self):
        question = input("Do you want a health tip? Yes or no: ")
        if question == "yes" or question == "Yes":
            print("Good! Eat less sugar.")
        else:
            print("Ok, see you next time!")

myDoctor = MyDoctor()

print(myDoctor.__doc__)
print(myDoctor.sayBye.__doc__)

myDoctor.sayHi()
myDoctor.askDocQuestion()
myDoctor.sayBye()

            
        
    

    
