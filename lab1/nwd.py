def nwd_iteration(x, y):
    if(isinstance(x, bool) or isinstance(y, bool)):
        raise Exception("Should be given an integer greater then 0, not a bool")
    if ((not isinstance(x, int)) or x < 1) or ((not isinstance(y, int)) or y < 1):
        raise Exception("Should be given an integer greater then 0")
    resztaZDzielenia = -1
    while( resztaZDzielenia != 0):
        resztaZDzielenia = x % y
        if(resztaZDzielenia == 0):
            return x / y
        else:
            x = y
            y = resztaZDzielenia

def nwd_recursive(x, y):
    if(isinstance(x, bool) or isinstance(y, bool)):
        raise Exception("Should be given an integer greater then 0, not a bool")
    if ((not isinstance(x, int)) or x < 1) or ((not isinstance(y, int)) or y < 1):
        raise Exception("Should be given an integer greater then 0")
    return nwd_recursive_without_check(x, y)

def nwd_recursive_without_check(x, y):
    resztaZDzielenia = x % y
    if(resztaZDzielenia == 0):
        return x / y
    else:
        return nwd_recursive_without_check(y, resztaZDzielenia)