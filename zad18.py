import itertools
import time
start_time = time.time()
danewejsciowe = input()
dane = danewejsciowe.split()
listadane = []
listadane = dane
n = int(dane[0])
n = n + 1
x = int(dane[1])
y = int(dane[2])

lista = []
for i in range(n):
    a = lista.append(i)

ilkart = list(itertools.product(lista, repeat=4))
#print(ilkart)

result = 0
for i in range(len(ilkart)):
   if (x*(ilkart[i][0]*ilkart[i][0]) + y*(ilkart[i][1]*ilkart[i][1]) - x*(ilkart[i][2]*ilkart[i][2]) - y*(ilkart[i][3]*ilkart[i][3])) == 0:
       result += 1
print(result)









#print(lista)
#def iloczynkartezjanski(xlisty):
#result = [[]]
#for xlist in lista, lista, lista:
 # result = [j+[k] for j in result for k in xlist]
  #print(result)

#listy = lista, lista, lista, lista
#ilkart = iloczynkartezjanski(listy)
#ilosc = pow(4, n-1)
#print(ilosc)
#result = 0
#ilkart = []
#for i in range(ilosc):
   # ilkart = list(itertools.product(lista, repeat=4))
  #  print(ilkart)
  #  if (x * (ilkart[i][0] * ilkart[i][0]) + y * (ilkart[i][1] * ilkart[i][1]) - x * (ilkart[i][2] * ilkart[i][2]) - y * (ilkart[i][3] * ilkart[i][3])) == 0:
       # result += 1
#result = 0
#for i in range(len(ilkart)):
   #if (x*(ilkart[i][0]*ilkart[i][0]) + y*(ilkart[i][1]*ilkart[i][1]) - x*(ilkart[i][2]*ilkart[i][2]) - y*(ilkart[i][3]*ilkart[i][3])) == 0:
     #  result += 1
#print(result)

print( (time.time() - start_time))