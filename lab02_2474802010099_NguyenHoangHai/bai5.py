import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split

# Đọc dữ liệu
df = pd.read_csv("data/sinh_vien.csv")

X = df[["gio_on"]]
y = df["qua_mon"]

# Chia dữ liệu
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=17,
    stratify=y
)

# Huấn luyện
model = LogisticRegression()
model.fit(X_train, y_train)

# Xác suất qua môn
p = model.predict_proba(X_test)[:, 1]

# Danh sách ngưỡng
thresholds = np.arange(0.05, 1.0, 0.05)

best_threshold = 0
best_f1 = -1

print("Ngưỡng     F1")
print("----------------")

for threshold in thresholds:

    y_pred = (p >= threshold).astype(int)

    f1 = f1_score(
        y_test,
        y_pred,
        zero_division=0
    )

    print(f"{threshold:.2f}       {f1:.4f}")

    if f1 > best_f1:
        best_f1 = f1
        best_threshold = threshold

print("\nNgưỡng có F1 cao nhất:", round(best_threshold, 2))
print("F1 cao nhất:", round(best_f1, 4))