a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

for number in range(a, b + 1):
    count = 0
    
    for i in range(1, so + 1):
        if number % i == 0:
            count += 1  
            
    if count == 2:
        print(number, end=" ")
