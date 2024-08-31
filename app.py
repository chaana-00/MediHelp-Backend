from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
from config import Config
from routes.user_routes import user_bp
from routes.admin_routes import admin_bp
from routes.chatbot_routes import chat_bp
from routes.doctors_routes import doctor_bp
from routes.prediction_routes import prediction_bp
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image, ImageOps
import logging
import os
import io
import tempfile

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

CORS(app)
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:63342", "http://127.0.0.1:5500"]}})

app.config['MYSQL'] = mysql
app.config['UPLOAD_FOLDER'] = 'static/uploads'

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(chat_bp, url_prefix='/chatbot')
app.register_blueprint(doctor_bp, url_prefix='/doctor')
app.register_blueprint(prediction_bp, url_prefix='/prediction')

logging.basicConfig(level=logging.INFO)

model = load_model("keras_model.h5", compile=False)
class_names = open("labels.txt", "r").readlines()

def predict_image(img_path):
    try:
        img = Image.open(img_path).convert("RGB")
        size = (224, 224)
        img = ImageOps.fit(img, size, Image.Resampling.LANCZOS)
        img_array = np.asarray(img)
        
        normalized_img_array = (img_array.astype(np.float32) / 127.5) - 1

        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        data[0] = normalized_img_array
        
        prediction = model.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index].strip()  
        
        confidence_score = prediction[0][index]
        
        return f"Class: {class_name}, Confidence Score: {confidence_score:.2f}"

    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return "Prediction Server Error"

# @app.route('/submit_form', methods=['POST'])
# def submit_form():
#     name = request.form.get('name')
#     email = request.form.get('email')
#     subject = request.form.get('subject')
#     message = request.form.get('message')

#     cursor = mysql.connection.cursor()

#     try:
#         query = "INSERT INTO contact_form (name, email, subject, message) VALUES (%s, %s, %s, %s)"
#         cursor.execute(query, (name, email, subject, message))
#         mysql.connection.commit()
#         return jsonify({'success': 'Form submitted successfully'})
    
#     except Exception as e:
#         return jsonify({'error': str(e)})
    
#     finally:
#         cursor.close()

# @app.route('/display_table')
# def display_table():
#     cursor = mysql.connection.cursor()
#     cursor.execute("SELECT * FROM contact_form")
#     data = cursor.fetchall()
#     cursor.close()

#     return render_template('display_table.html', data=data)


@app.route('/prediction', methods=['POST'])
def classify_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        upload_dir = app.config['UPLOAD_FOLDER']
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        
        file_path = os.path.join(upload_dir, file.filename)
        file.save(file_path)
        
        result = predict_image(file_path)
        
        return jsonify({'classification': result})
    
    return jsonify({'error': 'File upload failed'}), 400

@app.route('/most_common_gender', methods=['GET'])
def most_common_gender():
    cursor = mysql.connection.cursor()
    
    try:
        cursor.execute('SELECT DISTINCT userId FROM prediction')
        user_ids = cursor.fetchall()
        
        if not user_ids:
            return jsonify({'message': 'No predictions found'})
        
        user_ids = [user_id[0] for user_id in user_ids]  

        format_strings = ','.join(['%s'] * len(user_ids))
        cursor.execute(f'SELECT gender FROM users WHERE id IN ({format_strings})', tuple(user_ids))
        genders = cursor.fetchall()
        
        gender_count = {}
        for gender in genders:
            gender = gender[0] 
            if gender in gender_count:
                gender_count[gender] += 1
            else:
                gender_count[gender] = 1
        
        most_common_gender = max(gender_count, key=gender_count.get)
        
        return jsonify({'most_common_gender': most_common_gender})
    
    except Exception as e:
        return jsonify({'error': str(e)})
    
    finally:
        cursor.close()
    cursor = mysql.connection.cursor()
    
    try:
        cursor.execute('SELECT userId FROM prediction')
        user_ids = cursor.fetchall()
        
        if not user_ids:
            return jsonify({'message': 'No predictions found'})
        
        user_ids = [user_id[0] for user_id in user_ids]  

        format_strings = ','.join(['%s'] * len(user_ids))
        cursor.execute(f'SELECT gender FROM users WHERE id IN ({format_strings})', tuple(user_ids))
        genders = cursor.fetchall()
        
        gender_count = {}
        for gender in genders:
            gender = gender[0]
            if gender in gender_count:
                gender_count[gender] += 1
            else:
                gender_count[gender] = 1
        
        most_common_gender = max(gender_count, key=gender_count.get)
        
        return jsonify({'most_common_gender': most_common_gender})
    
    except Exception as e:
        return jsonify({'error': str(e)})
    
    finally:
        cursor.close()

    cursor = mysql.connection.cursor()

    try:
        cursor.execute('SELECT DISTINCT userId FROM prediction')
        user_ids = cursor.fetchall()

        if not user_ids:
            return jsonify({'message': 'No predictions found'})

        user_ids = [user_id[0] for user_id in user_ids]

        format_strings = ','.join(['%s'] * len(user_ids))
        cursor.execute(f'SELECT gender FROM users WHERE id IN ({format_strings})', tuple(user_ids))
        genders = cursor.fetchall()

        gender_count = {}
        for gender in genders:
            gender = gender[0]
            if gender in gender_count:
                gender_count[gender] += 1
            else:
                gender_count[gender] = 1

        most_common_gender = max(gender_count, key=gender_count.get)

        return jsonify({'most_common_gender': most_common_gender})

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        cursor.close()
    cursor = mysql.connection.cursor()

    try:
        cursor.execute('SELECT userId FROM prediction')
        user_ids = cursor.fetchall()

        if not user_ids:
            return jsonify({'message': 'No predictions found'})

        user_ids = [user_id[0] for user_id in user_ids]

        format_strings = ','.join(['%s'] * len(user_ids))
        cursor.execute(f'SELECT gender FROM users WHERE id IN ({format_strings})', tuple(user_ids))
        genders = cursor.fetchall()

        gender_count = {}
        for gender in genders:
            gender = gender[0]
            if gender in gender_count:
                gender_count[gender] += 1
            else:
                gender_count[gender] = 1

        most_common_gender = max(gender_count, key=gender_count.get)

        return jsonify({'most_common_gender': most_common_gender})

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        cursor.close()


if __name__ == '__main__':
    app.run(debug=True)
