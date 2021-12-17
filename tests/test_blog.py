
from flask_testing import TestCase
from flask import url_for

from datetime import date, datetime
from os import getenv
from blog import app, electrical
from blog.models import Blogpost
from flask_sqlalchemy import SQLAlchemy


class TestBase(TestCase):

    def create_app(self):
        user = str(getenv('MYSQL_USER')) 
        pwd = str(getenv('MYSQL_PWD'))
        ip= "localhost"
        dbname = str(getenv('MYSQL_DBNAME'))
        app.config.from_pyfile('config.cfg')
        


        return app

    def setUp(self):
        electrical.create_all()
        sample = Blogpost(title='This is an item', subtitle='sample subtitle', author='Sheel', date_posted=date(2021, 1, 1), content ='Content sample')
        electrical.session.add(sample)
        electrical.session.commit()
    
    def tearDown(self):
        electrical.session.remove()
        electrical.drop_all()
#routing tests
class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_about(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)
    def test_add(self):    
        response = self.client.get(url_for('add'))
        self.assertEqual(response.status_code, 200)
    def test_contact(self):
        response = self.client.get(url_for('contact'))
        self.assertEqual(response.status_code, 200)
  #  def test_addpost(self):
   #     response = self.client.post(url_for('addpost', post_id=4, title='test title', subtitle='test subtitle', author='test description',  content='test content'))
    #    self.assertEqual(response.status_code, 200)
    def test_update(self):
        response = self.client.get(url_for('update', post_id=1, title='update title', subtitle='update subtitle', author='update description', content='update content'))
        self.assertEqual(response.status_code, 200)
   # def test_delete(self):
    #    response = self.client.post(url_for('delete', post_id=1))
     #   self.assertEqual(response.status_code, 200)
