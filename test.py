import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
from keras.models import load_model

num_landmarks = 21
num_features = 3
3
# Load the test data
test_csv_file = 'left_hand.csv'  # Replace with your test CSV file path
test_data = pd.read_csv(test_csv_file, header=None)

allowed_labels = {'q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b', 'space'}
#allowed_labels = {'y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm', 'backspace'}
test_data = test_data[test_data.iloc[:, -1].isin(allowed_labels)]

# Separate features (X_test_new) and labels (y_test_new) for the test data
X_test_new = test_data.iloc[:, :-1].values  # All columns except the last one are features
y_test_new = test_data.iloc[:, -1].values   # The last column is the label

label_encoder = LabelEncoder()
y_test_new = label_encoder.fit_transform(y_test_new)
num_classes = len(np.unique(y_test_new))  # Dynamically determine number of classes

# Reshape X_test_new to match the input shape for the 1D CNN
X_test_new = X_test_new.reshape(-1, num_landmarks, num_features)  # Reshape to (num_samples, 21, 3)

# Encode labels (a to z, none, space, backspace) as integers (if y_test_new contains labels)
y_test_new_encoded = label_encoder.transform(y_test_new)  # Convert labels to integers (0 to 28)

# One-hot encode the labels (if y_test_new contains labels)
y_test_new_onehot = to_categorical(y_test_new_encoded, num_classes)  # Convert to one-hot encoded vectors

# Get the model's predictions on the test data
model = load_model('models/final_left.keras')
predictions = model.predict(X_test_new)

# Convert predictions from probabilities to class labels
predicted_labels = np.argmax(predictions, axis=1)

# Decode the predicted labels back to their original string labels
predicted_labels_decoded = label_encoder.inverse_transform(predicted_labels)

# Print the predicted labels
print("Predicted Labels:", predicted_labels_decoded)