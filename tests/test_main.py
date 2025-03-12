import unittest
from flask import Flask
from app.main import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        """Test the home page."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Ask a Question', response.data)

    def test_ask(self):
        """Test the ask endpoint."""
        response = self.app.post('/ask', data=dict(question='What is AI?'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Answer:', response.data)

if __name__ == '__main__':
    unittest.main()