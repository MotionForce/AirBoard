import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split, ParameterGrid
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.regularizers import l2
from tensorflow.keras.optimizers import Adam

# Load the CSV file
csv_file = 'left_hand.csv'  # Replace with your CSV file path
#csv_file = 'right_hand.csv'
data = pd.read_csv(csv_file, header=None)

allowed_labels = {'q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b', 'space'}
#allowed_labels = {'y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm', 'backspace'}
data = data[data.iloc[:, -1].isin(allowed_labels)]

# Separate features (X) and labels (y)
X = data.iloc[:, :-1].values  # All columns except the last one are features
y = data.iloc[:, -1].values   # The last column is the label

# Reshape X to match the input shape for the 1D CNN
num_landmarks = 21
num_features = 3
X = X.reshape(-1, num_landmarks, num_features)  # Reshape to (num_samples, 21, 3)

# Normalize the features
scaler = StandardScaler()
X = X.reshape(-1, num_landmarks * num_features)  # Flatten for scaling
X = scaler.fit_transform(X)
X = X.reshape(-1, num_landmarks, num_features)  # Reshape back to original format

# Encode labels (a to z, none, space, backspace) as integers
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# One-hot encode the labels
num_classes = len(np.unique(y))  # Dynamically determine number of classes
y = to_categorical(y, num_classes)

# Split the data into training, validation, and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.15, random_state=42)

# Function to create the model
def create_model(optimizer='adam', dropout_rate=0.5, num_filters=64, kernel_size=3, pool_size=2, learning_rate=0.0001):
    model = Sequential([
        Conv1D(num_filters, kernel_size=kernel_size, activation='relu', input_shape=(num_landmarks, num_features), padding='same'),
        BatchNormalization(),
        MaxPooling1D(pool_size=pool_size),
        
        Conv1D(128, kernel_size=kernel_size, activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling1D(pool_size=pool_size),
        
        Flatten(),
        Dense(256, activation='relu', kernel_regularizer=l2(0.01)),
        Dropout(dropout_rate),
        Dense(128, activation='relu', kernel_regularizer=l2(0.01)),
        Dropout(dropout_rate),
        Dense(64, activation='relu'),
        Dense(num_classes, activation='softmax')
    ])
    
    model.compile(optimizer=Adam(learning_rate=learning_rate), loss='categorical_crossentropy', metrics=['accuracy'])
    return model# Use the best hyperparameters to create the final model
best_params = {
    'batch_size': 64,
    'dropout_rate': 0.3,
    'epochs': 100,
    'kernel_size': 3,
    'learning_rate': 0.001,
    'num_filters': 128,
    'pool_size': 2
}

# Create the final model with the best hyperparameters
final_model = create_model(
    dropout_rate=best_params['dropout_rate'],
    num_filters=best_params['num_filters'],
    kernel_size=best_params['kernel_size'],
    pool_size=best_params['pool_size'],
    learning_rate=best_params['learning_rate']
)

# Train the final model on the full training set (X_train + X_val)
# Combine X_train and X_val for final training
X_train_full = np.concatenate((X_train, X_val), axis=0)
y_train_full = np.concatenate((y_train, y_val), axis=0)

# Train the model
history = final_model.fit(
    X_train_full, y_train_full,
    validation_data=(X_test, y_test),  # Use the test set for validation during training
    epochs=best_params['epochs'],
    batch_size=best_params['batch_size'],
    callbacks=[
        EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True),
        ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=5)
    ],
    verbose=1
)

# Evaluate the final model on the test set
test_loss, test_accuracy = final_model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_accuracy:.4f}")
print(f"Test Loss: {test_loss:.4f}")

final_model.save('final_left.keras')
#final_model.save('final_right.keras')

# Plot training and validation accuracy and loss
plt.figure(figsize=(12, 5))

# Accuracy Plot
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.grid()

# Loss Plot
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()