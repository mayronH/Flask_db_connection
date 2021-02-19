from . import db

class User(db.Model):
    __tablename = 'flask-sqlalchemy-users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=False, unique=True, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    created_date = db.Column(db.DateTime, index=False, nullable=False)
    bio = db.Column(db.Text, index=False, nullable=True)
    admin = db.Column(db.Boolean, index=False, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)