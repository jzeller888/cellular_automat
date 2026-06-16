import numpy as np 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
m1 = input("ilosc ewolucji: ")
m = int(m1)
nrf1 = input("numer funkcji: ")
nrf = int(nrf1)
status01 = input("po-czatkowy stan komorek: ")
status02 = list(status01)
status03 = []
for i in status02:
    o = int(i)
    status03.append(o)

status0 = status03


argumenty0 = []
zbior = [0,1,2]
for i in zbior:
    for j in zbior:
        for k in zbior:
            argumenty0.append((i,j,k))
argumenty = list(reversed(argumenty0))           
            
#dict0 = {i for i in argumenty : }
            
#test0 = ["".join(map(str,i)) for i in argumenty]
#test1 = [int(i) for i in test0]
            
### int -> int            
def dectotrip(dec):
    if dec == 0:
        return "0"    
    trip = ""
    while dec > 0:
        r = dec % 3  
        trip = str(r) + trip  
        dec //= 3
    wyj = trip
    return wyj


### int -> int
def triptodec(trip):
    retrip = reversed(str(trip))
    dec = 0
    p = 0
    for i in retrip:
        dec = dec + int(i)*(3**p)
        p = p + 1
    return dec        
        



class automat:
    
        def __init__(self, nrf, status):
            self.nrf = nrf
            self.status = status
            
        def defcells(self, status):
            status = self.status
            lcry = []
            for i in range(len(status)):
                if i-1 == -1:
                    c = status[i] 
                    l = status[7]
                    r = status[i+1]
                    lcry.append((l,c,r))
                elif i-1 != -1 and 1+i != 8:
                    c = status[i] 
                    l = status[i-1]
                    r = status[i+1]
                    lcry.append((l,c,r))
                elif i+1==8:
                    c = status[i] 
                    l = status[i-1]
                    r = status[0]
                    lcry.append((l,c,r))            
            return lcry
        
        def dectof(self, nrf):
            nrf = self.nrf
            nrf3 = dectotrip(nrf)
            linrf3 = list(nrf3)
            revlinrf3 = list(reversed(linrf3))
            dop0 = 27 - len(linrf3)
            for i in range(dop0):
                revlinrf3.append("0")
            im = list(reversed(revlinrf3))
            dictf = {argumenty[i] : im[i] for i in range(len(im))}
            return dictf
            
        def iteracja(self, nrf, status):
            nrf = self.nrf
            status = self.status
            defdcells = self.defcells(status)
            f = self.dectof(nrf)
            nowystatus = []
            for i in defdcells:
                c = f[i]
                nowystatus.append(c)
            intnowystatus = []
            for j in nowystatus:
                o = int(j)
                intnowystatus.append(o)
            return intnowystatus

        

matrix = []
matrix.append(status0)
statuswej = status0
for i in range(1,m):
    p1 = automat(nrf,statuswej)
    statuswyj = p1.iteracja(nrf,statuswej)
    matrix.append(statuswyj)
    statuswej = statuswyj

#print(matrix)
cmap = ListedColormap(['red','blue','green'])
def obrazkowanie(matrix):
    matrix = np.array(matrix)
    fig, ax = plt.subplots(figsize=(matrix.shape[1], matrix.shape[0]))  
    ax.imshow(matrix, cmap=cmap)
    ax.axis('off')
    plt.show()
    
    
obrazkowanie(matrix)