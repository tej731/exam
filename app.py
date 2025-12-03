from flask import Flask, render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('form.html')
@app.route('/submit',methods=["POST"])
def submit():
    username=request.form['username']
    rollno=request.form['rollno']
    year=request.form['year']
    email=request.form['email']
    return render_template('result.html', name=username, roll=rollno, yr=year, mail=email)
if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True, port=5001)