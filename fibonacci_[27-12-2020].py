def fibonacci(limit):
    f = 1
    fList = list()
    fList.append(f)
    fList.append(f)
    for n in range(2, limit):
        calc = fList[n - 1] + abs(fList[n - 2])
        fList.append(calc)
    print(fList)

# Prints upto 15 numbers
fibonacci(15)
