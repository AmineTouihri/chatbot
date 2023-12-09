import re
import requests
import os
from app.controllers.imageComparison import compareTwoImages

from app.controllers.post import getPosts


#--------------- get the post id from the post sent by the user i used this methode because i recognized that facebook change the post url every dat but the post id is the same -----------

def extract_post_id_from_permalink(url):
    pattern = r'story_fbid=(\d+)'
    match = re.search(pattern, url)
    if match:
        post_id = match.group(1)
        return post_id
    else:
        return None



#   ------------------ if the attachment sent by costumer is an image call this methode ----------------------

def attatchmentIsImage(attachment,pageId,sender_id,API):
    image_url=attachment['payload']['url']
    image_response=requests.get(image_url)
    if image_response.status_code==200:
        file_name=os.path.join('images',"recivedimage.jpg")
        with open(file_name, 'wb') as image_file:
            image_file.write(image_response .content)

        result=compareTwoImages(pageId)
        if (result!=-1 and result!=-2):
            request_body={
                "recipient":{"id":sender_id},
                "message":{"text":result}
            }
            response=requests.post(API,json=request_body).json()
            return response



# -------------- if the image sent by costumer is of type fallback call this message to check if the post is the same as one of posts saved in the bd of the page --------------------

def attachmentIsFallBack(attachment,pageId,sender_id,API):
    post_url=attachment['payload']['url']
    posts=getPosts(pageId)
    if posts==-1 :
        return "nothing",201
    for post in posts:
        print("im from posts")
        print(post)
        if 'postUrl' in post :
            
            postID=extract_post_id_from_permalink(post['postUrl'])
            ID_Post_Send_By_customer=extract_post_id_from_permalink(post_url)

            if postID==ID_Post_Send_By_customer :
                request_body={
                    "recipient":{"id":sender_id},
                    "message":{"text":post['postDescription']}
                }
                response=requests.post(API,json=request_body).json()
                return response

                    #   ------------------- want to make webscraping to get photos and compare them  !!!! -------------------------------
                                # response=requests.get(post_url)

                                # print(response)

                                # if response.status_code ==200 :
                                #     soup=BeautifulSoup(response.content,'html.parser')
                                #     images=soup.find_all('img')
                                #     print(images.__len__())
                                #     for img in images :
                                        
                                #         print(img.get('src'))  
        

def messageIsText(message,API,sender_id):
    if message['text'] == "hi":
        request_body = {
            "recipient": {
                "id": sender_id
            },
            "message": {
                "text": "hello, world!"
            }
        }
        response = requests.post(API, json=request_body).json()
        print("from he says hi !")
        print(response)
        return response
    elif message['text'] == "quick":
        request_body = {
            "recipient": {
                "id": sender_id
            },
            "messaging_type": "RESPONSE",
            "message": {
                "text": "Pick a color:",
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "Red",
                        "payload": "<POSTBACK_PAYLOAD>",
                        "image_url": "http://example.com/img/red.png"
                    }, {
                        "content_type": "text",
                        "title": "Green",
                        "payload": "<POSTBACK_PAYLOAD>",
                        "image_url": "http://example.com/img/green.png"
                    }
                ]
            }
        }
        response = requests.post(API, json=request_body).json()
        return response
