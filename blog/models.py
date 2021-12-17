from blog import electrical

class Blogpost(electrical.Model):
    id = electrical.Column(electrical.Integer, primary_key = True)
    title = electrical.Column(electrical.String(50))
    subtitle = electrical.Column(electrical.String(50))
    author = electrical.Column(electrical.String(20))
    date_posted = electrical.Column(electrical.DateTime)
    content = electrical.Column(electrical.Text)
    
electrical.drop_all()
electrical.create_all()