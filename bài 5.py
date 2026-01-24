c = input("Nhập vào một chữ cái hoa: ")
if 'A' <= c <= 'Z':
    if c == 'A':
        print("Trường hợp đặc biệt: không có chữ cái thường đứng trước 'a'")
    else:
        chữ_thường = chr(ord(c) + 32)
        chữ_liền_trước = chr(ord(chữ_thường) - 1)
        print("Kết quả:", chữ_liền_trước)
else:
    print("Ký tự không phải là chữ cái hoa.")