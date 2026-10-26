import nbformat as nbf
from pathlib import Path

nb = nbf.v4.new_notebook()
nb.metadata = {
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python", "version": "3.x"},
}
cells = []
def md(s): cells.append(nbf.v4.new_markdown_cell(s))
def code(s): cells.append(nbf.v4.new_code_cell(s))

md("""# Lab 4 – K láng giềng gần nhất (KNN)

Notebook giải **6 bài tập** ở mục 7 của `Lab04_KNN.pdf`. Các kết quả được tính từ ba CSV đi kèm. Chạy lần lượt từ trên xuống dưới; phần thời gian có thể thay đổi tùy máy.

> Các file CSV đang nằm cùng thư mục với notebook. Phần tìm dữ liệu cũng hỗ trợ thư mục con `data/` như hướng dẫn trong PDF.""")
code("""from pathlib import Path
import time
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.metrics import accuracy_score, mean_absolute_error
from sklearn.linear_model import LinearRegression

def tim_csv(*ten_file):
    'Tìm CSV cạnh notebook hoặc trong thư mục data/.'
    for ten in ten_file:
        for duong_dan in (Path(ten), Path("data") / ten):
            if duong_dan.exists():
                return duong_dan
    raise FileNotFoundError(f"Không tìm thấy file nào trong: {ten_file}")

df_sinh_vien = pd.read_csv(tim_csv("sinh_vien_mo_rong.csv"))
df_hai_vang = pd.read_csv(tim_csv("hai_vang_trang.csv"))
df_gia_nha = pd.read_csv(tim_csv("gia_nha.csv", "gia_nha (1).csv"))
print("Sinh viên:", df_sinh_vien.shape)
print("Hai vầng trăng:", df_hai_vang.shape)
print("Giá nhà:", df_gia_nha.shape)""")

md("""## Bài tập 1 – Tự viết KNN bằng NumPy

Hàm bên dưới tính khoảng cách Euclid, lấy `k` điểm gần nhất và bỏ phiếu đa số. Chia dữ liệu hai vầng trăng đúng như mục 4 (`random_state=17`, `stratify=y`), rồi so với `KNeighborsClassifier`.

**Nhận xét:** hai kết quả phải trùng nhau vì cùng dùng khoảng cách Euclid và quy tắc bỏ phiếu đa số.""")
code("""def knn_du_doan(X_hoc, y_hoc, x_moi, k):
    X_hoc = np.asarray(X_hoc, dtype=float)
    y_hoc = np.asarray(y_hoc)
    x_moi = np.asarray(x_moi, dtype=float)
    if not 1 <= k <= len(X_hoc):
        raise ValueError("k phải nằm trong khoảng từ 1 đến số mẫu huấn luyện")
    khoang_cach = np.sqrt(((X_hoc - x_moi) ** 2).sum(axis=1))
    chi_so_lang_gieng = np.argsort(khoang_cach)[:k]
    nhan, so_phieu = np.unique(y_hoc[chi_so_lang_gieng], return_counts=True)
    return nhan[np.argmax(so_phieu)]

X = df_hai_vang[["x1", "x2"]].to_numpy(dtype=float)
y = df_hai_vang["nhan"].to_numpy()
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.25, random_state=17, stratify=y
)
y_tu_viet = np.array([knn_du_doan(X_tr, y_tr, x, k=13) for x in X_te])
acc_tu_viet = accuracy_score(y_te, y_tu_viet)
mh_knn = KNeighborsClassifier(n_neighbors=13).fit(X_tr, y_tr)
acc_sklearn = accuracy_score(y_te, mh_knn.predict(X_te))
print(f"KNN tự viết, accuracy: {acc_tu_viet:.4f}")
print(f"scikit-learn, accuracy: {acc_sklearn:.4f}")
print("Hai kết quả trùng nhau:", np.isclose(acc_tu_viet, acc_sklearn))""")

