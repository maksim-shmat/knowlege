"""Tensorflow about."""

#1 Neural networks

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

X_train = tf.keras.utils.normalize(X_train)
X_test = tf.keras.utils.normalize(X_train)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(units=128, activation='relu'))
model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# training and testing

model.fit(X_train, Y_train, epochs=3)
loss, accuracy = model.evaluate(X_test, Y_test)
print('Loss:', loss)
print('Accuracy:', accuracy)

