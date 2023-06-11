from base_app.ext.database import db
from sqlalchemy_serializer import SerializerMixin
from passlib.hash import bcrypt


class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140), unique=True)
    password = db.Column(db.String(512))

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.generate_password()

    def generate_password(self):
        self.password = bcrypt.hash(self.password)

    def verify_password(self, password):
        return bcrypt.verify(password, self.password_hash)
