from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict",methods=["POST","GET"])
def predict():
    weight = request.form['weight']
    height = request.form['height']
    
    weight = float(weight)
    height = float(height)
    
    height = height/100
    BMI = weight/(height*height)
    
    BMI = round(BMI,2)
    
    if BMI <= 16:
        return render_template('result.html', pred = f'Your Body Mass Index is {BMI} which means you are Severely Underweight.')
    elif BMI <= 18.5:
        return render_template('result.html', pred = f'Your Body Mass Index is {BMI} which means you are Underweight.')
    elif BMI <= 25:
        return render_template('result.html', pred = f'Your Body Mass Index is {BMI} which means you are Healthy.')
    elif BMI <= 30:
        return render_template('result.html', pred = f'Your Body Mass Index is {BMI} which means you are Overweight.')
    else:
        return render_template('result.html', pred = f'Your Body Mass Index is {BMI} which means you are Severely Overweight.')
app.run(debug=True)
