from transformers import pipeline
import re
from PIL import Image
import numpy as np
import tensorflow as tf
from collections import Counter
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions


text_classification_pipeline = pipeline("text-classification", model="bert-base-uncased")
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_task(task_text):
    classification = text_classification_pipeline(task_text)
    sentiment = sentiment_pipeline(task_text)

    importance = "Low"
    category = "General"
    description = "No description available."

    if classification:
        label = classification[0]['label']
        importance_mapping = {
            "LABEL_0": "Low",
            "LABEL_1": "Medium",
            "LABEL_2": "High"
        }
        category_mapping = {
            "LABEL_0": "Work",
            "LABEL_1": "Personal",
            "LABEL_2": "Shopping"
        }
        importance = importance_mapping.get(label, "Low")
        category = category_mapping.get(label, "General")

    if re.search(r'\burgent\b|\basap\b', task_text, re.IGNORECASE):
        importance = "High"
    elif re.search(r'\bdeadline\b|\bimportant\b', task_text, re.IGNORECASE):
        importance = "Medium"
    
    if re.search(r'\bmeeting\b|\bcall\b', task_text, re.IGNORECASE):
        category = "Work"
    elif re.search(r'\bgrocery\b|\bshopping\b', task_text, re.IGNORECASE):
        category = "Shopping"

    description = f"Task: {task_text} | Importance: {importance} | Category: {category} | Sentiment: {sentiment[0]['label']}"
    return importance, category, description

model = VGG16(weights='imagenet')

def get_dominant_colors(image_file, num_colors=5):
    # Open img
    image = Image.open(image_file)
    image = image.convert('RGB')

    # convert image to numpy
    image_array = np.array(image)

    pixels = image_array.reshape(-1, 3)
    
    color_counts = Counter(map(tuple, pixels))
    most_common_colors = color_counts.most_common(num_colors)
    
    # Convert colors to a convenient format
    colors_hex = ['#{:02x}{:02x}{:02x}'.format(*color) for color, _ in most_common_colors]
    
    return colors_hex

def handle_uploaded_image(image_file):
    # Analyze an image to extract primary colors
    dominant_colors = get_dominant_colors(image_file)
    
    image = Image.open(image_file)
    image = image.convert('RGB')

    # Preparing an image for the model
    image = image.resize((224, 224))
    image_array = np.array(image)
    image_array = np.expand_dims(image_array, axis=0)
    image_array = preprocess_input(image_array)

    # Image recognition
    predictions = model.predict(image_array)
    decoded_predictions = decode_predictions(predictions, top=3)[0]

    # Create a list of colors with a HEX code
    color_boxes = [{'hex': color} for color in dominant_colors]

    result = {
        'description': ', '.join([f"{desc} ({prob:.2f})" for (_, desc, prob) in decoded_predictions]),
        'colors': color_boxes
    }

    return result