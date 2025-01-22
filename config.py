import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

pymysql.install_as_MySQLdb()

db = SQLAlchemy()
migrate = Migrate()