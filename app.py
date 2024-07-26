from flask import Flask
from models import db
from routers import b1, music_bp
import config
import logging
 
# logger info
logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('test.log', encoding="UTF-8")

formatter = logging.Formatter("%(asctime)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
 
app = Flask(__name__)

app.config.from_object(config)

db.init_app(app)

app.register_blueprint(b1)
app.register_blueprint(music_bp)
 
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5050')
 

