from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/users', method=['get'])
def users():
    return jsonify(
        [
            {
                "name",
                "suit",
                "color",
                "value"
            }
        ]
    )

if __name__ == "__main__":
    app.run(debug=True, port=8080)