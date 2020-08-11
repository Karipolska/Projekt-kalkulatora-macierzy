import numpy as np

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



print( "Witaj w programie 'Kalkulator macierzowy'.\n \nDostępne operacje: \n-dodawanie, \n-odejmowanie, \n-mnożenie, \n"
      "-potęgowanie, \n-wyprowadzanie postaci Jordana, \n-odwracanie macierzy, \n-czyszczenie pamięci,"
      " \n-odczytanie poprzedniego działania.\n" )

chooseAction()
