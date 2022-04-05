import os
from time import sleep

#Calculator class
class Calculator:
    #Variable declaration
    input1 = input2 = 0

    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    #Addition function
    def adder(self):
        return self.input1 + self.input2

    #Subtract function
    def subtractor(self):
        return self.input1 - self.input2

    #Multiply function
    def multiplier(self):
        return self.input1 * self.input2

    #Dividing function
    def divider(self):
        return self.input1 / self.input2

    #Set values to 0
    def clear(self):
        self.input1 = 0
        self.input2 = 0

#ClockTime class
class ClockTime:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        
    def setHours(self):
        return self.hours
    
    def setMinutes(self):
        return self.minutes
        
    def setSeconds(self):
        return self.seconds
        
    def setTime(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds 
        
    def showTime(self):
        print("%d:%02d:%02d" %(self.hours, self.minutes, self.seconds))

def tutQuestion01():
    """Week11 Tutorial Question 01"""


    #Instantiate Calculator object
    cal = Calculator(0, 0)

    #Lock in loop till valid input
    while True:
        clearConsole()
        print("\nQuestion 01:\n")

        print("Value01: " + str(cal.input1))
        print("Value02: " + str(cal.input2))
        print("\n[Opt]---[Action]-----------------")

        print("[0]\tChange Value01")
        print("[1]\tChange Value02")
        print("[2]\tExecute Addition")
        print("[3]\tExecute Subtraction")
        print("[4]\tExecute Multiplication")
        print("[5]\tExecute Divide")
        print("[6]\tClear values")
        print("[7]\tExit")

        #Acquire operation selection
        userInput = input("Select operation [Opt]: ")

        #User input validation
        if userInput.isnumeric():
            userInputInt = int(userInput)
        
            #Process action
            match userInputInt:
                #Change Input01
                case 0:
                    userInput = input("Value01: ")
                    #Acquire user input for Value01
                    try:
                        userInputInt = int(userInput)
                        cal.input1 = userInputInt
                    #User input is not in numeric form
                    except ValueError:
                        print("Invalid numeric input")
                        enterToCont()
                #Change Input02
                case 1:
                    userInput = input("Value02: ")
                    #Acquire user input for Value01
                    try:
                        userInputInt = int(userInput)
                        cal.input2 = userInputInt
                    #User input is not in numeric form
                    except ValueError:
                        print("Invalid numeric input")
                        enterToCont()
                #Execute addition
                case 2:
                    userInputInt = cal.adder()
                    print("\nAdd: " + str(userInputInt))
                    enterToCont()
                #Execute subtraction
                case 3:
                    userInputInt = cal.subtractor()
                    print("\nSubtract: " + str(userInputInt))
                    enterToCont()
                #Execute multiply
                case 4:
                    userInputInt = cal.multiplier()
                    print("\nMultiply: " + str(userInputInt))
                    enterToCont()
                #Execute divide
                case 5:
                    userInputInt = cal.divider()
                    print("\nDivide: " + str(userInputInt))
                    enterToCont()
                #Clear values
                case 6:
                    cal.input1 = 0
                    cal.input2 = 0
                    print("\nValues cleared.")
                    enterToCont()
                #Exit question
                case 7:
                    return
                #Default case
                case _:
                    print("Invalid input...")
                    enterToCont()
        else:
            print("Invalid input...")
            enterToCont()

def tutQuestion02():
    """Week11 Tutorial Question 02"""
    print("\nQuestion 02:\n")

    #Get input for hours
    getHours = int(input("Enter the number of hours: "))

    #Get input for minutes
    getMinutes = int(input("Enter the number of minutes: "))

    #Get input for seconds
    getSeconds = int(input("Enter the number of seconds: "))

    #Create ClockTime object with values
    time = ClockTime(getHours, getMinutes, getSeconds)
    time.showTime()

#Helper Function - Clear console
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
#Helper Function - Allow user to acknowledge UI
def enterToCont():
    input("\nPress enter to continue...")

def run():
    """Week 11 Tutorial Questions"""
    tutQuestion01()
    tutQuestion02()

if __name__ == "__main__":
    run()