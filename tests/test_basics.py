import unittest
from flask import current_app
from app import create_app

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        '''
        Set up Method to prepare the test fixture. To be called initially before calling the test method; other than AssertionError or SkipTest, any exception raised by this method will be considered an error rather than a test failure.
        '''
        self.app = create_app('development')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        '''
        Tear Down method that executes a set of instructions after every test in the entire application
        Tidies up after the test method completes execution
        '''
        self.app_context.pop()

    def test_app_exists(self):
        '''
        Method to test the current application instance's existence is true (or false).
        '''
        self.assertFalse(current_app is None)