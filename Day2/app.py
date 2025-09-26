from flask import Flask, request, render_template_string

app = Flask(__name__)

# Vulnerable route: Reflected XSS
@app.route("/")
def home():
    query = request.args.get("q", "")
    return render_template_string("""
        <h1>Welcome to Vulnerable App</h1>
        <form method="get">
            <input name="q" placeholder="Search...">
            <button type="submit">Search</button>
        </form>
        <p>You searched for: """ + query + """</p>
    """)

# Vulnerable route: SQL Injection (dummy simulation)
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    # BAD: Simulating SQL injection vulnerability
    sql_query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    return f"<p>Executed query: {sql_query}</p><p>Login failed!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
