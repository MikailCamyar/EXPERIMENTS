import cv2 
from adafruit_servokit import ServoKit 
mykit = ServoKit(channels = 16)
pan = 0
tilt= 120 

width = 640 
height = 480


mykit.servo[0].angle=pan 
mykit.servo[1].angle=tilt 




cam=cv2.VideoCapture(0)


face_cascade = cv2.CascadeClassifier("/home/miki/Desktop/pyPro/cascade/face.xml")
eye_cascade = cv2.CascadeClassifier("/home/miki/Desktop/pyPro/cascade/eye.xml")


while True  :
    ret, frame = cam.read() 

    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayFrame,1.3,5)
    for x,y,w,h in faces: 
        
        Xcent = x+w/2 
        Ycent = y+h/2 
        errorPan  = int(Xcent-width/2)  
        errorTilt = int(Ycent-height/2) 
        if abs(errorPan)>9:
                pan=pan-errorPan/40
        if abs(errorTilt)>9 :
                tilt = tilt + errorTilt/40
        if pan>180: 
                pan= 180 
                print("pan out of range") 
        if pan<0: 
                pan=0 
                print("pan out of range")
        if tilt>180: 
                tilt= 180 
                print("tilt out of range")
        if tilt<0: 
                tilt= 0 
                print("pan out of range")
        
        mykit.servo[0].angle = pan 
        mykit.servo[1].angle = tilt
        
        roi_gray=grayFrame[y:y+h,x:x+w]
        roi_color= frame[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes: 
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),1)
            cv2.rectangle(frame,(x,y),(x+w,w+h),(255,0,0),1)
        break
    cv2.imshow('webcam', frame) 
    if cv2.waitKey(1) == ord('q'):
        break  
cam.release() 
cv2.destroyAllWindows()