from flask import Flask
from flask import request
import os
import ilta_db
import json



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
  item_id=request.args.get('id')
  item={'id': item_id,
        'partitionKey': "sensmax-1", 
        'sensor': sensor,
        'direction_in': direction_in,
        'direction_out': direction_out}
  container=ilta_db.connect()
  ilta_db.create_item(container,item)
  return sensor

@app.route('/read')
def read():
  container=ilta_db.connect()
  data=ilta_db.read_items(container)
  return str(data)

if __name__ == "__main__":
  app.run()
