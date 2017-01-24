import cv2,os
import numpy as np
from PIL import Image
def facechop(image):  
    facedata = "E:\code\project\Arpit\XXml\haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier(facedata)

    img = cv2.imread(image)

    minisize = (img.shape[1],img.shape[0])
    miniframe = cv2.resize(img, minisize)

    faces = cascade.detectMultiScale(miniframe)

    for f in faces:
        x, y, w, h = [ v for v in f ]
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255))

        sub_face = img[y:y+h, x:x+w]
        face_file_name = "E:\code\project\Arpit\subject102.jpg"
        cv2.imwrite(face_file_name, sub_face)

    cv2.imshow(image, img)

if __name__=="__main__":
    facechop("E:\code\project\Arpit\subject101.jpg")