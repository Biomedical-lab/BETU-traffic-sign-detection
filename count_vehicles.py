"""
🚗 Đếm xe real-time qua webcam — Code mẫu (~30 dòng)
Cuộc thi: "Phát triển hệ thống nhận diện giao thông" — BETU 2026
"""
from ultralytics import YOLO
import cv2

# Tải model YOLOv8 pretrained (tự động download lần đầu)
model = YOLO("yolov8n.pt")

# Các class xe trong COCO dataset
VEHICLE_CLASSES = {2: "car", 3: "motorcycle", 5: "bus", 7: "truck", 1: "bicycle"}

# Mở webcam (0 = camera mặc định)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Nhận diện phương tiện
    results = model(frame, verbose=False)[0]

    # Đếm và vẽ bounding box
    count = {name: 0 for name in VEHICLE_CLASSES.values()}
    for box in results.boxes:
        cls_id = int(box.cls[0])
        if cls_id in VEHICLE_CLASSES:
            name = VEHICLE_CLASSES[cls_id]
            count[name] += 1
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{name} {conf:.0%}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Hiển thị số đếm
    total = sum(count.values())
    info = f"Total: {total} | " + " | ".join(f"{k}: {v}" for k, v in count.items() if v > 0)
    cv2.putText(frame, info, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Vehicle Counter - BETU 2026", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
