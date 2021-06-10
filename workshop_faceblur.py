import face_recognition
import cv2
#face = [top, right, bottom, left]
def blurfaces(img):
    kwidth = 17 #kwidth and kheight should be odd
    kheight = 21
    faces = face_recognition.face_locations(img)#top right bottom left
    for face in faces:
        croppedimg = img[face[0]:face[2], face[3]:face[1]]
        blurimg=cv2.blur(croppedimg,(kwidth,kheight))
        img[face[0]:face[2], face[3]:face[1]] = bluring
    return img