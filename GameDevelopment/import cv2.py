import cv2

vid = cv2.video
i = 0
while True:
    ret, frame = vid.red()
    if ret:
        cv2.imwrite("image/image_{}_final.png".format(i), frame)
        cv2.imshow("result", frame)
        i += 1
        if cv2.waitkey(1) == 27 or i > 50:
            break
        else:
            print("camera not found: ")
vid.release()
cv2.destroyallwindow()
