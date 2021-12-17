from blog.forms import ContactMeForm, UpdateForm
from flask_mail import  Mail
from blog import app
mail = Mail()

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'sheelmorjaria@gmail.com'
app.config["MAIL_PASSWORD"] = 'pmnkqihytyftmelt'
mail.init_app(app)