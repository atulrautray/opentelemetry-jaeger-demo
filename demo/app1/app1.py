from random import uniform
from time import sleep
import requests
from flask import Flask, jsonify, abort

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

def get_user():
    r = requests.get("http://app2:5001/user/profile")
    sleep(uniform(0.001,0.025)) # Add random delay between 1ms and 25ms
    return r.json()

@app.route("/todo")
def get_todo():
    get_user()
    r = requests.get("https://jsonplaceholder.typicode.com/todos")
    sleep(uniform(0.001,0.025))
    return jsonify(r.json())

@app.route("/todo/<id>")
def get_todo_by_id(id):
    get_user()
    if str(id) == "5":
        abort(400, 'ID not found')
    r = requests.get(f"https://jsonplaceholder.typicode.com/todos/{id}")
    sleep(uniform(0.001,0.025))
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
