# Face Recognition-Based Attendance System

An automated, contactless biometric attendance management system built using Python, OpenCV, and Tkinter[cite: 5, 10]. The system detects and recognizes faces in real time from a live camera feed and records subject-wise attendance into lightweight CSV logs[cite: 9, 10, 11].

---
## What steps you have to follow??
- Download or clone my Repository to your device
- type `pip install -r requirements.txt` in command prompt(this will install required package for project)
- Create a `TrainingImage` folder in a project folder.
- open `attendance.py` and `automaticAttendance.py`, change all the path accoriding to your system
- Run `attandance.py` file

---
## Features

- **Student Registration**: Capture facial image datasets mapped to student Enrollment Number and Name[cite: 21, 33].
- **Model Training**: Train a Local Binary Pattern Histogram (LBPH) recognizer with captured facial data[cite: 14, 16].
- **Real-Time Recognition**: Detect faces using Haar Cascade classifiers and identify individuals via webcam feeds[cite: 5, 14].
- **Automated Attendance Logging**: Automatically logs date, time, student ID, and presence status into subject-wise CSV files[cite: 9, 30].
- **Attendance Viewer**: Built-in GUI tables to view attendance records and calculate attendance percentages[cite: 35].
- **Desktop GUI**: Clean, interactive interface powered by Tkinter[cite: 10, 14, 32].

---

## Tech Stack

- **Language**: Python 3.8+[cite: 13]
- **Computer Vision**: OpenCV (`cv2`)[cite: 10, 13]
- **Face Detection**: Haar Cascade (`haarcascade_frontalface_default.xml`)[cite: 13, 16]
- **Face Recognition**: LBPH Face Recognizer (`cv2.face.LBPHFaceRecognizer`)[cite: 10, 14]
- **GUI Framework**: Tkinter[cite: 10, 13]
- **Data Manipulation & Storage**: NumPy, Pandas, CSV[cite: 10, 13]

---

## Project Structure

```text
Attendance-Management-system-using-face-recognition-master/
├── Attendance/
│   └── ML/
│       └── attendance.csv            # Generated attendance logs
├── StudentDetails/
│   └── studentdetails.csv            # Registered student records
├── TrainingImageLabel/
│   └── Trainner.yml                  # Trained facial feature encodings
├── UI_Image/                         # Icons and UI graphic assets
│   ├── back.png
│   ├── cross.png
│   ├── menu.png
│   └── titlesubmit.png
├── haarcascade_frontalface_default.xml
├── main.py                           # Application entry point
└── requirements.txt                  # Python dependencies



