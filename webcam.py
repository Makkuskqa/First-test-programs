import cv2     #cv2 you must install
# inicialization WEbc
cap = cv2.VideoCapture(0)  

while(True):                          
    ret, frame = cap.read()

    cv2.imshow('Original', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


