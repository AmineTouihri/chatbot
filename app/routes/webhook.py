from flask import Blueprint,request

from dotenv import load_dotenv

from pathlib import Path

import os

dotenv_path=Path('.')/'.env'



load_dotenv(dotenv_path)
API=os.getenv("API")


from app.controllers.autoReplyMethods import attachmentIsFallBack, attatchmentIsImage, messageIsText


webhook_bp=Blueprint('webhook',__name__)


@webhook_bp.route('/webhook',methods=['POST'])
def fbwebhook():
        print(API)
        data = request.get_json()
        print(data)
        
            # Read messages from facebook messanger.
        message = data['entry'][0]['messaging'][0]['message']
        sender_id = data['entry'][0]['messaging'][0]['sender']['id']
        pageId=str(data['entry'][0]['id'])

        if 'text' in message :
            response=messageIsText(message,API,sender_id)
            if response :
                return response
                
        elif 'attachments' in message :
            for attachment in message['attachments']:
                if attachment['type']=='image':
                    response=attatchmentIsImage(attachment,pageId,sender_id,API)
                if(response):
                    return response
                # if the customer sends the link of the whole post not image 
                elif attachment['type']=='fallback':
                    response=attachmentIsFallBack(attachment,pageId,sender_id,API)
                    if response :
                        return response

        return "nothing",201
