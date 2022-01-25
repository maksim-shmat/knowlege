"""Computer vision about."""

import cv2 as cv

# loading images from internet of use your owns

img = cv.imread('cap9.jpg', cv.IMREAD_COLOR)  # or IMREAD_GRAYSCALE for gray colors

cv.imshow('Cap9', img)
cv.waitKey(0)
cv.destroyAllWindows()

# Showing Images With Matplotlib
# import it first

#plt.imshow(img)
#plt.show()

# Converting color schemes

img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
# Craches after close

#2 Loading Video

import cv2 as cv

video = cv.VideoCapture('city.mp4')

while True:
    ret, frame = video.read()
if ret:
    cv.imshow('City Video', frame)
if cv.waitKey(30) == ord('x'):  # 30msec, 1sec == 1000 milliseconds, and 30msec == 33 frames per sec FPS
    break
else:
    break
video.release()
cv.destroyAllWindows()

# Play video in the loop

while True:
    ret, frame = video.read()
if ret:
    cv.imshow('City Video', frame)
if cv.waitKey(30) == ord('x'):
    break
else:
    video = cv.VideoCapture('city.mp4')

#3 Loading camera data

import cv2 as cv

video = cv.VideoCapture(0)
while True:
    ret, frame = video.read()
if ret:
    cv.imshow('City Video', frame)
if cv.waitKey(1) == ord('x'):
    break
else:
    video = cv.VideoCapture('city.mp4')
video.release()
cv.destroyAllWindows()

#4 Fundamental editing, Drawing line, rectangle and circle with openCV

cv.line(img, (50, 50), (250, 250), (255, 255, 0), 15)
cv.rectangle(img, (350, 450), (500, 350), (0, 255, 0), 5)
cv.circle(img, (500, 200), 100, (255, 0, 0), 7)

# Drawing with matplotlib

x_values = np.linspace(100, 900, 50)
y_values = np.sin(x_values)* 100 + 300

plt.imshow(img, cmap='gray')
plt.plot(x_values, y_values, 'c', linewidth=5)
plt.show()

# Copying elements

img[0:200, 0:300] = [0, 0, 0]  # cut left up square from image

copypart = img[300:500, 300:700]
img[100:300, 100:500] = copypart

img[300:500, 300:700] = [0, 0, 0]

# Saving images and videos

cv.imwrite('car_new.jpg', img)  # for image

# for videos

capture = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
writer = cv.VideoWriter('video.avi', fourcc, 60.0, (640, 480))

while True:
    ret, frame = capture.read()
    writer.write(frame)
    cv.imshow('Cam', frame)
    if cv.waitKey(1) == ord('x'):
        break
    capture.release()
    writer.release()
    cv.destroyAllWindows()

#5 Thresholding: insert logo

img1 = cv.imread('laptop.jpg')
img2 = cv.imread('logo.png')

logo_gray = cv.cvtColor(img2, cv.COLOR_RGB2GRAY)
ret, mask = cv.thresholding(logo_gray, 180, 255, cv.THRESH_BINARY_INV)

cv.imshow('Mask', mask)

mask_inv = cv.bitwise_not(mask)
mask_inv = np.invert(mask)  # Alternative way

rows, columns, channels = img2.shape
area = img1[0:rows, 0:columns]

img1_bg = cv.bitwise_and(area, area, mask=mask_inv)
img2_fg = cv.bitwise_and(img2, img2, mask=mask)

result = cv.add(img1_bg, img2_fg)
img1[0:rows, 0:columns] = result

cv.imshow('Result', img1)

#6 Making poorly lit images readable

img = cv.imread('bookpage.jpg')  # img with bad wiev letters
img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
ret, threshold = cv.threshold(img_gray, 32, 255, cv.THRESH_BINARY)

gaus = cv.adaptiveThreshold(img_gray, 255,
        cv.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv.THRESH_BINARY, 81, 4)

cv.imshow('Gaus', gaus)

#7 Filtering
# Creating a filter mask

img = cv.imread('parrot.jpg')  # red parrod, green background
hsv = cv.cvtColor(img, cv.COLOR_RGB2HSV)

minimum = np.array([100, 60, 0])
maximum = np.array([255, 255, 255])

mask = cv.inRange(hsv, minimum, maximum)
result = cv.bitwise_and(img, img, mask=mask)

