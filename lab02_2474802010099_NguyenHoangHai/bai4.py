import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
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

# Lấy TN, FP, FN, TP
tn, fp, fn, tp = confusion_matrix(
    y_test,
    y_pred
).ravel()

print("TN =", tn)
print("FP =", fp)
print("FN =", fn)
print("TP =", tp)

# Tự tính
accuracy = (tp + tn) / (tp + tn + fp + fn)

precision = tp / (tp + fp)

recall = tp / (tp + fn)

f1 = 2 * precision * recall / (precision + recall)

print("\nKết quả tự tính:")
print("Accuracy =", round(accuracy, 4))
print("Precision =", round(precision, 4))
print("Recall =", round(recall, 4))
print("F1 =", round(f1, 4))