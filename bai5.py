n = int(input("Nhập một số nguyên dương n: "))

if n < 0:
    print("Giai thừa không tồn tại cho số âm. Vui lòng nhập số dương!")
elif n == 0:
    print("0! = 1")
else:
    fac = 1
    for i in range(1, n + 1):
        fac *= i  
        
    print(f"{n}! = {fac}")