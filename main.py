import cv2
import os

video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("/Users/saianishmalla/PycharmProjects/sample1/venv/Python_Projects/motion_detector/haarcascade_frontalface_default.xml")

def increase():
    os.system("""osascript -e 'tell application "System Events"' -e 'repeat 32 times' -e 'key code 144' -e 'end repeat' -e ' end tell'""")

def decrease():
    os.system("""osascript -e 'tell application "System Events"' -e 'repeat 32 times' -e 'key code 145' -e 'end repeat' -e ' end tell'""")

motion = []
checker = False

while True:

    check, frame = video.read()
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey_frame, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

    try:
        if faces.any():
            motion.append(True)
    except:
        motion.append(False)

    key = cv2.waitKey(1)

    if len(motion) > 10:
        if all(element == motion[-1] for element in motion[-10:]) and motion[-1] == checker:
            print("IN IF")
            if checker == False:
                decrease()
                checker = True
            else:
                increase()
                checker = False

    print(f"checker: {checker}")
    if key == ord("q"):
        break

video.release()
cv2.destroyAllWindows()