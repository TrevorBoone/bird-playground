from keras import layers, Sequential, losses, applications
from keras_cv import models
import matplotlib.pyplot as plt
from dataset import get_datasets, IMAGE_SIZE

RESCALING=layers.Rescaling(1./255)
AUGMENTATION=Sequential([
        layers.RandomFlip('horizontal'),
        layers.RandomRotation(0.1, fill_mode='nearest'),
    ], name='augmentation')
IMAGENET = models.EfficientNetV2Backbone.from_preset(
    "efficientnetv2_b0_imagenet",
    load_weights=True,
    input_shape = (IMAGE_SIZE[0],IMAGE_SIZE[1],3),
    activation = "relu")

def create_model(num_classes, image_size):
    model = Sequential([
        AUGMENTATION,
        models.ImageClassifier(
            num_classes = num_classes,
            pooling = "max",
            activation = "softmax",
            backbone = IMAGENET),
    ])

    model.compile(optimizer='adam',
              loss=losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])
    
    return model

def train(model, data_dir, epochs=15): 
    train_ds, _, validate_ds = get_datasets(data_dir)

    history = model.fit(
        train_ds,
        validation_data=validate_ds,
        epochs=epochs)
    return history

def plot_history(history):
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs_range = range(len(acc))

    plt.figure(figsize=(8, 8))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')
    plt.show()