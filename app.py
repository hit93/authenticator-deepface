from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from deepface import DeepFace
import cv2
import base64
import numpy as np

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/userDB"
mongo = PyMongo(app)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

def capture_photo():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return None
    ret, frame = cap.read()
    cap.release()
    cv2.destroyAllWindows()
    if ret:
        _, buffer = cv2.imencode('.jpg', frame)
        jpg_as_text = base64.b64encode(buffer).decode('utf-8')
        return jpg_as_text
    else:
        return None

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        phone = request.form['phone']
        photo = capture_photo()
        
        if photo:
            user_data = {
                'username': username,
                'password': password,
                'email': email,
                'phone': phone,
                'photo': photo
            }
            mongo.db.users.insert_one(user_data)
            return redirect(url_for('landing'))
        else:
            return "Photo capture failed", 400

@app.route('/authenticate', methods=['POST'])
def authenticate():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        captured_photo = capture_photo()
        
        if captured_photo:
            users = mongo.db.users.find({'username': username, 'password': password})
            for user in users:
                stored_photo = base64.b64decode(user['photo'])
                nparr = np.frombuffer(stored_photo, np.uint8)
                stored_photo = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                
                captured_photo_data = base64.b64decode(captured_photo)
                nparr_captured = np.frombuffer(captured_photo_data, np.uint8)
                captured_photo = cv2.imdecode(nparr_captured, cv2.IMREAD_COLOR)
                
                try:
                    result = DeepFace.verify(captured_photo, stored_photo, model_name='VGG-Face')
                    if result['verified']:
                        return "User authenticated successfully!"
                except ValueError as e:
                    print(f"Error during verification: {e}")
                    return "Authentication failed!", 401
            return "Authentication failed!", 401
        else:
            return "Photo capture failed", 400

if __name__ == '__main__':
    app.run(debug=True)
