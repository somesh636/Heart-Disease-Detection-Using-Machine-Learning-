def constructModelInput(post):
    post= {'first_name' : post_first_name,
               'last_name' : post_last_name,
               'test_date' : post_test_date,
               'age':post_age,
               'gender':post_gender,
               'chest_pain_type':post_chest_pain_type,
               'serum_cholestoral' : post_serum_cholestoral,
               'proximal_left_anterior_descending_artery' : post_proximal_left_anterior_descending_artery,
               'distal_left_anterior_descending_artery' : post_distal_left_anterior_descending_artery,
               'main_circumflex_artery' : post_main_circumflex_artery,
               'proximal_right_coronary_artery' : post_proximal_right_coronary_artery,
               'distal_right_coronary_artery' : post_distal_right_coronary_artery,
               'first_obtuse_marginal ' : post_first_obtuse_marginal ,
               'old_peak' : post_old_peak,
               'rldv5e' : post_rldv5e,
               'ramus' : post_ramus,
               'thalach' : post_thalach}

    model_input=[post['age'],
                 post['gender'],
                 post['chest_pain_type'],
                 post['serum_cholestoral'],
                 post['proximal_left_anterior_descending_artery'],
                 post['distal_left_anterior_descending_artery'],
                 post['main_circumflex_artery'],
                 post['proximal_right_coronary_artery'],
                 post['distal_right_coronary_artery'],
                 post['first_obtuse_marginal'],
                 post['old_peak'],
                 post['rldv5e'],
                 post['ramus'],
                 post['thalach']]

    return model_input

def constructNewFeedback(request):    
    post_first_name = request.form['first_name']
    post_last_name = request.form['last_name']
    post_email = request.form['email']
    post_country = request.form['country']
    post_experience = request.form['experience']
    post_comments = request.form['comments']  

    new_feedback={'First Name': post_first_name,
                  'Last Name' : post_last_name,
                  'Email' : post_email,
                  'Country' : post_country,
                  'Experience Rating' : post_experience,
                  'Comments' : post_comments}

    return new_feedback
    
def constructNewPost(request):
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

    new_post= {'first_name' : post_first_name,
               'last_name' : post_last_name,
               'test_date' : post_test_date,
               'age':post_age,
               'gender':post_gender,
               'chest_pain_type':post_chest_pain_type,
               'serum_cholestoral' : post_serum_cholestoral,
               'proximal_left_anterior_descending_artery' : post_proximal_left_anterior_descending_artery,
               'distal_left_anterior_descending_artery' : post_distal_left_anterior_descending_artery,
               'main_circumflex_artery' : post_main_circumflex_artery,
               'proximal_right_coronary_artery' : post_proximal_right_coronary_artery,
               'distal_right_coronary_artery' : post_distal_right_coronary_artery,
               'first_obtuse_marginal ' : post_first_obtuse_marginal ,
               'old_peak' : post_old_peak,
               'rldv5e' : post_rldv5e,
               'ramus' : post_ramus,
               'thalach' : post_thalach}
    
    return new_post
