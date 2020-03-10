from config import app
from model import db, Reading

import api.api

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')