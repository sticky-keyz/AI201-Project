import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
pTime = 0
while True:
    
    #Find hand Landmarks
    #get the tip of index and middle fingers
    #check which is up
    #only index finger: is in  moving mode
        # Convert Coordinates
    #smooth values
    #move mouse
    #is in clickng mode
    #click
    #frame rate
    #display
    
    
    # find Hand LankMarks: 
    sucess, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print("[INFO] handmarks: {}".format(results.multi_hand_landmarks))

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for  lm in hand_landmarks.landmark:
                height, width, channel = img.shape
                cx, cy = int(lm.x * width), int(lm.y * height)
                cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    
    # frame rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20,50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    # Display
    cv2.imshow("AI MOUSE.exe", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
