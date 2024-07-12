import math
import mainOperations as mo
import arithmaticOperations as ao

# this function allows you to take your desired inputs
def takeInput():
    print('Select "1" to take simple value')
    print('Select "2" to take intermediate value')
    print('Select "3" to take trigonometric value')

    try:
        userInput = int(input("Enter your choice : "))
    except ValueError:
        print("Hey you are giving wrong input!!!!")
        return takeInput()

    if(userInput == 1):
        return getSimpleValue()
            
    elif(userInput == 2):
        return getIntermediateValue()
    
    elif(userInput == 3):
        return getTrigonometricValue()
    
    else:
        print("Hey you are giving wrong input!!!!")
        return takeInput()

# this function allows you to take simple inputs like int, float or pi values     
def getSimpleValue():
        print('Select "1" to take integer value')
        print('Select "2" to take float value')
        print('Select "3" to take pi value')
        
        try:
            userValueChoice = int(input("Enter your choice : "))
        except ValueError:
            print('Only choose from the options are given below')
            print("TRY AGAIN!!!!")
            return getSimpleValue()
        
        if(userValueChoice == 1):
            try:
                intVal = int(input("Enter your number : "))
                print("Answer =", intVal)
                return intVal
            except ValueError:
                print("Hey! You have selected integer value")
                return getSimpleValue()
            
        elif(userValueChoice == 2):
            try:
                floatVal = float(input("Enter your number : "))
                print("Answer =", floatVal)
                return floatVal
            except ValueError:
                print("Hey! You have selected float value")
                return getSimpleValue()
        
        elif(userValueChoice == 3):
            print("Answer =", math.pi)
            return math.pi
        
        else:
            print('Only choose from the options are given below')
            print("TRY AGAIN!!!!")
            return getSimpleValue()



# this function allows you to take intermediate inputs like 
# taking the power of a value
# taking the factorial of a value
# taking the logarithm value(with or without base)
# taking the square root value
def getIntermediateValue():
    print('Select "1" to get the power value')
    print('Select "2" to get the factorial value')
    print('Select "3" to get the logarithm value')
    print('Select "4" to get the square root value')
    
    try:
        userValueChoice = int(input("Enter your choice : "))
    except ValueError:
        print('Only choose from the options are given below')
        print("TRY AGAIN!!!!")
        return getIntermediateValue()
    
    if(userValueChoice == 1):
        try:
            base = valueChoiceFunc()
            power = int(input("Enter the power : "))
            print("Answer =",math.pow(base, power))
            return math.pow(base, power)
        except ValueError:
            print("Hey, select the right value !!")
            return getIntermediateValue()
    
    elif(userValueChoice == 2):
        try:
            num = int(input("Enter the number : "))
            print("Answer =",math.factorial(num))
            return math.factorial(num)
        except ValueError:
            print("Hey! you have selected integer value")
            return getIntermediateValue()
    
    elif(userValueChoice == 3):
        try:
            num = float(input("Enter the number : "))
        except ValueError:
                print("Hey, select the right value !!")
                return getIntermediateValue()
            
        userChoice = input("Do you want to add base of logarithm value?(y/n) ")        
        if(userChoice.lower() == 'y'):
            try:
                base = float(input("Enter the base : "))
                print("Answer =",math.log(num, base))
                return math.log(num, base)
            except ValueError:
                print("Hey, select the right value !!")
                return getIntermediateValue()
        
        elif(userChoice.lower() == 'n'):
            print("Answer =",math.log(num))
            return math.log(num)
        
    elif(userValueChoice == 4):
        try:
            num = float(input("Enter the number : "))
            print("Answer =", math.sqrt(num))
            return math.sqrt(num)
        except ValueError:
            print("Hey, select the right value !!")
            return getIntermediateValue()
    
    else:
        print('Only choose from the options are given below')
        print("TRY AGAIN!!!!")
        return getIntermediateValue()
    
    
    

# this function allows you to take trigonometric values such as
# the sine, cosine and tangent values
# also allows you to take the arc vales(sin,cos or tan)        
def getTrigonometricValue():
    print('Select "sin" for sine operation')
    print('Select "cos" for cosine operation')
    print('Select "tan" for tangent operation')
    print('Select "asin" for arc sine operation')
    print('Select "acos" for arc cosine operation')
    print('Select "atan" for arc tangent operation')
    
    try:
        userChoiceOption = input("Enter your choice : ")
    except ValueError:
        print('Only choose from the options are given below')
        print("TRY AGAIN!!!!")
        return getTrigonometricValue()
    
    if(userChoiceOption == 'sin'):
        val = valueChoiceFunc()
        val = trigoExtraCalc(val)
        print("Answer =", math.sin(val))
        return math.sin(val)
    
    elif(userChoiceOption == 'cos'):
        val = valueChoiceFunc()
        val = trigoExtraCalc(val)
        print("Answer =", math.cos(val))
        return math.cos(val)
    
    elif(userChoiceOption == 'tan'):
        val = valueChoiceFunc()
        val = trigoExtraCalc(val)
        print("Answer =", math.tan(val))
        return math.tan(val)
    
    elif(userChoiceOption in 'asinacosatan'):
        return arcValue(userChoiceOption)
    
    else:
        print('Only choose from the options are given below')
        print("TRY AGAIN!!!!")
        return getTrigonometricValue()





