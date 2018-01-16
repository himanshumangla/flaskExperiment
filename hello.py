from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/successArgument/<name>')
def success(name):
   return 'welcome %s' % name

@app.route("/renderTemplate/")
def index():
   return render_template("index.html")


@app.route('/fillStudent')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)



@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)