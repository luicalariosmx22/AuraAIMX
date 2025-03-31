from flask import Flask, render_template, request
from bot import preguntar_a_gpt  # Importamos la lógica del bot

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        mensaje = request.form.get("mensaje")
        respuesta = preguntar_a_gpt(mensaje)
        return render_template("index.html", respuesta=respuesta)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
