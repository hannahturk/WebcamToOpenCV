# webcamToOpenCV.py
# Author: Hannah Turk, Spring 2016
# Code in helper functions modified from pyimagesearch.com

import cv2
import urllib
from urllib.request import urlopen
import numpy as np
import sys
import argparse


# Parse input using -ip flag to enter IP address
parser = argparse.ArgumentParser(description='Input IP address.')
parser.add_argument("-ip", help = "IP Webcam IP address")
args = vars(parser.parse_args())


# Helper function that reads an image from a url
def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


# Helper function that returns OpenCV color detection
# given an imput image. Which color(s) it detects are
# currently hard-coded.
def detect_color(image):
    # define the list of colors to detect
    boundaries = [
        ([1, 1, 1], [75, 75, 255]),     # red
        # ([86, 31, 4], [220, 88, 50]),       # blue
        # ([25, 146, 190], [62, 174, 250]),   # yellow
        # ([103, 86, 65], [145, 133, 128])    # gray
    ]

    outputs = []    # list of color detection outputs

    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")
 
        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask = mask)
        # add color detection output to list of outputs
        outputs.append(output)

    return outputs


if __name__ == "__main__":
    # modify ip address url: adding "/shot.jpg" to the url 
    # displays only the current image from the phone's
    # video feed in the browser
    img_ip = args["ip"]     # input ip address
    img_host_str = "http://" + img_ip + ":8080/shot.jpg"

    while True:
        try:
            img = url_to_image(img_host_str)
            color_outputs = detect_color(img)
            for color in color_outputs:
                cv2.imshow("images", np.hstack([img, color]))
                cv2.waitKey(500)   # wait .5 seconds to get next img 
        except (KeyboardInterrupt, SystemExit):
            print('\nkeyboardinterrupt caught')
            print('\nexiting program!')
            raise

