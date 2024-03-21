def gcd_recursive(m, n):
    if n == 0:
        return m
    else:
        return gcd_recursive(n, m % n)

def gcd_iterative(m, n):
    while n != 0:
        m, n = n, m % n
    return m

def main():
    m = int(input("nhap so nguyen duong m (m >= 0): "))
    n = int(input("nhap so nguyen duong n (n >= 0): "))
    if m <= 0 or n <= 0:
        print("yeu cau 2 so nguyen nhap phai duong.")
        return
    print("Uoc so chung lon nhat cua", m, "va", n, "su dung de qui la:", gcd_recursive(m, n))
    print("Uoc so chung lon nhat cua", m, "và", n, "khong su dung de qui la:", gcd_iterative(m, n))
