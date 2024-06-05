import os
class Config:
    MONGO_URI = ""
    MONGO_URI = os.getenv("MONGO_URI",MONGO_URI)