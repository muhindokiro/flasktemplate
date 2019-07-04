from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Comment,User
from .forms import PitchForm,CommentForm,UpdateProfile
from flask_login import login_required
from .. import db,photos

all_pitches = []
#comment
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - ProjectPitch'
    return render_template('index.html',title = title)


# @main.route('/pitch/<int:id>')
# def pitch(id):
#     '''
#     View pitch page function that returns the pitch details page and its data
#     '''
#     return render_template('pitch.html',title = title,pitch = pitch)


@main.route('/new_comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    pitch = get_pitch(id)

    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data
        new_comment = Comment(comment)
        new_comment.save_comment()
        return redirect(url_for('pitch',id = pitch.id ))

    title = f'{pitch.title} comment'
    return render_template('new_comment.html',title = title, comment_form=form, pitch=pitch)

@main.route('/pitch/new',methods = ['GET','POST'])
def new_pitch():
    pitch_form = PitchForm()
    pitches = Pitch.query.order_by(Pitch.title).all()

    if pitch_form.validate_on_submit():
        title = pitch_form.title.data
        description = pitch_form.description.data
        new = Pitch(title=title, description=description)
        new.save_pitch()
        all_pitches.append(new)
        return redirect('/')

    return render_template('pitch.html',pitch_form=pitch_form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))