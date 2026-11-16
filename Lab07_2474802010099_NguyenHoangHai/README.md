# Bài 7 — Đánh giá mô hình

Notebook thực hành và bài tập theo tài liệu `Lab07_DanhGiaMoHinh.pdf` (Học máy ứng dụng, năm học 2026–2027). Dữ liệu mô phỏng gồm sinh viên có nguy cơ bỏ học và bộ dữ liệu giá nhà.

## Bảng mô tả dữ liệu sinh viên

| Cột | Ý nghĩa |
|---|---|
| `diem_tb` | Điểm trung bình học kỳ trước, thang 10. |
| `so_buoi_vang` | Số buổi vắng trong học kỳ. |
| `tin_chi_no` | Số tín chỉ còn nợ. |
| `gio_lam_them` | Số giờ làm thêm mỗi tuần. |
| `bo_hoc` | Nhãn cần đoán: 1 nếu bỏ học, 0 nếu học tiếp. |

## Nội dung

### Notebook thực hành

1. `notebooks/01_accuracy_danh_lua.ipynb` — accuracy và mô hình lười.
2. `notebooks/02_ma_tran_nham_lan.ipynb` — TP, FP, FN, TN.
3. `notebooks/03_precision_recall_f1.ipynb` — precision, recall, F1.
4. `notebooks/04_doi_nguong.ipynb` — đổi và chọn ngưỡng bằng cross-validation.
5. `notebooks/05_roc_auc.ipynb` — ROC, AUC và so sánh mô hình.
6. `notebooks/06_kiem_dinh_cheo_can_bang.ipynb` — phân tầng, cross-validation, cân bằng lớp.

### Bài tập

`baitap/` có notebook cho đủ sáu bài tập: tự viết hàm đánh giá, chữ số viết tay, chọn ngưỡng theo recall, vẽ ROC, cân bằng Random Forest/SVC, và MAE/RMSE trên dữ liệu giá nhà.

## Cách chạy

Mở thư mục `bai07_danh_gia` làm thư mục dự án trong Jupyter, sau đó mở notebook và chạy từ trên xuống. Cài các thư viện cần thiết nếu môi trường chưa có:

```bash
python -m pip install pandas numpy scikit-learn matplotlib jupyter
```

Các đường dẫn dữ liệu trong notebook dùng `../data/` tương ứng khi chạy notebook từ thư mục `notebooks/` hoặc `baitap/`. Không đưa `venv/` lên Git.

## Dữ liệu

- `data/sinh_vien_bo_hoc.csv`: 1.200 dòng mô phỏng, nhãn `bo_hoc` lệch lớp.
- `data/gia_nha.csv`: dữ liệu giá nhà dùng ở bài tập 6.
