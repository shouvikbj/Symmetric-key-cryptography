from flask import Flask, render_template, redirect, request, url_for, flash
import os

from cryptography.fernet import Fernet

app = Flask(__name__, static_url_path="")
app.secret_key = "this is a secret key"

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/encrypt")
def encrypt():
    return render_template("encrypt.html")

@app.route("/encrypttext", methods=["POST"])
def encrypttext():
    key = Fernet.generate_key()
    text = request.form.get("text")
    f = Fernet(key)
    cipher = f.encrypt(bytes(text, 'utf-8'))
    return render_template("afterencryption.html", key=key.decode(), cipher=cipher.decode())

@app.route("/afterencryption")
def afterencryption():
    return render_template("afterencryption.html")

@app.route("/decrypt")
def decrypt():
    return render_template("decrypt.html")

@app.route("/decrypttext", methods=["POST"])
def decrypttext():
    key = request.form.get("key")
    text = request.form.get("text")
    f = Fernet(bytes(key, 'utf-8'))
    decrypted_text = f.decrypt(bytes(text, 'utf-8'))
    return render_template("afterdecryption.html", decrypted_text=decrypted_text.decode())

@app.route("/afterdecryption")
def afterdecryption():
    return render_template("afterdecryption.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)