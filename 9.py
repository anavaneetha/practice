n=int(input("enter no.of row's:"))
for i in range(5):
    for k in range(5-i):
        print(end=' ')
    for j in range(i):
        print(i,end=' ')
    print()    