cv.imshow('Mask', mask)  # red => white, all_other_colors => black

cv.imshow('Result', result)  # red=> red, green=> black

#8 Blurring and smoothing

averages = np.ones((15, 15), np.float32)/225

smoothed = cv.filter2D(result, -1, averages)

cv.imshow('Smoothed', smoothed)  # blurry picture

smoothed2 = cv.filter2D(mask, -1, averages)
smoothed2 = cv.bitwise_and(img, img, mask=smoothed2)
cv.imshow('Smoothed2', smoothed2)

# Gaussian blur

blur = cv.GaussianBlur(result,(15, 15), 0)  # less blurry

# Median blur

median = cv.medianBlur(result, 15)
cv.imshow('Median', median)

median2 = cv.medianBlur(mask, 15)
median2 = cv.bitwise_and(img, img, mask=median2)
cv.imshow('Median2', median2)

# Filtering camera data

import cv2 as cv
import numpy as np

camera = cv.VideoCapture(0)
while True:
    _, img = camera.read()
    hsv = cv.cvtColor(img, cv.COLOR_RGB2HSV)

minimum = np.array([100, 60, 0])
maximum = np.array([255, 255, 255])

mask = cv.inRange(hsv, minimum, maximum)
median = cv.medianBlur(mask, 15)
median = cv.bitwise_and(img, img, mask=median)
cv.imshow('Median', median)
if cv.waitKey(5) == ord('x'):
    break
cv.destroyAllWindows()
camera.release()

# Object Recognition
# Edge detection

import cv2 as cv

img = cv.imread('room.jpg')
edges = cv.Canny(img, 100, 100)
cv.imshow('Edges', edges)

cv.waitKey(0)
cv.destroyAllWindows()  # that's look like a black&white graphucs

# Template matching
# Crop image laptop to one button 'f', with Gimp e.g

img_bgr = cv.imread('workspace.jpg')  # image laptop
img_gray = cv.cvtColor(img_bgr, cv.COLOR_BGR2GRAY)

template = cv.imread('key.jpg', 0)  # key == button 'f' e.g
width, height = template.shape[::-1]

result = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)

threshold = 0.8
area = np.where(result >= threshold)

for pixel in zip(*area[::-1]):
        cv.rectangle(img_bgr, pixel, (pixel[0] + width, pixel[1] + height), (0, 0, 255), 2)

cv.imshow('Result', img_bgr)
cv.waitKey(0)
cv.destroyAllWindows()

# Future Matching

img1 = cv.imread('workspace1.jpg', 0)  # laptop img view high
img2 = cv.imread('workspace2.jpg', 0)  # laptop img view askew perspective
orb = cv.ORB_create()

keypoints1, descriptors1 = orb.detectedAndCompute(img1, None)
keypoints2, descriptors2 = orb.detectedAndCompute(img2, None)

matcher = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
matches = matchrer.match(descriptors1, descriptors2)
matches = sorted(matches, key=lambda x: x.distance)

result = cv.drawMatches(img1, keypoints1, img2, keypoints2, matches[:10], None, flags=2)

result = cv.resize(result,(1600, 900))
cv.imshow('Result', result)
cv.waitKey(0)

# Movement detection (background subtraction)

# Alternative: video = cv.VideoCapture(0)
video = cv.VideoCapture('people.mp4')
subtractor = cv.createBackgroundSubtractorMOG2(20, 50)

while True:
    _, frame = video.read()
    mask = subtractor.apply(frame)

cv.imshow('Mask', mask)

if cv.waitKey(5) == ord('x'):
    break

cv.destroyAllWindows()
video.release()

# Object recognition
# Loading ressources from internet

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')  # license only for your home projects
clock_cascade = cv.CascadeClassifier('clock.xml')  # Nope

# Recognizing faces

img = cv.imread('people.jpg')  # picture with people for recognizing faces
img = cv.resize(img, (1400, 900))

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
faces = faces_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv.putText(img, 'FACE', (x, y+h+30), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

# Recognizing clocks
img = cv.imread('clocks.jpg')
img = cv.resize(img, (1400, 900))

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
clock = clock_cascade.detectMultiScale(gray, 1.3, 10)

for (x, y, w, h) in clocks:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv.putText(img, 'CLOCK', (x, y+h+30), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)


