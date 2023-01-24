from flask import Flask, redirect, url_for, request
from status import status

app = Flask(__name__)

file = status("status.txt")

@app.route("/")
def index():
	return "Index page"

@app.route("/status", methods = ["GET"])
def status_page():
	status = file.get_status()
	return f"{status}"


@app.route("/status/update")
def status_update():
	file.update_status(file.other(file.get_status()))
	print(f"Updated to {file.get_status()}")
	return redirect(url_for("status_page"))

if __name__ == "__main__":
	app.run(debug=True)

