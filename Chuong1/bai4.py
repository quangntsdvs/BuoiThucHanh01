def number(x, y):
    for num in range(x, y + 1):
        total = 0
        for i in range(1, num):
            if num % i == 0:
                total += i
        
        if total < num:
            print(f"{num} la deficient.")
        elif total == num:
            print(f"{num} la perfect.")
        else:
            print(f"{num} la abundant.")

x = int(input("Nhap so nguyen duong x: "))
y = int(input("Nhap so nguyen duong y (y >= x): "))
print(f"Phan loai cua cac so tu {x} den {y}:")
number(x, y)