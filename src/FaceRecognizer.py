'''
Created on 17 Oct 2015

@author: Alanna
'''

from TaskThread import TaskThread
import picamera
import picamera.array
import cv2
import time

class FaceRecognizer(TaskThread):
    def __init__(self):
        TaskThread.__init__(self)
        self.setInterval( 1 )
        cascPath = '/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml'
        self.faceCascade = cv2.CascadeClassifier(cascPath)
        self.subscribers = []
        self.camera = picamera.PiCamera()
        self.camera.resolution = (640,480)
        self.rawCapture = picamera.array.PiRGBArray(self.camera)
        time.sleep(0.1)
                       
    def task(self):
        self.camera.capture(self.rawCapture, format='bgr')
        image = self.rawCapture.array
        gray = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY)
        gray = cv2.transpose( gray )
        faces = self.faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=0
        )
        self.rawCapture.truncate(0)
        for subscriber in self.subscribers:
            subscriber.reportFaces(len(faces)) 
            
    def shutdown(self):
        TaskThread.shutdown(self)
        self.camera.close()
        
    def subscribe(self,subscriber):
        self.subscribers.append( subscriber )
        
