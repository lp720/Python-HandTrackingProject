import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mphands = mp.solutions.hands
hands = mphands.Hands()
mpdraw = mp.solutions.drawing_utils
handlinestyle = mpdraw.DrawingSpec(color=(0, 255 , 0), thickness = 5)
handpointstyle = mpdraw.DrawingSpec(color=(255, 0 , 0), thickness = 8)

while True:
    ret, img = cap.read()
    if ret:
        imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(imgrgb)
        imgheight = img.shape[0]
        imgwidth = img.shape[1]

        if result.multi_hand_landmarks:
            for handlms in result.multi_hand_landmarks:
                mpdraw.draw_landmarks(img, handlms, mphands.HAND_CONNECTIONS, handlinestyle, handpointstyle)
            #抓取位置
            #for i, lm in enumerate(handlms.landmark):
                #xpos = int(lm.x * imgwidth)
                #ypos = int(lm.y * imgheight)
                #標記幾號點
                #cv2.putText(img, str(i), (xpos-25, ypos+5), cv2.FONT_HERSHEY_SIMPLEX, 0.4 , (0, 0, 255), 2)
                #print(i, xpos, ypos)
        cv2.imshow('img', img)
        
    if cv2.waitKey(1) == ord('q'):
        break