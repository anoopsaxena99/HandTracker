import time

import cv2 #for video camera
import mediapipe as mp
# import time  # checking frame rate

mpHands = mp.solutions.hands #ritual
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0) #0 for primary camera
pTime,cTime=0,0
while True :
    success,img = cap.read() #give us frame
    imgRGB = cv2.cvtColor( img , cv2.COLOR_BGR2RGB )
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks :
        for handLms in results.multi_hand_landmarks :

            mpDraw.draw_landmarks(img , handLms,mpHands.HAND_CONNECTIONS)

    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img , str(int(fps)) ,(20,70) ,cv2.FONT_HERSHEY_PLAIN , 5 , (90,81,255) ,4 )

    cv2.imshow("Image",img)
    cv2.waitKey(1)# no says after how many milisecond frame will be capture but 0 waits for click


