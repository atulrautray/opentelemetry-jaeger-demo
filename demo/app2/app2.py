from random import uniform
from time import sleep
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/user/profile")
def get_user_profile():
    user = {"userId": "1234",
            "email": "user@example.com",
            "organization": "example.com"}
    sleep(uniform(0.001,0.025)) # Add random delay between 1ms and 25ms
    return jsonify(user)

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5001)