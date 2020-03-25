from flask import Flask, render_template, request,url_for,redirect
from flask_pymongo import PyMongo
from aux_modules.data_construction import *
from datetime import datetime
import pickle
import numpy as np
import os 

application = app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://172.17.0.2:27017/testdb"
mongo = PyMongo(app)

user_database_db = mongo.db.user_data
user_feedback_db = mongo.db.user_feedback

@app.route('/',methods=['POST','GET'])
def posts():
    if request.method == 'POST':
        user_post = constructNewPost(request) # create new post from request
        user_database_db.insert(user_post)

        inp = constructModelInput(user_post)

        predict = Ml_Prediction(inp)

        if int(user_post["gender"])==1:
            user_post["gender"]="male"
        else:
            user_post["gender"]="female"
        return render_template('result.html',f_data=user_post,prediction=predict)
        
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

    return predict


@app.route('/feedback/',methods=['POST','GET'])        
def feedback():
    if request.method == 'POST':
        new_feedback = constructNewFeedback(request)
        user_feedback.insert(new_feedback)
        return redirect(url_for('posts'))  
    else:
        return render_template('feedback.html')
    
if __name__ == '__main__':
    app.run()
