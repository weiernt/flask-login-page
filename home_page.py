#

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
@app.route("/home")
def hello_world():
    return 'Hello, World! This is the home page!'
	
@app.route("/<varname>")
def other_page(varname):
	return f'Hi, this page is {varname}. Enjoy!'
	
@app.route("/requests_page", methods=["GET", "POST"])
def requests_page():
	print(f"	Hi the request is {request.method}")
	input_json = request.get_json()
	print(input_json)
	# print(f"	{request.args}")
	# if request.method=="POST" and request.form["username"]:
		# print("i'm in the first")
		# return render_template("requests_page.html", first=request.args.get("username"), list_of_args=args)
	if request.method=="POST":
		return render_template("requests_page.html", first=input_json["username"])
	else:
		return render_template("requests_page.html", first="Getting apparently")
	
	
	
if __name__=="__main__":
	app.run(debug=True)
