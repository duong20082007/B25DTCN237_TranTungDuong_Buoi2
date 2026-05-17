# Yêu cầu người dùng nhập vào một số nguyên
number = int(input("Nhap mot so nguyen: "))

# Kiểm tra các điều kiện chia hết
if number % 3 == 0 and so % 5 == 0:
    print("So vua nhap chia het cho ca 3 va 5")
elif number % 3 == 0:
    print("So vua nhap chia het cho 3")
elif number % 5 == 0:
    print("So vua nhap chia het cho 5")
else:
    print("So vua nhap khong chia het cho 3 cung khong chia het cho 5")