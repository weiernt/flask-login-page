#

from flask import Flask, render_template, request, flash, session
from wtforms import Form, TextField, validators
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_super_secret_key'

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
		return render_template("requests_page.html", username=input_json["username"], 
													 password=input_json["password"])
	else:
		return render_template("requests_page.html", username="Getting apparently",
													 password="no password")
													 
													 
													 
@app.route("/query_page")
def query_page():
	name=request.args.get("name")
	return "query page is here!!! " +f"\n <h2> welcome to {name}</h2>"
	
class MyForm(Form):
	name = TextField('Name:', [validators.required(), validators.Length(min=6, max=120)])
	
@app.route("/form_page", methods=["GET", "POST"])
def form_page():
	
	form = MyForm(request.form)
	
	if request.method=='POST':
		name=request.form['name']
		print(f"just received post with name={name}")
		
	# elif request.method=='GET':
		# return 
	if hasattr(form_page, "first_time"):
		# not the first time this function has range
		
		if form.validate():
			flash("hello, " + name, "success")
			print("form validated")
		else:
			print("form validation false")
			flash("all forms field are required or length more than 6 needed", "error")
		
	
	# return "testing form_page"
	form_page.first_time=0
	return render_template("form_page.html", form=form)
	
	
	
if __name__=="__main__":
	app.run(debug=True)
