import cv2

video = cv2.VideoCapture(1)
success, frame = video.read()

while success:
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break
    success, frame = video.read()

video.release()
cv2.destroyAllWindows()
