from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'

class Pitch:
    '''
    Pitch class to define Pitch Objects
    '''

    def __init__(self,id,title,mypitch):
        self.id =id
        self.title = title
        self.mypitch = mypitch


class Comment:

    all_comments = []

    def __init__(self,pitch_id,title,mypitch,comment):
        self.pitch_id = pitch_id
        self.title = title
        self.mypitch = mypitch
        self.comment = comment


    def save_comment(self):
        Comment.all_comments.append(self)


    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()

    @classmethod
    def get_comments(cls,id):

        response = []

        for comment in cls.all_comments:
            if comment.movie_id == id:
                response.append(comment)

        return response

