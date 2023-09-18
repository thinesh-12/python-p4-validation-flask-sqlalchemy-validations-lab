from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates("name")
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Author must have name")
        return name
    
    @validates("phone_number")
    def validate_PN(self, key, pn):
        if len(pn) != 10:
            raise ValueError("Phone Number must be 10 digits")
        return pn

    def __repr__(self):
        return f"Author(id={self.id}, name={self.name})"

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    @validates("title")
    def validate_title(self, key, title):
        if not title:
            raise ValueError("Title cannot be empty")

        strings = ["Won't Believe", "Secret", "Top", "Guess"]
        num = 0
        for str in strings:
            if title.find(str) != -1:
                num += 1
        if num < 4:
            raise ValueError("not clickbaity enough")

        return title
    
    @validates("content")
    def validate_content(self, key, content):
        if not len(content) >= 250:
            raise ValueError("Post content must be 250 characters or more")
        return content

    @validates("summary")
    def validate_summary(self, key, summary):
        if len(summary) >= 250:
            raise ValueError("Summary cannot be greater than 250 characters")
        return summary

    @validates("category")
    def validate_category(self, key, category):
        cats = ["Fiction", "Non-Fiction"]
        if category not in cats:
            raise ValueError("Category must be Fiction or Non-Fiction")
        return category 


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
