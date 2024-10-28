from flask import Flask,render_template,request,jsonify
import pickle
import numpy

app=Flask(__name__)


@app.route("/")

def home():
    return render_template('index.html')  

@app.route("/predict",methods=['GET','POST'])

@app.route("/predict")

def predict():
    if request.method=='POST':
        prep=request.form.get('pregnancies')
        glu=request.form.get('glucose')
        bp=request.form.get('bloodPressure')
        skinthick=request.form.get('skinThickness')
        insulin=request.form.get('insulin')
        BMI=request.form.get('bmi')
        dpf=request.form.get('diabetesPedigreeFunction')
        age=request.form.get('age')
        print(prep,glu,bp,skinthick,insulin,BMI,dpf,age)
        with open("model.pickle","rb") as model_file:
            model=pickle.load(model_file)
        res=model.predict([[float(prep),float(glu),float(bp),float(skinthick),float(insulin),float(BMI),float(dpf),float(age)]])
        g=''
        if res[0]==1:
            g = 'Diabetic' 
        else:
            g = 'Non Diabetic'
        return jsonify({"You are ":[g]})
    else:
        return render_template('predict.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = 5050)
 
