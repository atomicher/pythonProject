def buble (arr):
    l = len(arr)
    for i in range(l):
        for j in range(0,l-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

try:
    m = int(input("Введи довжину: "))
    n=[]

    print("Введи елементи: ")
    for i in range (0,m):
      element = input()
      n.append(element)
    print(n)

    sort = buble(n)
    print(sort)

except ValueError:
    print("Неправильні числові дані")
