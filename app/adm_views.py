from flask.helpers import url_for
from pymysql import NULL
from werkzeug.utils import redirect
from werkzeug.wrappers import request
from app import app
from flask import Flask, render_template, request, redirect, flash, session, url_for
from datetime import datetime
from app import dbController
from passlib.hash import pbkdf2_sha256
# contendra todas nuestra vistas


@app.route("/admin/admin_cuentas")
def admin_adm_cuentas():
    if session["account"] == 1:
        return render_template("/public/Administrador/Admin-cuentas.html")
    return redirect(url_for("logout"))


@app.route("/admin/admin_vuelos")
def admin_adm_vuelos():
    if session["account"] == 1:
        return render_template("/public/Administrador/Admin-vuelos.html")


@app.route("/admin/agregar_cuentas")
def admin_agg_cuentas():
    if session["account"] == 1:
        return render_template("/public/Administrador/Agregar-cuentas.html")


@app.route("/admin/agregar_vuelos")
def admin_agg_vuelos():
    if session["account"] == 1:
        return render_template("/public/Administrador/Agregar-vuelos.html")


@app.route("/admin/agregar_vuelos", methods=["POST", "GET"])
def admin_agregar_vuelos():
    if request.method == "GET":
        return render_template("/public/Administrador/Agregar-vuelos.html")
    if request.method == "POST":
        fecha = request.form.get("fecha")
        origen = request.form.get("origen")
        destino = request.form.get("destino")
        idAvion = request.form.get("idAvion")
        codvuelo = request.form.get("codvuelo")
        estado = request.form.get("status")
        horasalida = 15
        tickets = 100
        total = 8000
        pilotodoc = 300000
        pilotorol = 3
        tiempovuelo = 12
        dbController.agregar_vuelo(codvuelo, destino, idAvion, fecha, horasalida, origen, tickets, total, pilotodoc, pilotorol, tiempovuelo, estado)
        return redirect("/admin/agregar_vuelos")