from cmath import e
from crypt import methods
from flask import Flask, request, jsonify
from module.database import Database

app = Flask(__name__)
db = Database()

@app.route("/")
def index():
    return "Hola mundo"

@app.route("/readphone", methods=["GET"])
def readphone():
    if request.method == "GET":
        print("GET")
        try:
            result = db.read(request.json["id"])
            print(result)
        except Exception as e:
            return e
    return jsonify(result)

@app.route("/addphone", methods=["POST"])
def addphone():
    if request.method == "POST":
        print("POST")
        try:
            print(request)
            db.insert(request.json)
        except Exception as e:
            print(e)
            return e
    return jsonify({ "add_phone": request.json["phone"]})

@app.route("/updatephone", methods=["POST"])
def updatephone():
    if request.method == "POST":
        try:
            print(request)
            db.update(request.json)
        except Exception as e:
            return e
    return jsonify({ "update_phone": request.json["id"]})

@app.route("/deletephone", methods=["POST"])
def deletephone():
    if request.method == "POST":
        try:
            db.delete(request.json["id"])
        except Exception as e:
            return e
    return jsonify({ "deleted_phone_id": request.json["id"]})
    

if __name__ == "__main__":
    app.debug = True
    app.run()