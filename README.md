# 🚨 Real-Time Motion Detection System

## 📌 About

This is a real-time **Motion Detection System** built using **Python and OpenCV**. The application uses a webcam to detect movement in the video stream by comparing frames and identifying changes. When motion is detected, it highlights the moving area and updates the status on the screen.

This project is commonly used as a basic foundation for **security surveillance systems**.

---

## ⚙️ Tech Stack

* Python
* OpenCV
* Time module

---

## 🚀 Features

* Real-time motion detection using webcam
* Frame comparison-based detection
* Motion bounding box visualization
* Motion status indicator (Detected / No Motion)
* Threshold visualization window
* Lightweight and fast processing
* Beginner-friendly computer vision project

---

## 🎯 How It Works

* Webcam captures continuous video frames
* First frame is stored as reference background
* Each new frame is compared with the first frame
* Differences are calculated using frame subtraction
* Thresholding highlights motion areas
* Contours detect moving objects
* Bounding boxes are drawn around motion regions

---

## 📂 Project Structure

```text id="m0x7q2"
Motion-Detection-System/
│
├── main.py
├── README.md
```

---

## 📦 Installation

### Clone the Repository

```bash id="c8x1ab"
git clone https://github.com/your-username/motion-detection-system.git
cd motion-detection-system
```

### Install Dependencies

```bash id="d3k9pq"
pip install opencv-python
```

---

## ▶️ Usage

Run the script:

```bash id="e7v2lm"
python main.py
```

---

## 🎮 Controls

| Key | Action           |
| --- | ---------------- |
| Q   | Quit Application |

---

## 📊 Output Screens

* Live camera feed with motion detection boxes
* Threshold window showing detected motion areas
* Status text: "Motion Detected" / "No Motion"

---

## 🔮 Future Enhancements

* Email/SMS alert system on motion detection
* Save motion clips automatically
* Multiple camera support
* AI-based object detection upgrade (YOLO integration)
* Cloud-based surveillance system
* Face recognition + motion hybrid security system

---

## 👨‍💻 Author

**Hitanshu Meshram**
