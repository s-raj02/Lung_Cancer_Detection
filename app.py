from flask import Flask, render_template, url_for, request
import sqlite3

import numpy as np
from tensorflow.keras.models import load_model
import pickle
import shutil
from tensorflow.keras.preprocessing import image


import shutil
import cv2
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.preprocessing.image import  img_to_array , array_to_img
import numpy as np  # dealing with arrays
import os  # dealing with directories
from random import shuffle  # mixing up or currently ordered data that might lead our network astray in training.
import os
import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import matplotlib.pyplot as plt

from keras.preprocessing.image import img_to_array

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import load_img
from keras.preprocessing.image import load_img
from keras.preprocessing import image



import random
import shutil
import pickle
import sqlite3
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array







# Load the trained model
model = load_model('ResNet50_model.h5')

# Load class names from the pickle file
with open('class_names.pkl', 'rb') as f:
    class_names = pickle.load(f)

def predict_image(image):
    img =load_img(image, target_size=(150, 150))
    img_array =img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    
    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction)
    print(predicted_class_index)
    predicted_class = class_names[predicted_class_index]
    print("predicted_class:",predicted_class)
    prediction1 = prediction.tolist()
    print(prediction1[0][predicted_class_index]*100)
    return predicted_class, prediction1[0][predicted_class_index]*100

connection = sqlite3.connect('user_data.db')
cursor = connection.cursor()

command = """CREATE TABLE IF NOT EXISTS user(name TEXT, password TEXT, mobile TEXT, email TEXT)"""
cursor.execute(command)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/userlog', methods=['GET', 'POST'])
def userlog():
    if request.method == 'POST':

        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']

        query = "SELECT name, password FROM user WHERE name = '"+name+"' AND password= '"+password+"'"
        cursor.execute(query)

        result = cursor.fetchall()

        if len(result)==0:
            return render_template('index.html',msg='Sorry, Incorrect Credentials Provided,  Try Again')
        else:
            return render_template('userlog.html')

    return render_template('index.html')


@app.route('/userreg', methods=['GET', 'POST'])
def userreg():
    if request.method == 'POST':

        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']
        mobile = request.form['phone']
        email = request.form['email']
        
        print(name, mobile, email, password)

        command = """CREATE TABLE IF NOT EXISTS user(name TEXT, password TEXT, mobile TEXT, email TEXT)"""
        cursor.execute(command)

        cursor.execute("INSERT INTO user VALUES ('"+name+"', '"+password+"', '"+mobile+"', '"+email+"')")
        connection.commit()

        return render_template('index.html', msg='Successfully Registered')
    
    return render_template('index.html')



@app.route('/userlog.html', methods=['GET'])
def indexBt():
      return render_template('userlog.html')

@app.route('/graph.html', methods=['GET', 'POST'])
def graph():
    images = ['http://127.0.0.1:5000/static/accuracy_plot.png',
              'http://127.0.0.1:5000/static/loss_plot.png',
              'http://127.0.0.1:5000/static/confusion_matrix.png']
    content=['Accuracy Graph', 'Loss Graph','Confusion Matrix']
    return render_template('graph.html', images=images, content=content)


@app.route('/image', methods=['GET', 'POST'])
def image():
    if request.method == 'POST':
        fileName = request.form['filename']
        Type = request.form['diseaseType']
        
        if Type=="ResNet":
            model = load_model('ResNet50_model.h5')
        
        elif Type=="Vgg":
            
            model = load_model('VGG16_model.h5')
        else:
            raise ValueError("Invalid model type. Choose 'ResNet', or 'VGG'.")






        # Clear the images folder
        dirPath = "static/images"
        if os.path.exists(dirPath):
            shutil.rmtree(dirPath)
        os.makedirs(dirPath)

        fileName = request.form['filename']
        dst = "static/images"
        shutil.copy("upload/" + fileName, dst)
        image_path = "upload/" + fileName

        # Preprocess images
        image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('static/gray.jpg', gray_image)
        edges = cv2.Canny(image, 250, 254)
        cv2.imwrite('static/edges.jpg', edges)
        _, threshold = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
        cv2.imwrite('static/threshold.jpg', threshold)

        kernel_sharpening = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        sharpened = cv2.filter2D(image, -1, kernel_sharpening)
        cv2.imwrite('static/sharpened.jpg', sharpened)

        predicted_class, accuracy = predict_image("upload/"+fileName)
        print("Predicted class:", predicted_class)
        print("Accuracy is:", accuracy)
       
        f = open('acc.txt', 'w')
        f.write(str(accuracy))
        f.close()


       

       

        # Define treatment suggestions
        treatments = {
            "adenomacarcinoma": [
                "Surgery to remove the tumor or affected bone.",
                "Radiation therapy for shrinking or killing cancer cells.",
                "Chemotherapy for aggressive or metastatic cases."
            ],
            "cancer_final_stage": [
                "Lumpectomy or mastectomy (surgical removal).",
                "Chemotherapy or hormone therapy depending on hormone receptor status.",
                "Radiation therapy to prevent recurrence."
            ],
            "cancer_stage1": [
                "Antiviral medications (e.g., Paxlovid, Remdesivir) for severe cases.",
                "Oxygen therapy and ventilatory support if needed.",
                "Symptomatic treatment with fever reducers and hydration."
            ],
            "cancer_stage2": [
                "Surgery for early-stage tumors.",
                "Targeted therapy or immunotherapy for advanced stages.",
                "Chemotherapy and radiation therapy for non-surgical cases."
            ],
            "large_cell_carcinoma": [
                "Antibiotics for bacterial pneumonia.",
                "Oxygen therapy for severe respiratory distress.",
                "Cough suppressants and fever reducers for symptom relief."
            ],
            "squamous_cell_carcinoma": [
                "Long-term antibiotic regimen (e.g., Rifampin, Isoniazid).",
                "Directly observed therapy (DOT) to ensure medication adherence.",
                "Supportive care with proper nutrition and rest."
            ]
        }

        treatment_list = treatments.get(predicted_class, ["No specific treatment required."])

        f = open('acc.txt', 'r')
        accuracy = f.read()
        f.close()
        print(accuracy)



        return render_template('results.html', 
                               status=predicted_class,
                               accuracy=accuracy,
                               Treatment=treatment_list,
                               ImageDisplay=f"http://127.0.0.1:5000/static/images/{fileName}",
                               ImageDisplay1="http://127.0.0.1:5000/static/gray.jpg",
                               ImageDisplay2="http://127.0.0.1:5000/static/edges.jpg",
                               ImageDisplay3="http://127.0.0.1:5000/static/threshold.jpg",
                               ImageDisplay4="http://127.0.0.1:5000/static/sharpened.jpg")
                               
    return render_template('userlog.html')





