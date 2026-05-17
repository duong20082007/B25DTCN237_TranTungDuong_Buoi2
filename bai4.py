so = input("Nhập một số nguyên dương: ")

if so == so[::-1]:
    print(f"Số {so} là số đối xứng (palindrome).")
else:
    print(f"Số {so} không phải là số đối xứng.")