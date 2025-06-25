from app import create_app
from flask_cors import CORS

CORS(app, supports_credentials=True)

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)