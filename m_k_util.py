import pyautogui as util

def display_res():
    return util.size()

def m_move(px, py):
    util.moveTo(px, py, duration = 0.3)

def m_movRel(px,py):
    x,y = util.position()
    #print(f'x:{x},y:{y},px:{px},py:{py},px-x:{px-x},py-y:{py-y}')
    if (x+px >= 1920 or x+px <= 0 or y+py >= 1080 or y+py <= 0):
        return
    util.moveRel(px, py, duration = 0.2)

def m_pos():
    print(util.position())

def m_click():
    px, py = util.position()
    util.click(px, py)

def m_drag(px, py):
    util.dragTo(px, py, duration = 0.1)
    
