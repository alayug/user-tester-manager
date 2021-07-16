'''testing main program using unittest classes'''
import unittest 

# import all classes with testing methods to be run via unittest.main()
from tests.InsertUserValidatorTestCase import *

# main method program starts here
if __name__ == '__main__':
    unittest.main(verbosity=2)
