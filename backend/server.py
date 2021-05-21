from app import create_app
from app.model import *

app = create_app()

if __name__ == '__main__':
    app.run(debug=False, host="127.0.0.1")

from app.create_db import *
remove_db()
