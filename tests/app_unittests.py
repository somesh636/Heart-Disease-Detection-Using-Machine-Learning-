import os
import tempfile
import pytest

from application import create_app

@pytest.fixture
def client():
    db_fd, cv_application.config['DATABASE'] = tempfile.mkstemp()
    cv_application = create_app()
    cv_application.config['TESTING']=True

    with cv_application.test_client() as client:
        with cv_application.app_context():
            cv_application.init_db()
        yield client

    os.close(db_fd)
    os.unlink(cv_application.config['DATABASE'])
"""
class TestAppInput(unittest.TestCase): # these tests deal with the input side of things
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
