import tensorflow as tf
from utils.preprocess import preprocess_image

model = tf.keras.models.load_model("model/leaf_model.h5")

classes = [
    "Healthy Leaf",
    "Bacterial Spot",
    "Early Blight",
    "Late Blight",
    "Leaf Mold"
]

def predict_leaf(image):

    processed = preprocess_image(image)

    prediction = model.predict(processed)

    result = classes[prediction.argmax()]

    confidence = prediction.max()

    return result, confidence
