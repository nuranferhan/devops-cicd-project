from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "DevOps CI/CD Pipeline Demo",
        "status": "running",
        "version": "1.0.0"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "service": "devops-demo"
    })

@app.route('/info')
def info():
    return jsonify({
        "environment": os.getenv('ENVIRONMENT', 'development'),
        "port": os.getenv('PORT', '5000')
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)