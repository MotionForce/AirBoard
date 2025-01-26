import pyautogui as p
import time
import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize the data to the range [0, 1]
x_train = x_train / 255.0
x_test = x_test / 255.0

# Add a channel dimension (required for Conv2D layers)
x_train = x_train[..., tf.newaxis]
x_test = x_test[..., tf.newaxis]

# Build the model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')  # 10 classes for digits 0-9
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, batch_size=32)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {test_accuracy:.2f}")

sample_image = np.expand_dims(x_test[0], axis=0)  # Add batch dimension

# Perform inference
predictions = model.predict(sample_image)

# Process the output
predicted_class = np.argmax(predictions, axis=1)  # Get the class with the highest probability
print(f"Predicted Class: {predicted_class[0]}")

# Verify the actual class
actual_class = y_test[0]
print(f"Actual Class: {actual_class}")