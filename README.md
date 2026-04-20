# 🚦 CUỘC THI: "Phát triển hệ thống nhận diện giao thông"

### Ngày hội Công nghệ Thông tin — BETU 2026

> 📝 **[ĐĂNG KÝ NHÓM TẠI ĐÂY](https://forms.gle/HXa6bXhfoxBKR5KX7)** — ⏰ Hạn đăng ký: **30/04/2026**

| Thông tin | Chi tiết |
|-----------|----------|
| 📅 Ngày thi | **29/05/2026** (Thứ Sáu) |
| ⏰ Hạn nộp bài | **23/05/2026 (23:59)** |
| 👨‍🏫 Phụ trách | Thầy Nguyễn Ba Duy |
| 🤝 Phối hợp | Lê Văn Xin |
| 👥 Nhóm | 2 – 3 sinh viên |

---

## 📌 Chủ Đề Cuộc Thi

> **"Phát triển hệ thống nhận diện giao thông"**
>
> ✅ Sản phẩm **bắt buộc phải kết nối camera**, có thuật toán để **đếm số lượng xe** và **nhận diện hình ảnh các loại xe**.

### Yêu cầu bắt buộc:
- 📷 **Kết nối camera** (webcam laptop hoặc USB camera)
- 🔢 **Đếm số lượng** phương tiện giao thông
- 🚗 **Nhận diện loại xe**: ô tô, xe máy, xe tải, xe buýt, xe đạp (tối thiểu 3 loại)
- 🖥️ **Giao diện demo** trực quan (Streamlit / Gradio / Flask)

### Yêu cầu khuyến khích (cộng điểm):
- 🎯 Tracking xe qua nhiều frame (SORT/DeepSORT)
- 📊 Dashboard thống kê lưu lượng, biểu đồ, heatmap
- 🚧 Phân làn xe, đếm theo hướng
- 🔔 Cảnh báo khi mật độ giao thông cao
- 🇻🇳 Fine-tune model trên dữ liệu giao thông Việt Nam

---

## 📁 Starter Kit

```
Starter_Kit/
├── count_vehicles.py       ← ⭐ Code mẫu đếm xe qua webcam (~45 dòng)
├── Demo_App.py             ← Ứng dụng Streamlit đầy đủ (camera + video + ảnh)
├── requirements.txt        ← Thư viện cần cài
└── README.md               ← File hướng dẫn này
```

---

## 🚀 Bắt Đầu Nhanh

### 1. Cài thư viện

```bash
pip install -r requirements.txt
```

### 2. Chạy code mẫu đếm xe (đơn giản nhất)

```bash
python count_vehicles.py
```
→ Mở webcam, nhận diện xe, đếm real-time. Nhấn `Q` để thoát.

### 3. Chạy ứng dụng Streamlit (đầy đủ)

```bash
streamlit run Demo_App.py
```
→ Mở `http://localhost:8501` → Chọn Webcam / Video / Ảnh → Xem kết quả.

> 💡 **Model tự động tải lần đầu** (`yolov8n.pt` ~6MB), không cần tải thủ công.

---

## 📜 THỂ LỆ CUỘC THI

### 1. Đối tượng & Hình thức
- **Đối tượng**: Sinh viên Khoa KT-CN, Trường ĐH KT-KT Bình Dương
- **Nhóm**: 2 – 3 sinh viên/nhóm
- **Thời gian phát triển**: 4 tuần (26/04 – 23/05/2026)
- **Ngày thi**: 29/05/2026 – Demo trực tiếp trước Ban giám khảo

### 2. Bài toán

**Xây dựng hệ thống kết nối camera để đếm số lượng xe và nhận diện hình ảnh các loại phương tiện giao thông.**

| | Yêu cầu |
|---|---|
| **Input** | 📷 Camera (BẮT BUỘC), video, hoặc ảnh giao thông |
| **Output** | 🚗 Loại xe + 🔢 Số đếm + 📍 Bounding box + 💯 Confidence |
| **Giao diện** | Streamlit / Gradio / Flask — BẮT BUỘC có GUI |

### 3. Tiêu chí chấm điểm

| STT | Tiêu chí | Trọng số | Mô tả |
|-----|----------|----------|-------|
| 1 | Độ chính xác nhận diện | **25%** | Nhận diện đúng loại xe, đếm chính xác |
| 2 | Kết nối camera & Real-time | **25%** | Kết nối camera thành công, xử lý mượt mà |
| 3 | Giao diện & Demo | **20%** | UI trực quan, hiển thị bounding box, số đếm |
| 4 | Sáng tạo & Mở rộng | **15%** | Tracking, phân làn, heatmap, dashboard... |
| 5 | Tốc độ xử lý | **5%** | FPS khi inference qua camera |
| 6 | Thuyết trình | **10%** | Trình bày rõ ràng, trả lời Q&A tốt |
| | **TỔNG CỘNG** | **100%** | |

### 4. Nộp bài

> ⚠️ **DEADLINE: 23/05/2026 — 23:59** → Nộp qua mail: **nguyenbaduy@ktkt.edu.vn**

```
Nhom_X_TenNhom.zip
├── 📂 source_code/       ← Toàn bộ code (app.py, ...)
├── 📂 model/             ← File model (nếu fine-tune)
├── 📂 demo_video/        ← Video demo sản phẩm (2-3 phút)
├── 📄 Bao_cao.pdf        ← Báo cáo kỹ thuật (3-5 trang)
└── 📄 README.md          ← Hướng dẫn cài đặt & chạy
```

### 5. Quy trình ngày thi (29/05/2026)

| Thời gian | Nội dung |
|-----------|----------|
| 08:00 – 08:15 | Khai mạc |
| 08:15 – 08:30 | Setup thiết bị, kết nối camera |
| 08:30 – 10:00 | Demo: 7 phút/nhóm + 3 phút Q&A |
| 10:00 – 10:15 | Giải lao |
| 10:15 – 10:45 | BGK hội ý chấm điểm |
| 10:45 – 11:15 | Công bố kết quả, trao giải |

---

## 🛠️ HƯỚNG DẪN KỸ THUẬT

### A. YOLOv8 — Nhận diện phương tiện

**YOLOv8 pretrained trên COCO** đã nhận diện sẵn các loại xe, **không cần train**:

| Class ID | Tên tiếng Anh | Tên tiếng Việt |
|----------|---------------|----------------|
| 1 | bicycle | Xe đạp |
| 2 | car | Ô tô |
| 3 | motorcycle | Xe máy |
| 5 | bus | Xe buýt |
| 7 | truck | Xe tải |

```python
from ultralytics import YOLO

# Tải model (tự động download lần đầu)
model = YOLO("yolov8n.pt")  # nano (nhanh) | yolov8s.pt (chính xác hơn)

# Nhận diện trên ảnh
results = model("traffic.jpg")
results[0].show()  # Hiển thị kết quả

# Nhận diện trên video
results = model("traffic.mp4", show=True)
```

### B. OpenCV — Kết nối Camera

```python
import cv2

# Mở webcam (0 = camera mặc định)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Xử lý frame ở đây...

    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### C. Kết hợp YOLOv8 + Camera = Đếm xe

```python
from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")
VEHICLES = {2: "car", 3: "motorcycle", 5: "bus", 7: "truck", 1: "bicycle"}

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)[0]

    count = {}
    for box in results.boxes:
        cls_id = int(box.cls[0])
        if cls_id in VEHICLES:
            name = VEHICLES[cls_id]
            count[name] = count.get(name, 0) + 1
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{name} {float(box.conf[0]):.0%}",
                        (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    total = sum(count.values())
    cv2.putText(frame, f"Total: {total}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Vehicle Counter", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
```

### D. Streamlit — Tạo giao diện web

```python
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

model = YOLO("yolov8n.pt")

st.title("🚦 Nhận diện giao thông")
uploaded = st.file_uploader("Upload ảnh", type=["jpg", "png"])

if uploaded:
    image = Image.open(uploaded)
    results = model(np.array(image))[0]

    # Vẽ kết quả
    annotated = results.plot()
    st.image(annotated, caption="Kết quả", use_container_width=True)

    # Đếm xe
    VEHICLES = {2: "car", 3: "motorcycle", 5: "bus", 7: "truck"}
    for box in results.boxes:
        cls_id = int(box.cls[0])
        if cls_id in VEHICLES:
            st.write(f"- {VEHICLES[cls_id]}: {float(box.conf[0]):.0%}")
```

### E. Nâng cao — Tracking với SORT

```python
# pip install sort-tracker
from sort import Sort
import numpy as np

tracker = Sort()

# Trong vòng lặp camera:
#   detections = [[x1, y1, x2, y2, conf], ...]
#   tracked = tracker.update(np.array(detections))
#   Mỗi tracked object có ID riêng → đếm không trùng
```

---

## 📊 So Sánh Các Model YOLOv8

| Model | Kích thước | Tốc độ (FPS) | Độ chính xác | Gợi ý |
|-------|-----------|-------------|-------------|-------|
| `yolov8n.pt` | 6 MB | ~45 FPS | ⭐⭐⭐ | Nhanh, phù hợp laptop yếu |
| `yolov8s.pt` | 22 MB | ~35 FPS | ⭐⭐⭐⭐ | Cân bằng tốc độ/chính xác |
| `yolov8m.pt` | 50 MB | ~20 FPS | ⭐⭐⭐⭐⭐ | Chính xác cao |

> 💡 **Khuyến nghị**: Dùng `yolov8n.pt` để phát triển, chuyển sang `yolov8s.pt` cho bản nộp.

---

## 📎 Tài Nguyên

| Tài nguyên | Link |
|-----------|------|
| YOLOv8 Docs | [docs.ultralytics.com](https://docs.ultralytics.com) |
| OpenCV | [opencv.org](https://opencv.org) |
| Streamlit | [docs.streamlit.io](https://docs.streamlit.io) |
| SORT Tracking | [github.com/abewley/sort](https://github.com/abewley/sort) |
| VisDrone Dataset | [github.com/VisDrone](https://github.com/VisDrone/VisDrone-Dataset) |
| COCO Classes | [cocodataset.org](https://cocodataset.org) |
| Roboflow (gán nhãn) | [roboflow.com](https://roboflow.com) |

---

## ❓ Hỗ Trợ

- 💬 **[Group Zalo cuộc thi](https://zalo.me/g/jbous724jjhkhzn2eogt)** — BETU-traffic-sign-detection
- 👨‍🏫 **Thầy Nguyễn Ba Duy** (phụ trách kỹ thuật)
- 🤝 **Lê Văn Xin** (phối hợp tổ chức)

---

> ⚠️ **LƯU Ý QUAN TRỌNG**
> - Sản phẩm **BẮT BUỘC** kết nối camera và demo real-time ngày thi.
> - Chuẩn bị **laptop có webcam** hoặc **camera USB**.
> - BTC chuẩn bị 02 camera USB dự phòng cho ngày thi.
> - Sản phẩm phải là công sức của nhóm. **Nghiêm cấm sao chép.**

---

**Chúc các nhóm thi tốt! 🎯🚗💨**

*Bình Dương, ngày 20 tháng 04 năm 2026*
**NGƯỜI PHỤ TRÁCH — Thầy Nguyễn Ba Duy**
