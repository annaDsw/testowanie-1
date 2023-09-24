def silnia_iteration(x):
    if(isinstance(x, bool)):
        raise Exception("Should be given an integer greater then 0, not a bool")
    if (not isinstance(x, int)) or x < 0:
        raise Exception("Should be given an integer greater then 0")
    if (x == 0):
        return 1
    result = 1
    currentNumber = 1
    while(currentNumber <= x):
        result *= currentNumber
        currentNumber += 1
    return result

def silnia_recursive(x):
    if(isinstance(x, bool)):
        raise Exception("Should be given an integer greater then 0, not a bool")
    if (not isinstance(x, int)) or x < 0:
        raise Exception("Should be given an integer greater then 0")
    return silnia_recursive_without_check(x)

def silnia_recursive_without_check(x):
    if x == 0:
        return 1
    else:
        return x * silnia_recursive_without_check(x - 1)

