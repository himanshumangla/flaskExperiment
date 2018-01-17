from flask import Flask, redirect, url_for, request, render_template
from werkzeug import secure_filename
from flask_mail import Mail, Message
import csv
app = Flask(__name__)

@app.route('/successArgument/<name>')
def success(name):
   return 'welcome %s' % name



@app.route("/renderTemplate/")
def index():
   return render_template("index.html")



@app.route('/fillStudent/')
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


@app.route('/upload')
def upload_file():
   return render_template('upload.html')
   
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
   if request.method == 'POST':
      f = request.files['file']
      myFileName = secure_filename(f.filename)
      f.save(myFileName)
      print(myFileName)
      with open(myFileName, 'rb') as myfile:
         myreader = csv.reader(myfile)
         for row in myreader:
            print(row)
      return 'file uploaded successfully'
      
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'him.mangla@gmail.com'
app.config['MAIL_PASSWORD'] = '**'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/sendMail")
def sendEmail():
   print("hi")
   msg = Message('Hello', sender = 'him.mangla@gmail.com', recipients = ['himanshu.mangla@mykaarma.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return "Sent"
if __name__ == '__main__':
   app.run(debug = True)