app = Flask(__name__)

@app.route("/sum", methods=["POST"])
def somar():
    data = request.get_json()
    x = data["x"]
    y = data["y"]
    result = x + y
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
