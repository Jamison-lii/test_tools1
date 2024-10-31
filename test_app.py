# test_app.py
import unittest
from flask import Flask , jsonify
#from test_app import app

app = Flask(__name__)

@app.route('/')

def home():
    return jsonify(message="Hello level 400 FET, Quality Assurance!")


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello level 400 FET, Quality Assurance!"})


if __name__ == '__main__':
    unittest.main()