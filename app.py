from flask import Flask, render_template, request, redirect, url_for, flash 
import requests
app = Flask(__name__)
app.secret_key='hola'
API = "https://pokeapi.co/api/v2/pokemon/"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=['POST'])
def search_pokemon():
    Poke = request.form.get('Poke','').strip().lower()
    
    if not Poke:
        flash('Porfavor ingresa un nombre de pokemon real', 'error')
        return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True)