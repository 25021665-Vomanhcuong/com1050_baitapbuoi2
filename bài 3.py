c = input("Nhập vào một ký tự: ")
if 'A' <= c <= 'Z':
    print("Ký tự sau khi đổi:", c.lower())
elif 'a' <= c <= 'z':
    print("Ký tự sau khi đổi:", c.upper())
else:
    print("Ký tự không phải là chữ cái.")