##########################################VGGG########################################################


#model=Load the trained model
model = load_model('VGG16_model.h5')

# Load class names from the pickle file
with open('class_names.pkl', 'rb') as f:
    class_names = pickle.load(f)

def predict_image(image):
    img =load_img(image, target_size=(150, 150))
    img_array =img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    
    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction)
    print(predicted_class_index)
    predicted_class = class_names[predicted_class_index]
    print("predicted_class:",predicted_class)
    prediction1 = prediction.tolist()
    print(prediction1[0][predicted_class_index]*100)
    return predicted_class, prediction1[0][predicted_class_index]*100



@app.route('/image', methods=['GET', 'POST'])
def vgg():
    if request.method == 'POST':
        # Clear the images folder
        dirPath = "static/images"
        if os.path.exists(dirPath):
            shutil.rmtree(dirPath)
        os.makedirs(dirPath)

        fileName = request.form['filename']
        dst = "static/images"
        shutil.copy("upload/" + fileName, dst)
        image_path = "upload/" + fileName

        # Preprocess images
        image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('static/gray.jpg', gray_image)
        edges = cv2.Canny(image, 250, 254)
        cv2.imwrite('static/edges.jpg', edges)
        _, threshold = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
        cv2.imwrite('static/threshold.jpg', threshold)

        kernel_sharpening = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        sharpened = cv2.filter2D(image, -1, kernel_sharpening)
        cv2.imwrite('static/sharpened.jpg', sharpened)

        predicted_class, accuracy = predict_image("upload/"+fileName)
        print("Predicted class:", predicted_class)
        print("Accuracy is:", accuracy)
       
        f = open('acc.txt', 'w')
        f.write(str(accuracy))
        f.close()


       

        # Define treatment suggestions
        treatments = {
            "adenomacarcinoma": [
                "Surgery to remove the tumor or affected bone.",
                "Radiation therapy for shrinking or killing cancer cells.",
                "Chemotherapy for aggressive or metastatic cases."
            ],
            "cancer_final_stage": [
                "Lumpectomy or mastectomy (surgical removal).",
                "Chemotherapy or hormone therapy depending on hormone receptor status.",
                "Radiation therapy to prevent recurrence."
            ],
            "cancer_stage1": [
                "Antiviral medications (e.g., Paxlovid, Remdesivir) for severe cases.",
                "Oxygen therapy and ventilatory support if needed.",
                "Symptomatic treatment with fever reducers and hydration."
            ],
            "cancer_stage2": [
                "Surgery for early-stage tumors.",
                "Targeted therapy or immunotherapy for advanced stages.",
                "Chemotherapy and radiation therapy for non-surgical cases."
            ],
            "large_cell_carcinoma": [
                "Antibiotics for bacterial pneumonia.",
                "Oxygen therapy for severe respiratory distress.",
                "Cough suppressants and fever reducers for symptom relief."
            ],
            "squamous_cell_carcinoma": [
                "Long-term antibiotic regimen (e.g., Rifampin, Isoniazid).",
                "Directly observed therapy (DOT) to ensure medication adherence.",
                "Supportive care with proper nutrition and rest."
            ]
        }
        treatment_list = treatments.get(predicted_class, ["No specific treatment required."])

       
        accuracy = f"The predicted image is {predicted_class} with a confidence of {confidence:.2%}"

        return render_template('results.html', 
                               status=predicted_class,
                               accuracy=accuracy,
                               Treatment=treatment_list,
                               ImageDisplay=f"http://127.0.0.1:5000/static/images/{fileName}",
                               ImageDisplay1="http://127.0.0.1:5000/static/gray.jpg",
                               ImageDisplay2="http://127.0.0.1:5000/static/edges.jpg",
                               ImageDisplay3="http://127.0.0.1:5000/static/threshold.jpg",
                               ImageDisplay4="http://127.0.0.1:5000/static/sharpened.jpg")
                             

    return render_template('userlog.html')

@app.route('/logout')
def logout():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
