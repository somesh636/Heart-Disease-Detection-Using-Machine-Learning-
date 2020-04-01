import os
import requests
import pytest
from bs4 import BeautifulSoup

#from app.main import createWebApplication as create_app
import app.aux_modules as aux

def makeDummyModelRequest():
    url = 'localhost:5000'
    post_data = {'first_name':'Fname',
                 'last_name':'Lname',
                 'test_date':'2020-04-03',
                 'age':'20',
                 'gender':'0',
                 'chest_pain_type':'2',
                 'serum_cholestoral':'1',
                 'proximal_left_anterior_descending_artery':'1',
                 'distal_left_anterior_descending_artery':'1',
                 'main_circumflex_artery':'1',
                 'proximal_right_coronary_artery':'1',
                 'distal_right_coronary_artery':'1',
                 'first_obtuse_marginal':'1',
                 'old_peak':'1',
                 'rldv5e':'1',
                 'ramus':'1',
                 'thalach':'1'}
    return requests.post(url, post_data)

def makeDummyFeedbackRequest():
    url = 'localhost:5000/feedback'
    post_data = {'first_name':'Fname',
                 'last_name':'Lname',
                 'email':'foo@bar.baz',
                 'country':'CA',
                 'experience':'average',
                 'comments':'No comment'}
    return requests.post(url, post_data)

def test_constructModelInput():
    expected_post = [20, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    req = makeDummyModelRequest()
    new_post = aux.constructModelInput(req)
        
    assert(new_post==expected_post)

def test_constructNewFeedback():
    expected_post = {'first_name':'Fname',
                     'last_name':'Lname',
                     'email':'foo@bar.baz',
                     'country':'CA',
                     'experience':'average',
                     'comments':'No comment'}

    req = makeDummyFeedbackRequest()
    new_post = aux.constructModelInput(req)

    assert(new_post==expected_post)

def test_constructNewPost():
    pass
