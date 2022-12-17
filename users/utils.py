def add_binary(a, b):
    '''
    Retorna la suma de dos numeros decimales en digitos binarios.

            Parametros:
                    a (int): numero entero 
                    b (int): numero entero 

            Retorna:
                    binary_sum (str): Binario en String de la suma de a y b
    '''
    binary_sum = bin(a+b)[2:]
    return binary_sum


print(add_binary.__doc__)