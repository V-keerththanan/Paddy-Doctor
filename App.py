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
  img = request.files['my_image']
  img_path = "static/" + img.filename	
  img.save(img_path)
  p = predict_label(img_path).tolist()
  ind=p[0].index(max(p[0]))
  
 return f"{ind}"
        
def predict_label(img_path):
  model=tf.keras.models.load_model("Myresnet.h5")
  i = tf.keras.preprocessing.image.load_img(img_path, target_size=(680,480))
  i = tf.keras.preprocessing.image.img_to_array(i)/255.0
  i = i.reshape(1, 680,480,3)
  p = model.predict(i)
  return p
if __name__=='__main__':
    app.run(debug=True)