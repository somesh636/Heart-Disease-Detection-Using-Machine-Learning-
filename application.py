from flask import Flask, render_template, request,url_for
from flask_sqlalchemy  import SQLAlchemy
from datetime import datetime


application = app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///posts.db'
db=SQLAlchemy(app)
class Feature(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    age = db.Column(db.Integer,nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    chest_pain_type = db.Column(db.Integer, nullable=False)
    resting_blood_pressure = db.Column(db.Integer,nullable=False)#r
    serum_cholestoral = db.Column(db.Integer,nullable=False)#r
    fasting_blood_sugar = db.Column(db.Integer, nullable=False)#r
    resting_electrocardiographic_results = db.Column(db.Integer, nullable=False)#r
    maximum_heart_rate_achieved = db.Column(db.Integer, nullable=False)
    exercise_induced_angina = db.Column(db.Integer, nullable=False)
    ST_depression_induced = db.Column(db.Float, nullable=False)
    slope_of_the_peak_exercise_ST_segment = db.Column(db.Integer, nullable=False)
    major_vessels_colored_by_flourosopy=db.Column(db.Integer,nullable=False)
    thal=db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return 'No of Post:'+ str(self.id)

@app.route('/',methods=['POST','GET'])
def posts():
    if request.method == 'POST':
        post_age = request.form['age']
        post_gender = request.form['gender']
        post_chest_pain_type = request.form['chest_pain_type']
        post_resting_blood_pressure = request.form['resting_blood_pressure']
        post_serum_cholestoral = request.form['serum_cholestoral']
        post_fasting_blood_sugar = request.form['fasting_blood_sugar']
        post_resting_electrocardiographic_results = request.form['resting_electrocardiographic_results']
        post_maximum_heart_rate_achieved = request.form['maximum_heart_rate_achieved']
        post_exercise_induced_angina = request.form['exercise_induced_angina']
        post_ST_depression_induced = request.form['ST_depression_induced']
        post_slope_of_the_peak_exercise_ST_segment = request.form['slope_of_the_peak_exercise_ST_segment']
        post_major_vessels_colored_by_flourosopy = request.form['major_vessels_colored_by_flourosopy']
        post_thal = request.form['thal']
        
        new_post= Feature(age=post_age,\
            gender=post_gender,\
            chest_pain_type=post_chest_pain_type,\
            resting_blood_pressure = post_resting_blood_pressure,\
            serum_cholestoral = post_serum_cholestoral,\
            fasting_blood_sugar = post_fasting_blood_sugar,\
            resting_electrocardiographic_results= post_resting_electrocardiographic_results,\
            maximum_heart_rate_achieved = post_maximum_heart_rate_achieved,\
            exercise_induced_angina = post_exercise_induced_angina,\
            ST_depression_induced = post_ST_depression_induced,\
            slope_of_the_peak_exercise_ST_segment = post_slope_of_the_peak_exercise_ST_segment,\
            major_vessels_colored_by_flourosopy =post_major_vessels_colored_by_flourosopy,\
            thal = post_thal)
        db.session.add(new_post)
        db.session.commit()
        all_posts = Feature.query.order_by(Feature.date_created.desc()).first()
        #all_posts = Feature.query().one()
        return render_template('hello.html',f_data=all_posts)
        
    else:
        return render_template('index.htm')
        all_posts = Feature.query.order_by(Feature.date_created).all()



if __name__ == '__main__':
    app.run(debug=True)