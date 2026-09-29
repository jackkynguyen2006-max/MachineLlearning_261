import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("data/sinh_vien.csv")

# Nhóm có điểm giữa kỳ từ 7 trở lên
nhom_7 = df[df["diem_giua_ky"] >= 7]

# Nhóm còn lại
nhom_con_lai = df[df["diem_giua_ky"] < 7]

# Tính kết quả
so_luong = len(nhom_7)
ty_le_nhom_7 = nhom_7["qua_mon"].mean()
ty_le_con_lai = nhom_con_lai["qua_mon"].mean()

print("Số sinh viên có điểm giữa kỳ từ 7 trở lên:", so_luong)
print("Tỷ lệ qua môn của nhóm >= 7:", round(ty_le_nhom_7, 4))
print("Tỷ lệ qua môn của nhóm < 7:", round(ty_le_con_lai, 4))

print("\nNhận xét:")
if ty_le_nhom_7 > ty_le_con_lai:
    print("Nhóm có điểm giữa kỳ từ 7 trở lên có tỷ lệ qua môn cao hơn nhóm còn lại.")
else:
    print("Nhóm có điểm giữa kỳ từ 7 trở lên không có tỷ lệ qua môn cao hơn nhóm còn lại.")