from flask import Flask
from config import db,migrate
from dotenv import load_dotenv
import os
from routes.user import user_bp

load_dotenv()

app =Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(user_bp, url_prefix='/users')


if __name__ == '__main__':
    app.run(debug=True)