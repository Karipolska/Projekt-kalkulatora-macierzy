import numpy as np
import sys
from sympy import Matrix


memory = [0 for i in range(10)]
index = 0


# funkcja zapisująca macierze wynikowe do listy
def saveResult(matrix):
    global index
    global memory
    memory[index] = matrix
    index += 1
    if index >= 10:
        index = 0


# funkcja sprawdzająca czy macierze są takie same (do dodawania i odejmowania)
def sameSize(matrix_a, matrix_b):
    if matrix_a.shape == matrix_b.shape:
        return True
    print("Macierze mają różne wymiary, nie można przeprowadzić wybranej operacji")
    return False


# funkcja sprawdzająca czy macierze mają odpowiednie wymiary do przeprowadzenia operacji mnożenia
def canMultiply(matrix_a, matrix_b):
    (w, r) = matrix_a.shape
    (s, t) = matrix_b.shape

    if r == s:
        return True
    print("Macierze mają nieodpowiednie rozmiary do przeprowadzenia operacji mnożenia")
    return False


# funkcja sprawdzania czy macierz jest kwadratowa
# funkcja zwraca parametr True, gdy przekazana do niej macierz jest kwadratowa, w przeciwnym wypadku wyświetla komunikat o błędzie i zwraca parametr False)
def isSquare(matrix):
    if matrix.shape[0] == matrix.shape[1]:
        return True
    print("Macierz nie jest kwadratowa, wykonanie działania jest niemożliwe.")
    return False


# funkcja wyboru sposobu wprowadzenia macierzy
def choiceMatrix():
    c = input("Wybierz sposób wprowadzania macierzy:\n"
              "[1] z klawiatury\n"
              "[2] z pliku\n"
              "[3] użycie macierzy wynikowej z historii działań\n")
    if c == '1':
        return enterMatrix()
    elif c == '2':
        return loadFile()
    elif c == '3':
        return loadPrevious()
    else:
        print("Wprowadzono nieprawidłowy numer operacji")
        choiceMatrix()


# funkcja wczytywania macierzy z pliku
def loadFile():
    print("Aby macierz została prawidłowo załadowana kolejne liczby w wierszu powinny być oddzielone"
          " spacją, a wiersze przejściem do nowej linii")
    counter = 0
    name = str(input("Podaj ścieżkę pliku: "))
    try:
        file = open(name)
    except FileNotFoundError:
        print("Plik pod ścieżką {} nie istnieje".format(name))
        return None

    for line in file:
        if counter == 0:
            a = line.split()
            M = np.array([a])
            counter += 1
        else:
            a = line.split()
            M = np.vstack([M, a])
    file.close()
    return M


# funkcja wprowadzania macierzy
def enterMatrix():
    w = int(input("Podaj liczbę wierszy macierzy: "))
    r = int(input("Podaj liczbę kolumn macierzy: "))

    list = []
    for i in range(r):
        print("Podaj", i + 1, "liczbę w 1 wierszu")
        x = int(input())
        list.append(x)
    M = np.array([list])

    for i in range(2, w + 1):
        list = []
        for j in range(r):
            print("Podaj", j + 1, "liczbę w", i, "wierszu")
            x = int(input())
            list.append(x)
        M = np.vstack([M, list])
    return M


#funkcja wprowadzająca macierz będącą wynikiem jednego z poprzednich działań
def loadPrevious():
    x = int(input("Wynik którego z działań chcesz użyć: "))
    x -= 1
    try:
        if (memory[x] != 0).any():
            print("\n")
            return memory[x]
    except AttributeError:
        print("Brak zapisanego wyniku")


# funkcje wykonujące działania
def addition():
    matrix_a = choiceMatrix()
    matrix_b = choiceMatrix()
    if sameSize(matrix_a, matrix_b):
        M = np.add(matrix_a, matrix_b)
        print("Suma macierzy wynosi:\n", M)
        saveResult(M)
    return None


def subtraction():
    matrix_a = choiceMatrix()
    matrix_b = choiceMatrix()

    if sameSize(matrix_a, matrix_b):
        M = np.subtract(matrix_a, matrix_b)
        print('Różnica macierzy wynosi:\n', M)
        saveResult(M)
    return None


