"""
🚦 DEMO ỨNG DỤNG NHẬN DIỆN BIỂN BÁO GIAO THÔNG
Cuộc thi "Phát triển hệ thống nhận diện giao thông" — BETU 2026

Cách chạy:
    pip install -r requirements.txt
    streamlit run Demo_App.py
"""

import streamlit as st
import cv2
import numpy as np
from PIL import Image
import tempfile
import os

# ============================================================
# CẤU HÌNH TRANG
# ============================================================
st.set_page_config(
    page_title="🚦 Nhận Diện Biển Báo Giao Thông",
    page_icon="🚦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CSS TÙY CHỈNH
# ============================================================
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
        background: linear-gradient(135deg, #1a237e 0%, #0d47a1 50%, #01579b 100%);
        color: white;
        border-radius: 12px;
        margin-bottom: 2rem;
    }
    .main-header h1 {
        color: white;
        font-size: 2rem;
        margin-bottom: 0.3rem;
    }
    .main-header p {
        color: #bbdefb;
        font-size: 1rem;
    }
    .result-box {
        background: #e8f5e9;
        border-left: 4px solid #4caf50;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    .warning-box {
        background: #fff3e0;
        border-left: 4px solid #ff9800;
        padding: 1rem;
        border-radius: 8px;
    }
    .metric-card {
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 1rem;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .stButton > button {
        background: linear-gradient(135deg, #1a237e, #0d47a1);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        font-size: 1rem;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD MODEL
# ============================================================
@st.cache_resource
def load_model(model_path="best.pt"):
    """Tải model YOLOv8 đã train"""
    try:
        from ultralytics import YOLO
        if os.path.exists(model_path):
            model = YOLO(model_path)
            return model, True
        else:
            # Dùng model pretrained mặc định nếu chưa có model riêng
            st.warning(f"⚠️ Không tìm thấy file `{model_path}`. Đang dùng model YOLOv8n mặc định.")
            model = YOLO("yolov8n.pt")
            return model, False
    except Exception as e:
        st.error(f"❌ Lỗi khi tải model: {e}")
        return None, False


def run_detection(model, image, confidence=0.5):
    """Chạy nhận diện trên ảnh"""
    results = model.predict(
        source=image,
        conf=confidence,
        save=False,
        verbose=False
    )
    return results


def draw_results(image, results):
    """Vẽ bounding box và nhãn lên ảnh"""
    annotated = results[0].plot()
    return annotated


def get_detection_info(results):
    """Lấy thông tin các biển báo được phát hiện"""
    detections = []
    if results[0].boxes is not None:
        for box in results[0].boxes:
            cls_id = int(box.cls[0])
            cls_name = results[0].names[cls_id]
            conf = float(box.conf[0])
            bbox = box.xyxy[0].tolist()
            detections.append({
                "class": cls_name,
                "confidence": conf,
                "bbox": bbox
            })
    return detections


# ============================================================
# GIAO DIỆN CHÍNH
# ============================================================
st.markdown("""
<div class="main-header">
    <h1>🚦 Nhận Diện Biển Báo Giao Thông</h1>
    <p>Cuộc thi "Phát triển hệ thống nhận diện giao thông" — BETU 2026</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.markdown("## ⚙️ Cài đặt")
    st.markdown("---")
    
    # Model path
    model_path = st.text_input(
        "📂 Đường dẫn model (.pt)",
        value="best.pt",
        help="Đường dẫn tới file model đã train (best.pt)"
    )
    
    # Confidence threshold
    confidence = st.slider(
        "🎯 Ngưỡng tin cậy (Confidence)",
        min_value=0.1,
        max_value=1.0,
        value=0.5,
        step=0.05,
        help="Chỉ hiển thị kết quả có độ tin cậy >= ngưỡng này"
    )
    
    st.markdown("---")
    st.markdown("## 📋 Hướng dẫn")
    st.markdown("""
    1. Chọn file model đã train
    2. Upload ảnh hoặc video
    3. Xem kết quả nhận diện
    """)
    
    st.markdown("---")
    st.markdown("## 👥 Thông tin nhóm")
    team_name = st.text_input("Tên nhóm:", placeholder="VD: Nhóm 1")
    st.markdown(f"**Nhóm:** {team_name}" if team_name else "")

# ============================================================
# TABS CHÍNH
# ============================================================
tab1, tab2, tab3 = st.tabs(["📸 Nhận diện từ ảnh", "🎥 Nhận diện từ video", "ℹ️ Hướng dẫn"])

# ---------- TAB 1: ẢNH ----------
with tab1:
    st.markdown("### 📸 Upload ảnh chứa biển báo giao thông")
    
    uploaded_file = st.file_uploader(
        "Chọn ảnh (JPG, PNG, JPEG)",
        type=["jpg", "jpeg", "png"],
        key="image_upload"
    )
    
    if uploaded_file is not None:
        # Đọc ảnh
        image = Image.open(uploaded_file)
        image_np = np.array(image)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🖼️ Ảnh gốc")
            st.image(image, use_container_width=True)
        
        # Load model và chạy nhận diện
        with st.spinner("🔄 Đang nhận diện biển báo..."):
            model, is_custom = load_model(model_path)
            
            if model is not None:
                results = run_detection(model, image_np, confidence)
                annotated_image = draw_results(image_np, results)
                detections = get_detection_info(results)
                
                with col2:
                    st.markdown("#### 🎯 Kết quả nhận diện")
                    st.image(annotated_image, channels="BGR", use_container_width=True)
                
                # Thông tin kết quả
                st.markdown("---")
                st.markdown("### 📊 Chi tiết kết quả")
                
                if detections:
                    # Metrics
                    m1, m2, m3 = st.columns(3)
                    with m1:
                        st.metric("🔢 Số biển báo phát hiện", len(detections))
                    with m2:
                        avg_conf = sum(d['confidence'] for d in detections) / len(detections)
                        st.metric("📈 Độ tin cậy trung bình", f"{avg_conf:.1%}")
                    with m3:
                        classes = set(d['class'] for d in detections)
                        st.metric("🏷️ Số loại biển báo", len(classes))
                    
                    # Bảng chi tiết
                    st.markdown("#### Danh sách biển báo phát hiện:")
                    for i, det in enumerate(detections):
                        st.markdown(f"""
                        <div class="result-box">
                            <strong>#{i+1} — {det['class']}</strong><br>
                            Độ tin cậy: <strong>{det['confidence']:.1%}</strong>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="warning-box">
                        ⚠️ Không phát hiện biển báo nào. Thử giảm ngưỡng tin cậy hoặc upload ảnh khác.
                    </div>
                    """, unsafe_allow_html=True)


# ---------- TAB 2: VIDEO ----------
with tab2:
    st.markdown("### 🎥 Upload video chứa biển báo giao thông")
    
    uploaded_video = st.file_uploader(
        "Chọn video (MP4, AVI)",
        type=["mp4", "avi", "mov"],
        key="video_upload"
    )
    
    if uploaded_video is not None:
        # Lưu video tạm
        tfile = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
        tfile.write(uploaded_video.read())
        tfile.close()
        
        st.video(uploaded_video)
        
        if st.button("🚀 Bắt đầu nhận diện video", key="detect_video"):
            model, is_custom = load_model(model_path)
            
            if model is not None:
                cap = cv2.VideoCapture(tfile.name)
                total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                
                stframe = st.empty()
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                frame_count = 0
                total_detections = 0
                
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break
                    
                    frame_count += 1
                    
                    # Xử lý mỗi 3 frame để tăng tốc
                    if frame_count % 3 == 0:
                        results = run_detection(model, frame, confidence)
                        annotated = draw_results(frame, results)
                        detections = get_detection_info(results)
                        total_detections += len(detections)
                        
                        # Hiển thị frame
                        stframe.image(annotated, channels="BGR", use_container_width=True)
                    
                    # Cập nhật progress
                    progress = frame_count / total_frames
                    progress_bar.progress(min(progress, 1.0))
                    status_text.text(f"Frame {frame_count}/{total_frames} | Tổng biển báo phát hiện: {total_detections}")
                
                cap.release()
                st.success(f"✅ Hoàn thành! Đã xử lý {frame_count} frames, phát hiện {total_detections} biển báo.")
        
        # Cleanup
        os.unlink(tfile.name)


# ---------- TAB 3: HƯỚNG DẪN ----------
with tab3:
    st.markdown("""
    ### 📖 Hướng dẫn sử dụng
    
    #### 1. Chuẩn bị model
    - Train model YOLOv8 bằng notebook `Train_YOLOv8_Bien_Bao.ipynb` trên Google Colab
    - Tải file `best.pt` về máy
    - Đặt file `best.pt` cùng thư mục với `Demo_App.py`
    
    #### 2. Chạy ứng dụng
    ```bash
    pip install -r requirements.txt
    streamlit run Demo_App.py
    ```
    
    #### 3. Sử dụng
    - **Tab Ảnh**: Upload ảnh JPG/PNG chứa biển báo → xem kết quả
    - **Tab Video**: Upload video MP4 → bấm nút nhận diện → xem kết quả từng frame
    
    #### 4. Tùy chỉnh
    - Điều chỉnh **ngưỡng tin cậy** ở thanh sidebar để lọc kết quả
    - Đổi đường dẫn model nếu file `best.pt` ở vị trí khác
    
    ---
    
    ### 💡 Gợi ý cải tiến
    
    | # | Ý tưởng | Độ khó |
    |---|---------|--------|
    | 1 | Thêm nhận diện real-time qua webcam | ⭐⭐ |
    | 2 | Thêm dashboard thống kê (biểu đồ) | ⭐⭐ |
    | 3 | Thêm cảnh báo âm thanh | ⭐ |
    | 4 | Thêm tracking biển báo qua video | ⭐⭐⭐ |
    | 5 | Giao diện dark mode | ⭐ |
    | 6 | Export kết quả ra PDF/CSV | ⭐⭐ |
    
    ---
    
    ### 🔗 Tài nguyên
    - [YOLOv8 Docs](https://docs.ultralytics.com/)
    - [Streamlit Docs](https://docs.streamlit.io/)
    - [OpenCV Tutorial](https://docs.opencv.org/)
    """)

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #888;'>"
    "🚦 Cuộc thi Nhận Diện Giao Thông — Ngày hội CNTT BETU 2026 | "
    "Phụ trách: Thầy Nguyên Ba Duy"
    "</p>",
    unsafe_allow_html=True
)
