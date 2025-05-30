import face_recognition
import cv2

# Load known image and encode it
known_image = face_recognition.load_image_file("known.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

# Load unknown image and encode
unknown_image = face_recognition.load_image_file("unknown.jpg")
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

# Compare faces
results = face_recognition.compare_faces([known_encoding], unknown_encoding)

if results[0]:
    print("Face matched!")
else:
    print("Face not matched.")
