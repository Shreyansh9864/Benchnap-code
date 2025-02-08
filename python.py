import cv2
from deepface import Deepface

harc_ascade = r"C:\Users\rahul\Downloads\haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(harc_ascade)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        # face_roi = frame[y:y + h, x:x + w]
        # face_roi = face_roi.astype('uint8')

        try:
            result = deepface.analyze(frame, actions=["emotion"], enforce_detection=False)
            dominant_emotion = result
            print(dominant_emotion)
            font = cv2.FONT_HERSHEY_SIMPLEX
            dominant_emotion = result[0]["dominant_emotion"]
            cv2.putText(frame, dominant_emotion, (x, y - 10), font, 0.9, (0, 255, 0), 2, cv2.LINE_AA)
        except Exception as e:
            print(f"Error analyzing face: {e}")

    cv2.imshow("frame", frame)
    if cv2.waitKey(2) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
