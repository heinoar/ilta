
from flask import Flask
import os


def main():
  app = Flask(__name__)
  app.run()
@app.route('/')
def index():
  #conn_str=os.environ.get('MYSQLCONNSTR_PRIMARY_CONNECTION_STRING','ei löytynny')
  #return conn_str
  return 'Web App with Python Flask!'

if __name__ == "__main__":
  main()
  