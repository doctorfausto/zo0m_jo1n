import os
import time
import webbrowser
import json
import pyautogui


def main():
    time_ = time.localtime()
    day = str(time_.tm_wday)
    minute = time_.tm_min
    hour = time_.tm_hour
    schedule_path = os.path.dirname(__file__)

    # can join 15 minutes before class starts
    if minute >= 45 and hour % 2 == 1:
        hour += 1
    hour = str(hour)

    # load the schedule for the day
    with open(os.path.join(schedule_path, 'schedule.json')) as f:
        schedule = json.load(f)[day]

    # find which class is due for the current hour
    for class_ in schedule:
        if hour in class_.split('-'):
            class_url = schedule[class_]
            break

    # open the zoom url, wait 5 seconds and close the tab
    webbrowser.open(class_url)
    time.sleep(5)
    pyautogui.hotkey('alt', 'tab')
    pyautogui.hotkey('ctrl', 'w')


if __name__ == '__main__':
    main()
