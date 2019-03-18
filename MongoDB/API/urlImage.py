# import the necessary packages
from PIL import Image
import numpy as np
import urllib
import cv2

# this here converts the image to cv2 type 
def urlImage(url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    # return the image 
    return image