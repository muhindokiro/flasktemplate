from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Blog,Comment,User
from .forms import BlogForm,CommentForm,UpdateProfile
from flask_login import login_required
from .. import db,photos

all_blogs = []
#comment
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - MyBlog'
    return render_template('index.html',title = title)

@main.route('/football')
@login_required
def football():
    '''
    View root page function that returns the football page and its data
    '''
    title = 'Home - MyBlog'
    return render_template('football.html',title = title)

@main.route('/cycling')
@login_required
def cycling():
    '''
    View root page function that returns the cycling page and its data
    '''
    title = 'Home - MyBlog'
    return render_template('cycling.html',title = title)

@main.route('/rugby')
@login_required
def rugby():
    '''
    View root page function that returns the rugby page and its data
    '''
    title = 'Home - MyBlog' 
    return render_template('rugby.html',title = title)

@main.route('/basketball')
@login_required
def basketball():
    '''
    View root page function that returns the basketball page and its data
    '''
    title = 'Home - MyBlog'
    return render_template('basketball.html',title = title)

@main.route('/comment', methods = ['GET','POST'])
@login_required
def new_comment():
    form = CommentForm()
    #blog = (id)

    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data

        new_comment = Comment(comment)
        new_comment.save_comment()
        #return redirect(url_for('/',id = blog.id ))

    #title = f'{blog.title} comment'
    return render_template('comment.html', comment_form=form)

@main.route('/blog',methods = ['GET','POST'])
def new_blog():
    blog_form = BlogForm()
    #blogs = Blog.query.order_by(Blog.title).all()

    if blog_form.validate_on_submit():
        title = blog_form.title.data
        description = blog_form.description.data
        new = Blog(title=title, description=description)
        new.save_blog()
        all_blogs.append(new)

        return redirect('/')

    return render_template('blog.html',blog_form=blog_form)

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