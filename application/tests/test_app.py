#!/usr/bin/python3

##########  Imports ##########

import unittest
from flask import url_for
from flask_testing import TestCase

from app import app, db, Clothing

class TestBase (TestCase):

    def create_app (self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True
                )

        return app

    def setUp (self):
        db.create_all()

        sample1 = Clothing(name="Bunny onesie")
        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_index_get(self):
        responce = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete'))
        self.assertEqual(response.status_code,405)

    def test_update_get(self):
        response = self.client.get(url_for('update'))
        self.assertEqual(response.status_code, 405)

class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(
            url_for('home'),
            data = dict(name="Purple dress"))
        self.assertIn(b'Purple dress',response.data)
                
class TestUpdate(TestBase):
    def test_update_post(self):
        response = self.client.post(
            url_for('update'),
            data = dict(oldname="Black dress", newname="Little black dress"),
            follow_redirects=True
            )
        self.assertEqual(response.status_code,200)
                
class TestDelete(TestBase):
    def test_delete_post(self):
        response = self.client.post(
            url_for('delete'),
            data = dict(name="Black dress"),
            follow_redirects=True
            )
        self.assertEqual(response.status_code,200)

