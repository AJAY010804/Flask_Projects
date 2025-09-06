from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Projects</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                min-height: 100vh;
            }
            .container {
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            }
            h1 {
                text-align: center;
                margin-bottom: 30px;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
            }
            .feature {
                background: rgba(255, 255, 255, 0.1);
                margin: 20px 0;
                padding: 20px;
                border-radius: 10px;
                border-left: 4px solid #fff;
            }
            .feature h3 {
                margin-top: 0;
                color: #fff;
            }
            .api-demo {
                margin-top: 30px;
                text-align: center;
            }
            button {
                background: linear-gradient(45deg, #667eea, #764ba2);
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 25px;
                cursor: pointer;
                font-size: 16px;
                margin: 10px;
                transition: transform 0.2s;
            }
            button:hover {
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            }
            #result {
                margin-top: 20px;
                padding: 15px;
                background: rgba(0, 0, 0, 0.2);
                border-radius: 8px;
                min-height: 50px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Flask Projects</h1>
            <p>Welcome to your Flask application running on Replit! This is a basic setup that's ready for development.</p>
            
            <div class="feature">
                <h3>✨ Features</h3>
                <p>This Flask app is configured to work properly in the Replit environment with:</p>
                <ul>
                    <li>Proper host configuration (0.0.0.0:5000)</li>
                    <li>Replit proxy compatibility</li>
                    <li>Basic routing structure</li>
                    <li>API endpoints for development</li>
                </ul>
            </div>
            
            <div class="feature">
                <h3>🔧 Getting Started</h3>
                <p>You can now start building your Flask projects. The basic structure includes:</p>
                <ul>
                    <li><strong>app.py</strong> - Main Flask application</li>
                    <li><strong>requirements.txt</strong> - Python dependencies</li>
                    <li>Replit workflow configuration</li>
                </ul>
            </div>
            
            <div class="api-demo">
                <h3>🔗 API Demo</h3>
                <p>Test the API functionality:</p>
                <button onclick="testApi()">Test API Endpoint</button>
                <button onclick="testData()">Get Sample Data</button>
                <div id="result"></div>
            </div>
        </div>
        
        <script>
        async function testApi() {
            try {
                const response = await fetch('/api/test');
                const data = await response.json();
                document.getElementById('result').innerHTML = 
                    `<strong>API Response:</strong><br>${JSON.stringify(data, null, 2)}`;
            } catch (error) {
                document.getElementById('result').innerHTML = 
                    `<strong>Error:</strong> ${error.message}`;
            }
        }
        
        async function testData() {
            try {
                const response = await fetch('/api/data');
                const data = await response.json();
                document.getElementById('result').innerHTML = 
                    `<strong>Sample Data:</strong><br>${JSON.stringify(data, null, 2)}`;
            } catch (error) {
                document.getElementById('result').innerHTML = 
                    `<strong>Error:</strong> ${error.message}`;
            }
        }
        </script>
    </body>
    </html>
    '''

@app.route('/api/test')
def api_test():
    return jsonify({
        'status': 'success',
        'message': 'Flask API is working!',
        'environment': 'Replit',
        'version': '1.0.0'
    })

@app.route('/api/data')
def api_data():
    return jsonify({
        'projects': [
            {'name': 'Web App', 'status': 'active', 'framework': 'Flask'},
            {'name': 'API Server', 'status': 'planned', 'framework': 'Flask'},
            {'name': 'Data Processing', 'status': 'development', 'framework': 'Python'}
        ],
        'total_projects': 3,
        'last_updated': '2024-09-06'
    })

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy', 'service': 'flask-projects'})

if __name__ == '__main__':
    # Configure for Replit environment
    # Use 0.0.0.0 to accept connections from Replit's proxy
    app.run(host='0.0.0.0', port=5000, debug=True)