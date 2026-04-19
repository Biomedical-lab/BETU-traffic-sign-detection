# 📘 STARTER KIT — Cuộc Thi Nhận Diện Giao Thông

## 🚦 Ngày hội Công nghệ Thông tin — BETU 2026

> 📝 **[ĐĂNG KÝ NHÓM TẠI ĐÂY](https://forms.gle/HXa6bXhfoxBKR5KX7)**

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

## 🚀 Hướng Dẫn Sử Dụng

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
- 💬 Tham gia **[Group Zalo cuộc thi](https://zalo.me/g/jbous724jjhkhzn2eogt)** — BETU-traffic-sign-detection
- Liên hệ **Thầy Nguyên Ba Duy** (Tổ chức)
- Liên hệ **Lê Văn Xin** (Hỗ trợ)

---

**Chúc các nhóm thi tốt! 🎯**

---

## 📜 THỂ LỆ CUỘC THI

> **TRƯỜNG ĐẠI HỌC KINH TẾ - KỸ THUẬT BÌNH DƯƠNG**
> **NGÀY HỘI CÔNG NGHỆ THÔNG TIN 2026**

### CHỦ ĐỀ: "Phát triển hệ thống nhận diện giao thông"

| Thông tin | Chi tiết |
|-----------|----------|
| 📅 Ngày thi | **29/05/2026** |
| ⏰ Hạn nộp bài | **23/05/2026 (23:59)** |
| 👨‍🏫 Phụ trách | Thầy Nguyên Ba Duy |
| 🤝 Phối hợp | Lê Văn Xin |

---

### 1. Bài Toán

Xây dựng hệ thống nhận diện biển báo giao thông Việt Nam sử dụng trí tuệ nhân tạo (AI).

**Mô tả:** Hệ thống nhận ảnh hoặc video đầu vào chứa biển báo giao thông, tự động phát hiện vị trí biển báo và phân loại chính xác loại biển báo đó. Hệ thống cần có giao diện trực quan để người dùng dễ dàng sử dụng và xem kết quả.

---

### 2. Yêu Cầu Kỹ Thuật

#### 2.1. Đầu vào (Input)
- Ảnh chụp chứa biển báo giao thông (JPG, PNG)
- Hoặc video quay cảnh đường phố có biển báo (MP4, AVI)
- Hoặc luồng video trực tiếp từ webcam (khuyến khích)

#### 2.2. Đầu ra (Output)
- Tên, loại biển báo giao thông được nhận diện
- Vị trí biển báo trong ảnh (bounding box)
- Độ tin cậy của kết quả (confidence score, %)
- Hiển thị kết quả trực quan trên giao diện

#### 2.3. Yêu cầu bắt buộc
- Nhận diện được tối thiểu **10 loại biển báo** giao thông khác nhau
- Có giao diện người dùng (GUI) để upload ảnh/video và xem kết quả
- Giao diện có thể là: web app (Streamlit, Gradio, Flask) hoặc desktop app
- Source code chạy được trên Google Colab hoặc máy tính cá nhân

#### 2.4. Yêu cầu khuyến khích (cộng điểm)
- Nhận diện real-time qua webcam
- Nhận diện trên video (không chỉ ảnh tĩnh)
- Sử dụng/tự thu thập dữ liệu biển báo Việt Nam thực tế
- Tính năng mở rộng: tracking, đếm, cảnh báo âm thanh, dashboard thống kê...
- Số loại biển báo nhận diện được > 20 loại

---

### 3. Công Nghệ Gợi Ý

Các nhóm được tự do lựa chọn công nghệ. Dưới đây là gợi ý tham khảo:

| Thành phần | Công nghệ gợi ý | Ghi chú |
|------------|-----------------|---------|
| Ngôn ngữ | Python 3.10+ | Bắt buộc |
| Model AI | YOLOv8, YOLOv11 | Hoặc model tương đương |
| Framework | PyTorch, TensorFlow | Tùy chọn |
| Giao diện | Streamlit, Gradio, Flask | Bắt buộc có GUI |
| Xử lý video | OpenCV | Nếu xử lý video |
| Training GPU | Google Colab | Miễn phí GPU T4 |
| Gán nhãn dữ liệu | Roboflow, LabelImg | Nếu tự thu thập data |

---

### 4. Dataset (Bộ Dữ Liệu)

#### 4.1. Dataset có sẵn (cung cấp trong Starter Kit)
- **GTSRB** (German Traffic Sign Recognition Benchmark) — 43 loại biển báo, ~50.000 ảnh
- Link: [https://benchmark.ini.rub.de/gtsrb_news.html](https://benchmark.ini.rub.de/gtsrb_news.html)

#### 4.2. Tự thu thập (được cộng điểm)
- Chụp ảnh biển báo giao thông thực tế tại Bình Dương, TP.HCM
- Gán nhãn bằng [Roboflow](https://roboflow.com/) (miễn phí) hoặc LabelImg
- Mỗi loại biển báo cần tối thiểu 50 ảnh để train tốt

> [!TIP]
> Các nhóm tự thu thập dữ liệu biển báo Việt Nam sẽ được **cộng 10% điểm** trong tiêu chí "Dữ liệu Việt Nam".

---

### 5. Tiêu Chí Chấm Điểm

| STT | Tiêu chí | Trọng số | Mô tả chi tiết |
|-----|----------|----------|-----------------|
| 1 | Độ chính xác | **30%** | Số loại biển báo nhận diện được, mAP/F1-score trên tập test chung do BTC cung cấp |
| 2 | Giao diện & Demo | **25%** | UI đẹp, trực quan, dễ sử dụng. Demo chạy mượt, ổn định |
| 3 | Sáng tạo & Mở rộng | **15%** | Tính năng bổ sung: real-time webcam, tracking, cảnh báo, dashboard thống kê... |
| 4 | Tốc độ xử lý | **10%** | FPS khi inference, khả năng xử lý nhanh trên ảnh/video |
| 5 | Dữ liệu Việt Nam | **10%** | Tự thu thập/sử dụng ảnh biển báo VN thực tế |
| 6 | Thuyết trình | **10%** | Trình bày rõ ràng, logic, trả lời Q&A tốt |
| | **TỔNG CỘNG** | **100%** | |

---

### 6. Quy Định Nộp Bài

#### 6.1. Hạn nộp

> [!IMPORTANT]
> **DEADLINE: 23/05/2026 - 23:59**
> Nộp vào mail: **nguyenbaduy@ktkt.edu.vn**

#### 6.2. Nội dung nộp

Mỗi nhóm nộp 1 thư mục nén (`.zip`) với cấu trúc sau:

```
Nhom_X_TenNhom.zip
├── 📂 source_code/          ← Toàn bộ code dự án
│   ├── train.py hoặc train.ipynb
│   ├── app.py               ← File chạy demo
│   ├── requirements.txt     ← Thư viện cần cài
│   └── ...
├── 📂 model/                ← File model đã train
│   └── best.pt              ← Weights tốt nhất
├── 📂 dataset/              ← Dataset (hoặc link Google Drive)
│   └── README.md            ← Mô tả nguồn dataset
├── 📂 demo_video/           ← Video quay demo sản phẩm (2-3 phút)
│   └── demo.mp4
├── 📄 Bao_cao.pdf           ← Báo cáo kỹ thuật (3-5 trang)
└── 📄 README.md             ← Hướng dẫn cài đặt & chạy
```

#### 6.3. Yêu cầu báo cáo kỹ thuật (Bao_cao.pdf)

Báo cáo 3–5 trang, bao gồm:
- Giới thiệu bài toán và mục tiêu
- Mô tả dữ liệu sử dụng (nguồn, số lượng, số lớp)
- Kiến trúc mô hình và phương pháp huấn luyện
- Kết quả đánh giá (accuracy, mAP, F1-score, FPS)
- Hướng dẫn sử dụng hệ thống
- Phân công công việc trong nhóm

---

### 7. Quy Trình Ngày Thi (29/05/2026)

| Thời gian | Nội dung | Ghi chú |
|-----------|----------|---------|
| 08:00 – 08:15 | Khai mạc, giới thiệu Ban giám khảo | |
| 08:15 – 08:30 | Các nhóm setup thiết bị, chuẩn bị demo | |
| 08:30 – 10:00 | Trình bày và Demo (7 phút demo + 3 phút Q&A/nhóm) | 6 nhóm × 10 phút |
| 10:00 – 10:15 | Nghỉ giải lao | |
| 10:15 – 10:45 | Ban giám khảo hội ý, chấm điểm | |
| 10:45 – 11:15 | Công bố kết quả, trao giải | |

---

### 8. Tài Nguyên Tham Khảo

- [Ultralytics YOLOv8](https://docs.ultralytics.com)
- [Roboflow (gán nhãn miễn phí)](https://roboflow.com)
- [Google Colab (GPU miễn phí)](https://colab.research.google.com)
- [Streamlit (tạo web app)](https://streamlit.io)
- [Gradio (tạo demo ML)](https://gradio.app)
- [Dataset GTSRB](https://benchmark.ini.rub.de/gtsrb_news.html)
- [OpenCV (xử lý ảnh/video)](https://opencv.org)

---

### 9. Liên Hệ & Hỗ Trợ

Mọi thắc mắc về đề bài, kỹ thuật, hoặc nộp bài, vui lòng liên hệ:
- 👨‍🏫 **Thầy Nguyên Ba Duy** (phụ trách kỹ thuật)
- 🤝 **Lê Văn Xin** (phối hợp tổ chức)
- 💬 **[Group Zalo cuộc thi](https://zalo.me/g/jbous724jjhkhzn2eogt)** — BETU-traffic-sign-detection

---

> [!CAUTION]
> **LƯU Ý QUAN TRỌNG**
> - Starter Kit (notebook mẫu + dataset mẫu) sẽ được phát cùng đề bài.
> - Các nhóm được khuyến khích sáng tạo và mở rộng vượt xa yêu cầu cơ bản.
> - Sản phẩm phải là công sức của nhóm. **Nghiêm cấm sao chép từ nhóm khác.**
> - BTC sẽ cung cấp tập test riêng vào ngày thi để đánh giá công bằng.

*Bình Dương, ngày 20 tháng 04 năm 2026*

**NGƯỜI PHỤ TRÁCH — Thầy Nguyên Ba Duy**
