from flask import render_template, request, redirect, url_for, flash
from datetime import datetime
from application import app, db
from application.models import Blogpost
from application.forms import UpdateForm, ContactMeForm
from application.mail import mail
from flask_mail import Message

@app.route('/')
def index():
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()

    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    if request.method == 'POST':
        post = Blogpost.query.filter_by(id=post_id).first()
        form = UpdateForm()
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.author = form.author.data
        post.content = form.content.data
        db.session.commit()
        db.session.close()
        return redirect(url_for('index', id=post_id))
    elif request.method == 'GET':
        return render_template('update.html', post_id = post_id)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactMeForm()
 
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender=form.email.data, recipients=['sheelmorjaria@gmail.com'])
            msg.body = """
            From: %s %s
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
 
        return render_template('contact.html', form=form, success=True)
 
    elif request.method == 'GET':
        return render_template('contact.html', form=form)

@app.route('/add')
def add():
    return render_template('add.html')



@app.route('/delete/<int:post_id>', methods=['GET', 'POST'])
def delete(post_id):
    post_to_delete=Blogpost.query.filter_by(id=post_id).first()
    db.session.delete(post_to_delete)
    db.session.commit()
    db.session.close()

    return redirect(url_for('index', id=post_id))


   

@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()
    db.session.close()

    return redirect(url_for('index'))