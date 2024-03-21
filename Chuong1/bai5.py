def pascal(n):
    for i in range(n):
        coef = 1  
        for j in range(1, n - i + 1):
            print(" ", end="")
        
        for j in range(0, i + 1):
            print(" ", coef, sep="", end="")
            coef = coef * (i - j) // (j + 1)
        print()

n = int(input("Nhap so nguyen duong n: "))
pascal(n)