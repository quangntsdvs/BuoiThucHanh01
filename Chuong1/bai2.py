def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def neper(n):
    e_sum = 0
    for k in range(n + 1):
        a_k = 1 / factorial(k)
        e_sum += a_k
    return e_sum

def main():
    n = int(input("nhap so nguyen n >= 0: "))
    if n < 0:
        print("so n nhap khong duoc am.")
        return
    print("tong cac so hang a0 + a1 + ... + a", n, "la:", neper(n))
    
if __name__ == "__main__":
    main()