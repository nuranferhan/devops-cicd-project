import unittest
import json
import sys
import os

# Add the parent directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
src_dir = os.path.join(parent_dir, 'src')
sys.path.insert(0, src_dir)

# Now import the app
from app import app

class TestApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_home_endpoint(self):
        """Test the home endpoint"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'DevOps CI/CD Pipeline Demo')
        self.assertEqual(data['status'], 'running')
        self.assertEqual(data['version'], '1.0.0')
    
    def test_health_endpoint(self):
        """Test the health check endpoint"""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')
        self.assertEqual(data['service'], 'devops-demo')
    
    def test_info_endpoint(self):
        """Test the info endpoint"""
        response = self.app.get('/info')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertIn('environment', data)
        self.assertIn('port', data)
    
    def test_invalid_endpoint(self):
        """Test invalid endpoint returns 404"""
        response = self.app.get('/invalid')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()