a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

if a + b > c and a + c > b and b + c > a:
    print("La 3 canh tam giac")
else:
    print("Khong phai 3 canh tam giac")
