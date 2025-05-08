from pymongo import MongoClient
from config import settings
if settings.uri_format == 'mongodb':
    
    client = MongoClient(f'{settings.uri_format}://{settings.mongo_initdb_root_username}:{settings.mongo_initdb_root_password}@{settings.host}:{settings.port}', uuidRepresentation='standard')
else:
    client = MongoClient(f'{settings.uri_format}://{settings.mongo_initdb_root_username}:{settings.mongo_initdb_root_password}@{settings.host}', uuidRepresentation='standard')

db = client.mydatabase
users_collection = db.users