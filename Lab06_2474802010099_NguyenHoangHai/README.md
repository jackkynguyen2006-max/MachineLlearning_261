# Học máy ứng dụng — Lab 06: Support Vector Machine

## Thông tin sinh viên

| Nội dung | Thông tin |
|---|---|
| Họ và tên | Nguyễn Hoàng Hải |
| Mã số sinh viên | 2474802010099 |
| Học phần | Học máy ứng dụng |
| Mã lớp học phần | 261_71ITAI41203_0101 |
| Khóa | 30 |
| Năm học | Năm 3 |

## Thông tin giảng viên

- **Giảng viên:** ThS. Nguyễn Thái Anh
- **Học vị:** Thạc sĩ ngành Khoa học Dữ liệu và Trí tuệ Nhân tạo (Data Science & Artificial Intelligence).
- **Đơn vị công tác:** Giảng viên Khoa Công nghệ Thông tin, Trường Đại học Văn Lang.
- **Lĩnh vực quan tâm và nghiên cứu:** Khoa học dữ liệu (Data Science), Trí tuệ nhân tạo (AI) và Học máy (Machine Learning).
- **GitHub:** [github.com/AnhNguyenVLU](https://github.com/AnhNguyenVLU)

## Nội dung

Các notebook được sắp xếp theo thứ tự thực hành trong tài liệu Lab 06:

1. [g1_le_rong_nhat.ipynb](g1_le_rong_nhat.ipynb) — Đường có lề rộng nhất và vectơ hỗ trợ.
2. [g2_tham_so_c.ipynb](g2_tham_so_c.ipynb) — Tham số C, lề mềm và chuẩn hoá dữ liệu.
3. [g3_kernel.ipynb](g3_kernel.ipynb) — Nâng chiều bằng tay và các kernel.
4. [g4_chon_tham_so.ipynb](g4_chon_tham_so.ipynb) — Ảnh hưởng của gamma và dò lưới tham số.
5. [g5_chu_so.ipynb](g5_chu_so.ipynb) — Nhận dạng chữ số viết tay với `load_digits`.
6. [g6_bai_tap.ipynb](g6_bai_tap.ipynb) — Sáu bài tập cuối tài liệu.

## Dữ liệu

- [sinh_vien (1).csv](sinh_vien%20(1).csv) — Dữ liệu sinh viên cơ bản (`gio_on`, `diem_giua_ky`, `qua_mon`).
- [sinh_vien_mo_rong.csv](sinh_vien_mo_rong.csv) — Dữ liệu sinh viên bổ sung cột chi tiêu.
- [hai_vang_trang.csv](hai_vang_trang.csv) — Bộ dữ liệu hai vầng trăng.
- [Lab06_SVM.pdf](Lab06_SVM.pdf) — Tài liệu hướng dẫn thực hành.

Notebook tự tìm CSV trong thư mục hiện tại hoặc thư mục `data/`. File `sinh_vien (1).csv` được nhận diện thay cho tên `sinh_vien.csv` dùng trong tài liệu.

## Cách chạy

Mở các tệp `.ipynb` bằng Jupyter Notebook, JupyterLab hoặc VS Code và chạy lần lượt các ô từ trên xuống. Môi trường Python cần có `numpy`, `pandas`, `matplotlib`, `scikit-learn` và `nbformat` (nbformat chỉ cần khi làm việc với định dạng notebook bằng mã).
