import numpy as np
import matplotlib.pyplot as plt

# Hàm sigmoid
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Tạo dữ liệu
z = np.linspace(-8, 8, 500)
y = sigmoid(z)

# Vẽ đồ thị
plt.figure(figsize=(8, 5))

plt.plot(z, y, label="Sigmoid")

# Đường ngang y = 0.5
plt.axhline(
    0.5,
    linestyle="--",
    label="y = 0.5"
)

# Đường dọc z = 0
plt.axvline(
    0,
    linestyle="--",
    label="z = 0"
)

plt.xlabel("z")
plt.ylabel("Sigmoid(z)")
plt.title("Hàm Sigmoid")

plt.grid(True)
plt.legend()

plt.savefig("sigmoid.png", dpi=300)
plt.show()