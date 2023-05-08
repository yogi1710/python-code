for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()


for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()


for i in range(5):
    for k in range(5-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()


for i in range(5):
    for k in range(5-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()


for i in range(5):
    for k in range(i):
        print(" ",end= "")
    for j in range(5-i):
        print("*",end="")
    print()


for i in range(5):
    for k in range(i):
        print(" ",end= "")
    for j in range(5-i):
        print("*",end=" ")
    print()


for i in range(5):
    for k in range(i):
        print(" ",end= "")
    for j in range(5-i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()


for i in range(5-1):
    for k in range(i):
        print(" ",end= "")
    for j in range(5-i):
        print("*",end=" ")
    print()
for i in range(5):
    for k in range(5-i-1):
        print(" ",end= "")
    for j in range(i+1):
        print("*",end= " ")
    print()


var = 1
for i in range(5):
    for j in range(5-i-1):
        print(" ",end="")
    for k in range(i+1):
        print(var,end=" ")
        var += 1
    print()


for i in range(5):
    var = 1
    for k in range(5-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(var,end=" ")
        var += 1
    print()


for i in range(5):
    var = 5-1+1
    for k in range(5-i-1):
        print(" ",end= "")
    for j in range(i+1):
        print(var,end = " ")
        var -=1
    print()



for i in range(5):
    var = 1+i
    for k in range(5-i-1):
        print(" ",end= "")
    for j in range(i+1):
        print(var,end = " ")
        var -=1
    print()