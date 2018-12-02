from datetime import datetime
from picamera import PiCamera

def takePicture(fileName):
    camera = PiCamera()
    camera.capture('./'+fileName+'.png')
    camera.close()


takePicture("{0:%Y}-{0:%m}-{0:%d}-{0:%H}-{0:%M}-{0:%S}".format(datetime.now())+'.png')

