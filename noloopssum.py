dane = input()
list = dane.split()
def funkcja(x):
    if len(x)==0:
        return 0
    else:
        return int(x[0])+int(funkcja(x[1: :]))
wynik = funkcja(list)
print(wynik)