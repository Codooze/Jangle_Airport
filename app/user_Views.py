from app import app
from flask import render_template

@app.route("/user/profile")
def user_perfil():
    return render_template("/public/usuarios/Mi_Perfil_Usuario.html")