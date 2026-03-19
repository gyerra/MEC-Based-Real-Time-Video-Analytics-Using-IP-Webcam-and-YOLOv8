import cv2
from ultralytics import YOLO
import time

# Load YOLOv8 nano model (auto-download on first run)
model = YOLO("yolov8n.pt")

print("===================================")
print("  MEC AI Video Detection System")
print("===================================")
print("Choose video source:")
print("1 - Laptop Webcam")
print("2 - IP Webcam (Phone Camera)")
print("===================================")

choice = input("Enter choice (1 or 2): ").strip()

if choice == "1":
    cap = cv2.VideoCapture(0)
else:
    stream_url = input(
        "Enter IP Webcam URL (example: http://192.168.43.1:8080/video): "
    ).strip()
    cap = cv2.VideoCapture(stream_url)

if not cap.isOpened():
    print("❌ Error: Unable to open video source.")
    exit(1)

prev_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to receive frame. Check IP or connection.")
        break

    # MEC / Edge AI inference
    results = model(frame, imgsz=640, conf=0.5)

    # Draw detections
    annotated_frame = results[0].plot()

    # FPS calculation
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    cv2.putText(
        annotated_frame,
        f"FPS: {int(fps)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("MEC AI Video Detection (Edge)", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

