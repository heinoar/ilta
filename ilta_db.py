import os
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import datetime


#Seuraavassa luetaan ympäristömuuttujia
def connect():
  HOST = os.environ.get('MYSQLCONNSTR_HOST')
  MASTER_KEY = os.environ.get('MYSQLCONNSTR_MASTER_KEY')
  DATABASE_ID = os.environ.get('MYSQLCONNSTR_DATABASE_ID')
  CONTAINER_ID = os.environ.get('MYSQLCONNSTR_CONTAINER_ID')

  client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent="CosmosDBPython", user_agent_overwrite=True)
  try:
        # setup database for this sample
        try:
            db = client.create_database(id=DATABASE_ID)
            print('Database with id \'{0}\' created'.format(DATABASE_ID))

        except exceptions.CosmosResourceExistsError:
            db = client.get_database_client(DATABASE_ID)
            print('Database with id \'{0}\' was found'.format(DATABASE_ID))

        # setup container for this sample
        try:
            container = db.create_container(id=CONTAINER_ID, partition_key=PartitionKey(path='/partitionKey'))
            print('Container with id \'{0}\' created'.format(CONTAINER_ID))

        except exceptions.CosmosResourceExistsError:
            container = db.get_container_client(CONTAINER_ID)
            print('Container with id \'{0}\' was found'.format(CONTAINER_ID))
  except exceptions.CosmosHttpResponseError as e:
        print('\nDatabase creation has caught an error. {0}'.format(e.message))
    

  finally:
        print("\nDatabase creation success")
        return container


def create_item(container,item):
    print('\nCreating Items\n'+str(item))
    print(container)
    container.create_item(body=item)

