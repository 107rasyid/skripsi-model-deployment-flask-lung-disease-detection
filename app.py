import os
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Layer
from tensorflow.keras import backend as K
from tensorflow.keras.utils import custom_object_scope
from flask import Flask, render_template, request, redirect, send_file, url_for
from werkzeug.utils import secure_filename
import matplotlib.pyplot as plt
import zipfile

# Initialize app
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
RESULT_FOLDER = 'static/results'
ZIP_FOLDER = 'static/zips'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER
app.config['ZIP_FOLDER'] = ZIP_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Pastikan folder ada
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)
os.makedirs(ZIP_FOLDER, exist_ok=True)

class Cast(Layer):
    def __init__(self, **kwargs):
        super(Cast, self).__init__(**kwargs)

    def call(self, inputs):
        return tf.cast(inputs, tf.keras.backend.floatx())

    def get_config(self):
        config = super(Cast, self).get_config()
        return config

# Define custom metrics
def iou_metric(y_true, y_pred):
    y_pred = K.cast(y_pred > 0.5, K.floatx())
    intersection = K.sum(K.abs(y_true * y_pred), axis=[1, 2, 3])
    union = K.sum(y_true, axis=[1, 2, 3]) + K.sum(y_pred, axis=[1, 2, 3]) - intersection
    iou = K.mean((intersection + 1e-10) / (union + 1e-10), axis=0)
    return iou

def precision_metric(y_true, y_pred):
    y_pred = K.cast(y_pred > 0.5, K.floatx())
    true_positives = K.sum(y_true * y_pred, axis=[1, 2, 3])
    predicted_positives = K.sum(y_pred, axis=[1, 2, 3])
    precision = K.mean((true_positives + 1e-10) / (predicted_positives + 1e-10), axis=0)
    return precision

def recall_metric(y_true, y_pred):
    y_pred = K.cast(y_pred > 0.5, K.floatx())
    true_positives = K.sum(y_true * y_pred, axis=[1, 2, 3])
    possible_positives = K.sum(y_true, axis=[1, 2, 3])
    recall = K.mean((true_positives + 1e-10) / (possible_positives + 1e-10), axis=0)
    return recall

def f1_metric(y_true, y_pred):
    precision = precision_metric(y_true, y_pred)
    recall = recall_metric(y_true, y_pred)
    f1_score = 2 * (precision * recall) / (precision + recall + 1e-10)
    return f1_score

# Load models
UNET_MODEL_PATH = 'model/skripsi_model_unet.h5'
CNN_MODEL_PATH = 'model/skripsi_model_cnn.h5'

with custom_object_scope({
    'iou_metric': iou_metric,
    'precision_metric': precision_metric,
    'recall_metric': recall_metric,
    'f1_metric': f1_metric,
    'Cast': Cast
}):
    cnn_model = load_model(CNN_MODEL_PATH)
    unet_model = load_model(UNET_MODEL_PATH)

# Preprocessing functions
def apply_clahe(image):
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    return clahe.apply(image)

def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (256, 256))
    img_clahe = apply_clahe(img)
    img_clahe = img_clahe.astype(np.float32) / 255.0
    return img_clahe

# Segmentation using U-Net
def segment_image(image, model, threshold=0.5):
    image_reshaped = np.expand_dims(image, axis=(0, -1))  # Shape: (1, 256, 256, 1)
    pred = model.predict(image_reshaped)
    pred_binary = (pred > threshold).astype(np.uint8)
    return pred_binary[0, :, :, 0]

# Classification using CNN
def classify_image(segmented_image, model):
    segmented_image_rgb = np.repeat(segmented_image[..., np.newaxis], 3, axis=-1)
    predictions = model.predict(np.expand_dims(segmented_image_rgb, axis=0))
    predicted_class = np.argmax(predictions, axis=-1)[0]
    class_labels = ['NORMAL', 'TUBERCULOSIS', 'PNEUMONIA', 'COVID19']
    return predicted_class, class_labels[predicted_class]

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            if not allowed_file(file.filename):
                return "Invalid file type. Please upload an image file."

            # Simpan file yang diupload
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Dummy proses untuk segmentasi dan klasifikasi
            original_image = preprocess_image(filepath)
            predicted_mask = segment_image(original_image, unet_model)
            segmented_image = original_image * predicted_mask
            segmented_image_normalized = segmented_image.astype(np.float32) / np.max(segmented_image)
            predicted_class_idx, predicted_class_label = classify_image(segmented_image_normalized, cnn_model)

            # Simpan citra asli
            original_image_filename = f"original_{filename}"
            original_image_path = os.path.join(app.config['RESULT_FOLDER'], original_image_filename)
            plt.imsave(original_image_path, original_image, cmap='gray')

            # Simpan hasil segmentasi
            result_filename = f"segmented_{filename}"
            result_path = os.path.join(app.config['RESULT_FOLDER'], result_filename)
            plt.imsave(result_path, segmented_image, cmap='gray')

            # Simpan hasil prediksi mask
            mask_result_filename = f"mask_{filename}"
            mask_result_path = os.path.join(app.config['RESULT_FOLDER'], mask_result_filename)
            plt.imsave(mask_result_path, predicted_mask, cmap='gray')

            # Buat file ZIP berisi semua hasil
            zip_filename = f"{filename.rsplit('.', 1)[0]}_results.zip"
            zip_path = os.path.join(app.config['ZIP_FOLDER'], zip_filename)
            with zipfile.ZipFile(zip_path, 'w') as zipf:
                zipf.write(filepath, os.path.basename(filepath))  # Tambah citra asli
                zipf.write(result_path, os.path.basename(result_filename))  # Tambah hasil segmentasi
                zipf.write(mask_result_path, os.path.basename(mask_result_filename))  # Tambah mask prediksi

            # Redirect ke halaman hasil
            return render_template('result.html',
                                   original_image=filename,
                                   result_image=result_filename,
                                   predicted_class=predicted_class_label,
                                   predicted_mask=mask_result_filename,
                                   zip_path=zip_path)

    return render_template('index.html')

@app.route('/download/<path:filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

# Jalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)