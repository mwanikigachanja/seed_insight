import unittest
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_get_seeds(self):
        response = self.client.get('/api/v1/seeds')
        self.assertEqual(response.status_code, 200)
        # Add more tests for other endpoints

if __name__ == '__main__':
    unittest.main()
