import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

def main():
    """
    1. Load MNIST dataset
    2. Build and train a Convolutional Neural Network (CNN)
    3. Evaluate on test set
    4. Display confusion matrix
    """
    
    # ----------------------
    # 1. Load and Preprocess Data
    # ----------------------
    # TensorFlow/Keras has a built-in MNIST loader
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

    # Normalize images from [0, 255] to [0, 1] for better training
    x_train = x_train / 255.0
    x_test  = x_test  / 255.0

    # MNIST images are 28x28. For CNN, we need a channel dimension (depth = 1 for grayscale).
    # Shape after reshaping: (num_samples, 28, 28, 1)
    x_train = x_train.reshape((x_train.shape[0], 28, 28, 1))
    x_test  = x_test.reshape((x_test.shape[0], 28, 28, 1))

    # ----------------------
    # 2. Build the CNN Model
    # ----------------------
    model = tf.keras.models.Sequential([
        # First convolutional layer
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        tf.keras.layers.MaxPooling2D((2, 2)),

        # Second convolutional layer
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),

        # Flatten the 2D feature maps into a 1D vector
        tf.keras.layers.Flatten(),

        # Dense (fully connected) layer
        tf.keras.layers.Dense(64, activation='relu'),

        # Output layer with 10 neurons (one for each digit class 0-9)
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    # Compile the model with appropriate loss function and optimizer
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    # ----------------------
    # 3. Train the Model
    # ----------------------
    # We'll train for a few epochs (5 is usually enough for a basic example)
    model.fit(x_train, y_train, epochs=5, validation_split=0.2)

    # ----------------------
    # 4. Evaluate on Test Data
    # ----------------------
    test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=2)
    print(f"\nTest Accuracy: {test_accuracy:.4f}")

    # ----------------------
    # 5. Generate Predictions and Confusion Matrix
    # ----------------------
    # Get the predicted class for each image in the test set
    y_pred = model.predict(x_test)
    y_pred_classes = np.argmax(y_pred, axis=1)

    # Compute the confusion matrix
    cm = confusion_matrix(y_test, y_pred_classes)

    # Print the confusion matrix (numeric form)
    print("\nConfusion Matrix (numeric):")
    print(cm)

    # ----------------------
    # 6. Visualize the Confusion Matrix
    # ----------------------
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, cmap='Blues', fmt='d',
                xticklabels=[i for i in range(10)],
                yticklabels=[i for i in range(10)])
    plt.title("Confusion Matrix for MNIST Classification")
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.show()

if __name__ == "__main__":
    main()
