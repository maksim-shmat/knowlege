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

# Fundamental editing, Drawing line, rectangle and circle with openCV

cv.line(img, (50, 50), (250, 250), (255, 255, 0), 15)
cv.rectangle(img, (350, 450), (500, 350), (0, 255, 0), 5)
cv.circle(img, (500, 200), 100, (255, 0, 0), 7)

# Drawing with matplotlib

x_values = np.linspace(100, 900, 50)
y_values = np.sin(x_values)* 100 + 300

plt.imshow(img, cmap='gray')
plt.plot(x_values, y_values, 'c', linewidth=5)
plt.show()


