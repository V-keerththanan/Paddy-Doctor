import matplotlib.pyplot as plt
import tensorflow as tf
from distutils.log import debug
from flask import Flask, render_template,request
app=Flask(__name__)

@app.route("/")
def sayHi():
    return render_template('index.html')

@app.route("/uploaded",methods = ['POST','GET'])
def getimage():
    if request.method=='POST':
        print(request.files.get('filename'))
        array_image=tf.keras.preprocessing.image.load_img(request.form.get('filename'))
        print(array_image)
        return "lol"

if __name__=='__main__':
    app.run(debug=True)