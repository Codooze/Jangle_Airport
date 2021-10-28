# brights our application together
from flask import Flask
app = Flask(__name__)
app.secret_key = "something only you know"

from app import All_Views  # - dicen que se debe hacer así con flask, para evitar no sé  que circular import
 #ctrl + shift + p / save withoud formating
from app import adm_views
