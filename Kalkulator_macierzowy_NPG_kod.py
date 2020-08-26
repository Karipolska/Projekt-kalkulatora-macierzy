import numpy as np

#funkcja sprawdzająca czy macierze są takie same (do dodawania i odejmowania)
def sameSize(matrix_a, matrix_b):
    if matrix_a.shape == matrix_b.shape:
        return True
    else:
        print("Macierze mają różne wymiary, nie można przeprowadzić wybranej operacji")
        return False

#funkcja sprawdzająca czy macierze mają odpowiednie wymiary do przeprowadzenia operacji mnożenia
def canMultiply(matrix_a, matrix_b):
    (w, r) = matrix_a.shape
    (s, t) = matrix_b.shape

    if r == s:
        return True
    else:
        print("Macierze mają nieodpowiednie rozmiary do przeprowadzenia operacji mnożenia")
        return False

#funkcja sprawdzania czy macierz jest kwadratowa 
#funkcja zwraca parametr True, gdy przekazana do niej macierz jest kwadratowa, w przeciwnym wypadku wyświetla komunikat o błędzie i zwraca parametr False)
def isSquare(matrix):
    (w,r) = matrix.shape
    if w == r:
        return True
    else:
        print("Macierz nie jest kwadratowa, wykonanie działania jest niemożliwe.")
        return False
    
#funkcja wyboru sposobu wprowadzenia macierzy
def choiceMatrix():
    c=int(input("Aby wprowadzic macierz z klawiatury wybierz 1, aby wczytac z pliku wybierz 2"))
    if c==1:
        enterMatrix()
    elif c==2:
        loadFile()
    else:
        print("Nie wybrałeś poprawnego numeru operacji")
        return False
    
#funkcja wczytywania macierzy z pliku
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
            M = np.vstack([M, a]) #czy napewno vstack?
    file.close()
    return M


#funkcja wprowadzania macierzy
def enterMatrix():

    w = int(input("Podaj liczbę wierszy macierzy: "))
    r = int(input("Podaj liczbę kolumn macierzy: "))

    list = []
    for i in range (r):
        print("Podaj liczbę w 1 wierszu")
        x = int(input())
        list.append(x)
    M = np.array([list])

    for i in range (2, w+1):
        list = []
        for j in range (r):
            print("Podaj liczbę w", i, "wierszu")
            x = int(input())
            list.append(x)
        M = np.vstack([M, list])
        return M

#funkcje wykonujące działania - uzupełnić!!!
def addition(matrix_a, matrix_b):
    if sameSize(matrix_a, matrix_b):
        return np.add(matrix_a, matrix_b)
    return None


def subtraction(matrix_a, matrix_b):
    if sameSize(matrix_a, matrix_b):
        return np.subtract(matrix_a, matrix_b)
    return None


def multiplication():
    # Wywołanie funkcji wyboru sposobu wprowadzania macierzy i wprowadzenie macierzy M oraz M2
    if canMultiply(M, M2):
        return M.dot(M2)


def exponentiation():
    matrix = choiceMatrix()
    if isSquare(matrix) == True:
        p = int(input("Podaj potęgę: "))
        W = matrix
        for i in range(p - 1):
            W = W.dot(matrix)
        print (W)

def jordanForm():
    pass


def inversion():
    pass


def clearMemory():
    pass


def seePrevious():
    pass


#funkcja wyboru operacji
def chooseAction():
    action = input( "Podaj działanie na macierzach, które chcesz wykonać "
                   "\n(wpisz taką nazwę działania jaka znajduje się na liście dostępnych operacji):" )

    def switch(action):

        switcher = {
            "dodawanie": addition(),
            "odejmowanie": subtraction(),
            "mnożenie": multiplication(),
            "potęgowanie": exponentiation(),
            "wyprowadzanie postaci Jordana": jordanForm(),
            "odwracanie macierzy": inversion(),
            "czyszczenie pamięci": clearMemory(),
            "odczytanie poprzedniego działania": seePrevious(),
        }
        return switcher.get(action,"Wprowadzono niepoprawną nazwę działania!")

    switch(action)



print( "Witaj w programie 'Kalkulator macierzowy'.\n")



print("Dostępne operacje: \n-dodawanie, \n-odejmowanie, \n-mnożenie, \n"
      "-potęgowanie, \n-wyprowadzanie postaci Jordana, \n-odwracanie macierzy, \n-czyszczenie pamięci,"
      " \n-odczytanie poprzedniego działania.\n" )

chooseAction()
