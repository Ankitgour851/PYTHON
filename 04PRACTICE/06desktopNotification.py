import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water",
            message ="Drinking water is good for health",
            app_icon ="D:\Desktopnotification\icon.ico",
            timeout = 5
        )
        time.sleep(60*60) #Sleep for 1 hour 360 seconds

# Doesn't work in DESKTOP in C drive Work on D drive paste the folder in D drive
#  Run python file in background use pythonw .\main.py and close the file from taskbar to stop