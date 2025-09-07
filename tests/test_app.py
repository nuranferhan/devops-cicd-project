import unittest
import json
import os
import sys

# Test dosyasının bulunduğu dizini al
test_dir = os.path.dirname(os.path.abspath(__file__))
# Proje root dizinini al  
project_root = os.path.dirname(test_dir)
# src dizinini Python path'e ekle
sys.path.insert(0, os.path.join(project_root, 'src'))

# Import app
try:
    from app import app
except ImportError as e:
    print(f"Import error: {e}")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Python path: {sys.path}")
    raise

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