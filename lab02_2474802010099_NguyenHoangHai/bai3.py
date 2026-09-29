import pandas as pd
from sklearn.linear_model import LogisticRegression

# Đọc dữ liệu
df = pd.read_csv("data/sinh_vien.csv")

# X và y
X = df[["gio_on"]]
y = df["qua_mon"]

# Huấn luyện mô hình
model = LogisticRegression()
model.fit(X, y)

# Lấy hệ số
w = float(model.coef_[0][0])
b = float(model.intercept_[0])

print("w =", round(w, 6))
print("b =", round(b, 6))

# Hàm dự đoán
def du_doan(gio):
    z = w * gio + b

    p = 1 / (1 + __import__("math").exp(-z))

    nhan = 1 if p >= 0.5 else 0

    print(
        f"gio = {gio:5.2f} | "
        f"z = {z:8.4f} | "
        f"xac suat = {p:.4f} | "
        f"nhan = {nhan}"
    )


# Các trường hợp yêu cầu
print("\nDự đoán:")
for gio in [3, 8, 12.89, 18, 26]:
    du_doan(gio)