md("""## Bài tập 2 – Khoảng cách Manhattan

Giữ nguyên cách chia tập, chọn `k` lẻ trong khoảng 1–51 bằng kiểm định chéo 5 phần **chỉ trên tập huấn luyện**. Sau đó mới chấm tập kiểm tra; làm tương tự với Euclid để so sánh.""")
code("""def chon_k_va_cham(metric):
    bang_diem = {}
    for k in range(1, 52, 2):
        model = KNeighborsClassifier(n_neighbors=k, metric=metric)
        bang_diem[k] = cross_val_score(model, X_tr, y_tr, cv=5).mean()
    k_tot = max(bang_diem, key=bang_diem.get)
    model = KNeighborsClassifier(n_neighbors=k_tot, metric=metric).fit(X_tr, y_tr)
    acc_test = accuracy_score(y_te, model.predict(X_te))
    return k_tot, bang_diem[k_tot], acc_test, bang_diem

k_euclid, cv_euclid, acc_euclid, diem_euclid = chon_k_va_cham("euclidean")
k_manhattan, cv_manhattan, acc_manhattan, diem_manhattan = chon_k_va_cham("manhattan")
pd.DataFrame([
    {"Khoảng cách": "Euclid", "k tốt nhất": k_euclid, "CV trung bình": cv_euclid, "Accuracy kiểm tra": acc_euclid},
    {"Khoảng cách": "Manhattan", "k tốt nhất": k_manhattan, "CV trung bình": cv_manhattan, "Accuracy kiểm tra": acc_manhattan},
])
print(f"Chênh lệch accuracy kiểm tra: {abs(acc_manhattan - acc_euclid):.4f}")""")
md("""**Nhận xét:** hãy dựa vào hai accuracy vừa in để nhận xét mức thay đổi. Chọn k bằng cross-validation giữ tập kiểm tra ngoài quá trình lựa chọn.""")

md("""## Bài tập 3 – Đổi đơn vị đo

Đổi `chi_tieu` từ nghìn đồng sang triệu đồng (chia 1000), rồi chạy KNN `k=7` không chuẩn hóa trên ba cột. So thêm với trường hợp chuẩn hóa bằng pipeline. Pipeline chỉ fit scaler trên tập huấn luyện.""")
code("""from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

sv = df_sinh_vien.copy()
sv["chi_tieu_trieu"] = sv["chi_tieu"] / 1000
cot_moi = ["gio_on", "diem_giua_ky", "chi_tieu_trieu"]
X_sv = sv[cot_moi]
y_sv = sv["qua_mon"]
Xsv_tr, Xsv_te, ysv_tr, ysv_te = train_test_split(
    X_sv, y_sv, test_size=0.25, random_state=17, stratify=y_sv
)

knn_khong_chuan = KNeighborsClassifier(n_neighbors=7).fit(Xsv_tr, ysv_tr)
acc_doi_don_vi = accuracy_score(ysv_te, knn_khong_chuan.predict(Xsv_te))
knn_co_chuan = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=7)).fit(Xsv_tr, ysv_tr)
acc_co_chuan = accuracy_score(ysv_te, knn_co_chuan.predict(Xsv_te))
print(f"Không chuẩn hóa sau khi đổi đơn vị: {acc_doi_don_vi:.4f} (mốc trước đổi: 0.5333)")
print(f"Có chuẩn hóa sau khi đổi đơn vị: {acc_co_chuan:.4f}")""")
md("""**Giải thích:** không chuẩn hóa thì chia cột chi tiêu cho 1000 làm giảm mạnh đóng góp của nó vào khoảng cách, nên láng giềng và accuracy có thể đổi rõ rệt. Khi chuẩn hóa, phép đổi đơn vị tuyến tính dương bị triệt tiêu bởi việc scaler trừ trung bình và chia độ lệch chuẩn; kết quả dự đoán về cơ bản không đổi.""")

md("""## Bài tập 4 – Láng giềng có trọng số

So sánh KNN bỏ phiếu đều và KNN `weights="distance"` với `k=1, 13, 101`. Tập train/test dùng cùng phép chia ở các bài trên.""")
code("""dong_ket_qua = []
for k in (1, 13, 101):
    for weights in ("uniform", "distance"):
        model = KNeighborsClassifier(n_neighbors=k, weights=weights).fit(X_tr, y_tr)
        dong_ket_qua.append({
            "k": k,
            "weights": weights,
            "Accuracy train": accuracy_score(y_tr, model.predict(X_tr)),
            "Accuracy kiểm tra": accuracy_score(y_te, model.predict(X_te)),
        })
pd.DataFrame(dong_ket_qua)""")
md("""**Nhận xét về k=101:** đối chiếu accuracy kiểm tra của hai cách trọng số. Trọng số theo khoảng cách ưu tiên các điểm gần hơn nên có thể giảm ảnh hưởng của các điểm xa, nhưng với k rất lớn nhiều láng giềng vẫn tham gia và các điểm gần nhau có thể nhận phiếu cùng lớp; vì vậy không đảm bảo khắc phục hoàn toàn hiện tượng mô hình quá trơn.""")

