# 📘 STARTER KIT — Cuộc Thi Nhận Diện Giao Thông

## 🚦 Ngày hội Công nghệ Thông tin — BETU 2026

---

## 📁 Cấu trúc Starter Kit

```
Starter_Kit/
├── Train_YOLOv8_Bien_Bao.ipynb   ← Notebook train model (mở trên Google Colab)
├── Demo_App.py                    ← Ứng dụng demo Streamlit
├── requirements.txt               ← Thư viện cần cài
└── README.md                      ← File hướng dẫn này
```

---

## 🚀 Hướng Dẫn Sử Dụng (Từng Bước)

### Bước 1: Train model trên Google Colab

1. Mở file **`Train_YOLOv8_Bien_Bao.ipynb`**
2. Truy cập [Google Colab](https://colab.research.google.com/)
3. Chọn **File → Upload notebook** → chọn file `.ipynb`
4. Chọn **Runtime → Change runtime type → GPU (T4)**
5. Chạy từng ô (cell) từ trên xuống dưới
6. Sau khi train xong, tải file `best.pt` về máy

### Bước 2: Chạy ứng dụng Demo trên máy tính

#### Cài đặt thư viện:
```bash
pip install -r requirements.txt
```

#### Chạy ứng dụng:
```bash
streamlit run Demo_App.py
```

#### Mở trình duyệt:
- Truy cập: `http://localhost:8501`
- Upload ảnh biển báo → xem kết quả nhận diện

---

## 📊 Dataset

### Dataset có sẵn (GTSRB)
- **German Traffic Sign Recognition Benchmark** — 43 loại biển báo, ~50.000 ảnh
- 📥 **Link tải trực tiếp:**
  - [Training data (~263 MB)](https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/GTSRB_Final_Training_Images.zip)
  - [Test data (~84 MB)](https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/GTSRB_Final_Test_Images.zip)
  - [Trang chủ GTSRB](https://benchmark.ini.rub.de/gtsrb_news.html)
- 💡 **Notebook sẽ tự động tải dataset này**, không cần tải thủ công

### Tự thu thập dữ liệu (cộng 10% điểm!)
- Chụp ảnh biển báo giao thông tại Bình Dương, TP.HCM
- Sử dụng [Roboflow](https://roboflow.com/) để gán nhãn (miễn phí)
- Mỗi loại biển báo cần ít nhất 50 ảnh

---

## 🛠️ Công Nghệ Sử Dụng

| Công nghệ | Phiên bản | Mục đích |
|-----------|-----------|----------|
| Python | 3.10+ | Ngôn ngữ lập trình |
| YOLOv8 | Ultralytics | Model nhận diện vật thể |
| PyTorch | 2.0+ | Framework deep learning |
| Streamlit | 1.30+ | Tạo giao diện web |
| OpenCV | 4.8+ | Xử lý ảnh/video |
| Pillow | 10.0+ | Xử lý ảnh |

---

## 💡 Gợi Ý Cải Tiến (Để Được Điểm Cao)

1. **Thu thập biển báo Việt Nam** — Chụp thực tế, gán nhãn → cộng 10% điểm
2. **Nhận diện real-time** — Dùng webcam để nhận diện trực tiếp
3. **Tăng số lớp** — Train thêm nhiều loại biển báo (> 20 loại)
4. **Làm đẹp giao diện** — CSS, animation, dashboard thống kê
5. **Tracking** — Theo dõi biển báo qua nhiều frame video
6. **Cảnh báo âm thanh** — Phát âm thanh khi phát hiện biển báo quan trọng

---

## 📎 Tài Nguyên Tham Khảo

- [Ultralytics YOLOv8 Docs](https://docs.ultralytics.com/)
- [Roboflow - Gán nhãn miễn phí](https://roboflow.com/)
- [Google Colab](https://colab.research.google.com/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [OpenCV Tutorial](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)

---

## ❓ Hỗ Trợ

Nếu gặp lỗi hoặc cần giúp đỡ:
- Hỏi trong **Group Zalo cuộc thi**
- Liên hệ **Thầy Nguyên Ba Duy** (Tổ chức)
- Liên hệ **Lê Văn Xin** (phối hợp tổ chức)

---

**Chúc các nhóm thi tốt! 🎯**
