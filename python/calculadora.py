def suma(a , b):
    '''
    try:
        return a + b
    except TypeError:
        print("one or both of arguments is not a float or integer type variable")
        return 0.0
    '''
    return a + b


def resta(a , b):
    '''
    try:
        return a - b
    except TypeError:
        print("one or both of arguments is not a float or integer type variable")
        return 0.0
    '''
    return a - b


def multiplicacion(a , b):
    '''
    try:
        return a * b
    except TypeError:
        print("one or both of arguments is not a float or integer type variable")
        return 0.0
    '''
    return a * b


def division(a ,b ):
    '''
    try:
        if b == 0:
            print("error: división entre 0. regresando valor 0 (cero)")
            return 0
        else:
            return a / b
    except TypeError:
        print("one or both of arguments is not a float or integer type variable")
        return 0.0
    '''
    if b == 0:
        print("error: división entre 0. regresando valor 0 (cero)")
        return 0
    else:
        return a / b

def potencia(a , b):
    '''
    try:
        return a ** b
    except TypeError:
        print("one or both of arguments is not a float or integer type variable")
        return 0.0
    '''
    return a ** (b)

def raiz(a , b):
    '''
    try:
        return a ** (1/b)
    except TypeError:
        print("one or both of arguments is not a float or integer type variable")
        return 0.0
    '''
    return a ** (1 / b)


