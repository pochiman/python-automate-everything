import cv2

video = cv2.VideoCapture("video.mp4")
cat = cv2.imread("catface.png",1)
success, frame = video.read()
 
width= frame.shape[1]
height = frame.shape[0]
 
face_cascade = cv2.CascadeClassifier('faces.xml')
 
output= cv2.VideoWriter('catoutput.avi',cv2.VideoWriter_fourcc(*'DIVX'),30,(width,height))
 
count = 0
 
while success:
    faces = face_cascade.detectMultiScale(frame,1.1,4)
    for (x,y,w,h) in faces:
        rscat = cv2.resize(cat,(w,h))
        place = frame[y:y+h,x:x+w]
        cv2.imwrite('rscat.jpg',place)
        blend=cv2.addWeighted(place,0,rscat,1,0)
        cv2.imwrite("fcat.jpg",blend)
        frame[y:y+h,x:x+w] = blend
    output.write(frame)
    success, frame = video.read()
    count += 1
    print(count)

output.release
