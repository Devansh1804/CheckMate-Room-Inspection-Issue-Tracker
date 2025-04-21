import os

class Config:
    SECRET_KEY = 'your-secret-key'
    MONGO_URI = 'mongodb://localhost:27017/checkmate'
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'uploads')
