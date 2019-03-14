# import the necessary packages
from PIL import Image
import numpy as np
import urllib

def urlImage(url):
    resp = urllib.request.urlopen(userInput)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    return image