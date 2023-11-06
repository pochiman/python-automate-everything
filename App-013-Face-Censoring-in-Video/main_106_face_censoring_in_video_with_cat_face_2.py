import cv2
 
video = cv2.VideoCapture(0)
success, frame = video.read()
catfaceimg = cv2.imread('catface.png')
 
height = frame.shape[0]
width = frame.shape[1]
face_cascade = cv2.CascadeClassifier('faces.xml')
 
# creating a new video
output = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, (width, height))
 
count = 0
while success:
    faces = face_cascade.detectMultiScale(frame, 1.1, 5)
    for (x, y, w, h) in faces:
        cat_face_resized = cv2.resize(catfaceimg, (w, h))
        frame[y:y + h, x:x + w] = cat_face_resized
    cv2.imshow("Recording", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    success, frame = video.read()
    count +=1
output.release()
video.release()
cv2.destroyAllWindows()
