import os
import tempfile
import pytest
from bs4 import BeautifulSoup

from app.application import create_app
#"""
""" START OF TESTS """
### APP TESTS
def test_landing_page(client):
    req=client.get('/') # get root page
    parser = BeautifulSoup(req.data, features="lxml") # parse html

    expected_heading = "A.I. based framework for the Prediction of Heart Disease"
    received_heading = parser.h2.string # get heading of page
    
    assert expected_heading in received_heading # assert the heading contains what we expect


def test_valid_input(client):

    request_data = "age=33&gender=1&chest_pain_type=0&resting_blood_pressure=33&serum_cholestoral=33&fasting_blood_sugar=1&resting_electrocardiographic_results=0&maximum_heart_rate_achieved=33&exercise_induced_angina=1&ST_depression_induced=33&slope_of_the_peak_exercise_ST_segment=0&major_vessels_colored_by_flourosopy=0&thal=0&button="
    
    request_dict = {'age':27,
                    'gender':1,
                    'chest_pain_type':0,
                    'resting_blood_pressure':3,
                    'serum_cholestoral':4,
                    'fasting_blood_sugar':1,
                    'resting_electrocardiographic_results':0,
                    'maximum_heart_rate_achieved':3,
                    'exercise_induced_angina':1,
                    'ST_depression_induced':4,
                    'slope_of_the_peak_exercise_ST_segment':0,
                    'major_vessels_colored_by_flourosopy':0,
                    'thal':0}#,
                    #'button':''}
    #breakpoint()
    req = client.post('/', data=request_dict)
    parser = BeautifulSoup(req.data, features="lxml") # parse html
    breakpoint()
    pass

def test_invalid_input(client):

    pass
### END OF APP TESTS


""" END OF TESTS """


@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp() # create a file to be used as a temp database
    db_uri = 'sqlite:///{0}'.format(db_path) # create the temp database URI

    cv_application = create_app(db_uri)
    cv_application.config['TESTING']=True #configure for testing

    with cv_application.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(db_path)
    
"""
class test_AppInput(unittest.TestCase): # these tests deal with the input side of things
    @classmethod
    def setup_class(cls): # set up
        self.application = create_app()
        self.application.run(debug=True)

    @classmethod
    def teardown_class(cls): # set up

        self.application.run(debug=True)

        
    def testValidInput(): # the user enters valid data and proceeds
        
        assert(valid_input_behaviour)

    def testInvalidInput(): # the user misses some necessary input and receives notification of this 

        assert(invalid_input_behaviour)

    def testMalformedInput(): # the user enters some weird nonstandard input and is notified

        assert(malformed_input_behaviour)

class TestAppFunctionality(unittest.TestCase):
    def processesInput(): # receives input and returns graph and report
        pass

    def highRiskUser(): # receieves input we class as high risk and notifies user
        pass

    def lowRiskUser(): # receieves input we class as low risk and notifies user
        pass
            

if __name__ == '__main__':
    unittest.main()
"""
