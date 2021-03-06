from flask_testing import TestCase 
from app.main import db
from manage import app 
import json



class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app 

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestCase_db_down(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app 