import tkinter 
import tkinter.ttk
from tkinter.filedialog import askopenfilename
import cv2
import workshop_faceblur
def blurfile():
    path = askopenfilename()
    img = cv2.imread(path)
    img =faceblur.blurfaces(img)
    cv2.imshow("Blured image",img)
def blurwebcam():
    cam = cv2.VideoCapture(0)
    while True:
        ret, img = cam.read()
        img =workshop_faceblur.blurfaces(img)
        cv2.imshow("WEBCAM", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
window = tkinter.Tk()
window.title("Face Blurring Software")
window.minsize(300,300)
logo = tkinter.PhotoImage(file = "icon.png")
window.iconphoto(False, logo)
imageLabel = tkinter.ttk.Label(window, image = logo)
imageLabel.grid()
textLabel = tkinter.ttk.Label(window, text = "Face Blurring Software \n Press the button to start blurring")
textLabel.grid()
fileButton = tkinter.ttk.Button(window, text = "Blur Image File", command = blurfile)
fileButton.grid()
webcamButton = tkinter.ttk.Button(window, text = "Blur Webcam", command = blurwebcam)
webcamButton.grid()
window.mainloop()