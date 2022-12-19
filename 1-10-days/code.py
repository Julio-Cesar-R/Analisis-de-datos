import sys
import numpy as np

#!---------------------------DAY ONE----------------------------------------------------
def python_version():
    """
    Este metodo imprime la version de python que se esta utilizando
    """
    print(sys.version.split()[0])


def valid_array():
    """Este metodo muestra los arreglos validos con la funcion 'np.all()'"""
    A = np.array([[3, 2, 1, 4], [5, 2, 1, 6]])

    B = np.array([[3, 2, 1, 4], [5, 2, 0, 6]])

    C = np.array([[True, False, False], [True, True, True]])

    D = np.array([0.1, 0.3])

    for name, array in zip(list("ABCD"), [A, B, C, D]):
        print(f"{name}: {np.all(array)}")


def valid_array2():
    """Este metodo muestra los arreglos validos con la funcion 'np.all()' usando axis"""
    A = np.array([[3, 2, 1, 4], [5, 2, 1, 6]])

    B = np.array([[3, 2, 1, 4], [5, 2, 0, 6]])

    C = np.array([[True, False, False], [True, True, True]])

    for name, array in zip(list("ABC"), [A, B, C]):
        print(f"{name}: {np.all(array, axis=1)}")


def any_valid_array():
    """Valida que almenos un elemnto del array sea valido"""

    A = np.array([[0, 0, 0], [0, 0, 0]])

    B = np.array([[0, 0, 0], [0, 1, 0]])

    C = np.array([[False, False, False], [True, False, False]])

    D = np.array([[0.1, 0.0]])

    for name, array in zip(list("ABCD"), [A, B, C, D]):
        print(f"{name}: {np.any(array)}")


def all_valid_array():
    """valida cada posicion de los arreglos para verificar que sean datos validos"""
    A = np.array([[0, 0, 0], [0, 0, 0]])

    B = np.array([[0, 0, 0], [0, 1, 0]])

    C = np.array([[False, False, False], [True, False, False]])

    D = np.array([[0.1, 0.0]])

    for name, array in zip(list("ABCD"), [A, B, C, D]):
        print(f"{name}: {np.any(array, axis=0 )}")


#!-----------------------------DAY TWO-------------------------------------------------------
def array_null_parameters():
    """Busca los datos que sean nulos dentro del arreglo"""
    A = np.array([[3, 2, 1, np.nan], [5, np.nan, 1, 6]])
    print(np.isnan(A))


def arrays_equal():
    """Compara arreglos y verifica si son casi iguales o iguales"""
    A = np.array([0.4, 0.5, 0.3])
    B = np.array([0.39999999, 0.5000001, 0.3])
    print(np.allclose(A, B))


def arrays_equal2():
    """Compara arreglos y verifica si son iguales"""
    A = np.array([0.4, 0.5, 0.3])
    B = np.array([0.39999999, 0.5000001, 0.3])
    print(A == B)
    # *Another form
    print(np.equal(A, B))


#!-----------------------------DAY THREE-------------------------------------------------------


def array_greater():
    """
    Compara ambos arreglos mostrarndo cual es el numero mayor en cada uno de ellos
    El primer paramatro que se ingrese se tomara como referencia para hacer la comparacion
    """
    A = np.array([0.4, 0.5, 0.3, 0.9])
    B = np.array([0.38, 0.51, 0.3, 0.91])
    C = np.array([1.38, 1.51, 1.3, 1.91])
    print(np.greater(C, A))
    # Another form
    print(A > B)


def array_zero():
    """
    Crea un arreglo bidimencional de "0" en todas las posiciones

    """

    print(np.zeros((4, 4), dtype=int))


def arrya_full():
    """
    Esta funcion genera un arreglo con valores predeterminados
    ya sea de un solo numero o varios

    """
    # First example
    print(np.full((10, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float))
    # Second example
    print(np.full(shape=(10, 10), fill_value=255, dtype="float"))
    # Third example using "np.ones()"
    print(np.ones(shape=(10, 10), dtype="float") * 255)


# !-----------------------------DAY FOUR-------------------------------------------------------
def array_range_jumps():
    """
    Esta funcion crea un arreglo con un rango de numeros especificados
    """
    # *First example
    print(np.arange(10, 100))
    # *Second example
    print(np.arange(1, 10, 2))


def array_range_reshape():
    """
    Esta funcion modifica un diccionario unidimencional a bidimencional
    """
    # * Array
    array = np.arange(10, 100)
    # *Reshape
    new_array = array.reshape(9, 10)
    print(new_array)
    # * Another form
    print(np.arange(10, 100).reshape(-1, 10))


def array_diagonal():
    """
    Crea un arreglo de dos dimenciones con una linea diagonal
    con numeros "1"
    """
    print(np.eye(6, dtype=int))


#!-----------------------------DAY FIVE-------------------------------------------------------
def array_random_rand_seed():
    # TODO Im not for sure
    array = np.random.seed(10)
    print(np.random.rand(30))
    #!-Investigacion de funcionalidad de "seed"
    np.random.seed(20)
    print(np.random.randn(10, 4))
    #!Ejemplo avanzado
    np.random.seed(30)
    sigma = np.sqrt(5)
    mu = 100
    print(sigma * np.random.randn(10, 4) + mu)


# TODO!-----------------------------DAY SIX-------------------------------------------------------


def array_print_all():
    """
    Este metodo imprime por separado toda
    la informacion contenida en el arreglo
    """
    # * Manera tradicional
    A = np.array([[1, 4, 3], [5, 2, 6]])

    for n in A:
        for nn in n:
            print(nn)

    # * Manera con Nunmpy
    A = np.array([[1, 4, 3], [5, 2, 6]])

    for data in np.nditer(A):
        print(data)
