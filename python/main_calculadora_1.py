import calculadora
'''
# print(dir())
print(calculadora.suma(1,2))

print(calculadora.resta(1,2))
print("\n\n")
# otra forma de utilizar nuestras funciones
suma = calculadora.suma
resta = calculadora.resta

print(suma(1,2))
print(resta(1,2))

'''
if __name__ == "__main__":
    import sys
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    print(calculadora.suma(a,b))
    print(calculadora.resta(a,b))
