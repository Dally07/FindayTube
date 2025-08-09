import os
import time
import pyautogui

def focus_browser_window():
    # Change "YouTube" par un morceau du titre de ta fenêtre navigateur
    os.system('wmctrl -a "YouTube"')
    time.sleep(0.5)  # attends que la fenêtre soit active

def click_center_video():
    # Position approximative du centre de la vidéo
    # Tu peux ajuster selon ta résolution et fenêtre
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width // 2
    center_y = screen_height // 2
    pyautogui.click(center_x, center_y)
    time.sleep(0.2)

def play_pause():
    focus_browser_window()
    click_center_video()
    pyautogui.press("k")

def next_video():
    focus_browser_window()
    click_center_video()
    pyautogui.hotkey("shift", "n")

def prev_video():
    focus_browser_window()
    click_center_video()
    pyautogui.hotkey("shift", "p")

def search_youtube(query):
    if query:
        pyautogui.hotkey("ctrl", "l")
        time.sleep(0.2)
        pyautogui.typewrite(f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}")
        time.sleep(0.2)
        pyautogui.press("enter")
   
