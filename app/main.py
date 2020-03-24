from flask import Flask, render_template, request,url_for,redirect
from flask_pymongo import PyMongo
from datetime import datetime
import pickle
import numpy as np
import os 

application = app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://User_info:userinfo123@cluster0-hmtuj.gcp.mongodb.net/test?retryWrites=true&w=majority"
mongo = PyMongo(app)
u_d=mongo.db.user_data3
u_f=mongo.db.feedback_data3
@app.route('/',methods=['POST','GET'])
def posts():
    if request.method == 'POST':
        post_first_name = request.form['first_name']
        post_last_name = request.form['last_name']
        post_test_date = request.form['test_date']
        post_age = request.form['age']
        post_gender = request.form['gender']
        post_chest_pain_type = request.form['chest_pain_type']
        post_serum_cholestoral = request.form['serum_cholestoral']
        post_proximal_left_anterior_descending_artery = request.form['proximal_left_anterior_descending_artery']
        post_distal_left_anterior_descending_artery = request.form['distal_left_anterior_descending_artery']
        post_main_circumflex_artery = request.form['main_circumflex_artery']
        post_proximal_right_coronary_artery = request.form['proximal_right_coronary_artery']
        post_distal_right_coronary_artery = request.form['distal_right_coronary_artery']
        post_first_obtuse_marginal  = request.form['first_obtuse_marginal']
        post_old_peak = request.form['old_peak']
        post_rldv5e = request.form['rldv5e']
        post_ramus = request.form['ramus']
        post_thalach = request.form['thalach']

        new_post= {'first_name' : post_first_name,\
            'last_name' : post_last_name,\
            'test_date' : post_test_date,\
            'age':post_age,\
            'gender':post_gender,\
            'chest_pain_type':post_chest_pain_type,\
            'serum_cholestoral' : post_serum_cholestoral,\
            'proximal_left_anterior_descending_artery' : post_proximal_left_anterior_descending_artery,\
            'distal_left_anterior_descending_artery' : post_distal_left_anterior_descending_artery,\
            'main_circumflex_artery' : post_main_circumflex_artery,\
            'proximal_right_coronary_artery' : post_proximal_right_coronary_artery,\
            'distal_right_coronary_artery' : post_distal_right_coronary_artery,\
            'first_obtuse_marginal ' : post_first_obtuse_marginal ,\
            'old_peak' : post_old_peak,\
            'rldv5e' : post_rldv5e,\
            'ramus' : post_ramus,\
            'thalach' : post_thalach  }

        u_d.insert(new_post)

        inp=[post_age,post_gender,post_chest_pain_type,post_serum_cholestoral,\
            post_proximal_left_anterior_descending_artery,post_distal_left_anterior_descending_artery,post_main_circumflex_artery,\
            post_proximal_right_coronary_artery,post_distal_right_coronary_artery,post_first_obtuse_marginal ,\
            post_old_peak,post_rldv5e,\
            post_ramus,\
            post_thalach ]

        predict = Ml_Prediction(inp)

        if int(new_post["gender"])==1:
            new_post["gender"]="male"
        else:
            new_post["gender"]="female"
        return render_template('result.html',f_data=new_post,prediction=predict)
        
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
def feedback1():
    if request.method == 'POST':
        post_first_name = request.form['first_name']
        post_last_name = request.form['last_name']
        post_email = request.form['email']
        post_country = request.form['country']
        post_experience = request.form['experience']
        post_comments = request.form['comments']  

        new_feedback={
            'First Name': post_first_name,\
            'Last Name' : post_last_name,\
            'Email' : post_email,\
            'Country' : post_country,\
            'Experience Rating' : post_experience,\
            'Comments' : post_comments
        }
        u_f.insert(new_feedback)
        return redirect(url_for('posts'))  
    else:
        return render_template('feedback.html')
        
        
if __name__ == '__main__':
    app.run(debug=True)