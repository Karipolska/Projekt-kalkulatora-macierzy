import numpy as np


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

#funkcje wykonujące działania - uzupełnić!!!
def addition():
    pass

def subtraction():
    pass

def multiplication():
    pass

def exponentiation():
    pass

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



print( "Witaj w programie 'Kalkulator macierzowy'.\nWprowadź swoją macierz:\n")

enterMatrix()

print(\n"Dostępne operacje: \n-dodawanie, \n-odejmowanie, \n-mnożenie, \n"
      "-potęgowanie, \n-wyprowadzanie postaci Jordana, \n-odwracanie macierzy, \n-czyszczenie pamięci,"
      " \n-odczytanie poprzedniego działania.\n" )

chooseAction()
