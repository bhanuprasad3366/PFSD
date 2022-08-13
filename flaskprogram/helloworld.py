from flask import Flask,render_template,redirect,url_for
app = Flask(__name__)
@app.route("/")
def hello():
	return "bhanu prasad"
@app.route('/emp/<int:emp1>')
def show_emp(emp1):
	return 'EMP ID Number %d' %emp1
@app.route('/sample1')
def index():
	return render_template('login.html')
@app.route('/user/<name>')
def hello_user(name):
	if name =="admin":
		return redirect(url_for('hello admin'))
	else:
		return redirect(url_for('hello_guest',guest =name))
@app.route('/admin')
def hello_admin():
	return 'hello admin'

if __name__ == "__main__":
	app.run()
