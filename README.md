# 🚦 CUỘC THI: "Phát triển hệ thống nhận diện giao thông"

### Ngày hội Công nghệ Thông tin — BETU 2026

> 📝 **[ĐĂNG KÝ NHÓM TẠI ĐÂY](https://docs.google.com/forms/d/e/1FAIpQLSe-N0hmLiP9FC74LOCokDVVs7C-vysAd_o6tz7FKZl8ub_dDA/viewform)** — ⏰ Hạn đăng ký: **30/04/2026**

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
> Sản phẩm **bắt buộc phải kết nối camera** (dùng **điện thoại cá nhân** qua app DroidCam), có thuật toán để **đếm số lượng xe** và **nhận diện hình ảnh các loại xe**.

---

## 📱 CÁCH HOẠT ĐỘNG

> Điện thoại = **camera quay phim** (DroidCam) → Laptop = **bộ não AI** (YOLOv8) → Kết quả hiển thị trên màn hình

```
📱 Điện thoại                💻 Laptop
┌──────────────────┐  WiFi  ┌───────────────────────────┐
│  App DroidCam     │──────►│ Phần mềm SV viết          │
│  (chỉ quay video) │       │ → Nhận hình từ điện thoại  │
│                   │       │ → YOLOv8 detect xe         │
│  Chĩa camera     │       │ → Đếm xe, hiển thị kết quả │
│  ra ngoài đường   │       │ → Chiếu lên máy chiếu      │
└──────────────────┘        └───────────────────────────┘
```

**Điện thoại nào cũng làm được** — chỉ cần có camera + WiFi. Không cần mua thêm thiết bị!

---

## 🗺️ HÀNH TRÌNH SINH VIÊN: TỪ ĐĂNG KÝ → DỰ THI

### Bước 1: 📝 Đăng ký (trước 30/04)
- Lập nhóm 2-3 SV → **[đăng ký tại đây](https://docs.google.com/forms/d/e/1FAIpQLSe-N0hmLiP9FC74LOCokDVVs7C-vysAd_o6tz7FKZl8ub_dDA/viewform)**
- Tham gia [Group Zalo cuộc thi](https://zalo.me/g/jbous724jjhkhzn2eogt)

### Bước 2: 📥 Nhận Starter Kit
- 📦 **[Tải Starter Kit tại đây](https://github.com/Biomedical-lab/BETU-traffic-sign-detection)** (có sẵn trên GitHub)
- Cài thư viện: `pip install -r requirements.txt`
- Chạy thử: `python count_vehicles.py` → xem code mẫu hoạt động

### Bước 3: 📱 Cài DroidCam (5 phút)
- **Điện thoại**: Cài app **DroidCam** (miễn phí) từ Google Play / App Store
- **Laptop**: Tải **DroidCam Client** từ [dev47apps.com](https://dev47apps.com)
- Kết nối cùng WiFi → nhập IP → xong!
- 📺 [Video hướng dẫn DroidCam (tiếng Việt)](https://www.youtube.com/results?search_query=hướng+dẫn+dùng+DroidCam)

### Bước 4: 💻 Phát triển sản phẩm (2-4 tuần)
- Dựa trên code mẫu `Demo_App.py` → chỉnh sửa, mở rộng
- Kết nối điện thoại qua DroidCam → test detect xe real-time
- Làm đẹp giao diện, thêm tính năng sáng tạo
- Test nhiều lần → hoàn thiện

### Bước 5: 📦 Nộp bài (trước 23/05 – 23:59)
- Đóng gói: source code + báo cáo PDF (3-5 trang) + video demo (2-3 phút)
- Nộp file `.zip` qua email: **nguyenbaduy@ktkt.edu.vn**

### Bước 6: 🏆 Ngày thi 29/05
1. **Setup**: Mở laptop → kết nối điện thoại (DroidCam/WiFi) → chạy app
2. **Demo live**: Cầm điện thoại chĩa ra ngoài đường → BGK xem trên máy chiếu
3. **Demo video**: Chạy app trên video BTC cung cấp
4. **Thuyết trình + Q&A** → BGK chấm điểm → Trao giải

---

## � GỢI Ý PHÁT TRIỂN SÁNG TẠO (15% điểm)

> Starter Kit chỉ là **điểm bắt đầu**. Các nhóm cần phát triển thêm tính năng để tạo sự khác biệt!

### ⭐ Mức 1 — Dễ (nên làm)
| Tính năng | Mô tả |
|-----------|-------|
| 🎨 Giao diện đẹp | Thêm CSS, màu sắc theo loại xe, animation |
| 📊 Hiển thị thống kê | Bảng tổng hợp số xe theo loại |
| 📸 Chụp ảnh | Nút chụp & lưu kết quả nhận diện |

### ⭐⭐ Mức 2 — Trung bình (nổi bật)
| Tính năng | Mô tả |
|-----------|-------|
| 📈 Biểu đồ real-time | Chart số xe theo thời gian (dùng `st.line_chart`) |
| 🔔 Cảnh báo | Thông báo khi số xe vượt ngưỡng |
| 📹 Ghi video | Lưu lại video đã detect để xem lại |
| 🎯 Chọn vùng detect | Cho phép vẽ vùng quan tâm (ROI) trên khung hình |

### ⭐⭐⭐ Mức 3 — Nâng cao (điểm cao nhất)
| Tính năng | Mô tả |
|-----------|-------|
| 🆔 Tracking xe | Gán ID từng xe, theo dõi qua nhiều frame (SORT/DeepSORT) |
| 📍 Đếm xe qua vạch | Vẽ counting line, đếm xe đi qua không trùng |
| ️ Heatmap | Bản đồ nhiệt mật độ giao thông |
| 🕐 Lịch sử thống kê | Lưu lại lịch sử đếm xe, so sánh theo thời gian |

---

## �📁 Starter Kit

```
Starter_Kit/
├── count_vehicles.py       ← ⭐ Code mẫu đếm xe qua điện thoại (~50 dòng)
├── Demo_App.py             ← Ứng dụng Streamlit đầy đủ (DroidCam + video + ảnh)
├── requirements.txt        ← Thư viện cần cài
└── README.md               ← File hướng dẫn này
```

---

## 🚀 Bắt Đầu Nhanh

### 1. Cài thư viện
```bash
pip install -r requirements.txt
```

### 2. Cài DroidCam
- 📱 Điện thoại: Tải **DroidCam** từ Google Play / App Store
- 💻 Laptop: Tải **DroidCam Client** từ [dev47apps.com](https://dev47apps.com)
- Kết nối cùng WiFi → mở DroidCam → laptop nhận camera

### 3. Chạy code mẫu
```bash
python count_vehicles.py
```
→ Cầm điện thoại chĩa ra đường → laptop hiện bounding box + đếm xe. Nhấn `Q` để thoát.

### 4. Chạy ứng dụng Streamlit
```bash
streamlit run Demo_App.py
```
→ Mở `http://localhost:8501` → Chọn **Camera Điện thoại** / Video / Ảnh → Xem kết quả.

---

## 📜 THỂ LỆ CUỘC THI

### 1. Đối tượng & Hình thức
- **Đối tượng**: Sinh viên Khoa KT-CN, Trường ĐH KT-KT Bình Dương
- **Nhóm**: 2 – 3 sinh viên/nhóm
- **Thời gian phát triển**: 4 tuần (26/04 – 23/05/2026)
- **Ngày thi**: 29/05/2026 – Demo trực tiếp trước Ban giám khảo

### 2. Bài toán

**Xây dựng hệ thống kết nối camera điện thoại để đếm số lượng xe và nhận diện hình ảnh các loại phương tiện giao thông.**

| | Yêu cầu |
|---|---|
| **Input** | 📱 Camera điện thoại qua DroidCam (BẮT BUỘC), video hoặc ảnh |
| **Output** | 🚗 Loại xe + 🔢 Số đếm + 📍 Bounding box + 💯 Confidence |
| **Giao diện** | Streamlit / Gradio / Flask — BẮT BUỘC có GUI |

### 3. Yêu cầu bắt buộc
- 📱 **Kết nối camera** điện thoại qua DroidCam
- 🔢 **Đếm số lượng** xe theo từng loại (tối thiểu 3 loại)
- 🖥️ **Giao diện** hiển thị bounding box, số đếm, loại xe
- Sản phẩm tự phát triển, hạn chế sao chép

### 4. Yêu cầu khuyến khích (cộng điểm)
- 🎯 Tracking xe qua nhiều frame (SORT/DeepSORT)
- 📊 Dashboard thống kê, biểu đồ số xe theo thời gian
- � Đếm xe qua vạch (counting line), đếm không trùng
- 🔔 Cảnh báo khi mật độ giao thông cao
- 🗺️ Heatmap mật độ, lịch sử thống kê

### 5. Tiêu chí chấm điểm

| STT | Tiêu chí | Trọng số | Mô tả |
|-----|----------|----------|-------|
| 1 | Độ chính xác nhận diện | **25%** | Nhận diện đúng loại xe, đếm chính xác |
| 2 | Kết nối camera & Real-time | **25%** | Kết nối DroidCam thành công, xử lý mượt mà |
| 3 | Giao diện & Demo | **20%** | UI trực quan, hiển thị bounding box, số đếm |
| 4 | Sáng tạo & Mở rộng | **15%** | Tracking, phân làn, heatmap, dashboard... |
| 5 | Tốc độ xử lý | **5%** | FPS khi inference qua camera |
| 6 | Thuyết trình | **10%** | Trình bày rõ ràng, trả lời Q&A tốt |

### 6. Nộp bài

> ⚠️ **DEADLINE: 23/05/2026 — 23:59** → Email: **nguyenbaduy@ktkt.edu.vn**

```
Nhom_X_TenNhom.zip
├── 📂 source_code/       ← Toàn bộ code (app.py, ...)
├── 📂 model/             ← File model (nếu fine-tune)
├── 📂 demo_video/        ← Video demo sản phẩm (2-3 phút)
├── 📄 Bao_cao.pdf        ← Báo cáo kỹ thuật (3-5 trang)
└── 📄 README.md          ← Hướng dẫn cài đặt & chạy
```

### 7. Quy trình ngày thi (29/05/2026)

| Thời gian | Nội dung |
|-----------|----------|
| 08:00 – 08:15 | Khai mạc |
| 08:15 – 08:30 | Setup: kết nối điện thoại (DroidCam), test WiFi |
| 08:30 – 10:00 | Demo: 7 phút/nhóm + 3 phút Q&A |
| 10:00 – 10:15 | Giải lao |
| 10:15 – 10:45 | BGK hội ý chấm điểm |
| 10:45 – 11:15 | Công bố kết quả, trao giải |

---

## 🛠️ HƯỚNG DẪN KỸ THUẬT

### A. Cài đặt DroidCam (biến điện thoại thành camera)

| Bước | Điện thoại 📱 | Laptop 💻 |
|------|-------------|-----------|
| 1 | Tải **DroidCam** từ Store | Tải **DroidCam Client** từ [dev47apps.com](https://dev47apps.com) |
| 2 | Mở app → cấp quyền Camera | Cài đặt → mở app |
| 3 | Ghi nhớ **WiFi IP** hiển thị | Nhập IP → nhấn **Start** |
| 4 | ✅ Điện thoại = camera cho laptop | ✅ Laptop nhận hình từ điện thoại |

> 💡 Cũng có thể kết nối qua **cáp USB** để hình ảnh mượt hơn WiFi.

### B. YOLOv8 — Nhận diện phương tiện

YOLOv8 pretrained trên COCO **đã nhận diện sẵn** xe, không cần train:

| Class ID | Tên | Ghi chú |
|----------|-----|---------|
| 1 | bicycle | Xe đạp |
| 2 | car | Ô tô |
| 3 | motorcycle | Xe máy |
| 5 | bus | Xe buýt |
| 7 | truck | Xe tải |

```python
from ultralytics import YOLO
model = YOLO("yolov8n.pt")  # Tự động tải lần đầu (~6MB)
results = model("traffic.jpg")
results[0].show()
```

### C. Kết hợp Điện thoại + YOLOv8 = Đếm xe

```python
from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")
VEHICLES = {2: "car", 3: "motorcycle", 5: "bus", 7: "truck", 1: "bicycle"}

# Cách 1: DroidCam Client (điện thoại kết nối laptop)
cap = cv2.VideoCapture(0)

# Cách 2: IP Camera
# cap = cv2.VideoCapture("http://192.168.1.x:4747/video")

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

    cv2.putText(frame, f"Total: {sum(count.values())}", (10, 30),
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
    st.image(results.plot(), caption="Kết quả", use_container_width=True)
```

### E. So sánh Model YOLOv8

| Model | Kích thước | Tốc độ | Chính xác | Gợi ý |
|-------|-----------|--------|-----------|-------|
| `yolov8n.pt` | 6 MB | ~45 FPS | ⭐⭐⭐ | Laptop yếu, phát triển |
| `yolov8s.pt` | 22 MB | ~35 FPS | ⭐⭐⭐⭐ | Bản nộp |
| `yolov8m.pt` | 50 MB | ~20 FPS | ⭐⭐⭐⭐⭐ | Laptop mạnh |

---

## 📎 Tài Nguyên

| Tài nguyên | Link |
|-----------|------|
| YOLOv8 Docs | [docs.ultralytics.com](https://docs.ultralytics.com) |
| DroidCam | [dev47apps.com](https://dev47apps.com) |
| OpenCV | [opencv.org](https://opencv.org) |
| Streamlit | [docs.streamlit.io](https://docs.streamlit.io) |
| SORT Tracking | [github.com/abewley/sort](https://github.com/abewley/sort) |
| VisDrone Dataset | [github.com/VisDrone](https://github.com/VisDrone/VisDrone-Dataset) |

---

## ❓ Hỗ Trợ

- 💬 **[Group Zalo cuộc thi](https://zalo.me/g/jbous724jjhkhzn2eogt)**
- 👨‍🏫 **Thầy Nguyễn Ba Duy** (Chịu trách nhiệm chính)
- 🤝 **Lê Văn Xin** (Phối hợp)

---

> ⚠️ **LƯU Ý QUAN TRỌNG**
> - Sản phẩm **BẮT BUỘC** kết nối camera và demo real-time ngày thi.
> - Chuẩn bị **laptop + điện thoại cài sẵn DroidCam**.
> - Phòng thi có **WiFi** cho kết nối DroidCam.
> - Sản phẩm phải là công sức của nhóm. **Nghiêm cấm sao chép.**

---

**Chúc các nhóm thi tốt! 🎯🚗💨**

*Bình Dương, ngày 20 tháng 04 năm 2026*
**NGƯỜI PHỤ TRÁCH — Thầy Nguyễn Ba Duy**
