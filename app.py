from flask import Flask,render_template,request

# from db.mongodb_connection import pages_collection

from app.routes.page_route import page_bp

from app.routes.webhook import webhook_bp

from app.controllers.post import getPosts

from datetime import datetime

from app.controllers.autoReplyMethods import extract_post_id_from_permalink

from app.controllers.autoReplyMethods import attatchmentIsImage,attachmentIsFallBack,messageIsText
# from models.post import Post

# from controllers.page import createPage

# from controllers.imageComparison import compareTwoImages 
import cv2
import os   

import requests

from app.controllers.imageComparison import compareTwoImages

from bs4 import BeautifulSoup



app=Flask(__name__)

PAGE_ACCESS_TOKEN="EAAMfE8HUFEUBOwhvV0NfaOt0lOTZAHOxEHe89MNxxDU8PpiZBt99JT6cQLFrR6m0EOVd6S46JHc2bbDP2Pof4oDM7dvN3KE9u8ZBQjcklrKgUbJDZBXuiNQT0nUJugjoA1zHwGB24Vx6yCGVxvGneQ6o9IWvJRVyoq2JK8Q3QC2TG6HT7DCgJfzsgNEvvpl4"

API= "https://graph.facebook.com/v13.0/me/messages?access_token="+PAGE_ACCESS_TOKEN




UPLOAD_FOLDER = 'images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

userId="158726557314858"

app.register_blueprint(page_bp)

app.register_blueprint(webhook_bp)


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)






@app.route("/")
def landPage():   
    return render_template('./index.html',userId=userId)


@app.route("/webhook", methods=['GET'])
def fbverify():
    print(request)
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token")=="anystring":
            return "Verification token missmatch", 403

        print(request.args.get("hub.challenge"))
        return request.args.get("hub.challenge"),200
    return "Hello world", 200


# @app.route("/webhook", methods=['POST'])
# def fbwebhook():
#     data = request.get_json()
#     print(data)
    
#         # Read messages from facebook messanger.
#     message = data['entry'][0]['messaging'][0]['message']
#     sender_id = data['entry'][0]['messaging'][0]['sender']['id']
#     pageId=str(data['entry'][0]['id'])

#     if 'text' in message :
#         response=messageIsText(message,API,sender_id)
#         if response :
#             return response

#     elif 'attachments' in message :
#         for attachment in message['attachments']:
#             if attachment['type']=='image':
#                response=attatchmentIsImage(attachment,pageId,sender_id,API)
#                if(response):
#                 return response
#             # if the customer sends the link of the whole post not image 
#             elif attachment['type']=='fallback':
#                 response=attachmentIsFallBack(attachment,pageId,sender_id,API)
#                 if response :
#                     return response

#     return "nothing",201




if __name__== '__main__':
    app.run()





CONNECTION_STRING="mongodb+srv://mohamedaminetouihri9:OUGCjVq1Kg6OAfrM@cluster0.iym5nvs.mongodb.net/?retryWrites=true&w=majority"



