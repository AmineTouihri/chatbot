from pymongo import MongoClient

import os

# connection_string=os.getenv("CONNECTION_STRING")    


connection_string="mongodb+srv://mohamedaminetouihri9:OUGCjVq1Kg6OAfrM@cluster0.iym5nvs.mongodb.net/?retryWrites=true&w=majority"




print(connection_string)
try:

    # Create a MongoClient instance
    client =MongoClient(connection_string)
    db=client['pythonChatbot']
    
    pages_collection=db['pages']
    # Return the MongoClient instance
    

except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
