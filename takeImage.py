import csv
import os
import cv2
import numpy as np
import pandas as pd
import datetime
import time


def TakeImage(l1, l2, haarcasecade_path, trainimage_path, message, err_screen, text_to_speech):
    if (l1 == "") and (l2 == ""):
        t = "Please Enter your Enrollment Number and Name."
        text_to_speech(t)
        return
    elif l1 == "":
        t = "Please Enter your Enrollment Number."
        text_to_speech(t)
        return
    elif l2 == "":
        t = "Please Enter your Name."
        text_to_speech(t)
        return

    try:
        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        detector = cv2.CascadeClassifier(haarcasecade_path)
        Enrollment = l1.strip()
        Name = l2.strip()
        sampleNum = 0

        # Create directory safely
        directory = f"{Enrollment}_{Name}"
        path = os.path.join(trainimage_path, directory)
        os.makedirs(path, exist_ok=True)

        print("[INFO] Starting camera. Press 'q' to quit.")

        while True:
            ret, img = cam.read()
            if not ret:
                print("[ERROR] Failed to grab frame.")
                break

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                sampleNum += 1
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

                # Save captured face
                filename = f"{Name}_{Enrollment}_{sampleNum}.jpg"
                cv2.imwrite(os.path.join(path, filename), gray[y:y+h, x:x+w])

                cv2.imshow("Capturing Faces - Press 'q' to Quit", img)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
            elif sampleNum >= 50:
                break

        cam.release()
        cv2.destroyAllWindows()

        # Ensure student details file exists
        os.makedirs("StudentDetails", exist_ok=True)
        with open("StudentDetails/studentdetails.csv", "a+", newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow([Enrollment, Name])

        res = f"Images Saved for Enrollment No: {Enrollment}, Name: {Name}"
        message.configure(text=res)
        text_to_speech(res)
        print("[INFO] Face capture complete!")

    except Exception as e:
        err = f"Error: {str(e)}"
        print(err)
        text_to_speech(err)
        err_screen(err)
