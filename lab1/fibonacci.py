def fibonacci_iteration(x):
    if(isinstance(x, bool)):
        raise Exception("Should be given an integer greater then 0, not a bool")
    if (not isinstance(x, int)) or x < 1:
        raise Exception("Should be given an integer greater then 0")
   
    if x == 1:
        return 1
    elif x == 2:
        return 1
    
    currentNumber = 2
    previousNumber = 1
    howManyNumbers = 3

    while howManyNumbers < x:
        newNumber = currentNumber + previousNumber
        previousNumber = currentNumber
        currentNumber = newNumber
        howManyNumbers += 1

    return currentNumber

def fibonacci_recursion(x):
    if(isinstance(x, bool)):
        raise Exception("Should be given an integer greater then 0, not a bool")
    if (not isinstance(x, int)) or x < 1:
        raise Exception("Should be given an integer greater then 0")
    return fiboncacci_recursion_without_check(x)

def fiboncacci_recursion_without_check(x):
    if x <= 1:  
        return x 
    else:  
        return(fiboncacci_recursion_without_check(x-1) + fiboncacci_recursion_without_check(x-2)) 