md("""## Bài tập 5 – Chọn k cho hồi quy

Dùng diện tích làm đặc trưng, chia dữ liệu đúng như PDF (`test_size=0.2`, `random_state=42`). Chọn `k` từ 1 đến 20 bằng CV 5 phần, tối ưu MAE; sau đó so MAE tập kiểm tra với hồi quy tuyến tính.""")
code("""X_nha = df_gia_nha[["dien_tich"]]
y_nha = df_gia_nha["gia"]
Xn_tr, Xn_te, yn_tr, yn_te = train_test_split(
    X_nha, y_nha, test_size=0.2, random_state=42
)
diem_cv_mae = {}
for k in range(1, 21):
    diem_am = cross_val_score(
        KNeighborsRegressor(n_neighbors=k), Xn_tr, yn_tr,
        cv=5, scoring="neg_mean_absolute_error"
    )
    diem_cv_mae[k] = -diem_am.mean()
k_nha_tot = min(diem_cv_mae, key=diem_cv_mae.get)
knn_nha = KNeighborsRegressor(n_neighbors=k_nha_tot).fit(Xn_tr, yn_tr)
tuyen_tinh = LinearRegression().fit(Xn_tr, yn_tr)
mae_knn_toi_uu = mean_absolute_error(yn_te, knn_nha.predict(Xn_te))
mae_tuyen_tinh = mean_absolute_error(yn_te, tuyen_tinh.predict(Xn_te))
print(f"k tốt nhất theo CV: {k_nha_tot}, MAE CV: {diem_cv_mae[k_nha_tot]:.4f}")
print(f"MAE kiểm tra KNN: {mae_knn_toi_uu:.4f}")
print(f"MAE kiểm tra hồi quy tuyến tính: {mae_tuyen_tinh:.4f}")
print("KNN có MAE thấp hơn đường thẳng:", mae_knn_toi_uu < mae_tuyen_tinh)""")
md("""**Nhận xét:** so sánh hai MAE kiểm tra; MAE thấp hơn là tốt hơn. Kết quả dùng k đã chọn trên tập huấn luyện bằng cross-validation, không dùng tập kiểm tra để chọn k.""")

md("""## Bài tập 6 – Đo thời gian dự đoán

Với mỗi cỡ dữ liệu, tạo hai đặc trưng ngẫu nhiên và một nhãn nhị phân. Đo riêng thời gian `fit` và thời gian dự đoán 1000 mẫu mới. Để so sánh công bằng, dùng cùng 1000 truy vấn cho cả ba kích thước.""")
code("""rng = np.random.default_rng(0)
X_moi = rng.random((1000, 2))
kq_thoi_gian = []
for n in (1_000, 10_000, 100_000):
    X_ngau_nhien = rng.random((n, 2))
    y_ngau_nhien = (X_ngau_nhien[:, 0] + X_ngau_nhien[:, 1] > 1).astype(int)
    model = KNeighborsClassifier(n_neighbors=5)

    bat_dau = time.perf_counter()
    model.fit(X_ngau_nhien, y_ngau_nhien)
    giay_fit = time.perf_counter() - bat_dau

    bat_dau = time.perf_counter()
    model.predict(X_moi)
    giay_predict = time.perf_counter() - bat_dau

    kq_thoi_gian.append({
        "Số mẫu huấn luyện": n,
        "Thời gian fit (giây)": giay_fit,
        "Thời gian predict 1000 mẫu (giây)": giay_predict,
    })
bang_thoi_gian = pd.DataFrame(kq_thoi_gian)
bang_thoi_gian""")
md("""**Giải thích:** `fit` của KNN chủ yếu lưu dữ liệu nên thường rất nhanh. Khi `predict`, mỗi truy vấn phải được so với dữ liệu đã lưu, nên thời gian dự đoán thường tăng theo số mẫu huấn luyện. KNN được gọi là **mô hình học lười** vì gần như không xây dựng mô hình khái quát trong bước huấn luyện mà dồn phần lớn tính toán sang lúc dự đoán.""")

md("""## Tổng kết

- KNN tự viết cho kết quả trùng với scikit-learn khi dùng cùng quy tắc láng giềng.
- KNN nhạy với cách đo khoảng cách, đơn vị và đặc trưng đưa vào; chuẩn hóa giúp loại ảnh hưởng đơn vị.
- Cross-validation trên tập huấn luyện dùng để chọn siêu tham số; tập kiểm tra chỉ dùng đánh giá cuối.
- KNN dễ áp dụng nhưng dự đoán tốn công hơn khi dữ liệu tăng, và hồi quy KNN không ngoại suy ra ngoài vùng dữ liệu.""")

nb.cells = cells
nbf.write(nb, Path("Lab04_KNN_BaiTap.ipynb"))
