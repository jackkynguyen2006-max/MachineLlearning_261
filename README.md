MSSV: 2474802010099
HoVaTen: Nguyễn Hoàng Hải
Học Phần: Học máy ứng dụng
Giảng viên: Thạc Sĩ Nguyễn Thái Anh
Bài: Bài 1 - Hồi quy tuyến tính
Môi trường: googlecolab
# LAB 01 - HỒI QUY TUYẾN TÍNH

## 1. Giới thiệu

Bài Lab 01 thực hành các kiến thức cơ bản về **hồi quy tuyến tính (Linear Regression)** bằng Python.

Nội dung chính:

* Đọc và phân tích dữ liệu giá nhà.
* Trực quan hóa dữ liệu.
* Xây dựng mô hình hồi quy tuyến tính một biến.
* Đánh giá mô hình bằng các độ đo MAE, MSE, RMSE và R².
* Phân tích phần dư.
* Cài đặt thuật toán Gradient Descent.
* Xây dựng hồi quy tuyến tính nhiều biến.
* Thực hiện các bài tập mở rộng.

---

## 2. Công nghệ sử dụng

* Python
* Google Colab
* NumPy
* Pandas
* Matplotlib
* Scikit-learn

---

## 3. Dữ liệu

File dữ liệu:

```text
gia_nha.csv
```

Dữ liệu gồm **60 căn nhà** với 4 thuộc tính:

| Thuộc tính  | Ý nghĩa            |
| ----------- | ------------------ |
| `dien_tich` | Diện tích nhà (m²) |
| `so_phong`  | Số phòng           |
| `tuoi_nha`  | Tuổi của căn nhà   |
| `gia`       | Giá nhà (tỷ đồng)  |

Kích thước dữ liệu:

```text
(60, 4)
```

Không có giá trị bị thiếu trong dữ liệu.

---

## 4. Hồi quy tuyến tính một biến

Sử dụng:

```text
X = dien_tich
y = gia
```

Mô hình:

```text
y = wx + b
```

Kết quả mô hình:

```text
w = 0.078367
b = 0.401752
```

Phương trình hồi quy:

```text
gia = 0.078367 × dien_tich + 0.401752
```

---

## 5. Đánh giá mô hình

Dữ liệu được chia:

```text
Tập huấn luyện: 48 mẫu
Tập kiểm tra: 12 mẫu
```

Kết quả trên tập kiểm tra:

| Độ đo |        Kết quả |
| ----- | -------------: |
| MAE   | 0.2578 tỷ đồng |
| MSE   |         0.1392 |
| RMSE  | 0.3730 tỷ đồng |
| R²    |         0.9622 |

R² = 0.9622 cho thấy mô hình tuyến tính một biến giải thích được phần lớn sự biến thiên của giá nhà trong tập dữ liệu kiểm tra.

---

## 6. Gradient Descent

Gradient Descent được sử dụng để tìm các tham số `w` và `b` làm giảm hàm mất mát MSE.

Thông số:

```text
Tốc độ học = 0.1
Số vòng lặp = 200
```

Kết quả sau 200 vòng:

```text
w = 1.5713
b = 6.4933
MSE = 0.1790
```

Sau khi chuyển tham số về thang đo ban đầu:

```text
w = 0.078367
b = 0.401752
```

Kết quả phù hợp với nghiệm thu được từ hồi quy tuyến tính.

---

## 7. Hồi quy tuyến tính nhiều biến

Sử dụng ba biến đầu vào:

```text
dien_tich
so_phong
tuoi_nha
```

Mô hình:

```text
gia = w1 × dien_tich + w2 × so_phong + w3 × tuoi_nha + b
```

Kết quả:

```text
dien_tich = +0.0701
so_phong  = +0.3042
tuoi_nha  = -0.0295
b         = +0.6917
```

Đánh giá:

```text
R² hồi quy một biến  = 0.9622
R² hồi quy ba biến   = 0.9761
```

Mô hình sử dụng ba biến có R² cao hơn mô hình chỉ sử dụng diện tích.

---

## 8. Các bài tập thực hành

### Bài 1

Lọc các căn nhà có:

```text
dien_tich > 100 m²
```

Sau đó tính:

* Số lượng căn nhà.
* Giá trung bình.

### Bài 2

Vẽ biểu đồ Scatter giữa:

```text
so_phong
gia
```

Biểu đồ được lưu thành:

```text
bai2.png
```

### Bài 3

Sử dụng công thức bình phương tối thiểu để xây dựng mô hình:

```text
gia = w × tuoi_nha + b
```

In ra `w` và `b` với 6 chữ số thập phân.

### Bài 4

Xây dựng mô hình hồi quy sử dụng:

```text
dien_tich
so_phong
```

Chia dữ liệu theo tỷ lệ:

```text
80% train
20% test
```

và đánh giá bằng R².

### Bài 5

So sánh Gradient Descent với hai tốc độ học:

```text
0.001
1.02
```

Sau 200 vòng lặp, ghi nhận MSE và phân tích sự khác nhau.

### Bài 6

Xây dựng hàm:

```python
du_doan_gia(dien_tich)
```

Hàm sử dụng mô hình:

```text
gia = 0.078367 × dien_tich + 0.401752
```

Nếu diện tích nằm ngoài khoảng:

```text
35.5 - 117.5 m²
```

thì đưa ra cảnh báo.

---

## 9. Ví dụ dự đoán

Với diện tích:

```text
60 m²
```

Giá dự đoán:

```text
5.103 tỷ đồng
```

Với diện tích:

```text
80 m²
```

Giá dự đoán:

```text
6.671 tỷ đồng
```

Với diện tích:

```text
200 m²
```

mô hình đưa ra cảnh báo vì diện tích nằm ngoài khoảng dữ liệu ban đầu.

---

## 10. Cấu trúc thư mục

```text
baitap01/
│
├── bai1.py
├── bai2.py
├── bai2.png
├── bai3.py
├── bai4.py
├── bai5.py
├── bai6.py
└── README.md
```

---

## 11. Cách chạy

### Bước 1: Cài đặt thư viện

```bash
pip install numpy pandas matplotlib scikit-learn
```

### Bước 2: Đặt file dữ liệu

Đặt file:

```text
gia_nha.csv
```

vào thư mục dự án.

### Bước 3: Chạy từng bài

```bash
python bai1.py
python bai2.py
python bai3.py
python bai4.py
python bai5.py
python bai6.py
```

Nếu sử dụng Google Colab, có thể tải file `gia_nha.csv` lên Colab và đọc bằng:

```python
df = pd.read_csv("/content/gia_nha.csv")
```

---

## 12. Kết luận

Qua bài Lab, đã thực hành được các nội dung:

* Đọc và xử lý dữ liệu bằng Pandas.
* Trực quan hóa dữ liệu bằng Matplotlib.
* Xây dựng mô hình hồi quy tuyến tính.
* Đánh giá mô hình bằng MAE, MSE, RMSE và R².
* Phân tích phần dư.
* Hiểu và cài đặt Gradient Descent.
* Xây dựng hồi quy tuyến tính nhiều biến.
* Sử dụng mô hình để dự đoán giá nhà.

Kết quả cho thấy diện tích có mối quan hệ tuyến tính rõ ràng với giá nhà trong bộ dữ liệu thực hành. Việc bổ sung `so_phong` và `tuoi_nha` giúp mô hình hồi quy nhiều biến đạt R² cao hơn so với mô hình chỉ sử dụng diện tích.