def multiplication():
    M = choiceMatrix()
    M2 = choiceMatrix()
    if canMultiply(M, M2):
        M = M.dot(M2)
        print("Wynik mnożenia wynosi:\n", M)
        saveResult(M)


def exponentiation():
    matrix = choiceMatrix()
    if isSquare(matrix):
        p = int(input("Podaj potęgę: "))
        W = matrix
        for i in range(p - 1):
            W = W.dot(matrix)
        print("Wynik potęgowania wynosi:\n", W)
        saveResult(W)


def jordanForm():
    M = choiceMatrix()
    if isSquare(M):
        values, vectors = np.linalg.eig(M)
        print("Wartości własne podanej macierzy to: \n", values)
        print("Wektory własne podanej macierzy to: vectors", vectors)
        M1 = Matrix(M)
        _, J = M1.jordan_form()
        print("Macierz Jordana podanej macierzy to: ", J)
        saveResult(J)


def inversion():
    matrix = choiceMatrix()
    if isSquare(matrix):
        if np.linalg.det(matrix) != 0:
            P = matrix
            P = np.linalg.inv(matrix)
            print("Macierz odwrotna ma postać:\n", P)
            saveResult(P)
        else:
            print("Wyznacznik macierzy wynosi 0, nie można jej odwrócić")
    else:
        print("Macierz nie jest kwadratowa, nie można jej odwrócić")


def clearMemory():
    global memory
    memory = [0 for i in range(10)]


def seePrevious():
    x = int(input("Wynik którego z działań chcesz zobaczyć: "))
    x -= 1
    try:
        if (memory[x] != 0).any():
            print(memory[x])
    except AttributeError:
        print("Brak zapisanego wyniku")


# funkcja wyboru operacji
def chooseAction():
    print("Dostępne operacje: \n[1] dodawanie / add, \n[2] odejmowanie / sub, \n[3] mnożenie / mul, \n"
          "[4] potęgowanie / exp, \n[5] wyprowadzanie postaci Jordana / Jordan, \n[6] odwracanie macierzy / inv, \n"
          "[7] czyszczenie pamięci / clear, \n[8] odczytanie poprzedniego działania / history.\n")
    action = input("Podaj działanie na macierzach, które chcesz wykonać:\n")

    def default():
        action = input(
            "\nWprowadzono niepoprawną nazwę działania! Spróbuj jeszcze raz lub wpisz '0' by zakończyć program:\n")
        if action == "0":
            sys.exit("Program został zakończony.")
        else:
            switch(action)

    def switch(action):

        switcher = {
            "dodawanie": addition,
            "1": addition,
            "add": addition,
            "odejmowanie": subtraction,
            "2": subtraction,
            "sub": subtraction,
            "mnożenie": multiplication,
            "3": multiplication,
            "mul": multiplication,
            "potęgowanie": exponentiation,
            "4": exponentiation,
            "exp": exponentiation,
            "wyprowadzanie postaci Jordana": jordanForm,
            "5": jordanForm,
            "Jordan": jordanForm,
            "odwracanie macierzy": inversion,
            "6": inversion,
            "inv": inversion,
            "czyszczenie pamięci": clearMemory,
            "7": clearMemory,
            "clear": clearMemory,
            "odczytanie poprzedniego działania": seePrevious,
            "8": seePrevious,
            "history": seePrevious,
        }
        return switcher.get(action, default)()

    switch(action)
    next()

    
def next():
    w = input("Wybierz:\n"
              "[1] aby kontynuować\n"
              "[2] aby zamknąć program\n")
    if w == '1':
        chooseAction()
    if w == '2':
        sys.exit("Program został zakończony")
    else:
        print("Wybrano złą opcję")
        next()


print("Witaj w programie 'Kalkulator macierzowy'.\n")

print("Aby działanie zostało wykonane należy wprowadzić jedną z trzech opcji\n"
      "  -numer działania\n"
      "  -pełną polską nazwę z listy\n"
      "  -skrót\n")
chooseAction()
