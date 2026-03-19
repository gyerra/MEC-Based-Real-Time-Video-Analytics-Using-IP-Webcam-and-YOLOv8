# 🎥 MEC-Based-Real-Time-Video-Analytics-Using-IP-Webcam-and-YOLOv8

A lightweight **Edge AI (MEC-based)** real-time video analytics system that performs object detection using **YOLOv8** on live video streams from either a laptop webcam or an IP webcam (mobile camera).

---

## 🚀 Features

- 📹 Supports:
  - Laptop Webcam
  - IP Webcam (Mobile Camera)
- ⚡ Real-time object detection using YOLOv8
- 🧠 Edge AI / MEC-based processing (no cloud dependency)
- 📊 Live FPS display
- 🎯 Uses lightweight YOLOv8 nano model

---

## 🛠️ Tech Stack

- Python  
- OpenCV  
- Ultralytics YOLOv8  
- IP Webcam (Android app)

---

## 📂 Project Structure

```
.
├── .gitignore              # Specifies files to ignore in Git
├── README.md               # Project documentation
├── mec_video_detection.py  # Main script for video detection
└── yolov8n.pt              # Pre-trained YOLOv8 model weights
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/mec-video-analytics.git
cd mec-video-analytics
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

Choose input source:

- `1` → Laptop Webcam  
- `2` → IP Webcam  

If using IP Webcam, enter stream URL:

```
http://<your-ip>:8080/video
```

---

## 📱 How to Use IP Webcam

1. Install **IP Webcam** app on your phone  
2. Start server in the app  
3. Connect both devices to the same WiFi  
4. Copy the video stream URL  
5. Paste it in the terminal  

---

## 🧠 How It Works

- Captures video frames using OpenCV  
- Runs YOLOv8 inference locally (Edge/MEC)  
- Draws bounding boxes on detected objects  
- Displays annotated frames with FPS  

---

## 📸 Output

- Real-time video window with:
  - Object detection boxes  
  - Class labels  
  - FPS counter  

---

## 📦 Requirements

Example `requirements.txt`:

```
opencv-python
ultralytics
```

---

## 🔮 Future Improvements

- Add object tracking (DeepSORT)  
- Deploy on edge devices (Raspberry Pi / Jetson Nano)  
- Build web dashboard for monitoring  
- Add alert system (email/SMS)  

---
