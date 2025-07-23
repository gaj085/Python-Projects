#WAP TO MAKE A TABLE IN PYTHON
n=int(input("Enter total columns: "))
G=[]
L=[]
K=[]
print("\nEnter all the column names one by one\n")
for i in range (n):
    G.append(input("Enter column name: "))
    c=int(input("Enter maximum char length of the column: "))
    print()
    if len(G[i])>c:
        L.append(len(G[i]))
    else:
        L.append(c)

def Row():
    for i in L:
        print('+','-'*(i),sep='',end='')
    print('+')

def Entries():
    F=[]
    global K
    for i in G:
        print("Enter",i,':',end='')
        F.append(input())
    K+=[F]
    
h=int(input("Enter number of entries in total: "))
for i in range (h):
    print("\nBegin filling entry number ",i+1)
    Entries()

Row()

print('|',end='')
for i in G:
    f=L[G.index(i)]-len(i)
    if f%2==0:
        print(' '*(f//2)+i+' '*(f//2),'|',sep='',end='')
    else:
        print(' '*((f+1)//2)+i+' '*((f-1)//2),'|',sep='',end='')
print()

for i in L:
    print('+','='*(i),sep='',end='')
print('+')

for j in K:
    print('|',end='')
    for i in j:
        f=L[j.index(i)]-len(i)
        if f%2==0:
            print(' '*(f//2)+i+' '*(f//2),'|',sep='',end='')
        else:
            print(' '*((f+1)//2)+i+' '*((f-1)//2),'|',sep='',end='')
    print()
    Row()
    
            
