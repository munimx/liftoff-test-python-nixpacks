from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(
        {
            "app": "liftoff-test-python-nixpacks",
            "stack": "python-flask",
            "mode": "nixpacks-autodetect",
            "ok": True,
        }
    )


if __name__ == "__main__":
    port = int(os.getenv("PORT", "3000"))
    app.run(host="0.0.0.0", port=port)
