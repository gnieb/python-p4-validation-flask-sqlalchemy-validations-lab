from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    phone_number = db.Column(db.Integer)

    @validates('name')
    def validate_name(self, key, n):
        if len(n) ==0 :
            raise ValueError("Failed name validation!")
        return n

    @validates('phone_number')
    def validate(self, key, phnum):
        if len(phnum) < 10:
            raise ValueError("Failed phone nuber validation!")
        return phnum

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    summary = db.Column(db.String)
    category = db.Column(db.String)


    @validates('title')
    def validate_title(self, key, t):
        if len(t) == 0 or "Won't Believe" not in t or "Secret" not in t or "Top" not in t or "Guess" not in t:
            raise ValueError("Failed title validation!")
        return t

    @validates('content')
    def validate_content(self, key, cont):
        if len(cont) < 250:
            raise ValueError("Failed content validation!")
        return cont
    
    @validates('summary')
    def validate_summ(self, key, summ):
        if len(summ) > 250:
            raise ValueError("Failed Summary validation")
        return summ
    
    @validates('category')
    def validate_cat(self, key, cat):
        if cat != 'Fiction' and cat != 'Non-Fiction':
            raise ValueError("Failed category validation!")
        
        return cat
    