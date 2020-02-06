from flask import Flask, render_template, request
from flask_sqlalchemy  import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///posts.db'
db=SQLAlchemy(app)
all_postss =[
    {
        'title' : 'Post 1',
        'content' : 'c1',

    },
    {
        'title' : 'Post 2',
        'content' : 'c2',
        
    }
]
class Feature(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    age = db.Column(db.Integer,nullable=False)
    chest_pain_type = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(200), nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'No of Post:'+ str(self.id)

@app.route('/',methods=['POST','GET'])
def posts():
    if request.method == 'POST':
        post_age = request.form['age']
        post_chest_pain_type = request.form['chest_pain_type']
        post_gender = request.form['gender']
        new_post= Feature(age=post_age,chest_pain_type=post_chest_pain_type,gender=post_gender)
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