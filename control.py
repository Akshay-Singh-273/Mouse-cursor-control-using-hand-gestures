import cv2 as cv
import numpy as np
import mediapipe as mp
import sup_func_tracking as sft
import m_k_util as ut

def dist(p1, p2):
    p1 = np.array((p1[0], p1[1]), dtype = float)
    p2 = np.array((p2[0], p2[1]), dtype = float)
    return np.linalg.norm(p1 - p2)

def control():
    cap = sft.init_cam()
    click = False
    frame = None
    ret = None
    cp = None
    cp1,cp2 = None,None
    h,w,c = None,None,None
    distance = None
    xerror = 6
    yerror = 4
    multi = 4.8
    hands_obj = sft.hand_obj()
    win_w, win_h = ut.display_res()

    print("hand_tracking executing!")

    while True:

        cp1, cp2, cp3 = sft.control_points(cap, hands_obj, win_w, win_h)
        if cp1 == None:
            continue
        d_13 = dist(cp1,cp3)
        d_12 = dist(cp1,cp2)
        #print(distance)

        if d_13 < 50:
            #print("drag!!")
            n_cp1, n_cp2, n_cp3 = sft.control_points(cap, hands_obj, win_w, win_h)

            if n_cp1 == None:
                continue
            if (-cp1[0]+n_cp1[0] < xerror and -cp1[0]+n_cp1[0] > 0) or (-cp1[0]+n_cp1[0] > -xerror and -cp1[0]+n_cp1[0] < 0) and (-cp1[1]+n_cp1[1] < yerror and -cp1[1]+n_cp1[1] > 0 or -cp1[1]+n_cp1[1] > -yerror and -cp1[1]+n_cp1[1] < 0):
                continue
            ut.m_movRel((-cp1[0]+n_cp1[0])*multi, (-cp1[1]+n_cp1[1])*multi)
            #ut.m_move((cp1[0]), (cp1[1]))
            #ut.m_click(cp1[0],cp1[1])
            
        if d_12 < 40 and click == False:
            print("click!!")
            ut.m_click()
            click = True
        if d_12 > 50 and click == True:
            #print('test')
            click = False
                
        if cv.waitKey(1) & 0xff == ord('q'):
            sft.close_cam(cap)
            break

control()
