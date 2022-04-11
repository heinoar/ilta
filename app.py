
from flask import Flask
from flask import request
import os
import ilta_db



app = Flask(__name__)

@app.route('/')
def index():
  #conn_str=os.environ.get('MYSQLCONNSTR_PRIMARY_CONNECTION_STRING','ei löytynny')
  
  return 'Web App with Python Flask! TEST'

@app.route('/insert')
def insert():
  sensor=request.args.get('sensor')
  direction_in=request.args.get('direction_in')
  direction_out=request.args.get('direction_out')
  item={'sensor': sensor,
        'direction_in': direction_in,
        'direction_out': direction_out}
  container=ilta_db.connect()
  ilta_db.create_item(container,item)
  return sensor

if __name__ == "__main__":
  app.run()
