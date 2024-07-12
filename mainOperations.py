
import valueOperations as vo
import arithmaticOperations as ao





# this function gives you choices if you want any calculation with your numbers
def mainFunction(n1):
    print("Want some calculation? Here is your choices")
    print('Select "+" for addition')
    print('Select "-" for subtraction')
    print('Select "*" for multiply')
    print('Select "/" for division')
    print('Select "%" for percent')
    print('Select "q" for quit/getting the value of your input')

    userChoiceOperator = input("Enter your choice for calculation : ")

    if(userChoiceOperator in "+-*/"):
        n2 = vo.takeInput()
        if(userChoiceOperator == '+'):
            print("Answer =",ao.add(n1, n2))
            backToMainFunction(ao.add(n1, n2))
            
        elif(userChoiceOperator == '-'):
            print("Answer =",ao.sub(n1, n2))
            backToMainFunction(ao.sub(n1, n2))
            
        elif(userChoiceOperator == '*'):
            print("Answer =",ao.mul(n1, n2))
            backToMainFunction(ao.mul(n1, n2))
            
        elif(userChoiceOperator == '/'):
            print("Answer =",ao.div(n1, n2))
            backToMainFunction(ao.div(n1, n2))

    elif(userChoiceOperator == '%'):
        print("Answer =",ao.percent(n1))
        backToMainFunction(ao.percent(n1))
        
    elif(userChoiceOperator.lower() == 'q'):
        newCalc = input("Do you want to start new calculation?(y/n) ")
        if(newCalc == 'y'):
            n1 = vo.takeInput()
            mainFunction(n1)
                
        elif(newCalc == 'n'):        
            n1 = n1
            print("Your final output is : ", n1)
            print("Thank you for trying out our calculator")
        
    else:
        print("WARNING!!!! You are choosing wrong operator")
        mainFunction(n1)
    




# this function allows you to go back to the main function to do another 
# calculation or you can leave with your final answer
def backToMainFunction(n1):
        backToMain = input("Do you want another Calculation with this?(y/n) ")
        
        if(backToMain.lower() == 'y'):
            mainFunction(n1)
                
        elif(backToMain.lower() == 'n'):
            newCalc = input("Do you want to start new calculation?(y/n) ")
            if(newCalc == 'y'):
                n1 = vo.takeInput()
                mainFunction(n1)
                
            elif(newCalc == 'n'):
                print("Your final output is : ", n1)
                print("Thank you for trying out our calculator")
            
            else:
                print("Wrong input!!!")
                return backToMainFunction(n1)
        
        else:
            print("Wrong input!!!")
            return backToMainFunction(n1)