# this function gives you the calculation of arc values(sin,cos or tan)
def arcValue(userChoiceOption):
        try:
            val = float(input("Enter value : "))
            if(val>1 or val<-1):
                print("Error: The value is between -1 and 1")
                return arcValue(userChoiceOption)
            
            else:
                if(userChoiceOption == 'asin'):
                    print("Answer =", math.asin(val))
                    return math.asin(val)
                
                elif(userChoiceOption == 'acos'):
                    print("Answer =", math.acos(val))
                    return math.acos(val)
            
                elif(userChoiceOption == 'atan'):
                    print("Answer =", math.atan(val))
                    return math.atan(val)
                
        except ValueError:
                print("Hey, select the right value !!")
                return arcValue(userChoiceOption)



            
# this function gives to choices to make your calcution progress continue or
# to go to the main function             
def calcAgain(n1):
        calcAgainInput = input("Do you want to go through your calculation?(y/n) ")
    
        if(calcAgainInput.lower() == 'y'):
            mo.mainFunction(n1)
            
        elif(calcAgainInput.lower() == 'n'):
            mo.backToMainFunction(n1)
            
        else:
            print("Oops, You have given wrong input. Try again")
            calcAgain(n1)    





# this function helps you to do any modification with your trigonometric value
def valueUpdateFunc(n1):
    print('Select "+" for addition')
    print('Select "-" for subtraction')
    print('Select "*" for multiply')
    print('Select "/" for division')
    print('Select "%" for percent')
    print('Select "q" for no further progress')

    userChoiceOperator = input("Enter your choice for calculation : ")

    if(userChoiceOperator in "+-*/"):
        n2 = takeInput()
        if(userChoiceOperator == '+'):
            print("After calculation =",ao.add(n1, n2))
            return loopingValueUpdate(ao.add(n1, n2))
            
        elif(userChoiceOperator == '-'):
            print("After calculation =",ao.sub(n1, n2))
            return loopingValueUpdate(ao.sub(n1, n2))
            
        elif(userChoiceOperator == '*'):
            print("After calculation =",ao.mul(n1, n2))
            return loopingValueUpdate(ao.mul(n1, n2))
            
        elif(userChoiceOperator == '/'):
            print("After calculation =",ao.div(n1, n2))
            return loopingValueUpdate(ao.div(n1, n2))

    elif(userChoiceOperator == '%'):
        print("After calculation =",ao.percent(n1))
        return loopingValueUpdate(ao.percent(n1))
        
    elif(userChoiceOperator.lower() == 'q'):
        n1 = n1
        return n1
        
    else:
        print("WARNING!!!! You are choosing wrong operator")
        valueUpdateFunc(n1)





# this function helps you to do the trigonometric function again and again        
def loopingValueUpdate(n1):
    backToMain = input("Do you want another Calculation with this?(y/n) ")
        
    if(backToMain.lower() == 'y'):
        valueUpdateFunc(n1)
        
    elif(backToMain.lower() == 'n'):
        return n1





# if you wanna go through you trigonometric calculation this function will
# help you to go for another calculation    
def trigoExtraCalc(n1):
    trigoValUpdate = input("Do you want any update in the value?(y/n) ")
    if(trigoValUpdate == 'y'):
        print('What type of update you want to do')
        print('Select "1" for basic change')
        print('Select "2" for intermediate change')
        try:
            valUpdateChoice = int(input("Enter the choice : "))
            if(valUpdateChoice == 1):
                return valueUpdateFunc(n1)
            elif(valUpdateChoice == 2):
                return getIntermediateValue()
            else:
                print("Wrong input!!!")
                return trigoExtraCalc(n1)
        
        except ValueError:
            print("Wrong input!!!")
            return trigoExtraCalc(n1)
        
    elif(trigoValUpdate == 'n'):
        return n1




# this function will give you choice to take pi value or your desired input 
# for another calculation        
def valueChoiceFunc():
    print('Select "pi" for pi value')
    print('Select "n" for your value')
    userValChoice = input("What type of value you are choosing? ")
    
    if(userValChoice == 'pi'):
        print("Answer =", math.pi)
        return math.pi
    
    elif(userValChoice == 'n'):
        try:
            number = float(input("Enter value : "))
            print("Answer =", number)
            return number
        except ValueError:
            print("Wrong input!!!")
            return valueChoiceFunc()
            
    else:
        print('Only choose from the options are given below')
        print("TRY AGAIN!!!!")
        return valueChoiceFunc()