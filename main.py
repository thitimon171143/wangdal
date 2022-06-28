import re
from flask import Flask, redirect , render_template, request, url_for , redirect , escape


def multiFunction():
    # getting data from user
    if request.method == 'POST':
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        gender = request.form['gender']
        Cholesterol = float(request.form['cholesterol'])
        Glucose =float(request.form['glucose'])
        Smoking = request.form['smoke']
        Systolic = float(request.form['systolic'])
        Diastolic = float(request.form['diastolic'])
        total = 0.0
        roundl = float(request.form["waistline"])
        Yat = request.form['relative']
        sweet = request.form['sweet']
        pressure = request.form['pressure']
        

        # gender เพศ
        if(gender == "Male"):
            if(roundl > 90):
                total = total + 1
            else:
                total = total + 0 
        elif(gender == "Female"):
            if(roundl >80):
                total = total + 1
            else:
                total = total + 0  

        if(Yat == "yes"):
            total = total + 1
        else:
            total = total + 0 

        if(Smoking == "yes"):
            total = total + 1
        else:
            total = total + 0 


        # cholesterol ไขมัน
        if(Cholesterol >280):
            total = total + 1
        else:
            total = total + 0  

        # glucose น้ำตาล
        if(Glucose > 131 or sweet == "yes"):
            total = total + 1
        else:
            total = total + 0   
        
        #ความดัน
        if(Systolic >= 140 or Diastolic >= 90 or pressure == "yes"):
            total = total + 1
        elif((Systolic >= 121 and Systolic <= 139)or(Diastolic >= 81 and Diastolic <= 89)):
            total = total + 0 
        else:
            total = total + 0 
        
        #เกณฑ์ความดัน
        if(Systolic >= 140 or Diastolic >= 90):
            blood_warn = 'first'
        elif((Systolic >= 121 and Systolic <= 139)or(Diastolic >= 81 and Diastolic <= 89)):
            blood_warn = 'second'
        else:
            blood_warn = 'third'
        
        #BMI
        BMI = round(weight / ((height/100)*(height/100)),2)
        if(BMI > 25):
            total = total + 1
            BMI_warn = 'abnormal'
        else:
            total = total + 0
            BMI_warn = 'normal'
        
        #ประเมิณ
        if(total == 3 or total == 4):
            my_prediction = 'medieum'
            my_probability = 'yellow'
        elif(total == 5):
            my_prediction = 'high1'
            my_probability = 'orange'
        elif(total == 6):
            my_prediction = 'high2'
            my_probability = 'red'              
        elif(total == 7):
            my_prediction = 'high3'
            my_probability = 'darkred'
        else:
            my_prediction = 'low'
            my_probability = 'green'

        return render_template("modal.html" ,prediction_text= my_prediction,
                                            prediction_text_probability=my_probability,
                                            BMI_text = BMI,
                                            BMI_warning = BMI_warn,
                                            blood_warning = blood_warn)

    else:
        return render_template("check.html")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("Home.html", pagetitle = "home", custom_css = "home")

@app.route("/check") 
def check():
    return multiFunction()

@app.route("/info1") 
def info1():
    return render_template("info1.html")

@app.route("/info2") 
def info2():
    return render_template("info2.html")

@app.route("/info3") 
def info3():
    return render_template("info3.html")

@app.route("/info4") 
def info4():
    return render_template("info4.html")

@app.route("/info5") 
def info5():
    return render_template("info5.html")
    
@app.route("/about") 
def about():
    return render_template("about.html")

# prediction page
@app.route("/modal" , methods =['POST']) #domain 
def modal():
    return multiFunction()


if __name__== "__main__":  #for make this content appear when file open directly not importent from another file
    app.run(debug=True, port=9000)