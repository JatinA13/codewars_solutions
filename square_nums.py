def square_digits(num):
    stri = ""
    for i in str(num):
        x = (int(i))**2
        stri+=str(x)
    print(stri)
    return int(stri)
