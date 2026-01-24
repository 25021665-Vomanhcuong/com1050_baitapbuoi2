a1, b1, c1, a2, b2, a3 = map(float, input("Nhập 6 điểm : ").split())
TB = ((a1 + b1 + c1) + (a2 + b2) * 2 + a3 * 3) / 10
print("Điểm trung bình:", round(TB, 1))
