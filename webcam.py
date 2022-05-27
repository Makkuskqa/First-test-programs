import cv2 
# inicialization WEbc
cap = cv2.VideoCapture(0)  

while(True):                          
    ret, frame = cap.read()

    cv2.imshow('Original', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


