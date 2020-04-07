from flask import Flask, render_template, request,url_for,redirect
from flask_pymongo import PyMongo
from aux_modules.data_construction import *
from datetime import datetime
import pickle
import numpy as np
import os 
import pandas as pd


app = Flask(__name__)
# NOTE: Please change the Mongo URI to match your local configuration for tests
# This IP address reflects the current docker settings, need to find a way to
# generate dynamically

app.config["MONGO_URI"] = "mongodb+srv://User_info:userinfo123@cluster0-hmtuj.gcp.mongodb.net/test?retryWrites=true&w=majority"
mongo = PyMongo(app)

user_database_db = mongo.db.user_data_fin
user_feedback_db = mongo.db.user_feedback_fin

@app.route('/',methods=['POST','GET'])
def posts():
    if request.method == 'POST':
        user_post = constructNewPost(request) # create new post from request
        user_database_db.insert(user_post)
        
        inp = constructModelInput(user_post)
        
        predict = Ml_Prediction(inp)
        
        if int(user_post["gender"])==1:
            user_post["gender"]="Male"
        else:
            user_post["gender"]="Female"
        return render_template('result.html',f_data=user_post,prediction=predict[0])        
    else:
        return render_template('index.htm')

@app.route('/',methods=['POST','GET'])    
def Ml_Prediction(inp):
        
    inp=np.reshape(inp,(1, 14))
    model= pickle.load(open(os.path.join('Pickle_Objects','algorithm.pkl'),'rb'))
    prediction=model.predict(inp)

    if prediction==1:
        predict='High Risk of Heart Disease'
    elif prediction==0:
        predict='Low Risk of Heart Disease'

    return [predict, prediction]


@app.route('/feedback/',methods=['POST','GET'])        
def feedback():
    if request.method == 'POST':
        new_feedback = constructNewFeedback(request)
        user_feedback_db.insert(new_feedback)
        return redirect(url_for('posts'))  
    else:
        return render_template('feedback.html')

@app.route('/time_series/',methods=['POST','GET'])        
def time_series():
    return render_template('time_series.html')


@app.route('/about_us/',methods=['POST','GET'])        
def about_us():
    return render_template('about_us.html')

@app.route('/contact_us/',methods=['POST','GET'])        
def contact_us():
    return render_template('contact_us.html')

if __name__ == '__main__':
    # app = create_app()
    app.run(debug=True)

