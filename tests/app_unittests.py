import pytest

class TestAppInput(unittest.TestCase): # these tests deal with the input side of things
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
