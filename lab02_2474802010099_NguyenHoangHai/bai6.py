import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score
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

# Dự đoán
y_pred = model.predict(X_test)

# Lớp 1 = qua môn
precision_1 = precision_score(
    y_test,
    y_pred,
    pos_label=1
)

recall_1 = recall_score(
    y_test,
    y_pred,
    pos_label=1
)

# Lớp 0 = rớt môn
precision_0 = precision_score(
    y_test,
    y_pred,
    pos_label=0
)

recall_0 = recall_score(
    y_test,
    y_pred,
    pos_label=0
)

print("Lớp 1 - Qua môn")
print("Precision =", round(precision_1, 4))
print("Recall =", round(recall_1, 4))

print("\nLớp 0 - Rớt môn")
print("Precision =", round(precision_0, 4))
print("Recall =", round(recall_0, 4))