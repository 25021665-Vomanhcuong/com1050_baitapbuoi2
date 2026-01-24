import math
a=float(input("cạnh thứ nhất của tam giác: "))
b=float(input("cạnh thứ hai của tam giác: "))
c=float(input("cạnh thứ ba của tam giác: "))
if a+b>c and a+c>b and b+c>a:
    p=(a+b+c)/2
    S=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(S,"là diện tích tam giác")
else:
    print("Khong phải 3 cạnh của tam giác")