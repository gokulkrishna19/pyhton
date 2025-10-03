# face_recognition_basic.py
# Simple face detection using OpenCV

import cv2

def main():
    # Load the pre-trained Haar Cascade face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Start video capture (0 = default webcam)
    cap = cv2.VideoCapture(0)

    print("🎥 Starting camera... Press 'q' to quit.")

    while True:  # do-while style loop
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Failed to capture frame.")
            break

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        # Draw rectangles around faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Show output
        cv2.imshow("Face Detection", frame)

        # Break on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
