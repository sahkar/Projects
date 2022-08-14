
def calculator():
    #Initialization
    expression = 0
    expression = input("Enter an expression to calculate \n")
    
    #The key word "break" to escape the while loop
    if expression == "break":
        print('Goodbye')
        quit()

    #More initialization
    nums = expression
    operations = []

    #Finiding the operation symbols in our expression and appending them to the operations list
    for a in expression:
        if a in ['+','-','*','/','^']:
            operations.append(a)   
    
    #Replacing the operation commands in nums to commas making it easy to convert to a list
    for o in['+','-','*','/','^']:
        nums = nums.replace(o,",")
    
    #Change nums from a string to a list by splitting on the commas
    nums = nums.split(',')
    
    #Setting total to the the first number nums. This will make it easy to update in the future
    total = int(nums[0])

    #Converting all numbers in nums to type int.
    for num in range(0,len(nums)):
        nums[num] = int(nums[num])

    #Loop to set num1 and num2 and update our total variable
    for i in range(1,len(nums)):
        num1 = total
        num2 = nums[i]
        op = operations[i-1]
        #Operation commands
        if op == "+":
            total = num1+num2
        elif op == "-":
            total = num1-num2
        elif op == "*":
            total = num1*num2
        elif op == "/":
            total = num1/num2
        elif op == "^":
            total = num1**num2
    return total

#While loop that allows us to keep entering new commands. To break the while loop, type "break"
while True:
    print(calculator())    

                



