# brights our application together
import os
from flask import Flask

app = Flask(__name__)
secret = os.urandom(16)
app.secret_key = secret

from app import All_Views  # - dicen que se debe hacer así con flask, para evitar no sé  que circular import
 #ctrl + shift + p / save withoud formating
from app import adm_views
