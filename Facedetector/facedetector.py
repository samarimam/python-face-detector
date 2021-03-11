import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# img = cv2.imread('JT.jpg')
# capture a viddeo
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    successful_frame_read, frame = webcam.read()

# covert to grayscale
   
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256),randrange(256), randrange(256)), 4)

    cv2.imshow('Samar Face detector', frame)
    key = cv2.waitKey(1)

    if key==81 or key==113:
        break

webcam.release()
cv2.destroyAllWindows()

print("success")

"""

face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256),randrange(256), randrange(256)), 4)
# print(face_coordinates)

cv2.imshow('Samar Face detector', img)
cv2.waitKey()
print("success")
"""