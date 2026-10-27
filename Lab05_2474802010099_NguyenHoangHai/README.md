# Bài 5 — Cây quyết định và Rừng ngẫu nhiên

Notebook thực hành cho học phần **Học máy ứng dụng · Lab 05**, đi kèm tài liệu PDF `Lab05_CayQuyetDinh_RungNgauNhien.pdf`.

## Nội dung

- Tính chỉ số Gini và tìm ngưỡng chia tốt nhất.
- Huấn luyện cây phân loại, chọn độ sâu bằng kiểm định chéo và nhận diện quá khớp.
- So sánh cây quyết định với rừng ngẫu nhiên và các cách đo độ quan trọng đặc trưng.
- Dùng cây và rừng hồi quy để dự đoán giá nhà, so sánh với hồi quy tuyến tính.
- Thực hiện sáu bài tập mở rộng ở cuối notebook.

## Tệp dữ liệu

- `khach_vay.csv`: dữ liệu phân loại khả năng trả nợ; nhãn `tra_dung_han` gồm 1 (đúng hạn) và 0 (trễ hạn).
- `gia_nha.csv`: dữ liệu hồi quy giá nhà; `gia` tính bằng tỷ đồng.

Giữ notebook và hai tệp CSV trong cùng thư mục.

## Cài đặt và chạy

Cần Python cùng các thư viện sau:

```bash
pip install numpy pandas matplotlib scikit-learn jupyter
```

Mở `Lab05_CayQuyetDinh_RungNgauNhien.ipynb` bằng Jupyter Notebook/JupyterLab và chạy các ô lần lượt từ trên xuống. Notebook cố định `random_state` để kết quả có thể tái lập; một số con số có thể khác nhẹ giữa các phiên bản scikit-learn.

## Kết quả

Notebook tạo biểu đồ cây `cay_nam_la.png` cùng các bảng và biểu đồ đánh giá mô hình ngay trong quá trình chạy.

"
thông tin sinh viên
Nguyễn Hoàng Hải
2474802010099
Học máy ứng dụng
Mã LHP:261_71ITAI41203_0101
sinh viên năm 3 khóa 30
"

không up file venv lên trên git

Thông tin giảng viên 

* **Học vị:^^** Thạc sĩ ngành Khoa học Dữ liệu & Trí tuệ Nhân tạo (Data Science & Artificial Intelligence).
* **Đơn vị công tác:^^** Giảng viên Khoa Công nghệ Thông tin, Trường Đại học Văn Lang.
* **Lĩnh vực quan tâm & Nghiên cứu:** **Khoa học dữ liệu (Data Science), Trí tuệ nhân tạo (AI) và Học máy (Machine Learning)**
* [github.com/AnhNguyenVLU](https://github.com/AnhNguyenVLU)
*
