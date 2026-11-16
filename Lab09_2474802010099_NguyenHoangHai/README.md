# Học máy ứng dụng — Lab 09: Mạng nơ-ron nhiều lớp

## Thông tin sinh viên

- **Họ tên:** Nguyễn Hoàng Hải
- **MSSV:** 2474802010099
- **Môn học:** Học máy ứng dụng
- **Mã lớp học phần:** 261_71ITAI41203_0101
- **Năm học:** Năm 3, khóa 30

## Thông tin giảng viên

- **Học vị:** Thạc sĩ ngành Khoa học Dữ liệu & Trí tuệ Nhân tạo (Data Science & Artificial Intelligence).
- **Đơn vị công tác:** Giảng viên Khoa Công nghệ Thông tin, Trường Đại học Văn Lang.
- **Lĩnh vực quan tâm và nghiên cứu:** Khoa học dữ liệu, Trí tuệ nhân tạo và Học máy.
- **GitHub:** [AnhNguyenVLU](https://github.com/AnhNguyenVLU)

## Bài thực hành

Các notebook được tách thành năm tệp và sắp theo đúng thứ tự trong tài liệu PDF:

| Mục | Notebook | Nội dung |
|---:|---|---|
| 2 | [m1_lan_truyen_tien.ipynb](code/m1_lan_truyen_tien.ipynb) | Tự tính lan truyền tiến bằng NumPy |
| 3 | [m2_xor.ipynb](code/m2_xor.ipynb) | Một nơ-ron và một lớp ẩn trên XOR |
| 4 | [m3_do_lon_mang.ipynb](code/m3_do_lon_mang.ipynb) | Độ lớn mạng và điều chuẩn |
| 5 | [m4_chuan_hoa.ipynb](code/m4_chuan_hoa.ipynb) | Mạng nơ-ron khi quên chuẩn hóa |
| 6 | [m5_chu_so.ipynb](code/m5_chu_so.ipynb) | Nhận dạng chữ số viết tay và các bài tập cuối chương |

Mỗi notebook có tệp mã `.py` tương ứng trong cùng thư mục `code/`. Notebook tổng hợp [Lab09_MLP.ipynb](Lab09_MLP.ipynb) cũng được giữ lại.

## Dữ liệu và cách chạy

Các bộ dữ liệu CSV nằm trong `data/`: `xor.csv`, `hai_vang_trang.csv`, `sinh_vien_mo_rong.csv` và `gia_nha.csv`. PDF đề bài là `Lab09_MLP.pdf` ở thư mục gốc.

Mở Jupyter từ thư mục gốc dự án, sau đó chạy từng notebook theo thứ tự trên. Có thể chạy các tệp Python tương ứng bằng lệnh `python code/<tên_tệp>.py`.

Cần Python 3, Jupyter, NumPy, pandas, Matplotlib và scikit-learn. Không đưa thư mục môi trường ảo `venv` lên Git.
