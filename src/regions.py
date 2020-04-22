from PIL import Image
import numpy

def getMask(str):
    return numpy.array(Image.open("./regions/" + str + ".png"))
