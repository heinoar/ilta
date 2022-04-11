
from flask import Flask
from flask import request
import os



app = Flask(__name__)

@app.route('/')
def index():
  #conn_str=os.environ.get('MYSQLCONNSTR_PRIMARY_CONNECTION_STRING','ei löytynny')
  
  return 'Web App with Python Flask!'

@app.route('/insert')
def insert():
  sensor=request.args.get('sensor')
  return sensor

if __name__ == "__main__":
  app.run()
