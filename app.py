
from flask import Flask
import os


app = Flask(__name__)

@app.route('/')
def index():
    #conn_str=os.environ.get('MYSQLCONNSTR_PRIMARY_CONNECTION_STRING','ei löytynny')
    #return conn_str
    return 'Web App with Python Flask!'

if __name__ == "__main__":
  app.run()