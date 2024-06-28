import cv2 as cv
import numpy as np
import mediapipe as mp

def init_cam():
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        print("cannot open camera!")
        exit()
    return cap

def close_cam(cap):
    print("Closing cam!!")
    cap.release()
    cv.destroyAllWindows()

def control_points(cap, hands_obj, win_w, win_h):
    ret, frame = cap.read()
    cp1,cp2,cp3 = None,None,None
    if not ret:
        print("can't receive frame. Exiting...")
        return cp1,cp2,cp3

    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    frame = cv.flip(frame, 1)
    cp = hand_tracking(hands_obj, frame)

    if cp != None:
        #cv.imshow("Hand Tracking",frame)
        #print(w,h)
        for id, lm in enumerate(cp.landmark): 
            if id == 4:
                cp1 = lm.x*win_w, lm.y*win_h
            if id == 8:
                cp2 = lm.x*win_w, lm.y*win_h
            if id == 12:
                cp3 = lm.x*win_w, lm.y*win_h
    return cp1, cp2, cp3
    
    
def hand_obj():
    mp_hands = mp.solutions.hands

    hands_obj = mp_hands.Hands(max_num_hands = 1, min_detection_confidence = 0.56, min_tracking_confidence = 0.55)
    return hands_obj

def hand_tracking(hands_obj, frame):
    
    results = hands_obj.process(frame)
    if results.multi_hand_landmarks:
        handLms = results.multi_hand_landmarks[0]
        return handLms

        return cp
