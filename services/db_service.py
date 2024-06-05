from pymongo.mongo_client import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)
mydb = client["madaurus"]
posts = mydb['posts']

def get_all_posts():
    return list(posts.find())

def get_post_by_id(post_id):
    return posts.find_one({'_id': post_id})

def get_posts_by_id(ids):
    return list(posts.find({'_id': {'$in': ids}}))

def add_post(id,corps, embedding):
    new_post = {
        "_id" :id,
        "corps": corps,
        "embedding": embedding
    }
    result = posts.insert_one(new_post)
    return result