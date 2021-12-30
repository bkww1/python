#3 punkty wspoliniowe, podejsce z nachyleniem prostych laczacych punkty A(x1,y1) B(x2,y2) C(x3,y3)
#nachylenieAB = (y2-y1)/(x2-x1)
#nachylenieBC = (y3-y2)/(x3-x2)
#nachylenieAC = (y3-y1)/(x3-x1)
#Sa wspoliniowe WTW,gdy nachylenieAB == nachylenieBC == nachylenieAC


#Wprowadzamy wspolrzedne
#in1 = input()
#A = in1.split()
#lA = []
#lA = A


#in2 = input()
#B = in2.split()
#lB = []
#lB = B


#in3 = input()
#C = in3.split()
#lC = []
#lC = C


#Obliczamy nachylenia
#nachylenieAB = (float(lB[1])-float(lA[1]))/(float(lB[0])-float(lA[0]))
#nachylenieBC = (float(lC[1])-float(lB[1]))/(float(lC[0])-float(lB[0]))
#nachylenieAC = (float(lC[1])-float(lA[1]))/(float(lC[0])-float(lA[0]))

#print(f'{nachylenieAB}, {nachylenieBC}, {nachylenieAC}')

#Pole trojkata utworzonego przez te 3 punkty musi byc rowne 0
in1 = input()
A = in1.split()
lA = []
lA = A

in2 = input()
B = in2.split()
lB = []
lB = B

in3 = input()
C = in3.split()
lC = []
lC = C

Pole = 0.5*abs(float(lA[0])*(float(lB[1])-float(lC[1]))+float(lB[0])*(float(lC[1])-float(lA[1]))+float(lC[0])*(float(lA[1])-float(lB[1])))

if Pole == 0:
    print('True')
else:
    print('False')