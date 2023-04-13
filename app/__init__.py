"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrpr1pmbg5e4khp9gl0-a.oregon-postgres.render.com",
        database="todo_app_umwn",
        user="todo_app_umwn_user",
        password="VyqK9wrb58MMSxgFnJ9TYFhFV9g7kLd1")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
