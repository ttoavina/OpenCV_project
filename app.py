import cv2
import numpy as np
import os
import json


face_path = cv2.CascadeClassifier("C:\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml")

def face_extractor(img):
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    face = face_path.detectMultiScale(gray,1.3,5)
    cropped_face = []
    
    if face in ():
        return None
    
    for(x,y,w,h) in face:
        cropped_face = img[y: y+h,x: x+w]
        return cropped_face
        
    
       
q= 'hey'
count = 0
while 1:
    data = {}
    with open("database.json",'r') as f:
        data = json.load(f)
        
    print(data)
    
    q = input("Entrez le nom d\'utilisateur:")

    if q == '' or q in data["user"]:
        break
    
    cap = cv2.VideoCapture(0)
    count = 0
    path = "C:\\Users\\Toavina\\Desktop\\Projet\\OpenCV\\User\\"+q
    os.mkdir(path)
    data["user"].append(q)
    data["path"].append(path)
    
    with open("database.json",'w') as f:
        json.dump(data , f)
    
    while 1:
        ret , frame = cap.read()
        if face_extractor(frame) is not None:
            count = count+1
            face = cv2.resize(face_extractor(frame),(200,200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            output_path = "C:\\Users\\Toavina\\Desktop\\Projet\\OpenCV\\User\\"+q+"\\"+str(count)+".jpg" 
            val = cv2.imwrite(output_path, face)
            cv2.putText(face,str(count),(50,50), cv2.FONT_HERSHEY_COMPLEX, 1 , (0,255,0) , 2)
            cv2.imshow("face cropper" , face)
            print(val , output_path)
            
        else:
            #print("No face detected!")
            pass
        if cv2.waitKey(1) == 13 or count == 100:
            break
        

    cap.release()
    cv2.destroyAllWindows()
    print("Tout les données collecté")
