from math.utils import *

def main():
    """
    main() -> None
    """
    myVariable = complex()
    print(myVariable)

    sumatoria(3)
    print(calVolumenParalelepipedo(2, 3, 10))
    print(sumatoria(3))
    print(sumatoriaLambda(3))

    return None

sumatoriaLambda = lambda x: (x * (x + 1)) / 2


# print(resultado)



def count_substring(string, sub_string):
    """
    Cuenta cuantas veces aparece el sub_string
    en el string
    Args:
        string: (string)
        sub_string: (string)
    rerturn : int
    """
    
    return string.count(sub_string)



if __name__ == "__main__":
    main()
    string = "Hola Codo a Codo"  # input().strip()
    sub_string = "codo"  # input().strip()
    count = count_substring(string, sub_string)
    print(count)

    str = "este es un string que tiene varias coincidencias de strings con el sub-str"
    sub_str = "string"

    print("La palabra [", sub_str, "] aparece ", count_substring(str, sub_str), " veces")

 
    