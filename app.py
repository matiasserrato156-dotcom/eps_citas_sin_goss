import os
from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from models.pacientes import (
    registrar_paciente, obtener_paciente,
    existe_paciente, listar_pacientes
)
from models.citas import (
    registrar_cita, obtener_citas_paciente,
    obtener_cita, actualizar_cita, eliminar_cita
)

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY


# ── Inicio ─────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")


# ── Registro de Paciente ───────────────────────
@app.route("/registro", methods=["GET", "POST"])
def registro_paciente():
    if request.method == "POST":
        documento = request.form.get("documento", "").strip()
        nombre    = request.form.get("nombre", "").strip()
        apellido  = request.form.get("apellido", "").strip()
        telefono  = request.form.get("telefono", "").strip()
        correo    = request.form.get("correo", "").strip()
        eps       = request.form.get("eps", "").strip()

        if not documento or not nombre or not apellido:
            flash("Documento, nombre y apellido son obligatorios.", "error")
            return render_template("registro_paciente.html")

        if existe_paciente(documento):
            flash(f"Ya existe un paciente con documento {documento}.", "error")
            return render_template("registro_paciente.html")

        registrar_paciente(documento, nombre, apellido, telefono, correo, eps)
        flash(f"Paciente {nombre} {apellido} registrado exitosamente.", "success")
        return redirect(url_for("index"))

    return render_template("registro_paciente.html")


# ── Reservar Cita ──────────────────────────────
@app.route("/reservar", methods=["GET", "POST"])
def reservar_cita_view():
    if request.method == "POST":
        documento  = request.form.get("documento", "").strip()
        medico     = request.form.get("medico", "").strip()
        tipo_cita  = request.form.get("tipo_cita", "").strip()
        fecha      = request.form.get("fecha", "").strip()
        hora       = request.form.get("hora", "").strip()
        direccion  = request.form.get("direccion", "").strip()

        if not existe_paciente(documento):
            flash("No se encontró un paciente con ese documento. Regístrelo primero.", "error")
            return render_template("reservar_cita.html")

        registrar_cita(documento, medico, tipo_cita, fecha, hora, direccion)
        flash("Cita reservada exitosamente.", "success")
        return redirect(url_for("resultado_cita", documento=documento))

    return render_template("reservar_cita.html")


# ── Consultar Cita ─────────────────────────────
@app.route("/consulta", methods=["GET", "POST"])
def consulta_cita_view():
    if request.method == "POST":
        documento = request.form.get("documento", "").strip()
        return redirect(url_for("resultado_cita", documento=documento))
    return render_template("consulta_cita.html")


# ── Resultado / Lista de Citas ─────────────────
@app.route("/resultado/<documento>")
def resultado_cita(documento):
    paciente = obtener_paciente(documento)
    if not paciente:
        flash("No se encontró ningún paciente con ese documento.", "error")
        return redirect(url_for("consulta_cita_view"))

    citas = obtener_citas_paciente(documento)
    return render_template("resultado_cita.html", paciente=paciente, citas=citas)


# ── Actualizar Cita ────────────────────────────
@app.route("/actualizar/<int:cita_id>", methods=["GET", "POST"])
def actualizar_cita_view(cita_id):
    cita = obtener_cita(cita_id)
    if not cita:
        flash("Cita no encontrada.", "error")
        return redirect(url_for("index"))

    if request.method == "POST":
        medico    = request.form.get("medico", "").strip()
        tipo_cita = request.form.get("tipo_cita", "").strip()
        fecha     = request.form.get("fecha", "").strip()
        hora      = request.form.get("hora", "").strip()

        actualizar_cita(cita_id, medico, tipo_cita, fecha, hora)
        flash("Cita actualizada exitosamente.", "success")
        return redirect(url_for("resultado_cita", documento=cita["documento"]))

    return render_template("actualizar_cita.html", cita=cita)


# ── Eliminar Cita ──────────────────────────────
@app.route("/eliminar/<int:cita_id>", methods=["POST"])
def eliminar_cita_view(cita_id):
    cita = obtener_cita(cita_id)
    if cita:
        documento = cita["documento"]
        eliminar_cita(cita_id)
        flash("Cita eliminada.", "success")
        return redirect(url_for("resultado_cita", documento=documento))
    flash("Cita no encontrada.", "error")
    return redirect(url_for("index"))


# ── Entry point ────────────────────────────────
if __name__ == "__main__":
    app.run(debug=Config.DEBUG, host="0.0.0.0", port=5000)
