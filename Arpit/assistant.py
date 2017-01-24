import cv2,os
import numpy as np
from PIL import Image
import time
try:

    os.remove('E:\code\project\Arpit\subject100.sad')
    os.remove('E:\code\project\Arpit\subject101.jpg')
    os.remove('E:\code\project\Arpit\subject102.jpg')
    os.remove('E:\code\project\Arpit\.idea')
except:
    pass
# Camera 0 is the integrated web cam
camera_port = 0
po=""
 
#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30
 
# Now we can initialize the camera capture object with the cv2.VideoCapture class.
camera = cv2.VideoCapture(camera_port)
def get_image():
	# read is the easiest way to get a full image out of a VideoCapture object.
	retval, im = camera.read()
	return im
 
# to adjust light levels, if necessary
for i in xrange(ramp_frames):
	temp = get_image()
print("Taking image...")
# Take the actual image we want to keep
camera_capture = get_image()
file = r"E:\code\project\Arpit\subject101.jpg"
cv2.imwrite(file, camera_capture)
 
#release the camera
del(camera)

'''IMAGE HAS BEEN CAPTURED !!!!!'''

import test1
test1.facechop("E:\code\project\Arpit\subject101.jpg")
'''IMAGE HAS BEEN CROPPED !!!!'''

img = cv2.imread('E:\code\project\Arpit\subject102.jpg')
 
height, width = img.shape[:2]
res = cv2.resize(img,(3*width-20, 2*height+40), interpolation = cv2.INTER_CUBIC)
face_file_name = "E:\code\project\Arpit\subject100.jpg"
cv2.imwrite(face_file_name, res)

'''IMAGE HAS BEEN RESIZED!!!!'''


thisFile = "subject100.jpg"
base = os.path.splitext(thisFile)[0]
os.rename(thisFile, base + ".sad")

'''EXTENSION HAS BEEN CHANGED SUCCESSFULLY'''


# For face detection we will use the Haar Cascade provided by OpenCV.
cascadePath = "E:\code\project\Arpit\XXml\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

# For face recognition we will the the LBPH Face Recognizer (LOCAL BINARY PATTERNS HISTOGRAM)
recognizer = cv2.createLBPHFaceRecognizer()


def get_images_and_labels(path):
    # Append all the absolute image paths in a list image_paths
    image_paths = [os.path.join(path, f).replace("\\","/") for f in os.listdir(path) if (not f.endswith('.sad') and not f.endswith('.py') and not f.endswith('.jpg') and not f.endswith('.pyc'))]
    # images will contains face images
    #print(image_paths)
    image_paths.remove('E:/code/project/Arpit/XXml')
    image_paths.remove('E:/code/project/Arpit/geodata.sqlite')
    image_paths.remove('E:/code/project/Arpit/where.html')
    image_paths.remove('E:/code/project/Arpit/where.js')
    image_paths.remove('E:/code/project/Arpit/where.data')
    try:
        image_paths.remove('E:\code\project\Arpit\.idea')
    except:
        pass
    images = []
    # labels will contains the label that is assigned to the image
    labels = []
    for image_path in image_paths:
        # Read the image and convert to grayscale
        image_pil = Image.open(image_path).convert('L')
        # Convert the image format into numpy array
        image = np.array(image_pil, 'uint8')
        # Get the label of the image
        nbr = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
        # Detect the face in the image
        faces = faceCascade.detectMultiScale(image)
        # If face is detected, append the face to images and the label to labels
        for (x, y, w, h) in faces:
            images.append(image[y: y + h, x: x + w])
            labels.append(nbr)
            cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
            cv2.waitKey(50)
    # return the images list and labels list
    #print labels
    return images, labels
# Path to the DataBase
path = 'E:\code\project\Arpit'
# Call the get_images_and_labels function and get the face images and the 
# corresponding labels
images, labels = get_images_and_labels(path)
cv2.destroyAllWindows()

# Perform the training
recognizer.train(images, np.array(labels))

# Append the images with the extension .sad into image_paths
image_paths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.sad')]
for image_path in image_paths:
    #global po
    predict_image_pil = Image.open(image_path).convert('L')
    predict_image = np.array(predict_image_pil, 'uint8')
    faces = faceCascade.detectMultiScale(predict_image)
    #print 'c'
    if faces ==():
		while True:
			#global po
			po=raw_input("Login through face detection failed !! Please provide your default password to login: ")
			if po=="Password" or po=="password":
				#name='P'
				break
			else:
				print "Incorrect Password TRY AGAIN !!"
    for (x, y, w, h) in faces:
        nbr_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w])
        nbr_actual = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
	#print (type(nbr_actual))
        #print nbr_predicted,nbr_actual,conf
	if conf<=5000:
			print "{} is Correctly Recognized with confidence {}".format(nbr_predicted, conf)
			print "LOGIN SUCCESSFUL"
			'''try:
				assert nbr_predicted<=14
				name="P"
			except:
				name="A"'''
	else:
		while True:
			#global po
			po=raw_input("Login through face detection failed !! Please provide your default password to login: ")
			print conf
			if po=="Password" or po=="password":
				break
			else:
				print "Incorrect Password TRY AGAIN !!"
			
		
        
        #cv2.imshow("Recognizing Face", predict_image[y: y + h, x: x + w])
        #cv2.waitKey(1000)
#print name
'''elif x=="Password1":
				name='A'
				break'''
				
'''elif x=="Password1":
				name='A'
				break'''				
if po =="password" or po=="Password" or conf<5000:
    import arpit
else:
    print("Shutting Down")
    time.sleep(2)
    exit(0)




try:

    #os.remove('E:\code\project\Arpit\subject100.sad')
    #os.remove('E:\code\project\Arpit\subject101.jpg')
    #os.remove('E:\code\project\Arpit\subject102.jpg')
    os.remove('E:\code\project\Arpit\.idea')
except:
    pass