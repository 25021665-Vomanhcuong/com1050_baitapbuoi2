ho_ten = input("Nhập họ tên chủ hộ: ")
chi_so_cu = int(input("Nhập chỉ số điện kế tháng trước: "))
chi_so_moi = int(input("Nhập chỉ số điện kế tháng này: "))
so_kwh = chi_so_moi - chi_so_cu
tien = 0
so_con_lai = so_kwh
if so_con_lai > 0:
    kwh = min(so_con_lai, 50)
    tien += kwh * 1984
    so_con_lai -= kwh
if so_con_lai > 0:
    kwh = min(so_con_lai, 50)
    tien += kwh * 2050
    so_con_lai -= kwh
if so_con_lai > 0:
    kwh = min(so_con_lai, 100)
    tien += kwh * 2380
    so_con_lai -= kwh
if so_con_lai > 0:
    kwh = min(so_con_lai, 100)
    tien += kwh * 2998
    so_con_lai -= kwh
if so_con_lai > 0:
    kwh = min(so_con_lai, 100)
    tien += kwh * 3350
    so_con_lai -= kwh
if so_con_lai > 0:
    tien += so_con_lai * 3460
tien_vat = round(tien * 1.08)
print("\n--- HÓA ĐƠN TIỀN ĐIỆN ---")
print("Chủ hộ:", ho_ten)
print("Số kWh tiêu thụ:", so_kwh)
print("Tiền điện (đã gồm VAT 8%):", tien_vat, "đồng")


