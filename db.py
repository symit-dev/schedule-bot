import pymongo

class Mango:
  def __init__(self):
    self.db_url = "mongodb+srv://test:sumit12345@cluster0.7hauv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    self.client = pymongo.MongoClient(self.db_url)
    self.db = self.client.schedule
    self.collection = self.db.col

  def insert(self, json_data):
    return self.collection.insert_one(json_data)
    
  def get_all_data(self, json_data):
    return self.collection.find(json_data)
    

  def get_single_data(self, json_data):
    self.return_json = self.collection.find_one(json_data)
    return self.return_json

  def delete_single_data(self, json_data):
    self.check = self.collection.delete_one(json_data)
    return self.check.deleted_count

  def delete_all_data(self, json_data):
    return self.collection.delete_many(json_data)


# db = mango()
# user = {'name': 'Halil', 'lang': 'Python'}
# print(db.insert(user))

# client = pymongo.MongoClient('mongodb+srv://bot:sumit12345@cluster0.7hauv.mongodb.net/myFirstDatabase?retryWrites=true&w=majorit')
# print(client.list_database_names())
