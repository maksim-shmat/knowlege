"""Neuron network about."""
'''
import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = tf.keras.utils.normalize(X_train, axis=1)
X_test = tf.keras.utils.normalize(X_test, axis=1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))  #?
model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))  #?
model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))

# Compiling the model

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Training and testing

model.fit(X_train, y_train, epochs=3)

loss, accuracy = model.evaluate(X_test, y_test)
print(loss)
print(accuracy)

model.save('digits.model')
model = tf.keras.models.load_model('digits.model')

# Classified your own digits

img = cv2.imread('digit.png')[:,:, 0]
img = np.invert(np.array([img]))

prediction = model.predict(img)
print("Prediction:{}".format(np.argmax(prediction)))
plt.imshow(img[0])
plt.show()

#2 Next. Generating texts

import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.layers import Activation, Dense, LSTM

filepath = tf.keras.utils.get_file('shakespeare.txt',
        'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(filepath, 'rb').read().decode(encoding='utf-8').lower()

text = text[300000: 800000]

# Converting text

characters = sorted(set(text))
char_to_index = dict((c,i) for i, c in enumerate(characters))
index_to_char = dict((i, c) for i, c in enumerate(characters))

# Splitting text

SEQ_LENGTH = 40
STEP_SIZE = 3

sentences = []
next_char = []

for i in range(0, len(text) - SEQ_LENGTH, STEP_SIZE):
    sentences.append(text[i:i+SEQ_LENGTH])
    next_char.append(text[i+SEQ_LENGTH])

# Convert to numpy format

x = np.zeros((len(sentences), SEQ_LENGTH,
    len(characters)), dtype=np.bool)
y = np.zeros((len(sentences),
    len(characters)).dtype=np.bool)

for i, satz in enumerate(sentences):
    for i, char in enumerate(satz):
        x[i, t, char_to_index[char]] = 1
        y[i, char_to_index[next_char[i]]] = 1


#3 Build Recurent Neural Network

import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.layers import Activation, Dense, LSTM

model = Sequential()
model.add(LSTM(128, input_shape=(SEQ_LENGTH, len(characters))))
model.add(Dense(len(characters)))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer=RMSprop(lr=0.01))
model.fit(x, y, batch_size=256, epochs=4)

def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds)/temperature
    exp_preds = np.exp(preds)
    preds = exp_preds/np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

def generate_text(length, temperature):
    start_index = random.randint(0, len(text) - SEQ_LENGTH -1)
    generated = ''
    sentence = text[start_index: start_index + SEQ_LENGTH]
    generated += sentence
    for i in range(length):
        x_predictions = np.zeros((1, SEQ_LENGTH, len(characters)))
        for t, char in enumerate(sentence):
            x_predictions[0, t, char_to_index[char]] = 1

    predictions = model.predict(x_predictions, verbose=0)[0]
    next_index = sample(predictions, temperature)
    next_character = index_to_char[next_index]

    generated += next_character
    sentence = sentence[1:] + next_character
    return generated

print(generate_text(300, 0.2))
print(generate_text(300, 0.4))
print(generate_text(300, 0.5))
print(generate_text(300, 0.6))
print(generate_text(300, 0.7))
print(generate_text(300, 0.8))
'''
#4 Image and object recognition

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, layers, models

(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
train_images, test_images = train_images/255.0, test_images/255.0

class_names = ['Plane', 'Car', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

for i in range(16):
    plt.subplot(4, 4, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i][0]])
plt.show()

train_images = train_images[:200000]
train_labels = train_labels[:200000]
test_images = test_images[:4000]
test_labels = test_labels[:4000]

# Building Neural Network

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
        metrics=['accuracy'])
model.fit(train_images,
          train_labels,
          epochs = 10,
          validation_data = (test_images, test_labels))

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)

# Classifying own images
# Download images car and hors from internet.
# Change pictures to 32x32 pixels with Gimp or Paint
img1 = cv.imread('car.jpg')
img1 = cv.cvtColor(img1, cv.COLOR_BGR2BGR)
img2 = cv.imread('horse.jpg')
img2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)
plt.imshow(img1, cmap=plt.cm.binary)
plt.show()

plt.imshow(img1, cmap=plt.cm.binary)
plt.show()

prediction = model.predict(np.array([img1])/255)
index = np.argmax(prediction)
print(class_names[index])
