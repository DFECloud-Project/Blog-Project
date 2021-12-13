from operator import pos
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from os import getenv
from forms import ContactMeForm, UpdateForm
from flask_mail import Message, Mail

mail = Mail()



app = Flask(__name__)
user = getenv('MYSQL_USER') 
pwd = getenv('MYSQL_PWD')
ip= getenv('MYSQL_IP')
db = getenv('MYSQL_DB')
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://"+user+":"+pwd+"@"+ip+"/"+db
app.config['SECRET_KEY'] = getenv('MYSQL_SK')
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'sheelmorjaria@gmail.com'
app.config["MAIL_PASSWORD"] = 'pmnkqihytyftmelt'
mail.init_app(app)

db = SQLAlchemy(app)

class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)




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


if __name__ == '__main__':
    app.run(debug=True)