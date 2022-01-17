"""OpenCV examples."""

#1
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread('digit.png')[:,:,0]
image = np.invert(np.array([image]))

prediction = model.predict(image)
print("Prediction:{}".format(np.argmax(prediction)))
plt.imshow(image[0])
plt.show()

# oh chee this is last chapter of scan big immage set from tensorflow_ex.py
# that is don't load
