from __future__ import annotations
from typing import Any
from flask import Flask, request, jsonify
import vulnerable_module
import ast

app = Flask(__name__)

# Hardcoded secret (intentional insecure practice for the lab)
API_KEY: str = "SUPER_SECRET_API_KEY_12345"


@app.route("/")
def home() -> str:
    return "Vulnerable Flask App - Day 4 Exercise\n"


# Safer parsing for demonstration (you can intentionally use `eval` for the lab,
# but Pylance/linters will warn strongly). Using ast.literal_eval avoids many warnings.
@app.route("/calc")
def calc() -> Any:
    expr = request.args.get("expr", "")
    if not expr:
        return jsonify({"error": "no expr provided"}), 400

    try:
        # Use ast.literal_eval to avoid executing arbitrary code.
        # If you want to intentionally demonstrate eval's danger, replace the next
        # line with: result = eval(expr)  (but that will trigger warnings)
        result = ast.literal_eval(expr)
        return jsonify({"expr": expr, "result": result})
    except Exception as exc:  # keep broad for demo purposes
        return jsonify({"error": str(exc)}), 400


# Endpoint leaking secret (intentional)
@app.route("/secret")
def secret() -> Any:
    # Only for demo: exposes hardcoded secret
    return jsonify({"api_key": API_KEY})


# Import insecure function from external module
@app.route("/insecure-action")
def insecure_action() -> Any:
    data = request.args.get("data", "")
    return jsonify({"output": vulnerable_module.insecure_process(data)})


if __name__ == "__main__":
    # Only run the dev server when executed directly (not when imported by tests or CI)
    app.run(host="0.0.0.0", port=5000, debug=False)
