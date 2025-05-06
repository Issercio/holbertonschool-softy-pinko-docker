from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/hello')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Important : Le serveur Flask doit être démarré sur 0.0.0.0 pour accepter les connexions externes.
    app.run(host='0.0.0.0', port=5252)
