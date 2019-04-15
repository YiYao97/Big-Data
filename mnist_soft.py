from __future__ import absolute_import, division, print_function
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image

#read mnist data set
mnist = tf.keras.datasets.mnist
(train_images, train_labels),(test_images, test_labels) = mnist.load_data()
train_images = train_images / 255.0
test_images = test_images / 255.0


checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)
# Create checkpoint callback
cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)

#tensorflow model
def create_model():
    model = tf.keras.models.Sequential( [
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(512, activation=tf.nn.relu),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation=tf.nn.softmax)
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

def train():
    model = create_model()
    model.fit(train_images, train_labels, epochs=5,
             callbacks = [cp_callback])

def evaluate():
    model = create_model()
    model.load_weights(checkpoint_path)
    model.evaluate(test_images, test_labels)

def predict(path):
    model = create_model()
    model.load_weights(checkpoint_path)
    img = Image.open(path).convert("L")
    img2arr = np.array(img)
    img2arr = (np.expand_dims(img2arr,0))
    prediction = model.predict(img2arr)
    return np.argmax(prediction[0])

if __name__ == "__main__":
    #train()
    # evaluate()
     print("Prediction: %d"%predict("/root/Big-Data/3/1004.jpg"))
